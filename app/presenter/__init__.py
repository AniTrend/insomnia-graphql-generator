from app.util import InputOutputHelper
from app.model import Property, ResourceBody


class BasePresenter:

    def __init__(self, file_name):
        self.data = InputOutputHelper.get_file_contents(file_name)
        self.input_folder = InputOutputHelper.get_input_directory()
        self.output_folder = InputOutputHelper.get_output_directory()
        self.directory_tree = []

    def generate_resource_map(self):
        resources = self.data[Property.Resources]
        for resource in resources:
            if ResourceBody.is_folder_type(resource):
                self.directory_tree.append({
                    Property.Id: resource[Property.Id],
                    Property.Name: resource[Property.Name],
                    Property.ParentId: resource[Property.ParentId],
                    Property.Children: None
                })
                continue
            if ResourceBody.is_request_type(resource):
                pass
        pass
