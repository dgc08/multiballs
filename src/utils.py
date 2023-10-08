import os
import subprocess


def get_device_name_by_number(device_number, p):
    device_info = p.get_device_info_by_index(device_number)
    device_name = device_info['name']
    return device_name

def get_command_output(com):
    # Run the command and capture its output
    p = subprocess.Popen(com, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()

    # Convert the byte string to a regular string
    output_str = output.decode('utf-8')

    # Print the output
    return output_str

def get_project_root():
    current_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    project_root = os.path.dirname(current_path)  # Get the directory containing the script

    return os.path.dirname(project_root).replace("\\", "/") + "/"  # Get the directory above the script's directory (the project root)


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = {} # Initialize the shared variable
        return cls._instance

    def get_value(self, key=None):
        return self.value.get(key, None)

    def set_value(self, new_value, key=None):
        self.value[key] = new_value

    @classmethod
    def get_instance(cls):
        return cls.__new__(cls)