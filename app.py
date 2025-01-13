from javaCompile import compile_java
from javaValidade import validade_java

if __name__ == "__main__":
    
    java_directory = 'javaCodes'
    
    print(compile_java(java_directory))
    print(validade_java(java_directory,'entradas.txt','saida.txt'))