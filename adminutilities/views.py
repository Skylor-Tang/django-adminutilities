from django.contrib import admin, messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from adminutilities.utils import execute_module_function


class CustomFunctionFormView(UserPassesTestMixin, TemplateView):
    """
    A view for executing custom functions via the admin interface.

    This view requires the user to be a superuser in order to execute functions.
    If the user is not a superuser, they will be redirected to the login page or receive a permission denied message.

    Attributes:
        template_name (str): The name of the template to be rendered.
        success_url (str): The URL to redirect to after executing the functions.
        permission_denied_message (str): The message to display when the user does not have permission to execute functions.
        raise_exception (bool): Whether to raise a PermissionDenied exception when the user does not have permission.
        login_url (str): The URL to redirect to if the user is not authenticated.

    Methods:
        handle_no_permission: Handles the case when the user does not have permission to execute functions.
        test_func: Checks if the user is a superuser.
        execute_function: Executes a custom function given its path.
        post: Handles the POST request and executes the selected functions.
        get_context_data: Adds additional context data to be passed to the template.
    """

    template_name = "adminutilities/admin/customfunction_form.html"
    success_url = reverse_lazy("customcunction_admin")
    permission_denied_message = "Only superuser can execute via admin."
    raise_exception = False
    login_url = None

    def handle_no_permission(self):
        """
        Handles the case when the user does not have permission to execute functions.

        If `raise_exception` is True or the user is authenticated, a PermissionDenied exception is raised.
        Otherwise, a simple HTML response with a login message is returned.
        """
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponse("<h1>please login</h1>")

    def test_func(self):
        """
        Checks if the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.request.user.is_superuser

    def execute_function(self, function_path: str):
        """
        Executes a custom function given its path.

        Args:
            function_path (str): The path to the function to be executed.
        """
        execute_module_function(function_path)

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request and executes the selected functions.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponseRedirect: The response object for redirecting to the success URL.
        """
        function_paths = request.POST.getlist("function_path", None)

        if function_paths:
            try:
                for function_path in function_paths:
                    self.execute_function(function_path)
                    messages.success(self.request, f"Function {function_path} successfully")

            except Exception as err:
                messages.error(
                    self.request,
                    f"Couldn't execute selected operation, something went wrong. Received error: {err}",
                )
        else:
            messages.warning(self.request, f"Has no selected operation to do!")

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to be passed to the template.

        Returns:
            dict: The context data.
        """
        context = super().get_context_data(**kwargs)
        assert hasattr(self.request, "admin_tool_functions"), "Please add 'adminutilities.middleware.GetAllAdminToolFunctionsMiddleware' " "to MIDDLEWARE in settings.py"
        context["admin_tool_functions"] = dict(self.request.admin_tool_functions)
        context["title"] = "Execute custom function"
        context["site_header"] = admin.site.site_header
        context["has_permission"] = True
        return context
