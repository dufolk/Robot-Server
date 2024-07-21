import speech_recognition as sr
import torch
import whisper
import io
import soundfile as sf
import numpy as np
import os
import time
import json
import random
from http import HTTPStatus
import dashscope
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role
key = os.getenv("DASHSCOPE_API_KEY")
dashscope.api_key = key

class SpeechService:
    def __init__(self) -> None:
        
        self.r = sr.Recognizer()
        self.r.whisper_model = getattr(self.r, "whisper_model", {})
        self.r.whisper_model["small"] = whisper.load_model("small")
        self.mic = sr.Microphone()
        print("SS service on")

    def recognize_whisper(self, audio_data, model="base", show_dict=False, load_options=None, language=None, translate=False, **transcribe_options):
        if load_options or not hasattr(self.r, "whisper_model") or self.r.whisper_model.get(model) is None:
            self.r.whisper_model = getattr(self.r, "whisper_model", {})
            self.r.whisper_model[model] = whisper.load_model(model, **load_options or {})
            print("exeu")

        # 16 kHz https://github.com/openai/whisper/blob/28769fcfe50755a817ab922a7bc83483159600a9/whisper/audio.py#L98-L99
        wav_bytes = audio_data.get_wav_data(convert_rate=16000)
        wav_stream = io.BytesIO(wav_bytes)
        audio_array, sampling_rate = sf.read(wav_stream)
        audio_array = audio_array.astype(np.float32)
        srt = time.time()
        result = self.r.whisper_model[model].transcribe(
            audio_array,
            language=language,
            task="translate" if translate else None,
            fp16=torch.cuda.is_available(),
            **transcribe_options
        )
        print(time.time() - srt)
        if show_dict:
            return result
        else:
            return result["text"]

    def record_and_recog(self):
        with sr.Microphone() as source:
            print("START")
            audio = self.r.listen(source, timeout=1.5, phrase_time_limit=2)
            print("OVER")
        res = self.recognize_whisper(audio, model="small", language="chinese")
        # recognize speech using whisper
        try:
            print("Whisper thinks you said: " + res)
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper")
        

        mode = self.call_with_stream(res)
        return int(mode)

    def call_with_stream(self, question):
        messages = [{'role': 'system', 'content': '到东边是模式1,到南边是模式2,到西边是模式3,到北边是模式4,逃跑是模式5,战斗及其他都是模式0.你需要根据我的语言表达判断我想要选择的模式，有时会有错别字，你需要根据相似的拼音判断我所说的内容。此外，我身处南边。你只需要给我返回模式数，不要给我返回任何其他内容。例1：输入：去东边战斗 返回：1 例2：输入：不要去西边，去动编 返回：1 例3：输入：过来 返回：2 例4：输入：淘寶淘寶 返回：5 '},
                    {'role': 'user', 'content': question}]
        response = Generation.call(model="qwen-max-1201",
                                messages=messages,
                                # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
                                seed=random.randint(1, 10000),
                                temperature=0.8,
                                top_p=0.8,
                                top_k=50,
                                # 将输出设置为"message"格式
                                result_format='message')
        if response.status_code == HTTPStatus.OK:
            content = response['output']['choices'][0]['message']['content']
            print(content)
            return content
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))

if __name__ == "__main__":
    ss = SpeechService()
    ss.record_and_recog()