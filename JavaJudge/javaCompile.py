import subprocess
import os

def comment_package_line(file_path):
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                comment_package_line(file_path)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith('package '):
                    file.write(f'// {line}')
                else:
                    file.write(line)
        
        return "Linhas de pacotes comentadas com sucesso."
    except Exception as e:
        return "Um erro ocorreu enquanto a linha de pacotes era comentada: " + str(e)

def compile_java(directory):
    try:
        java_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(os.path.join(root, file))
        
        if java_files:

            result = subprocess.run(['javac'] + java_files, capture_output=True, text=True)
            
            if result.returncode == 0:
                return {"status": True, "message": "Compilação bem-sucedida."}
            else:
                return {"status": False, "message": "Erro na compilação." + result.stderr}
        else:
            return {"status": False, "message": "Nenhum arquivo Java encontrado para compilar."}
    except Exception as e:
        return {"status": False, "message": "Um erro ocorreu: " + str(e)}