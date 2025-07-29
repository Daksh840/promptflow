# 🚦 PromptFlow: LLM Prompt Testing Toolkit

**PromptFlow** is a lightweight, modular toolkit for prompt engineers, AI researchers, and developers to compare, test, and analyze zero-shot, few-shot, and role-based prompts across multiple Large Language Models—using entirely free and open APIs or local inferencing.  
Test strategies seamlessly on OpenRouter, Groq, Hugging Face Inference, LM Studio, Ollama, and more—all inside an interactive Streamlit UI.

## ✨ Features

- **Prompt Strategy Comparison**: Side-by-side evaluation of zero-shot, few-shot, and role-based prompt techniques.
- **Cross-Model Testing**: Benchmark prompts across multiple models and providers (OpenRouter, Groq, HF, LM Studio, Ollama, etc.).
- **Interactive Streamlit Dashboard**: Visualize outputs, compare responses, and measure LLM behavior instantly.
- **Plug-and-play Framework**: Easily add new prompt templates, APIs, or test cases.
- **Local or Cloud**: Run models in the cloud (no credit card required) or locally (no internet once models are downloaded).
- **Extensible Evaluation**: Analyze similarity, consistency, hallucination, style, and more.

## 📸 Screenshots

> **Add your screenshots here for best results:**
>
> 1. Inside your project root, create a folder named `assets/`.
> 2. Save each screenshot there, e.g., `assets/streamlit_dashboard.png`.
> 3. Add images in this section with Markdown:
>
> ```markdown
> ![PromptFlow Streamlit UI](assets/streamlit_dashboard.png)
> ![Prompt Comparison Feature](assets/prompt_comparison.png)
> ```

Example placeholder:

![PromptFlow Streamlit Dashboard](assets/your_screenshot_here Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/promptflow.git
cd promptflow
```

### 2. Install Requirements

```bash
# Optionally: python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 3. Setup Free API Keys (Optional for Cloud Models)

- Sign up at [openrouter.ai](https://openrouter.ai/) or [groq.com](https://console.groq.com/) or [huggingface.co](https://huggingface.co/).
- Copy your API keys and paste into a `.env` file in the project root:
  ```
  OPENROUTER_API_KEY=your_key
  GROQ_API_KEY=your_key
  HF_API_TOKEN=your_token
  ```

- For running local models, set up [LM Studio](https://lmstudio.ai/) or [Ollama](https://ollama.com/) (no API key needed).

### 4. Run the App

```bash
streamlit run main.py
```
- The app will open automatically in your browser at `http://localhost:8501`.

## 🧰 Project Structure

```
promptflow/
├── main.py
├── apis/
│   ├── openrouter_api.py
│   ├── groq_api.py
│   ├── huggingface_api.py
│   ├── lmstudio_api.py
│   └── ollama_api.py
├── prompt_strategies.py
├── evaluation.py
├── test_cases.py
├── requirements.txt
├── .gitignore
└── assets/
```

## ⚙️ Usage

1. **Select Prompt Strategy**: Zero-shot, few-shot, or role-based from the sidebar.
2. **Choose LLM Provider**: OpenRouter, Groq, Hugging Face, LM Studio, or Ollama.
3. **Pick a Test Case**: Try summarization, classification, translation, etc.
4. **Review Prompt and Output**: Inspect results, compare across models, and analyze evaluation metrics live.
5. **Add Your Own Prompts/Cases**: Edit `test_cases.py` for more scenarios and richer evaluations.

## 🧪 Example Test Cases

The toolkit includes diverse test cases such as:

- Summarization
- Sentiment classification
- Translation
- Reasoning and explanation
- Creative writing
- Editing and corrections
- Procedural instructions
- Fact checking

> **Add/delete/modify in `test_cases.py` for your needs.**

## 💾 Security

- **Never share your `.env` file or API keys.**
- `.env` is listed in `.gitignore` (see included template) and should not be pushed to GitHub.
- If you ever commit sensitive info, revoke the key and reset your repo history before pushing again.

## 🤝 Contributing

Contributions, issues, and feature suggestions are welcome!  
Open an issue or pull request to discuss major changes first.

## ⭐️ Showcase

Want your PromptFlow usage featured here? PR your best screenshots or prompt workflows for demo!

## 📄 License

[MIT License](LICENSE)

**PromptFlow** empowers you to iterate, optimize, and compare LLM prompts—faster and more transparently than ever.

### 📲 Screenshot Directions Recap

- Place your images in an `assets/` folder in the project root.
- Use Markdown image syntax in the README to embed, like:
  ```markdown
  ![PromptFlow UI](assets/streamlit_dashboard.png)
  ```
- Commit and push both the screenshot files and updated README.

With this README, your PromptFlow project will stand out as professional, usable, and open-source ready!
