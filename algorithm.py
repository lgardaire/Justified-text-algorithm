def justification(words, width):
    words_count = len(words)
    matrix = [[0] * words_count for _ in range(words_count)]
    for i in range(words_count):
        matrix[i][i] = width - len(words[i])
        for j in range(i + 1, words_count):
            matrix[i][j] = matrix[i][j - 1] - len(words[j]) - 1
    minima = [0] + [10 ** 20] * words_count
    breaks = [0] * words_count
    for j in range(words_count):
        i = j
        while i >= 0:
            if matrix[i][j] < 0:
                cost = 10 ** 10
            else:
                cost = minima[i] + matrix[i][j] ** 2
            if minima[j + 1] > cost:
                minima[j + 1] = cost
                breaks[j] = i
            i -= 1
    lines = []
    j = words_count
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines


def run_algorithm(paragraph, M):
    penalties = dict()
    last_line = []
    words = paragraph.split()
    while len(" ".join(last_line)) <= M:
        lines = justification(words, M)
        penalty = sum([(M - len(line)) ** 2 for line in lines])
        penalties[penalty] = [lines, last_line.copy()]
        last_line.insert(0, words[len(words) - 1])
        words = words[0:len(words) - 1]
    best = min(penalties)
    justified_text = penalties[best][0]
    justified_text.append(" ".join(penalties[best][1]))

    return "\n".join(justified_text), best


def prepare_paragraph(filename):
    file = open(filename, 'r', -1, "utf-8")
    lines = file.readlines()
    file.close()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:len(lines[i]) - 1]
    return " ".join(lines)


def run_algorithm_once(filename, M):
    text, penalty = run_algorithm(prepare_paragraph(filename), M)
    print(text)
    print("Penalty : " + str(penalty))


def run_algorithm_to_optimize(filename, start, end):
    paragraph = prepare_paragraph(filename)
    results = dict()
    for M in range(start, end + 1):
        text, penalty = run_algorithm(paragraph, M)
        results[penalty] = [text, M]
    print(results[min(results)][0])
    print("Penalty minimum is : " + str(min(results)) + " for M = " + str(results[min(results)][1]))


if __name__ == '__main__':
    run_algorithm_to_optimize("decl.txt", 75, 81)
    # run_algorithm_once("decl.txt", 80)
