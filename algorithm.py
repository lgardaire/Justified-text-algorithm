MIN = 78
MAX = 81
FILENAME = "HP.txt"

def justification(words, width):
    """
    Compute the justification on the text passed in parameter as an array
    :param words: array of words forming the text to justify
    :param width: maximum line width in the justified text
    :return: array of justified text lines, penalty for the justification
    """

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
    lines = []
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines, minimum[-1]


def line_length(i, j, words_length):
    """
    Calculate the length of a line of words
    :param i: index of the first word of the line
    :param j: index of the last word of the line
    :param words_length: array containing word lengths
    :return: length of the line
    """

    return sum(words_length[i:j + 1]) + j - i


def run_algorithm(text, M):
    """
    Split the text to justify in paragraphs and justify each of them
    :param text: text to justify
    :param M: maximum line width in the justified text
    :return: justified text, penalty for this text
    """

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
    """
    Open the file to justify and read its content
    :param filename: name of the file to open
    :return: content of the file
    """

    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    return " ".join([i for i in lines])


def run_algorithm_to_optimize(filename, start, end):
    """
    Justify a text with different maximum lengths for a line to find the best one
    :param filename: name of the file to open
    :param start: minimum of the maximum length of the line
    :param end: maximum of the maximum length of the line
    """

    paragraph = prepare_paragraph(filename)
    results = {}
    for M in range(start, end + 1):
        text, penalty = run_algorithm(paragraph, M)
        results[penalty] = [text, M]
    print(results[min(results)][0])
    print("Penalty minimum is : %d  for M = %d" % (min(results), results[min(results)][1]))


if __name__ == '__main__':
    run_algorithm_to_optimize(FILENAME, MIN, MAX)
