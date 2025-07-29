import os, requests

def get_openrouter_response(prompt, model="qwen/qwen3-235b-a22b-2507:free"):
    key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512
    }
    res = requests.post(url, headers=headers, json=data)

    try:
        response_json = res.json()
        print("OpenRouter API response:", response_json)  # <-- Add this line to debug
        # Check for error key
        if "error" in response_json:
            raise Exception(f"OpenRouter API error: {response_json['error']}")

        return response_json["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error parsing OpenRouter response:", e)
        return f"API call failed: {e}"
