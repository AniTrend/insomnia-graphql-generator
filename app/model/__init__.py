

class Property:
    """Properties For Export File"""
    Id = "_id"
    Type = "_type"
    Body = {"body", "text"}
    Name = "name"
    ParentId = "parentId"
    Resources = "resources"
    Children = "children"


class ObjectType:
    """Resource Types For Export File"""
    WorkSpace = "workspace"
    Environment = "environment"
    Cookies = "cookie_jar"
    RequestGroup = "request_group"
    Request = "request"


class ResourceBody:
    """Request Body Segments"""
    Query = "query"
    Variables = "variables"
    Operation = "operationName"

    @staticmethod
    def is_folder_type(resource):
        return resource[Property.Type] is ObjectType.WorkSpace or resource[Property.Type] is ObjectType.RequestGroup

    @staticmethod
    def is_request_type(resource):
        return resource[Property.Type] is ObjectType.Request

    @staticmethod
    def create_parent_child(resource, dictionary):
        pass
