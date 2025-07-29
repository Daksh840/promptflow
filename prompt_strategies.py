def zero_shot_prompt(task):
    return task

def few_shot_prompt(task, examples):
    example_str = "\n".join([f"Q: {ex['input']}\nA: {ex['output']}" for ex in examples])
    return f"{example_str}\nQ: {task}\nA:"

def role_based_prompt(task, role_instruction):
    return f"{role_instruction}\n\n{task}"
