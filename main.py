import streamlit as st
from dotenv import load_dotenv
from apis.openrouter_api import get_openrouter_response
from apis.groq_api import get_groq_response
from apis.huggingface_api import get_hf_response
from apis.lmstudio_api import get_local_response as lmstudio_response
# from apis.ollama_api import get_local_response as ollama_response
from prompt_strategies import zero_shot_prompt, few_shot_prompt, role_based_prompt
from test_cases import TASKS

load_dotenv()

st.set_page_config(page_title="PromptFlow Free LLMs", layout="wide")
st.title("🔄 PromptFlow: LLM Prompt Testing (Free/Local Models)")

st.sidebar.header("Prompt Strategy & Model")
strategy = st.sidebar.selectbox("Strategy", ["Zero-shot", "Few-shot", "Role-based"])
model_choice = st.sidebar.selectbox("Model", [
    "OpenRouter",
    "Groq",
    "Hugging Face",
    "LM Studio (local)",
    "Ollama (local)"
])
task_idx = st.sidebar.selectbox("Test Case", list(range(len(TASKS))), format_func=lambda i: TASKS[i]['task'])
task_data = TASKS[task_idx]

# Prepare prompt
if strategy == "Zero-shot":
    prompt = zero_shot_prompt(task_data['task'])
elif strategy == "Few-shot":
    prompt = few_shot_prompt(task_data['task'], task_data.get("examples", []))
else:
    prompt = role_based_prompt(task_data['task'], task_data.get("role", ""))

st.subheader("Prompt Preview")
st.code(prompt)

def get_response():
    if model_choice == "OpenRouter":
        return get_openrouter_response(prompt)
    if model_choice == "Groq":
        return get_groq_response(prompt)
    if model_choice == "Hugging Face":
        return get_hf_response(prompt)
    if model_choice == "LM Studio (local)":
        return lmstudio_response(prompt)
    # if model_choice == "Ollama (local)":
    #     return ollama_response(prompt)
    return "No model selected!"

if st.button("Run Prompt"):
    with st.spinner("Querying model..."):
        st.markdown("## Model Output")
        st.write(get_response())

