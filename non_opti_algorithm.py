def length(wordLengths, i, j):
    return sum(wordLengths[i - 1:j]) + j - i + 1


def breakLine(words, L):
    # wl = lengths of words
    wl = [len(word) for word in words]
    # n = number of words in the text
    n = len(wl)
    # total badness of a text l1 ... li
    m = dict()
    # initialization
    m[0] = 0
    # auxiliary array
    s = dict()
    for i in range(1, n + 1):
        sums = dict()
        k = i
        while length(wl, k, i) <= L and k > 0:
            if i == len(words):
                sums[m[k - 1]] = k
            else:
                sums[(L - length(wl, k, i)) ** 2 + m[k - 1]] = k
            k -= 1
        m[i] = min(sums)  # minimum penalty (key)
        s[i] = sums[min(sums)]  # first word of line for minimum penalty

    text_justified = []
    while n > 1:
        line = ""
        for word in words[s[n] - 1:n]:
            line += word + " "
        line = line[0:len(line) - 1]
        text_justified.insert(0, line)
        n = s[n] - 1
    penalty = sum([(L - len(justified_line)) ** 2 for justified_line in text_justified])
    penalty -= (L - len(text_justified[len(text_justified) - 1])) ** 2
    return text_justified, penalty


def main():
    M = 80
    # paragraph = """Déclaration des Droits de l'homme et du citoyen du 26 août 1789.
    # Les Représentants du Peuple Français, constitués en Assemblée Nationale, considérant que l'ignorance, l'oubli ou le mépris des droits de l'Homme sont les seules causes des malheurs publics et de la corruption des Gouvernements, ont résolu d'exposer, dans une Déclaration solennelle, les droits naturels, inaliénables et sacrés de l'Homme, afin que cette Déclaration, constamment présente à tous les Membres du corps social, leur rappelle sans cesse leurs droits et leurs devoirs; afin que leurs actes du pouvoir législatif, et ceux du pouvoir exécutif, pouvant être à chaque instant comparés avec le but de toute institution politique, en soient plus respectés; afin que les réclamations des citoyens, fondées désormais sur des principes simples et incontestables, tournent toujours au maintien de la Constitution et au bonheur de tous. En conséquence, l'Assemblée Nationale reconnaît et déclare, en présence et sous les auspices de l'Etre suprême, les droits suivants de l'Homme et du Citoyen. Les hommes naissent et demeurent libres et égaux en droits. Les distinctions sociales ne peuvent être fondées que sur l'utilité commune. Le but de toute association politique est la conservation des droits naturels et imprescriptibles de l'Homme. Ces droits sont la liberté, la propriété, la sûreté, et la résistance à l'oppression. Le principe de toute Souveraineté réside essentiellement dans la Nation. Nul corps, nul individu ne peut exercer d'autorité qui n'en émane expressément.
    # La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui ainsi, l'exercice des droits naturels de chaque homme n'a de bornes que celles qui assurent aux autres Membres de la Société la jouissance de ces mêmes droits. Ces bornes ne peuvent être déterminées que par la Loi. La Loi n'a le droit de défendre que les actions nuisibles à la Société. Tout ce qui n'est pas défendu par la Loi ne peut être empêché, et nul ne peut être contraint à faire ce qu'elle n'ordonne pas. La Loi est l'expression de la volonté générale. Tous les Citoyens ont droit de concourir personnellement, ou par leurs Représentants, à sa formation. Elle doit être la même pour tous, soit qu'elle protège, soit qu'elle punisse. Tous les Citoyens étant égaux à ses yeux sont également admissibles à toutes dignités, places et emplois publics, selon leur capacité, et sans autre distinction que celle de leurs vertus et de leurs talents. Nul homme ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi, et selon les formes qu'elle a prescrites. Ceux qui sollicitent, expédient, exécutent ou font exécuter des ordres arbitraires, doivent être punis; mais tout citoyen appelé ou saisi en vertu de la Loi doit obéir à l'instant: il se rend coupable par la résistance. La Loi ne doit établir que des peines strictement et évidemment nécessaires, et nul ne peut être puni qu'en vertu d'une Loi établie et promulguée antérieurement au délit, et légalement appliquée.
    # Tout homme étant présumé innocent jusqu'à ce qu'il ait été déclaré coupable, s'il est jugé indispensable de l'arrêter, toute rigueur qui ne serait pas nécessaire pour s'assurer de sa personne doit être sévèrement réprimée par la loi. Nul ne doit être inquiété pour ses opinions, même religieuses, pourvu que leur manifestation ne trouble pas l'ordre public établi par la Loi. La libre communication des pensées et des opinions est un des droits les plus précieux de l'Homme: tout Citoyen peut donc parler, écrire, imprimer librement, sauf à répondre à l'abus de cette liberté dans les cas déterminés par la Loi. La garantie des droits de l'Homme et du Citoyen nécessite une force publique: cette force est donc instituée pour l'avantage de tous, et non pour l'utilité particulière de ceux auxquels elle est confiée. Pour l'entretien de la force publique, et pour les dépenses d'administration, une contribution commune est indispensable: elle doit être également répartie entre tous les citoyens, en raison de leurs facultés.
    # Tous les Citoyens ont le droit de constater, par eux-mêmes ou par leurs représentants, la nécessité de la contribution publique, de la consentir librement d'en suivre l'emploi, et d'en déterminer la quotité, l'assiette, le recouvrement et la durée. La Société a le droit de demander compte à tout Agent public de son administration. Toute Société dans laquelle la garantie des Droits n'est pas assurée, ni la séparation des Pouvoirs déterminée, n'a point de Constitution. La propriété étant un droit inviolable et sacré, nul ne peut en être privé, si ce n'est lorsque la nécessité publique, légalement constatée, l'exige évidemment, et sous la condition d'une juste et préalable indemnité.
    #    """
    paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer semper porta molestie. Vivamus nisl diam, malesuada id ligula sed, facilisis viverra tortor. Nunc dolor ante, consequat eu porttitor id, malesuada at eros. Mauris vehicula velit ac nibh semper tristique. Mauris lorem eros, condimentum a dolor et, maximus euismod ex. Sed eget odio ultrices, suscipit elit eget, vehicula mauris. Ut eget risus ut nibh tincidunt pharetra. Donec euismod nibh non pulvinar sagittis. Donec sodales id turpis ac pulvinar. Vivamus vel eleifend risus. Donec fringilla pharetra tempor."

    words = paragraph.split()
    text_justified, penalty = breakLine(words, M)
    for line in text_justified:
        print(line)
        print((M - len(line)) ** 2)
    print("Penalty : " + str(penalty))


if __name__ == '__main__':
    main()
