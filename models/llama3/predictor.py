import subprocess

def query_llama3(prompt: str, model_name="llama3:8b") -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model_name],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        output = result.stdout.decode("utf-8").strip()
        return output.split("\n")[0].strip()
    except subprocess.CalledProcessError as e:
        print("❌ LLaMA3 Error:", e.stderr.decode())
        return "Error"