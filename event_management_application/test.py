import os
import time
def get_installed_apps():
    installed_apps = [
     "adminlte3",
    "adminlte3_theme",
    "django_crontab",
    "event_management_application.apps.EventManagementApplicationConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "rest_framework",
    ]

    # Get the directory containing the modules
    modules_dir = os.path.join('/Users/jashkakadiya/Desktop/Python_training/event_management_', 'another')

    # Add each module in the modules directory to the installed apps
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path):
            installed_apps.append(module_name)

    return installed_apps


INSTALLED_APPS = get_installed_apps()
