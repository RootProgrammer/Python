"""                     //////////////////////////////////////////
                        ///                                    ///
                        ///        Django PROJECT CREATION     ///
                        ///      Version 1.2, Author: ZamaaN   ///
                        ///                                    ///
                        //////////////////////////////////////////
"""


import os
from pathlib import *
import webbrowser

class Django_tasks:
    def __init__(self):
        project_name = input("Enter Your Project Name: ")
        self.project_name = project_name.replace(" ", "_")
        app_name = input("Enter Your App Name: ")
        self.app_name = app_name.replace(" ", "_")

    def create_project(self):
        self.base_directory = Path(__file__).parent.absolute()
        self.project_path = self.base_directory / self.project_name
        if not self.project_path.is_dir():
            os.chdir(self.base_directory)
            os.system("django-admin startproject " + self.project_name)

    def create_app(self):
        self.app_path = self.project_path / self.app_name
        if not self.app_path.is_dir():
            os.chdir(self.project_path)
            os.system("python manage.py startapp "+self.app_name)
            os.system("python manage.py makemigrations")
            os.system("python manage.py migrate")

    def edit_settings(self):
        self.settings_path = self.project_path / self.project_name / "settings.py"
        with open(self.settings_path, 'r') as file:
            file_data = file.readlines()

        app_entry = f"'{self.app_name}'"

        with open(self.settings_path, 'w+') as file:
            for line in file_data:
                if line == "INSTALLED_APPS = [\n":
                    line += "\t"+app_entry+",\n"
                file.write(line)

    def check_path(self):
        print(self.base_directory, self.project_path, self.app_path, self.settings_path, sep="\n")

    def run_django_server(self):
        os.chdir(self.project_path)
        webbrowser.open("http://127.0.0.1:8000/")
        os.system("python manage.py runserver")

if __name__=='__main__':
    print("\t\t\t///////////////////////////////////////////\n\t\t\t///\t\t\t\t\t///\n\t\t\t///\t  Django PROJECT CREATION\t///\n\t\t\t///\tVersion 1.2, Author: ZamaaN\t///\n\t\t\t///\t\t\t\t\t///\n\t\t\t///////////////////////////////////////////\n")

    task = Django_tasks()

    task.create_project()
    task.create_app()
    task.edit_settings()
    task.check_path()
    task.run_django_server()