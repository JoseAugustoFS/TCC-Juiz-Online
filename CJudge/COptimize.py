import os
from IA_Agent import agent_call


def load_prompts(directory="PROMPTS/Optimization"):
    prompts = []
    for i in range(1, 4):
        file_path = os.path.join(directory, f"{i}.txt")

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")

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
    codes = get_c_codes(directory)
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