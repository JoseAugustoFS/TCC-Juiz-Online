from JavaJudge.javaCompile import compile_java
from JavaJudge.javaValidade import validade_java
from JavaJudge.javaEvaluate import evaluate_java
from JavaJudge.javaOptimize import optmize_java

def judge(directory):
    compilation = compile_java(directory)
    if(compilation["status"]):
        validated_percent = validade_java(directory,'entradas.txt', 'saida.txt','resposta.txt')
        if(validated_percent == 100.0):
            evalutation = evaluate_java(directory, 'avaliacao.txt')
            optimization = optmize_java(directory, 'Faça uma classe calculadora que consiga somar e subtrair.', 'avaliacao.txt')
            return {
                "compilation": compilation["message"], 
                "validated_percent": validated_percent, 
                "evalutation": evalutation["message"], 
                "optimization": optimization["message"]
                }
        else:
            return {"compilation": compilation["message"], "validated_percent": validated_percent}
    else:
        return compilation["message"]



    