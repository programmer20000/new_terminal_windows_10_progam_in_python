import os
from time import sleep

class Create_folders_and_files:
    def __init__(self):
        print("select variance")

        self.question_user()
        self.exit_program()

    def create_folder(self, name_folder):
        os.system(f"mkdir {name_folder}")

    def create_file(self, name_file, extension_file=''):
        os.system(f"type nul > {name_file}.{extension_file}")

    def start_program(self):
        pass

    def question_user(self):
        try:
            variance ="[1:create folder]: [2:create file]: [3:start program]: "
            self.variance = input(variance)

            print("=" * len(variance))
            match self.variance:
                case "1":
                    self.create_folder(input("Enter name folder: "))
                case "2":
                    self.create_file(input("Enter name file: "))

                case _:
                    print("variance not found")
                    
        except:
            return "finish"

    def exit_program(self):
        try:
            self.variance = input("[y:exit program]: [n:continue program]: ")
            while True:
                match self.variance:
                    case "y":
                        break

                    case "n":
                        self.question_user()
                        continue

                    case _:
                        print("variance not found")
                        break

        except:
            return "finish"

Create_folders_and_files()
