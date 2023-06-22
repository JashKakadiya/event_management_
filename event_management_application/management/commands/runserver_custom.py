import os
from django.core.management.base import BaseCommand
from django.core.management.commands.runserver import Command as RunserverCommand


def find_settings_file():
    current_directory = os.getcwd()
    for root, dirs, files in os.walk(current_directory):
        if "settings.py" in files:
            return os.path.join(root, "settings.py")
    return None


class Command(RunserverCommand):
    help = "Starts the custom runserver."

    def handle(self, args, *options):
        # Find the settings.py file
        settings_file = find_settings_file()

        if not settings_file:
            self.stdout.write("Unable to find settings.py file.")
            return

        # Get the app names available in the molecular folder
        molecular_apps = [
            app_name
            for app_name in os.listdir("molecules")
            if os.path.isdir(os.path.join("molecules", app_name))
        ]

        # Update the INSTALLED_APPS list in settings.py
        with open(settings_file, "r") as file:
            lines = file.readlines()

        with open(settings_file, "w") as file:
            for line in lines:
                if "INSTALLED_APPS" in line:
                    line = line.rstrip("\n")
                    line += ',\n    ' + ',\n    '.join(f'"molecular.{app_name}"' for app_name in molecular_apps)
                    line += "\n"
                file.write(line)

        self.stdout.write("App names added to INSTALLED_APPS in settings.py.")
        super().handle(*args, **options)

