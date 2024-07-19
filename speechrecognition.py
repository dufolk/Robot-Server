import speech_recognition as sr
import os
import time
import json
import random
from http import HTTPStatus
import dashscope
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("START")
#     audio = r.listen(source, timeout=3, phrase_time_limit=5)
#     print("OVER")

# # recognize speech using whisper
# try:
#     print("Whisper thinks you said: " + r.recognize_whisper(audio, model="small", language="chinese"))
# except sr.UnknownValueError:
#     print("Whisper could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Whisper")

def call_with_stream(question):
    messages = [{'role': 'system', 'content': '到北边是模式1,到东边是模式2,到南边是模式3,到西边是模式4,逃跑是模式5,战斗及其他都是模式0.你需要根据我的语言表达判断我想要选择的模式，有时会有错别字，你需要根据相似的拼音判断我所说的内容。此外，我身处南边。你只需要给我返回模式数，不要给我返回任何其他内容。例1：输入：去北边战斗 返回：1 例2：输入：不要去西边，去动编 返回：2 例3：输入：过来 返回：3'},
                {'role': 'user', 'content': '到我这来'}]
    response = Generation.call(model="qwen-turbo",
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


key = "sk-3d0c2dbbf211476e8d7cc3062ad33d45"
dashscope.api_key = key
text = '为什么我保存response的json文件，content为空'
call_with_stream(text)