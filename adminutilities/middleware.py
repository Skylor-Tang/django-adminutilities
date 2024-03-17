from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from adminutilities.utils import get_register_admin_tool_functions


def get_admin_tool_functions(request):
    """
    Retrieves the admin tool functions for the given request.

    Args:
        request (HttpRequest): The request object.

    Returns:
        list: The list of admin tool functions.
    """
    if not hasattr(request, "_cached_tool_functions"):
        request._cached_tool_functions = get_register_admin_tool_functions()
    return request._cached_tool_functions


class GetAllAdminToolFunctionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Adds the admin tool functions to the request object.

        Args:
            request (HttpRequest): The request object.
        """
        request.admin_tool_functions = SimpleLazyObject(lambda: get_admin_tool_functions(request))
