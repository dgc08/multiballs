import subprocess


def get_command_output(com):
    # Run the command and capture its output
    p = subprocess.Popen(com, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()

    # Convert the byte string to a regular string
    output_str = output.decode('utf-8')

    # Print the output
    return output_str