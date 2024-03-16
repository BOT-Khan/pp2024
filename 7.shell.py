import subprocess

while True:
    command = input("$ ")

    if command.lower() == 'exit':
        break

    input_redirect = '<' in command
    output_redirect = '>' in command

    if input_redirect:
        try:
            input_index = command.index('<')
            input_file = command[input_index + 1:].strip()
            command = command[:input_index].strip()
            with open(input_file, 'r') as input_file_obj:
                output = subprocess.run(command, shell=False, text=True, capture_output=True, input=input_file_obj)
        except FileNotFoundError:
            print(f"Error: The input file '{input_file}' does not exist.")
        except PermissionError:
            print(f"Error: You do not have permission to access the input file '{input_file}'.")
    else:
        output = subprocess.run(command, shell=False, text=True, capture_output=True)

    if output_redirect:
        try:
            output_index = command.index('>')
            output_file = command[output_index + 1:].strip()
            with open(output_file, 'w') as output_file_obj:
                output_file_obj.write(output.stdout)
        except FileNotFoundError:
            print(f"Error: The output file '{output_file}' does not exist.")
        except PermissionError:
            print(f"Error: You do not have permission to access the output file '{output_file}'.")
    else:
        print(output.stdout)