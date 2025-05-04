import os
import subprocess
from JavaJudge.javaJudge import judge
from CJudge.cValidade import cValidade
from CJudge.CAnalyzer import CAnalyzer
from CJudge.COptimize import optimize_c

system = os.name

if __name__ == "__main__":

    language = "C" 

    if(language=="JAVA"):
        java_directory = "./javaCodes"
        java_io_directory = "./javaIO"
        statement = "Faça uma classe calculadora que consiga somar e subtrair."

        try:
            with open(os.path.join(java_io_directory, "entradas.txt"), "r") as input_file:
                input = input_file.read()
            with open(os.path.join(java_io_directory, "resposta.txt"), "r", encoding="utf-8") as answer_file:
                answer = answer_file.read()
        except Exception as e:
            print("Erro: " + str(e))

        inputs = input.split("===")
        answers = answer.split("===")
        answers = [item.strip() for item in answers]
        answers.pop(0)

        result = judge(java_directory, inputs, answers, statement)

        print(result["compilation"])
        print(result["validated_percent"])
        if (result["validated_percent"] == 100.0):
            print(result["evalutation"])
            print(result["optimization"])

            response = "############\nValidação\n############\n"
            for index, evalutation_result in enumerate(result["evalutation_result"]):
                response += "Teste "+str(index+1)+":\n"+evalutation_result+"\n======================================\n"
            response +="############\nOtimização\n############\n"
            for index, optimization_result in enumerate(result["optimization_result"]):
                response += "Teste "+str(index+1)+":\n"+optimization_result+"\n======================================\n"

        if system == "nt":  # Windows
                decodeType = "unicode_escape"
        else: #Linux ou macOS (ou qualquer outro)
            decodeType = "utf-8"
        try:
            with open(os.path.join(java_io_directory, "saida.txt"), "a") as output_file:
                output_file.truncate(0)
                output_file.write(str("===\n"+"\n===\n".join(result["validation_result"])).encode("utf-8").decode(decodeType))
            if (result["validated_percent"] == 100.0):
                with open(os.path.join(java_io_directory, "avaliacao.txt"), "a") as response_file:
                    response_file.truncate(0)
                    response_file.write(response.encode('utf-8').decode(decodeType))
        except Exception as e:
            print("Error: " + str(e))

    elif language == "C":
        c_io_directory = "./cIO"
        c_judge = cValidade(
            source_code="cCodes/programa.c",
            executable=(
                "cCodes/programa.exe" if os.name == "nt" else "./cCodes/programa"
            ),
            input_file="cIO/entradas.txt",
            output_file="cIO/resposta.txt",
            output_log_file="cIO/Saida.txt",
        )

        if c_judge.compile():
            c_judge.load_test_cases()
            c_judge.run_tests()
        else:
            print("Linguagem inválida.")

        c_analyzer = CAnalyzer(
            source_code="cCodes/programa.c",
            input_file="cIO/entradas.txt",
            output_file="cIO/resposta.txt",
        )

        analysis_result = c_analyzer.analyze_code()

        print(analysis_result["message"])
        print(analysis_result["result"])

        if analysis_result["message"] == "Code analyzed":
            response = "############\nAnálise do Código C\n############\n"
            for index, evalutation_result in enumerate(analysis_result["result"]):
                response += (
                    "Teste "
                    + str(index + 1)
                    + ":\n"
                    + evalutation_result
                    + "\n======================================\n"
                )

            try:
                with open(
                    os.path.join(c_io_directory, "AnaliseCodigo.txt"),
                    "w",
                    encoding="utf-8",
                ) as response_file:
                    response_file.write(response)
                print("Resultado da análise salvo em cIO/AnaliseCodigo.txt.")
            except Exception as e:
                print("Erro ao escrever o resultado da análise:", str(e))

        statement = "Desenvolva um programa que solicite ao usuário que insira um ano no formato de quatro dígitos (ex: 2024) e determine se esse ano é ou não bissexto."
        optimization_result = optimize_c("./cCodes", statement)

        print(optimization_result["message"])
        print(optimization_result["result"])

        if optimization_result["message"] == "Code optimized":
            optimization_response = (
                "############\nOtimização do Código C\n############\n"
            )
            optimization_response += "\n".join(optimization_result["result"])

            try:
                with open(
                    os.path.join(c_io_directory, "OtimizacaoCodigo.txt"),
                    "w",
                    encoding="utf-8",
                ) as optimization_file:
                    optimization_file.write(optimization_response)
                print("Resultado da otimização salvo em cIO/OtimizacaoCodigo.txt.")
            except Exception as e:
                print("Erro ao escrever o resultado da otimização:", str(e))
    else:
        print("Linguagem inválida.")
        