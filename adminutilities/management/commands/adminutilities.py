from django.core.management.base import BaseCommand

from adminutilities.utils import get_register_admin_tool_function_paths, execute_module_function


class Command(BaseCommand):
    help = "Execute adminutilities custom function"

    def add_arguments(self, parser):
        parser.add_argument("function_path", nargs="+", type=str, help=f"Current optional: {', '.join(get_register_admin_tool_function_paths())}")

    def handle(self, *args, **options):
        function_paths = options["function_path"]

        for function_path in function_paths:
            try:
                execute_module_function(function_path)
                self.stdout.write(self.style.SUCCESS(f"Function {function_path} successfully"))
            except Exception as err:
                self.stderr.write(self.style.ERROR(err))
