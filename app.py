import os
from JavaJudge.javaJudge import judge

system = os.name

if __name__ == "__main__":
    
    language = "JAVA"

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
            print("Error: " + str(e))

        inputs = input.split("===")
        answers = answer.split("===")
        answers = [item.strip() for item in answers]
        answers.pop(0)

        result = judge(java_directory, inputs, answers, statement)

        print(result["compilation"])
        print(result["validated_percent"])
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
            with open(os.path.join(java_io_directory, "avaliacao.txt"), "a") as response_file:
                response_file.truncate(0)
                response_file.write(response.encode('utf-8').decode(decodeType))
        except Exception as e:
            print("Error: " + str(e))

    elif (language=="C"):
        print("Implementar C")
    else:
        print("Invalid language.")
