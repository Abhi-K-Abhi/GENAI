# models/deepseek/run_gerrit.py

import os
import csv
import gc
import math
from tqdm import tqdm
from sklearn.metrics import confusion_matrix, matthews_corrcoef

from .predictor import query_deepseek
from utils.dataset_loader import load_llm_dataset

# === Paths ===
DATA_PATH = "data/llm/test_gerrit.txt"
PROMPT_TEMPLATE_PATH = "models/deepseek/prompt_template.txt"
RESULT_PATH = "outputs/results_deepseek_gerrit.csv"

# === Load system prompt ===
with open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# === Load test dataset ===
dataset = load_llm_dataset(DATA_PATH)

y_true, y_pred = [], []

print("🚀 Running DeepSeek Zero-Shot on Gerrit...")

for entry, label in tqdm(dataset):
    y_true.append(label)

    # No special prompt wrapping needed for DeepSeek
    prompt = SYSTEM_PROMPT + "\n\n" + entry.strip() + "\nAnswer:"

    prediction = query_deepseek(prompt)
    pred = int(prediction[0]) if prediction and prediction[0] in "01" else 0
    y_pred.append(pred)

    gc.collect()

# === Metric computation ===
def compute_metrics(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    acc = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0
    gmean = math.sqrt(recall * (tn / (tn + fp))) if (tn + fp) else 0
    mcc = matthews_corrcoef(y_true, y_pred)
    return acc, precision, recall, f1, gmean, mcc

acc, precision, recall, f1, gmean, mcc = compute_metrics(y_true, y_pred)

# === Save results ===
with open(RESULT_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Dataset", "Accuracy", "Precision", "Recall", "F1 Score", "G-Mean", "MCC"])
    writer.writerow(["gerrit", acc, precision, recall, f1, gmean, mcc])

print(f"\n✅ DeepSeek results saved to {RESULT_PATH}")