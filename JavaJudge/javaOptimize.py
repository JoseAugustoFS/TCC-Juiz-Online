import os
from IA_Agent import agent_call

def load_prompts(directory='PROMPTS/Optimization'):
    prompts = []
    for i in range(1, 4):  # Ajuste o número 8 se o número de arquivos for diferente
        file_path = os.path.join(directory, f"{i}.txt")
        
        # Verifica se o arquivo existe antes de tentar abrir
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")
        
        # Lê o conteúdo do arquivo e adiciona na lista
        with open(file_path, 'r', encoding='utf-8') as file:
            prompts.append(file.read().strip())
    
    return prompts

def get_java_codes(directory):
    try:
        java_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(os.path.join(root, file))
        codes = ""
        for idx, java_file in enumerate(java_files, start=1):
            with open(java_file, 'r', encoding='utf-8') as file:
                codes += f"File {idx}:\n{file.read()}\n\n"

        return codes
    except Exception as e:
        return e

def optmize_java(directory, statement):

    codes = get_java_codes(directory)
    prompts = load_prompts()

    if isinstance(codes, Exception):
        return {"message": "An error occurred: " + str(codes), "result": ""}
    
    try:
        result = []
        for prompt in prompts:
            result.append(agent_call(prompt + statement + codes))

        return {"message": "Code optimized", "result": result}
    except Exception as e:
            return {"message": "An error occurred: " + str(e), "result": ""}
    