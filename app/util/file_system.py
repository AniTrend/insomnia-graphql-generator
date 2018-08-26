import json
import os
from pathlib import Path


class InputOutputHelper:

    @staticmethod
    def __get_base_dir() -> str:
        current_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_path, '..')

    @staticmethod
    def get_input_directory() -> str:
        base_dir = InputOutputHelper.__get_base_dir()
        return os.path.join(base_dir, 'io', 'input')

    @staticmethod
    def get_output_directory() -> str:
        base_dir = InputOutputHelper.__get_base_dir()
        return os.path.join(base_dir, 'io', 'output')

    @staticmethod
    def get_file_contents(file_name):
        with open(os.path.join(file_name)) as file:
            input_data = json.loads(file.read())
        return input_data

    @staticmethod
    def create_directory(directory_path) -> None:
        creation_path = os.path.join(InputOutputHelper.get_output_directory(), directory_path)
        if not os.path.exists(creation_path):
            path = Path(creation_path)
            path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_file(directory_path, filename, contents) -> None:
        creation_path = os.path.join(InputOutputHelper.get_output_directory(), directory_path)
        if not os.path.exists(creation_path):
            path = Path(creation_path)
            path.mkdir(parents=True, exist_ok=True)
        with open(os.path.join(creation_path, filename), "w+") as writer:
            writer.write(contents)
