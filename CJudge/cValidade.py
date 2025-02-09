import os
import subprocess


class cValidade:
    def __init__(self, source_code, executable, input_file, output_file):
        """
        Inicializa a classe com os caminhos necessários.

        :param source_code: Caminho para o arquivo C a ser compilado.
        :param executable: Caminho para o executável gerado após compilação.
        :param input_file: Caminho para o arquivo contendo as entradas.
        :param output_file: Caminho para o arquivo contendo as saídas esperadas.
        """
        self.source_code = source_code
        self.executable = executable
        self.input_file = input_file
        self.output_file = output_file
        self.system = os.name  # Identifica o sistema operacional

    def compile(self):
        """
        Compila o código C e verifica se há erros de compilação.
        """
        compile_process = subprocess.run(
            ["gcc", self.source_code, "-o", self.executable],
            capture_output=True,
            text=True,
        )

        if compile_process.returncode != 0:
            print("❌ Erro na compilação do código C:\n", compile_process.stderr)
            return False

        print("✅ Compilação bem-sucedida.")
        return True

    def load_test_cases(self):
        """
        Carrega as entradas e saídas esperadas a partir dos arquivos.
        """
        try:
            with open(self.input_file, "r") as file:
                inputs = file.read().strip().split("===")
                self.inputs = [entry.strip() for entry in inputs]
        except Exception as e:
            print("❌ Erro ao ler arquivo de entradas:", str(e))
            self.inputs = []

        try:
            with open(self.output_file, "r") as file:
                expected_outputs = file.read().strip().split("===")
                self.expected_outputs = [output.strip() for output in expected_outputs]
        except Exception as e:
            print("❌ Erro ao ler arquivo de respostas:", str(e))
            self.expected_outputs = []

    def run_tests(self):
        """
        Executa o código C para cada entrada e compara com a saída esperada.
        """
        if len(self.inputs) != len(self.expected_outputs):
            print(
                "❌ Erro: O número de entradas não corresponde ao número de respostas esperadas."
            )
            return

        for i, input_text in enumerate(self.inputs):
            print(f"\n🛠️ Executando teste {i + 1} com entrada: {input_text}")

            try:
                execute_process = subprocess.run(
                    [self.executable],
                    input=input_text,
                    text=True,
                    capture_output=True,
                )
                output = execute_process.stdout.strip()
                expected_output = self.expected_outputs[i]

                print("🔹 Saída obtida:", output)

                if output == expected_output:
                    print("✅ Resultado correto!")
                else:
                    print("❌ Resultado incorreto!")
                    print("   ➖ Esperado:", expected_output)
                    print("   ➖ Obtido:", output)

            except FileNotFoundError:
                print(
                    "❌ Erro: Arquivo do programa C não encontrado! Verifique o caminho do executável."
                )
                break
            except Exception as e:
                print("❌ Erro ao executar o programa C:", str(e))
