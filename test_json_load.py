import json

with open("prompts/few_shot.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Loaded successfully:", len(data), "examples")
