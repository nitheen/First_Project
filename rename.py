import os

def rename():
    file_list = os.listdir(r"C:\Users\Nitheen\Desktop\Udacity\prank")
    print(file_list)

    initial_path = os.getcwd()
    os.chdir(r"C:\Users\Nitheen\Desktop\Udacity\prank")

    for file in file_list:
        os.rename(file, file.translate("0123456789"))
        print(file)
    os.chdir(initial_path)

rename()