import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import subprocess


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

def generate_cot_prompt(cot_template, commit_info, diff):
    prompt = cot_template["instructions"] + "\n\nExamples:\n"
    for ex in cot_template["examples"]:
        prompt += f"Title: {ex['commit_info']}\n"
        prompt += f"Diff:\n{ex['diff']}\n"
        prompt += f"Thought: {ex['reasoning']}\nConclusion: {ex['label']}\n\n"
    prompt += f"Now analyze this commit:\nTitle: {commit_info}\n"
    prompt += f"Diff:\n{diff}\n"
    prompt += "Thought:"
    return prompt

def query_llm(prompt, model_source="openai", model_name="gpt-3.5-turbo"):
    #OpenAI
    if model_source == "openai":
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()

    #Ollama 
    elif model_source == "ollama":
        try:
            result = subprocess.run(
                ["ollama", "run", model_name],
                input=prompt.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            output = result.stdout.decode("utf-8").strip()
            return output.split("\n")[0].strip()  # Just get first clean line
        except subprocess.CalledProcessError as e:
            print("Error running Ollama:", e.stderr.decode())
            return "Error"
# INTEGRATE MODEL HERE (https://github.com/ollama/ollama) [Code Llama, Llama 3.1-8B, DeepSeek-R1, Mistral]
# Refer: https://youtu.be/d0o89z134CQ?si=3CNhQxTJJI_sc8Qp
