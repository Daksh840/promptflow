import requests

def get_local_response(prompt, endpoint="http://localhost:1234/v1/chat/completions", model="lmstudio", max_tokens=512):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens
    }
    res = requests.post(endpoint, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']
