import speech_recognition as sr
import os
import time
import json
import random
from http import HTTPStatus
import dashscope
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role

r = sr.Recognizer()
with sr.Microphone() as source:
    print("START")
    audio = r.listen(source, timeout=3, phrase_time_limit=5)
    print("OVER")

# recognize speech using whisper
try:
    print("Whisper thinks you said: " + r.recognize_whisper(audio, model="small", language="chinese"))
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")

def call_with_stream(question):
    messages = [
        {'role': 'user', 'content': f'{question}'}]
    responses = Generation.call(
        model='qwen-max-1201',
        max_tokens=1500,
        messages=messages,
        result_format='message',
        stream=True,
        incremental_output=True
    )
    full_content = ''
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
            api_reports(response, question)
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print(f'{question}:\n\n' + full_content)

def api_reports(output_response, text):
    time_now = time.strftime('%Y年%m月%d日%H点%M分%S秒', time.localtime())
    f = open(f'大模型调用记录/通义千文/{text}_{time_now}.json', 'w')
    output_json = json.dumps(output_response)
    f.write(output_json)
    f.close()

# key = os.getenv("DASHSCOPE_API_KEY")