from openai import OpenAI
import openai
import os
openai.api_base = "https://api.openai-proxy.com"
openai.api_key = "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"
# os.environ['http_proxy'] = 'http://127.0.0.1:10809'
# os.environ['https_proxy'] = 'http://127.0.0.1:10809'
client = OpenAI(
    api_key='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',
    base_url='https://api.openai-proxy.com'
)

resp = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': '你好!'}
    ]
)
print(resp.choices[0].message.content)