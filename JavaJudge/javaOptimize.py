import os
from IA_Agent import agent_call

OPTMIZE_PATTERNS = ["Analisar se o tipo primitivo foi usado de maneira correta",
                     "Otimizar uso das estruturas de seleção, apenas se houver necessidade usar",
                     "Otimizar uso das estruturas de repetição, apenas se houver necessidade usar"]

PROMPT = "Com base no enunciado abaixo e em todos os códigos java abaixo e ignorando que seus pacotes estão comentados, confirme se eles estão otimizado conforme especificamente o tópico abaixo, leve em conta se está tudo otimizado em relação ao que o enunciado pede, avitando coisas desnecessárias (caso sim informe apenas 'Otimizado', caso não informe 'Não otimizado' e na linha abaixo explique o porque está inválido): Enunciado: "

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
    updatedPrompt = PROMPT + statement + " Tópico: "
    codes = get_java_codes(directory)

    if isinstance(codes, Exception):
        return {"message": "An error occurred: " + str(codes), "result": ""}
    
    try:
        result = []

        for pattern in OPTMIZE_PATTERNS:
            result.append(agent_call(updatedPrompt + pattern + codes))

        return {"message": "Code optimized", "result": result}
    except Exception as e:
            return {"message": "An error occurred: " + str(e), "result": ""}
    