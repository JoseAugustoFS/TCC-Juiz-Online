from JavaJudge.javaJudge import judge

if __name__ == "__main__":
    
    language = "JAVA"

    if(language=="JAVA"):
        java_directory = './javaCodes'

        with open(java_directory+'/saida.txt', 'w') as file:
            file.truncate(0)
        with open(java_directory+'/avaliacao.txt', 'w') as file:
            file.truncate(0)
        
        print(judge(java_directory))
    elif (language=="C"):
        print("Implementar C")
    else:
        print("Invalid language.")