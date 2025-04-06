from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the CodeBART tokenizer and model from your local directory.
# Ensure that your CodeBART model is fine-tuned for commit risk prediction.
tokenizer = AutoTokenizer.from_pretrained("./codebart_model_classification", local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(
    "./codebart_model_classification",
    device_map="auto",
    local_files_only=True,
    num_labels=2
)
model.eval()

def query_codebart(prompt: str, model_name: str = "codebart") -> str:
    # Tokenize the prompt, ensuring truncation/padding as needed.
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    # Move tensors to the model's device.
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    with torch.no_grad():
        logits = model(**inputs).logits
    pred = torch.argmax(logits, dim=-1).item()
    # Return the prediction as a string.
    return str(pred)