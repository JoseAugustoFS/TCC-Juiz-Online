import os
import subprocess
from JavaJudge.javaJudge import judge
from CJudge.cValidade import cValidade

system = os.name  # Identifica se é Windows ou Linux/macOS

if __name__ == "__main__":

    language = "C"  # Alterar para "JAVA" para rodar código Java

    if language == "JAVA":
        java_directory = "./javaCodes"
        java_io_directory = "./javaIO"
        statement = "Faça uma classe calculadora que consiga somar e subtrair."

        try:
            with open(
                os.path.join(java_io_directory, "entradas.txt"), "r"
            ) as input_file:
                input_data = input_file.read()
            with open(
                os.path.join(java_io_directory, "resposta.txt"), "r", encoding="utf-8"
            ) as answer_file:
                answer_data = answer_file.read()
        except Exception as e:
            print("Erro ao ler arquivos de entrada/saída: " + str(e))

        inputs = input_data.split("===")
        answers = answer_data.split("===")
        answers = [item.strip() for item in answers]
        answers.pop(0)  # Remove possível entrada vazia no início

        result = judge(java_directory, inputs, answers, statement)

        print(result["compilation"])
        print(result["validated_percent"])
        if result["validated_percent"] == 100.0:
            print(result["evalutation"])
            print(result["optimization"])

            response = "############\nValidação\n############\n"
            for index, evalutation_result in enumerate(result["evalutation_result"]):
                response += (
                    "Teste "
                    + str(index + 1)
                    + ":\n"
                    + evalutation_result
                    + "\n======================================\n"
                )
            response += "############\nOtimização\n############\n"
            for index, optimization_result in enumerate(result["optimization_result"]):
                response += (
                    "Teste "
                    + str(index + 1)
                    + ":\n"
                    + optimization_result
                    + "\n======================================\n"
                )

            decodeType = "unicode_escape" if system == "nt" else "utf-8"
            try:
                with open(
                    os.path.join(java_io_directory, "saida.txt"), "w"
                ) as output_file:
                    output_file.write(
                        str("===\n" + "\n===\n".join(result["validation_result"]))
                        .encode("utf-8")
                        .decode(decodeType)
                    )
                with open(
                    os.path.join(java_io_directory, "avaliacao.txt"), "w"
                ) as response_file:
                    response_file.write(response.encode("utf-8").decode(decodeType))
            except Exception as e:
                print("Erro ao escrever arquivos de saída:", str(e))

    elif language == "C":
        c_judge = cValidade(
            source_code="cCodes/programa.c",
            executable=(
                "cCodes/programa.exe" if os.name == "nt" else "./cCodes/programa"
            ),
            input_file="cIO/entradas.txt",
            output_file="cIO/resposta.txt",
        )

        if c_judge.compile():
            c_judge.load_test_cases()
            c_judge.run_tests()
        else:
            print("Linguagem inválida.")
else:
    print("Linguagem inválida.")