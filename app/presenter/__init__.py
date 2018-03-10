import json
import os

from app.util import InputOutputHelper
from app.model import Property, ResourceBody


class BasePresenter:

    def __init__(self, file_name):
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

    def __create_workspaces(self, resource):
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

    def __init__(self, base):
        self.base = base

    def create_directories(self):
        self.__create_top_level()

    def __create_top_level(self):
        for workspace in self.base.workspaces:
            InputOutputHelper.create_directory(workspace[Property.Name])
            workspace[Property.Location] = workspace[Property.Name]
            for group in self.base.resource_groups:
                if group[Property.ParentId] == workspace[Property.Id]:
                    group[Property.Location] = os.path.join(workspace[Property.Location], group[Property.Name])
                    InputOutputHelper.create_directory(group[Property.Location])
            self.__create_sub_directories()
            self.__create_sub_files()

    def __key_exists_in(self, key):
        for group in self.base.resource_groups:
            if group[Property.Id] == key:
                return True, group
        return False, None

    def __create_sub_directories(self):
        for child in self.base.resource_groups:
            exists, parent = self.__key_exists_in(child[Property.ParentId])
            if exists:
                child[Property.Location] = os.path.join(parent[Property.Location],
                                                        child[Property.Name])
                InputOutputHelper.create_directory(child[Property.Location])

    def __create_sub_files(self):
        for group in self.base.resource_groups:
            for request in self.base.requests:
                exists, parent = self.__key_exists_in(request[Property.ParentId])
                if exists and request[Property.Body] is not None and Property.Text in request[Property.Body]:
                    request_body_text = json.loads(request[Property.Body][Property.Text])
                    if request_body_text is not None and Property.Query in request_body_text:
                        InputOutputHelper.create_file(parent[Property.Location],
                                                      "{}.graphql".format(request[Property.Name]),
                                                      request_body_text[Property.Query])
                        request[Property.Location] = os.path.join(group[Property.Location],
                                                                  "{}.graphql".format(request[Property.Name]))
