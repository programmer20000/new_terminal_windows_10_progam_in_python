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
        with open(file=f"{name_file}.{extension_file}", mode="w") as file:
            file.write("")

    def create_file_in_folder(self, name_folder, name_file, extension_file=''):
        if not os.path.exists(f"{name_folder}"):
            os.mkdir(name_folder)

            with open(file=f"{name_folder}/{name_file}.{extension_file}", mode="w") as file:
                file.write("")

    def search(self):
        select_variance = "[1:search file]: [2:search folder]: "
        self.select_variance = input(select_variance)

        def search_file(name_file):
            if os.path.isfile(name_file):
                print(f"file with name {name_file} is in this directory")
            else:
                print(f"file with name {name_file} not is in this directory")

        def search_folder(name_folder):
            if os.path.isdir(name_folder):
                print(f"folder with name {name_folder} is in this directory")
            else:
                print(f" folder with name {name_folder} not is in this directory")

        match self.select_variance:
            case "1":
                search_file(input("Enter name file: "))
            case "2":
                search_folder(input("Enter name folder: "))

    def question_user(self):
        try:
            variance = "[1:create folder]: [2:create file]: [3:create file in folder]: [4:search]: "
            self.variance = input(variance)

            print("=" * len(variance))
            match self.variance:
                case "1":
                    self.create_folder(input("Enter name folder: "))
                case "2":
                    self.create_file(input("Enter name file: "))

                case "3":
                    self.create_file_in_folder(
                        input("Enter name folder: "),
                        input("Enter name file: ")
                    )
                case "4":
                    self.search()

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


if __name__ == '__main__':
    Create_folders_and_files()
