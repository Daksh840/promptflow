TASKS = [
    {
        "task": "Summarize: New research finds that higher vitamin D levels may decrease the risk of heart disease.",
        "type": "summarization",
        "examples": [
            {
                "input": "Summarize: Scientists discover that regular exercise lowers blood pressure in adults.",
                "output": "Regular exercise can help reduce blood pressure."
            }
        ],
        "role": "You are a science journalist. Summarize the health news for general readers."
    },
    {
        "task": "Classify: Is the sentiment of the following review positive, negative, or neutral? 'I enjoyed the movie's plot, but the acting was mediocre.'",
        "type": "classification",
        "examples": [
            {
                "input": "Classify: Is the sentiment of the following review positive, negative, or neutral? 'The food arrived late, but tasted great.'",
                "output": "Neutral"
            }
        ],
        "role": "You are a sentiment analysis expert. Classify the following text."
    },
    {
        "task": "Explain: Why does an object accelerate when a constant force is applied?",
        "type": "reasoning",
        "examples": [
            {
                "input": "Explain: Why does the sky appear blue during the day?",
                "output": "Because shorter blue wavelengths scatter in the atmosphere more than longer red wavelengths."
            }
        ],
        "role": "You are a high school physics teacher."
    },
    {
        "task": "Translate: 'The quick brown fox jumps over the lazy dog.' into French.",
        "type": "translation",
        "examples": [
            {
                "input": "Translate: 'Good morning!' into French.",
                "output": "Bonjour !"
            }
        ],
        "role": "You are an expert French translator."
    },
    {
        "task": "Write a short poem about the importance of friendship.",
        "type": "creative-writing",
        "examples": [
            {
                "input": "Write a short poem about autumn leaves.",
                "output": "Golden leaves drift from the tree,\nWhispering winds set them free."
            }
        ],
        "role": "You are an award-winning poet."
    },
    {
        "task": "Edit the following sentence to correct any grammar and clarity issues: 'She don't likes the movie, but he did.'",
        "type": "editing",
        "examples": [
            {
                "input": "Edit: 'The cats plays in the garden every day.'",
                "output": "The cats play in the garden every day."
            }
        ],
        "role": "You are an English grammar teacher."
    },
    {
        "task": "List the steps required to change a car tire.",
        "type": "instruction",
        "examples": [
            {
                "input": "List the steps to make a cup of tea.",
                "output": "1. Boil water. 2. Add tea leaves. 3. Steep. 4. Pour. 5. Enjoy."
            }
        ],
        "role": "You are a roadside assistance agent explaining this to a beginner."
    },
    {
        "task": "Identify any factual mistakes in this statement: 'The capital of Australia is Sydney.'",
        "type": "fact-checking",
        "examples": [
            {
                "input": "Identify factual mistakes: 'Humans have four hearts.'",
                "output": "Mistake: Humans have one heart, not four."
            }
        ],
        "role": "You are a fact-checker reviewing educational content."
    },
]
