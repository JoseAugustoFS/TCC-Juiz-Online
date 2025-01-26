from javaCompile import compile_java
from javaValidade import validade_java
from javaEvaluate import evaluate_java
from javaOptimize import optmize_java
import time

if __name__ == "__main__":
    
    java_directory = 'javaCodes'
    
    print(compile_java(java_directory))
    print(validade_java(java_directory,'entradas.txt', 'saida.txt','resposta.txt'))

    print(evaluate_java(java_directory, 'avaliacao.txt'))
    print(optmize_java(java_directory, 'Faça uma classe calculadora que consiga somar e subtrair.', 'avaliacao.txt'))

    time.sleep(0.5)
    with open(java_directory+'/saida.txt', 'w') as file:
        file.truncate(0)