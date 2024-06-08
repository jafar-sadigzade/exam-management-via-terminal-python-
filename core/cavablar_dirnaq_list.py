import os


def read_file(prompt):
    """
    Prompt the user to input a filename and read the file's content.
    Checks for the file in the current directory, 'core', and 'txt' subdirectories.

    :param prompt: The prompt message to ask for the filename
    :return: The content of the file as a string
    """
    directories_to_check = [os.getcwd(), 'core', 'txt']

    while True:
        filename = input(prompt)
        file_found = False

        for directory in directories_to_check:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_found = True
                with open(filepath, "r") as file:
                    return file.read()

        if not file_found:
            print("Daxil etdiyiniz fayl tapılmadı! Yenidən cəhd edin!")


data = read_file('Cavablar olan faylın adını yazın: ')


def dzgn_cvb(a, b):
    return data[a:b]
