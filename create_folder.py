import os

class Create_folders_and_files:
    def __init__(self):
        print("select variance")

        self.question_user()
        self.exit_program()

    def create_folder(self, name_folder):
        if not os.path.exists(f"{name_folder}"):
            os.mkdir(name_folder)
            print(f"file with {name_folder} successful created")
        else:
            print(f"file with {name_folder} already exist")


    def create_file(self, name_file, extension_file=''):
        with open(file=f"{name_file}.{extension_file}",mode="w") as file:
            file.write("")

    def create_file_in_folder(self,name_folder,name_file,extension_file=''):
        if not os.path.exists(f"{name_folder}"):
            os.mkdir(name_folder)

            with open(file=f"{name_folder}/{name_file}.{extension_file}", mode="w") as file:
                file.write("")


    def question_user(self):
        try:
            variance ="[1:create folder]: [2:create file]: [3:create file in folder]: "
            self.variance = input(variance)

            print("=" * len(variance))
            match self.variance:
                case "1":
                    self.create_folder(input("Enter name folder: "))
                case "2":
                    self.create_file(input("Enter name file: "))

                case "2":
                    self.create_file_in_folder(
                        input("Enter name folder: "),
                        input("Enter name file: ")
                    )

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
