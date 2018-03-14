def main():
    M = 78
    file = "examples/decl.txt"
    f = open(file, 'r', -1, "utf-8")
    lines = [i.strip(" \n") for i in f.readlines()]
    print(lines)
    f.close()


if __name__ == '__main__':
    main()
