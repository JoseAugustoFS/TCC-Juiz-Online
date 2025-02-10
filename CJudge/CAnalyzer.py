import os
import subprocess
from IA_Agent import agent_call


class CAnalyzer:
    def __init__(
        self,
        source_code,
        input_file,
        output_file,
        prompt_directory="PROMPTS/Evaluation",
    ):
        self.source_code = source_code
        self.input_file = input_file
        self.output_file = output_file
        self.prompt_directory = prompt_directory

    def load_prompts(self):
        prompts = []
        for i in range(1, 8):  # Ajuste o número 8 conforme necessário
            file_path = os.path.join(self.prompt_directory, f"{i}.txt")

            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")

            with open(file_path, "r", encoding="utf-8") as file:
                prompts.append(file.read().strip())

        return prompts

    def get_c_code(self):
        try:
            with open(self.source_code, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            return str(e)

    def analyze_code(self):
        code = self.get_c_code()
        if isinstance(code, Exception):
            return {"message": "An error occurred: " + str(code), "result": ""}

        prompts = self.load_prompts()
        try:
            result = []
            for prompt in prompts:
                result.append(agent_call(prompt + code))
            return {"message": "Code analyzed", "result": result}
        except Exception as e:
            return {"message": "An error occurred: " + str(e), "result": ""}

    def compile_and_run(self):
        # Compilar o código C
        compile_command = (
            f"gcc {self.source_code} -o {self.source_code.replace('.c', '.exe')}"
        )
        process = subprocess.Popen(
            compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return {"message": "Compilation failed", "result": stderr.decode("utf-8")}

        # Executar o código C compilado
        executable = (
            self.source_code.replace(".c", ".exe")
            if os.name == "nt"
            else self.source_code.replace(".c", "")
        )
        run_command = f"{executable} < {self.input_file} > {self.output_file}"
        process = subprocess.Popen(
            run_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return {"message": "Execution failed", "result": stderr.decode("utf-8")}

        return {"message": "Execution successful", "result": stdout.decode("utf-8")}
