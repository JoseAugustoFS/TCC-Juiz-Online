import subprocess
import os


def read_and_display_c_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        print(f"Conteúdo do arquivo {file_path}:\n{content}")
        return True
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return False


def compile_c_file(file_path):
    try:
        # Definir o caminho para o executável
        output_file = os.path.splitext(file_path)[
            0
        ]  # Remove a extensão ".c" para gerar o executável
        result = subprocess.run(
            ["gcc", file_path, "-o", output_file], capture_output=True, text=True
        )

        if result.returncode == 0:
            print(
                f"Compilação bem-sucedida. Arquivo executável gerado: {output_file}.exe"
            )
            return f"{output_file}.exe"  # Retorna o caminho do executável gerado
        else:
            print(f"Erro na compilação:\n{result.stderr}")
            return None
    except Exception as e:
        print(f"Erro ao compilar o arquivo: {e}")
        return None


def execute_c_program(executable_path):
    try:
        # Executar o programa compilado
        result = subprocess.run([executable_path], capture_output=True, text=True)
        print("Saída do programa:")
        print(result.stdout)
        if result.stderr:
            print("Erros:")
            print(result.stderr)
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")


if __name__ == "__main__":
    # Caminho para o arquivo C
    c_file_path = r"C:\exemple1.c"

    # Passo 1: Ler e exibir o conteúdo do arquivo C
    if read_and_display_c_file(c_file_path):
        # Passo 2: Compilar o arquivo C
        executable_path = compile_c_file(c_file_path)

        if executable_path:
            # Passo 3: Executar o programa compilado
            execute_c_program(executable_path)
