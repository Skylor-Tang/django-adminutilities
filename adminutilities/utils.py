import importlib
import os
from collections import defaultdict

from django.apps import apps


def get_register_admin_tool_functions():
    """
    Get a dictionary of registered admin tool functions.

    Returns:
        A dictionary where the keys are the app names and the values are lists of tuples
        containing the tool function name and path.
    """
    admin_tool_functions = defaultdict(list)
    installed_apps = apps.get_app_configs()

    for app in installed_apps:
        admin_tools_path = os.path.join(app.path, "admin_tools.py")

        if os.path.exists(admin_tools_path):
            admin_tools_module = importlib.import_module(app.name + ".admin_tools")
            functions = [name for name, obj in vars(admin_tools_module).items() if callable(obj) and hasattr(obj, "is_admin_tools") and getattr(obj, "is_admin_tools")]

            for function_name in functions:
                function_path = f"{app.name}.{function_name}"
                admin_tool_functions[app.name].append((function_name, function_path))

    return admin_tool_functions


def get_register_admin_tool_function_paths() -> list:
    """
    Get a list of registered admin tool function paths.

    Returns:
        A list of function paths in the format 'app_name.function_name'.
    """
    register_admin_tool_functions = get_register_admin_tool_functions()

    function_paths = []

    for _, function_infos in register_admin_tool_functions.items():
        for function_info in function_infos:
            function_paths.append(function_info[1])

    return function_paths


def execute_module_function(function_path: str):
    """
    Execute a function in the module's admin_tools.

    Args:
        function_path: The path of the function in the format 'app_name.function_name'.

    Raises:
        ImportError: If the function_path is not a valid module path.
        ImportError: If the module does not define the specified function.
    """
    try:
        app_name, function_name = function_path.split(".")
        module_path = app_name + ".admin_tools"
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % function_path) from err

    admin_tools_module = importlib.import_module(module_path)

    try:
        getattr(admin_tools_module, function_name)()
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/function' % (module_path, function_name)) from err
