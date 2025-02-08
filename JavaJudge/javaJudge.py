from JavaJudge.javaCompile import compile_java
from JavaJudge.javaValidade import validade_java
from JavaJudge.javaEvaluate import evaluate_java
from JavaJudge.javaOptimize import optmize_java

def judge(directory, inputs, answers, statement):
    compilation = compile_java(directory)
    if(compilation["status"]):
        validation = validade_java(directory, inputs, answers)
        if(validation["validated_percent"] == 100.0):
            evalutation = evaluate_java(directory)
            optimization = optmize_java(directory, statement)
            return {
                "compilation": compilation["message"], 
                "validated_percent": validation["validated_percent"],
                "validation_result": validation["result"],
                "evalutation": evalutation["message"],
                "evalutation_result": evalutation["result"], 
                "optimization": optimization["message"],
                "optimization_result": optimization["result"]
                }
        else:
            return {"compilation": compilation["message"], "validated_percent": validation["validated_percent"], "validation_result": validation["result"]}
    else:
        return compilation["message"]



    