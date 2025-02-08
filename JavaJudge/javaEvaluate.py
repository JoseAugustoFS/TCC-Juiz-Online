import os
from IA_Agent import agent_call

EVALUATE_PATTERNS = ["Condenar o uso de variável global",
                     "Avaliar a possibilidade de uso de constantes no código, apenas se necessário",
                     "Nome das variáveis, identificadores e classes",
                     "Tratar a formatação",
                     "Avaliar se as variáveis estão sendo inicializadas",
                     "Tratar identação",
                     "Verificar identificadores não utilizados"]

PROMPT = "Com base em todos os códigos java abaixo e ignorando que seus pacotes estão comentados, confirme se eles seguem as boas práticas de programação conforme especificamente (caso sigam informe apenas Válido, caso não informe Inválido e na linha abaixo explique o porque está inválido): "

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

def evaluate_java(directory):
    
    codes = get_java_codes(directory)

    if isinstance(codes, Exception):
        return {"message": "An error occurred: " + str(codes), "result": ""}
    try:
        result = []
        for pattern in EVALUATE_PATTERNS:
            result.append(agent_call(PROMPT + pattern + codes))
        return {"message": "Code evaluate", "result": result}
    except Exception as e:
            return {"message": "An error occurred: " + str(e), "result": ""}