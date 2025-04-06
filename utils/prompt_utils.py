import json
import re


def load_prompt_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_prompt(prompt_template, commit_info, diff):
    prompt = prompt_template["instructions"] + "\n\nExamples:\n"
    for ex in prompt_template["examples"]:
        prompt += f"Commit Info: {ex['commit_info']}\nDiff: {ex['diff']}\nRisk: {ex['label']}\n\n"
    prompt += f"Now classify this commit:\nCommit Info: {commit_info}\nDiff: {diff}\nRisk:"
    return prompt

def generate_cot_prompt(cot_template, commit_info, diff):
    prompt = cot_template["instructions"] + "\n\nExamples:\n"
    for ex in cot_template["examples"]:
        prompt += f"Title: {ex['commit_info']}\nDiff:\n{ex['diff']}\nThought: {ex['reasoning']}\nConclusion: {ex['label']}\n\n"
    prompt += f"Now analyze this commit:\nTitle: {commit_info}\nDiff:\n{diff}\nThought:"
    return prompt

def extract_label_from_cot(output: str) -> str:
    """
    Extracts the final 'Conclusion: <label>' line from a CoT model response.
    Returns '0' or '1' if found, otherwise returns 'Unclear'.
    """
    match = re.search(r"Conclusion:\s*([01])", output)
    return match.group(1) if match else "Unclear"
