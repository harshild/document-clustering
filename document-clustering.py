import os


def main():
    for filename in sorted(os.listdir(os.curdir+"/files/")):
        with open(os.path.join(os.curdir,"./files/", filename), 'r') as f:
            print(filename)



if __name__ == '__main__':
    main()