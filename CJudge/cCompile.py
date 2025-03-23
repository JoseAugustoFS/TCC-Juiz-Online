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
        output_file = os.path.splitext(file_path)[
            0
        ]
        result = subprocess.run(
            ["gcc", file_path, "-o", output_file], capture_output=True, text=True
        )

        if result.returncode == 0:
            print(
                f"Compilação bem-sucedida. Arquivo executável gerado: {output_file}.exe"
            )
            return f"{output_file}.exe"
        else:
            print(f"Erro na compilação:\n{result.stderr}")
            return None
    except Exception as e:
        print(f"Erro ao compilar o arquivo: {e}")
        return None


def execute_c_program(executable_path):
    try:

        result = subprocess.run([executable_path], capture_output=True, text=True)
        print("Saída do programa:")
        print(result.stdout)
        if result.stderr:
            print("Erros:")
            print(result.stderr)
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")


if __name__ == "__main__":

    c_file_path = r"C:\exemple1.c"

    if read_and_display_c_file(c_file_path):
        executable_path = compile_c_file(c_file_path)

        if executable_path:
            execute_c_program(executable_path)
