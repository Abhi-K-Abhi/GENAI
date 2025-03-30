import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_prompt_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_prompt(prompt_template, commit_info, diff):
    prompt = prompt_template["instructions"] + "\n\nExamples:\n"
    for ex in prompt_template["examples"]:
        prompt += f"Commit Info: {ex['commit_info']}\nDiff: {ex['diff']}\nRisk: {ex['label']}\n\n"

    prompt += f"Now classify this commit:\nCommit Info: {commit_info}\nDiff: {diff}\nRisk:"
    return prompt


def query_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()