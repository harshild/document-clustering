import os
import html2text
from pip._vendor.chardet import detect


def main():
    input_file_list = os.listdir(os.curdir + "/files/")
    for filename in sorted(input_file_list):
        with open("./files/"+ filename, 'r',encoding="latin-1", errors="surrogateescape") as f:
            print(f.name)
            print(f.read())


if __name__ == '__main__':
    main()