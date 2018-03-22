import time


def optijustification(words, width):
    word_count = len(words)
    matrix = [[0] * word_count for _ in range(word_count)]
    for i in range(word_count):
        matrix[i][i] = width - len(words[i])
        for j in range(i + 1, word_count):
            if j - i + 1 > width / 2:
                break
            matrix[i][j] = matrix[i][j - 1] - len(words[j]) - 1
    minimum = [0] + [10 ** 20] * word_count
    breaks = [0] * word_count
    last_line_index = word_count
    for j in range(word_count):
        i = j
        while j - i + 1 <= width / 2:
            if matrix[i][j] < 0:
                cost = 10 ** 20
            elif j == word_count - 1:
                last_line_index -= 1
                cost = minimum[i] + matrix[i][j] ** 2
            else:
                cost = minimum[i] + matrix[i][j] ** 2
            if minimum[j + 1] > cost:
                minimum[j + 1] = cost
                breaks[j] = i
            i -= 1
    mini = 10 ** 20
    index = 0
    for i in range(last_line_index, word_count):
        if minimum[i] < mini:
            index = i
            mini = minimum[i]
    j = index
    lines = [' '.join(words[j:word_count])]
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines, minimum[index]


def run_algorithm(paragraph, M, algo):
    words = paragraph.split()
    justified_text, best = algo(words, M)
    return "\n".join(justified_text), best


def prepare_paragraph(filename):
    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    return " ".join([i.strip("\n") for i in lines])


def run_algorithm_to_optimize(filename, start, end, algo):
    paragraph = prepare_paragraph(filename)
    results = {}
    for M in range(start, end + 1):
        text, penalty = run_algorithm(paragraph, M, algo)
        # print(text)
        results[penalty] = [text, M]
    print(results[min(results)][0])
    print("Penalty minimum is : %d  for M = %d" % (min(results), results[min(results)][1]))


if __name__ == '__main__':
    start = time.time()
    run_algorithm_to_optimize("HP.txt", 20, 120, optijustification)
    end = time.time()
    print(end - start)
