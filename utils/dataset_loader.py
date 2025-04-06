# utils/dataset_loader.py

import re

def load_llm_dataset(path: str):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    blocks = raw.split("[COMMIT]")
    examples = []

    for block in blocks:
        if not block.strip():
            continue

        label_match = re.search(r"\[LABEL\]\s*(\d)\s*\[/LABEL\]", block)
        label = int(label_match.group(1)) if label_match else None

        # Remove LABEL, Commit_ID and strip
        clean = re.sub(r"\[LABEL\]\s*\d\s*\[/LABEL\]", "", block)
        clean = re.sub(r"Commit_ID: [^\n]+\n?", "", clean)
        clean = clean.strip()

        examples.append((clean, label))

    return examples