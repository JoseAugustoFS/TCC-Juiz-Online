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
        
        return "Package line commented successfully."
    except Exception as e:
        return "An error occurred while commenting package line: " + str(e)

def compile_java(directory):
    try:
        java_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(os.path.join(root, file))
        
        if java_files:
            # Compilar
            result = subprocess.run(['javac'] + java_files, capture_output=True, text=True)
            
            if result.returncode == 0:
                return "Compilation successful."
            else:
                return "Compilation failed." + result.stderr
        else:
            return "No Java files found to compile."
    except Exception as e:
        return "An error occurred: " + str(e)