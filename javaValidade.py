import subprocess
import os

system = os.name

def run_java(directory, input, output):
    try:
        # Find the main Java class file
        main_class = None
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.java'):
                    with open(os.path.join(root, file), 'r') as java_file:
                        if 'void main' in java_file.read():
                            main_class = os.path.splitext(file)[0]
                            break
        
        if main_class:
            # Run the Java program with the input and output redirection
            input_path = os.path.join(directory, input)
            output_path = os.path.join(directory, output)
            
            with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
                result = subprocess.run(['java', main_class], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, cwd=directory)
            
            if result.returncode == 0:
                return "Execution successful."
            else:
                return "Execution failed: " + result.stderr
        else:
            return "No compiled Java class found to execute."
    except Exception as e:
        return "An error occurred during execution: " + str(e)
    
def validade_java(directory, input_file_dir, output_file_dir, answer_file_dir):
    try:
        with open(os.path.join(directory, input_file_dir), 'r') as input_file:
            inputs = input_file.read().split('===')
        
        results = []
        for i, single_input in enumerate(inputs):
            temp_input_path = os.path.join(directory, f'temp_input_{i}.txt')
            temp_output_path = os.path.join(directory, f'temp_output_{i}.txt')
            
            with open(temp_input_path, 'w') as temp_input_file:
                temp_input_file.write(single_input.strip())
            
            result = run_java(directory, f'temp_input_{i}.txt', f'temp_output_{i}.txt')
            results.append(result)
            with open(temp_output_path, 'r') as temp_output_file:
                output_content = temp_output_file.read()
            
            if system == 'nt':  # Windows
                decodeType = 'unicode_escape'
            else: #Linux ou macOS (ou qualquer outro)
                decodeType = 'utf-8'

            with open(os.path.join(directory, output_file_dir), 'a') as output_file:
                output_file.write(f'===\n{output_content}'.encode('utf-8').decode(decodeType))
  
            os.remove(temp_input_path)
            os.remove(temp_output_path)
        with open(os.path.join(directory, output_file_dir), 'r', encoding='utf-8') as output_file:
                output = output_file.read().split('===')
        with open(os.path.join(directory, answer_file_dir), 'r', encoding='utf-8') as answer_file:
            answer = answer_file.read().split('===')
        
        if output == answer:
            return "All outputs match the expected answers."
        else:
            return "Some outputs do not match the expected answers."

    except Exception as e:
        return "An error occurred during validation: " + str(e)