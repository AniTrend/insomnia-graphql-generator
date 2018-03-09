import json
import os


class InputOutputHelper:

    @staticmethod
    def __get_base_dir():
        current_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_path, '..')

    @staticmethod
    def get_input_directory():
        base_dir = InputOutputHelper.__get_base_dir()
        return os.path.join(base_dir, 'io', 'input')

    @staticmethod
    def get_output_directory():
        base_dir = InputOutputHelper.__get_base_dir()
        return os.path.join(base_dir, 'io', 'output')

    @staticmethod
    def get_file_contents(file_name):
        input_dir = InputOutputHelper.get_input_directory()
        with open(os.path.join(input_dir, file_name)) as file:
            input_data = json.loads(file.read())
        return input_data
