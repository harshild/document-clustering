import os
import html2text
from pip._vendor.chardet import detect


def main():
    input_file_list = os.listdir(os.curdir + "/files/")
    for filename in sorted(input_file_list):
        with open("./files/" + filename, 'r', encoding="latin-1", errors="surrogateescape") as f:
            print(f.name)
            file_data = get_file_data(f.read())
            print(file_data)


def get_file_data(html_data):
    h = html2text.HTML2Text()
    data = h.handle(html_data)
    return data


if __name__ == '__main__':
    main()
