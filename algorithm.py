def main():
    M = 78
    file = "examples/decl.txt"
    f = open(file, 'r', -1, "utf-8")
    lines = [i.strip(" \n") for i in f.readlines()]
    f.close()
    words = []
    [words.extend(line.split()) for line in lines]
    print(words)


def square_penalty(M, words):
    len_words = sum(len(s) for s in words)
    return (M - len(words) + 1 - len_words) ** 2


if __name__ == '__main__':
    main()
