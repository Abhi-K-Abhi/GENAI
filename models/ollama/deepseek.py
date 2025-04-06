import subprocess

def query_llm(prompt, model_source="ollama", model_name="deepseek"):
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
        print("Error running Ollama:", e.stderr.decode())
        return "Error"
