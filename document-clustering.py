import os
import re

import html2text


def get_tokens(file_data):
    token_dict = {}
    file_data = file_data.lower()
    file_data = re.sub("[^a-z]", " ", file_data)

    for token in file_data.split(" "):
        stripped_token = token.strip()
        if stripped_token != "":
            if token_dict.keys().__contains__(stripped_token):
                token_dict[stripped_token] = token_dict[stripped_token] + 1
            else:
                token_dict[stripped_token] = 1
    return token_dict


def write_tokens_to_file(file_name, sorted_by, tokens_list):
    filename = "./output/" + file_name + "_" + sorted_by + ".txt"

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    for t, f in tokens_list:
        open(filename, "a+").write(t + " , " + str(f) + "\n")


def main():
    input_file_list = os.listdir(os.curdir + "/files/")

    #Step1
    tokenize(input_file_list[:1])


def tokenize(input_file_list):
    for filename in sorted(input_file_list[:]):
        with open("./files/" + filename, 'r', encoding="latin-1", errors="surrogateescape") as f:
            print(f.name)
            file_data = get_file_data(f.read())
            file_tokens = get_tokens(file_data)

            file_tokens_sorted_key = sorted(file_tokens.items(), key=lambda tf: (tf[0], tf[1]))
            write_tokens_to_file(filename.split(".html")[0], "token", file_tokens_sorted_key)

            file_tokens_sorted_count = sorted(file_tokens.items(), key=lambda tf: (tf[1], tf[0]))
            write_tokens_to_file(filename.split(".html")[0], "frequency", file_tokens_sorted_count)


def get_file_data(html_data):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    data = h.handle(html_data)
    return data


if __name__ == '__main__':
    main()
