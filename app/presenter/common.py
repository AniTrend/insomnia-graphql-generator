import json
import os

from app.util import InputOutputHelper
from app.model import Property, ResourceBody


class BasePresenter:

    def __init__(self, file_name: str):
        self.data = InputOutputHelper.get_file_contents(file_name)
        self.input_folder = InputOutputHelper.get_input_directory()
        self.output_folder = InputOutputHelper.get_output_directory()
        self.resource_groups = []
        self.workspaces = []
        self.requests = []

    def create_resources(self):
        resources = self.data[Property.Resources]
        for resource in resources:
            if ResourceBody.is_workspace(resource):
                self.__create_workspaces(resource)
                continue

            if ResourceBody.is_request_group(resource):
                self.__create_resource_groups(resource)
                continue

            if ResourceBody.is_request_type(resource):
                self.__create_resource_requests(resource)
                continue
        print()
        print(f"Generated {len(resources)} resources")

    def __create_workspaces(self, resource):
        print(f"Generating work space for {resource[Property.Name]}")
        self.workspaces.append({
            Property.Id: resource[Property.Id],
            Property.Name: resource[Property.Name],
            Property.Type: resource[Property.Type]
        })

    def __create_resource_groups(self, resource):
        self.resource_groups.append({
            Property.Id: resource[Property.Id],
            Property.Name: resource[Property.Name],
            Property.ParentId: resource[Property.ParentId],
            Property.Type: resource[Property.Type]
        })

    def __create_resource_requests(self, resource):
        self.requests.append({
            Property.Id: resource[Property.Id],
            Property.Name: resource[Property.Name],
            Property.ParentId: resource[Property.ParentId],
            Property.Body: resource[Property.Body],
            Property.Type: resource[Property.Type]
        })


class PersistencePresenter:

    def __init__(self, base: BasePresenter):
        self.base = base

    def create_directories(self):
        print()
        self.__create_top_level()

    def __create_top_level(self):
        print(f"Creating {len(self.base.workspaces)} work space directories")
        for workspace in self.base.workspaces:
            InputOutputHelper.create_directory(workspace[Property.Name])
            workspace[Property.Location] = workspace[Property.Name]
            for group in self.base.resource_groups:
                if group[Property.ParentId] == workspace[Property.Id]:
                    group[Property.Location] = os.path.join(workspace[Property.Location], group[Property.Name])
                    InputOutputHelper.create_directory(group[Property.Location])
            self.__create_sub_directories(workspace)
            self.__create_sub_files()

    def __key_exists_in(self, key) -> tuple:
        for group in self.base.resource_groups:
            if group[Property.Id] == key:
                return True, group
        return False, None

    def __create_sub_directories(self, workspace):
        print(f"Creating {len(self.base.resource_groups)} sub work space directories for {workspace[Property.Name]}")
        for child in self.base.resource_groups:
            (exists, parent) = self.__key_exists_in(child[Property.ParentId])
            if exists:
                child[Property.Location] = os.path.join(parent[Property.Location],
                                                        child[Property.Name])
                InputOutputHelper.create_directory(child[Property.Location])

    def __create_sub_files(self):
        print("Generating .graphql files into ./app/output/...")
        for group in self.base.resource_groups:
            for request in self.base.requests:
                exists, parent = self.__key_exists_in(request[Property.ParentId])
                if exists and request[Property.Body] is not None and Property.Text in request[Property.Body]:
                    request_body_text = json.loads(request[Property.Body][Property.Text])
                    if request_body_text is not None and Property.Query in request_body_text:
                        InputOutputHelper.create_file(parent[Property.Location],
                                                      f"{request[Property.Name]}.graphql",
                                                      request_body_text[Property.Query])
                        request[Property.Location] = os.path.join(group[Property.Location],
                                                                  f"{request[Property.Name]}.graphql")
        print()
