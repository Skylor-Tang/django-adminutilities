from functools import wraps


def admin_tool(func):
    """
    Decorator function to mark a function as an admin tool.

    Args:
        func: The function to be marked as an admin tool.

    Returns:
        The wrapped function.
    """
    setattr(func, "is_admin_tools", True)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper