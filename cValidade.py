import subprocess
import os

def run_c(directory, input_file, output_file):
    try:
        # Encontrar o arquivo C com a função main
        main_class = None
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.c'):
                    main_class = os.path.splitext(file)[0]
                    break
        
        if main_class:
            # Compilar o código C
            input_path = os.path.join(directory, input_file)
            output_path = os.path.join(directory, output_file)

            # Compilar o código C
            result = subprocess.run(['gcc', os.path.join(directory, f'{main_class}.c'), '-o', os.path.join(directory, main_class)], capture_output=True, text=True)
            
            if result.returncode != 0:
                return f"Erro na compilação:\n{result.stderr}"

            # Executar o programa C com redirecionamento de entrada e saída
            with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
                result = subprocess.run([os.path.join(directory, main_class)], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, cwd=directory)

            if result.returncode == 0:
                return "Execução bem-sucedida."
            else:
                return f"Falha na execução: {result.stderr}"
        else:
            return "Nenhuma classe principal encontrada para executar."
    except Exception as e:
        return "Ocorreu um erro durante a execução: " + str(e)

def validade_c(directory, input, output):
    try:
        with open(os.path.join(directory, input), 'r') as input_file:
            inputs = input_file.read().split('===')  # Separar os casos de teste
        
        results = []
        for i, single_input in enumerate(inputs):
            temp_input_path = os.path.join(directory, f'temp_input_{i}.txt')
            temp_output_path = os.path.join(directory, f'temp_output_{i}.txt')
            
            with open(temp_input_path, 'w') as temp_input_file:
                temp_input_file.write(single_input.strip())
            
            result = run_c(directory, f'temp_input_{i}.txt', f'temp_output_{i}.txt')
            results.append(result)
            
            with open(temp_output_path, 'r') as temp_output_file:
                output_content = temp_output_file.read()
            
            # Escrevendo a frase final no arquivo de saída
            with open(os.path.join(directory, output), 'a') as output_file:
                output_file.write(f'===\n{output_content.strip()}\n')

            # Remover arquivos temporários
            os.remove(temp_input_path)
            os.remove(temp_output_path)
        
        return results
    except Exception as e:
        return "Ocorreu um erro durante a validação: " + str(e)

# Caminho do diretório onde o código C está localizado
diretorio = r"C:\Users\Marcus\Documents\cValidacao"
# Arquivo de entrada para o teste
entrada = r"entrada.txt"
# Arquivo de saída para o resultado
saida = r"saida.txt"

# Teste com múltiplos casos de entrada
resultados = validade_c(diretorio, entrada, saida)
print(resultados)
