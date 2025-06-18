import requests
import json

from auth import OPENROUTER_API_KEY


def query_ai(query):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free", # Optional
        "messages": [
        {
            "role": "user",
            "content": query
        }
        ]
    })
    )
    return response.json()


if __name__ == '__main__':
    data = query_ai("What is the meaning of life?")
    message_content = data['choices'][0]['message']['content']
    print(message_content)
