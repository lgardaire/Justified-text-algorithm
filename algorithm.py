import time


def justification(words, width):
    word_count = len(words)
    minimum = [0] + [10 ** 20] * word_count
    breaks = [0] * word_count
    words_length = [len(i) for i in words]
    for j in range(word_count):
        i = j
        while line_length(i, j, words_length) <= width and i >= 0:
            if j == word_count - 1:
                cost = minimum[i]
            else:
                cost = minimum[i] + (width - line_length(i, j, words_length)) ** 2
            if minimum[j + 1] > cost:
                minimum[j + 1] = cost
                breaks[j] = i
            i -= 1
    j = word_count
    lines = [' '.join(words[j:word_count])]
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines, minimum[-1]


def line_length(i, j, words_length):
    return sum(words_length[i:j + 1]) + j - i


def run_algorithm(text, M):
    paragraphs = text.split("\n")
    result = ""
    penalty = 0
    for paragraph in paragraphs:
        words = paragraph.split()
        justified_text, best = justification(words, M)
        result += "\n".join(justified_text) + "\n"
        penalty += best
    return result, penalty


def prepare_paragraph(filename):
    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    return " ".join([i for i in lines])


def run_algorithm_to_optimize(filename, start, end):
    paragraph = prepare_paragraph(filename)
    results = {}
    for M in range(start, end + 1):
        text, penalty = run_algorithm(paragraph, M)
        results[penalty] = [text, M]
    print(results[min(results)][0])
    print("Penalty minimum is : %d  for M = %d" % (min(results), results[min(results)][1]))


if __name__ == '__main__':
    run_algorithm_to_optimize("HP.txt", 20, 120)
