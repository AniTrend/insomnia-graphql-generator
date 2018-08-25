

class Property:
    """Properties For Export File"""
    Id = "_id"
    Type = "_type"
    Body = "body"
    Text = "text"
    Query = "query"
    Name = "name"
    ParentId = "parentId"
    Resources = "resources"
    Groups = "groups"
    Requests = "requests"
    Location = "location"


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
    def is_workspace(resource):
        return resource[Property.Type] == ObjectType.WorkSpace

    @staticmethod
    def is_request_group(resource):
        return resource[Property.Type] == ObjectType.RequestGroup

    @staticmethod
    def is_request_type(resource):
        return resource[Property.Type] == ObjectType.Request
