import os
from IA_Agent import agent_call


def load_prompts(directory="PROMPTS/Optimization"):
    prompts = []
    for i in range(1, 4):  # Ajuste o número 3 se o número de arquivos for diferente
        file_path = os.path.join(directory, f"{i}.txt")

        # Verifica se o arquivo existe antes de tentar abrir
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")

        # Lê o conteúdo do arquivo e adiciona na lista
        with open(file_path, "r", encoding="utf-8") as file:
            prompts.append(file.read().strip())

    return prompts


def get_c_codes(directory):
    try:
        c_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".c"):
                    c_files.append(os.path.join(root, file))
        codes = ""
        for idx, c_file in enumerate(c_files, start=1):
            with open(c_file, "r", encoding="utf-8") as file:
                codes += f"File {idx}:\n{file.read()}\n\n"

        return codes
    except Exception as e:
        return e


def optimize_c(directory, statement):
    # Obtendo os códigos C do diretório especificado
    codes = get_c_codes(directory)
    prompts = load_prompts()

    if isinstance(codes, Exception):
        return {"message": "An error occurred: " + str(codes), "result": ""}

    try:
        result = []
        for prompt in prompts:
            # Chamando a IA para otimizar o código
            result.append(agent_call(prompt + statement + codes))

        return {"message": "Code optimized", "result": result}
    except Exception as e:
        return {"message": "An error occurred: " + str(e), "result": ""}
