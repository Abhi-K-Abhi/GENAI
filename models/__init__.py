def get_model_predictor(source, name):
    if source == "openai":
        from models.openai.predictor import query_llm
    elif source == "ollama":
        if name == "codellama":
            from models.ollama.codellama import query_llm
        elif name == "deepseek-coder":
            from models.ollama.deepseek import query_llm
        elif name == "llama3:8b":
            from models.ollama.llama3 import query_llm
        elif name == "mistral":
            from models.ollama.mistral import query_llm
        else:
            raise ValueError("Unsupported Ollama model")
    else:
        raise ValueError("Unsupported model source")
    return query_llm