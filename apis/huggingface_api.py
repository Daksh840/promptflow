import os
from huggingface_hub import InferenceClient

def get_hf_response(prompt, model_id="Qwen/Qwen3-Coder-480B-A35B-Instruct"):
    client = InferenceClient(model=model_id, token=os.getenv("HF_API_TOKEN"))
    # The prompt must be passed as a message in the 'messages' argument
    result = client.chat_completion(messages=[{"role": "user", "content": prompt}])
    return result.choices[0].message.content  # or adapt based on return structure












