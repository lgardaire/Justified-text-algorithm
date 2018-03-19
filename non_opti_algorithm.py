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
    #paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer semper porta molestie. Vivamus nisl diam, malesuada id ligula sed, facilisis viverra tortor. Nunc dolor ante, consequat eu porttitor id, malesuada at eros. Mauris vehicula velit ac nibh semper tristique. Mauris lorem eros, condimentum a dolor et, maximus euismod ex. Sed eget odio ultrices, suscipit elit eget, vehicula mauris. Ut eget risus ut nibh tincidunt pharetra. Donec euismod nibh non pulvinar sagittis. Donec sodales id turpis ac pulvinar. Vivamus vel eleifend risus. Donec fringilla pharetra tempor."

    paragraph = """De toute évidence, Ron s'était rendu compte qu'il avait attiré des ennuis à Harry car il n'avait plus rappelé. Hermione Granger, son autre meilleure amie, n'avait pas essayé de l'appeler. Harry se doutait que Ron lui avait conseillé de ne pas lui téléphoner et c'était bien dommage. Hermione, la meilleure élève de sa classe, avait en effet des parents moldus. Elle savait très bien se servir d'un téléphone et n'aurait jamais commis l'imprudence de dire qu'elle était une condisciple de Poudlard. Ainsi, pendant cinq longues semaines, Harry n'avait eu aucune nouvelle de ses amis sorciers et ces vacances d'été se révélaient presque aussi détestables que celles de l'année dernière. Il n'y avait qu'une toute petite amélioration: après avoir juré qu'il ne l'utiliserait pas pour envoyer des lettres à ses amis, Harry avait été autorisé à laisser Hedwige, sa chouette, se promener librement la nuit. L'oncle Vernon avait fini par céder pour mettre fin au vacarme que faisait Hedwige lorsqu'elle restait enfermée trop longtemps dans sa cage. Harry acheva de prendre ses notes sur Gwendoline la Fantasque et s'interrompit pour tendre à nouveau l'oreille. Seuls les lointains ronflements de Dudley, son énorme cousin, rompaient le silence qui régnait dans la maison. Il devait être très tard. Harry sentait dans ses yeux des picotements qui trahissaient sa fatigue et il estima préférable de finir son devoir le lendemain. Il reboucha la bouteille d'encre, enveloppa sa lampe torche, son livre, son parchemin, sa plume et l'encre dans une vieille taie d'oreiller, se leva et alla cacher le tout sous une lame de parquet branlante dissimulée par son lit. Puis il se releva, s'étira et regarda l'heure sur le cadran lumineux de son réveil posé sur la table de nuit. Il était une heure du matin. Harry sentit alors une étrange contraction dans son estomac. Depuis une heure, il avait treize ans et ne s'en était même pas aperçu. Un autre trait inhabituel de la personnalité de Harry, c'était le peu d'enthousiasme qu'il ressentait à l'approche de son anniversaire. De sa vie, il n'avait jamais reçu une carte pour le lui souhaiter. Les deux dernières années, les Dursley n'avaient pas pris la peine de le fêter et il n'y avait aucune raison pour qu'ils s'en souviennent davantage cette année. Harry traversa la pièce plongée dans l'obscurité. Il passa devant la cage vide d'Hedwige et alla ouvrir la fenêtre. Il s'appuya sur le rebord, appréciant la fraîcheur de l'air nocturne sur son visage, après tout ce temps passé sous les couvertures. Il y avait maintenant deux nuits qu'Hedwige n'était pas rentrée. Mais Harry n'était pas inquiet – il lui était déjà arrivé de s'absenter aussi longtemps. Il espérait cependant qu'elle serait bientôt de retour. Dans cette maison, c'était le seul être vivant qui n'avait pas un mouvement de recul en le voyant. Bien qu'il fût encore petit et maigre pour son âge, Harry avait grandi de plusieurs centimètres au cours de l'année écoulée. Ses cheveux d'un noir de jais, eux, n'avaient pas changé: ils étaient toujours en bataille et restaient obstinément rétifs à tous ses efforts pour les coiffer. Derrière ses lunettes, ses yeux brillaient d'un vert étincelant et sur son front, parfaitement visible derrière une mèche de cheveux, se dessinait une mince cicatrice en forme d'éclair. Davantage encore que tout le reste, cette cicatrice représentait ce qu'il y avait de plus extraordinaire chez Harry. Contrairement à ce que les Dursley avaient prétendu pendant dix ans, elle n'était pas un souvenir de l'accident de voiture qui avait tué ses parents, pour la bonne raison que Lily et James Potter n'étaient pas morts dans un accident de la route. Ils avaient été assassinés. Assassinés par le mage noir le plus redoutable qu'on ait connu depuis un siècle, Lord Voldemort. Harry, lui, avait survécu à l'attaque en s'en tirant avec cette simple cicatrice sur le front. Au lieu de le tuer, le sort que lui avait lancé Lord Voldemort s'était retourné contre son auteur et le sorcier maléfique avait dû prendre la fuite dans un état proche de la mort... Mais depuis que Harry était entré au collège Poudlard, il s'était à nouveau retrouvé face à face avec l'effroyable mage noir. Accoudé au rebord de la fenêtre, Harry contemplait le ciel nocturne en se disant qu'il avait eu de la chance de pouvoir atteindre son treizième anniversaire. Il scruta l'obscurité dans l'espoir d'apercevoir Hedwige. Peut-être allait-elle apparaître avec dans le bec un cadavre de souris qu'elle lui apporterait en s'attendant à recevoir des félicitations. Le regard perdu vers les toits des maisons environnantes, Harry mit quelques secondes à se rendre compte de ce qui se passait devant ses yeux. Sa silhouette découpée dans la lueur de la lune, une grande créature étrangement penchée de côté battait des ailes en volant dans la direction de Harry. Immobile, il la regarda descendre vers lui. Pendant une fraction de seconde, il hésita, la main sur la poignée de la fenêtre, en se demandant s'il ne ferait pas mieux de la refermer mais au même moment, la créature passa au-dessus d'un réverbère de Privet Drive. Harry vit alors de quoi il s'agissait et fit aussitôt un pas de côté. Trois hiboux s'engouffrèrent par la fenêtre ouverte. Deux d'entre eux portaient le troisième qui semblait évanoui. Ils atterrirent sur le lit avec un bruit mou et le hibou évanoui bascula sur le dos, les ailes en croix. Un paquet était attaché à ses pattes. Harry reconnut aussitôt le hibou inanimé. C'était un gros oiseau gris qui s'appelait Errol et appartenait à la famille Weasley. Harry se précipita sur le lit, détacha la ficelle autour de ses pattes et prit le paquet. Puis il porta le hibou dans la cage d'Hedwige. Errol entrouvrit un œil vitreux, laissa échapper un faible hululement en guise de remerciement et se mit à boire de l'eau à longues gorgées. Harry se tourna vers les deux autres oiseaux. L'un d'eux, une chouette au plumage d'un blanc de neige, n'était autre qu'Hedwige. Elle aussi portait un paquet et semblait très contente d'elle. Elle donna un affectueux coup de bec à Harry tandis qu'il lui enlevait son fardeau, puis elle traversa la pièce d'un coup d'aile pour rejoindre Errol. Harry ne connaissait pas le troisième oiseau, un magnifique hibou au plumage fauve, mais il sut tout de suite d'où il venait, car en plus d'un troisième paquet, il portait une lettre sur laquelle il reconnut immédiatement le sceau du collège Poudlard. Lorsque Harry l'eut délivré de son courrier, l'oiseau ébouriffa ses plumes d'un air avantageux, déploya ses ailes et s'envola par la fenêtre dans les profondeurs de la nuit. Harry s'assit sur son lit, prit le paquet qu'avait apporté Errol, arracha le papier kraft qui le protégeait et découvrit un cadeau enveloppé dans du papier doré ainsi que la première carte d'anniversaire qu'il eût jamais reçue. Les doigts légèrement tremblants, il ouvrit l'enveloppe d'où s'échappèrent deux morceaux de papier: une lettre et une coupure de journal. De toute évidence, la coupure provenait de La Gazette du sorcier, car les personnages représentés sur la photo en noir et blanc qui accompagnait l'article ne cessaient de bouger. Harry lissa le morceau de papier journal et lut: UN EMPLOYÉ DU MINISTÈRE DE LA MAGIE REMPORTE LE GRAND PRIX Arthur Weasley, directeur du service des détournements de l'Artisanat moldu. a remporté le grand prix de la loterie du Gallion organisée chaque année par La Gazette du sorcier. Mr Weasley, ravi, nous a déclaré: « Cet or va nous servir à faire cet été un voyage en Egypte où se trouve Bill, notre fils aîné. Il travaille là-bas comme conjureur de sorts pour le compte de la banque Gringotts, la banque des sorciers. » La famille Weasley va donc passer un mois en Egypte et sera de retour pour la rentrée des classes au collège Poudlard où cinq des enfants Weasley poursuivent leurs études. Harry examina la photographie animée et un sourire éclaira son visage lorsqu'il vit les neuf membres de la famille Weasley lui faire de grands signes de la main devant une pyramide égyptienne. Il reconnut Mrs Weasley, petite et dodue, la haute silhouette et le crâne chauve de Mr Weasley, ainsi que leurs six garçons et leur fille qui avaient tous des cheveux d'un roux éclatant (bien qu'il fût impossible de s'en rendre compte sur la photo en noir et blanc). Grand et dégingandé, Ron se tenait au centre du cliché. Il avait son rat Croûtard sur l'épaule et tenait enlacée sa petite sœur Ginny. Harry ne connaissait personne qui, plus que les Weasley, ait mérité de gagner un joli tas d'or. Ils étaient en effet extrêmement pauvres et d'une générosité sans égale. Harry déplia ensuite la lettre de Ron."""

    words = paragraph.split()
    text_justified, penalty = breakLine(words, M)
    for line in text_justified:
        print(line)
        print((M - len(line)) ** 2)
    print("Penalty : " + str(penalty))


if __name__ == '__main__':
    main()
