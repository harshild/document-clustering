import os

import html2text


def get_tokens(file_data):
    token_dict = {}
    for token in file_data.split(" "):
        stripped_token = token.strip()
        if stripped_token != "":
            if token_dict.keys().__contains__(stripped_token):
                token_dict[stripped_token] = token_dict[stripped_token] + 1
            else :
                token_dict[stripped_token] = 1
    return token_dict


def main():
    input_file_list = os.listdir(os.curdir + "/files/")
    for filename in sorted(input_file_list[:]):
        with open("./files/" + filename, 'r', encoding="latin-1", errors="surrogateescape") as f:
            print(f.name)
            file_data = get_file_data(f.read())
            file_tokens = get_tokens(file_data)

            print(sorted(file_tokens.items(), key=lambda kv: (kv[0], kv[1])))
            print(sorted(file_tokens.items(), key=lambda kv: (kv[1], kv[0])))


def get_file_data(html_data):
    h = html2text.HTML2Text()
    data = h.handle(html_data)
    return data


if __name__ == '__main__':
    main()
