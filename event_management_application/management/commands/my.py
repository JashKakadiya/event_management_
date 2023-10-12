from django.core.management.templates import TemplateCommand
import os


class Command(TemplateCommand):
    help = "My custom startapp command."
    
    def handle(self, *args, **options):
        app_name = options['name']
        self.stdout.write(app_name + "\n")
        base_directory = '/Users/jashkakadiya/Desktop/Python_training/event_management_/another/'
        target = os.path.join(base_directory, app_name)
        os.makedirs(target, exist_ok=True)
        super().handle('app', app_name=app_name, target=target, **options)
        self.stdout.write(f"App '{app_name}' created successfully in '{target}'.")
