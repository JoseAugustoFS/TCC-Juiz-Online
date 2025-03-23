import subprocess
import os

def run_java(directory, input_data):
    try:
        main_class = None
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.java'):
                    with open(os.path.join(root, file), 'r') as java_file:
                        if 'void main' in java_file.read():
                            main_class = os.path.splitext(file)[0]
                            break
        
        if main_class:
            result = subprocess.run(
                ['java', main_class],
                input=input_data,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=directory
            )

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"Execução falhou: {result.stderr.strip()}"
        else:
            return "Nenhuma classe Java encontrada para executar."
    except Exception as e:
        return f"Um erro ocorreu durante a execução: {str(e)}"
    
def validade_java(directory, inputs, answers):
    try:
        results = []
        for i, single_input in enumerate(inputs):
            result = run_java(directory, single_input.strip())
            results.append(result)
        
        correct_count = sum(1 for o, a in zip(results, answers) if o == a)
        validated_percent = correct_count / len(answers) * 100

        return {"percentual_validado": validated_percent, "resultado": results}

    except Exception as e:
        return {"percentual_validado": 0, "resultado": "Um erro ocorreu durante a validação: " + str(e)}