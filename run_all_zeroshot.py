# run_all_zeroshot.py
import subprocess
import sys
import os

# 👇 Ensure root directory is on the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

# ✅ Use module paths (so Python treats them as packages)
model_modules = {
    "Mistral": "models.mistral.run_gerrit",
    "DeepSeek": "models.deepseek.run_gerrit",
    "LLaMA3": "models.llama3.run_gerrit",
    "CodeBART": "models.codebart.run_gerrit"
}

print("\n🚀 Starting Zero-Shot Evaluation for All Models (Dataset: Gerrit)\n")

for model, module_path in model_modules.items():
    print(f"➡️ Running {model} on Gerrit...\n")
    try:
        subprocess.run([sys.executable, "-m", module_path], check=True)
        print(f"✅ {model} finished successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {model}:\n{e}\n")

    print("------------------------------------------------------------\n")