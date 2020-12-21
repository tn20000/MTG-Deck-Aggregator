import os

def parse(deck):
    main = {}
    side = {}
    inMain = False
    inSide = False
    for line in deck:
        if line == '\n':
            continue
        if line[-1] == '\n':
            line = line[:-1]
        if line == 'Deck':
            inMain = True
            continue
        if line == 'Sideboard':
            inSide = True
            inMain = False
            continue
        if not(inMain or inSide):
            continue
        if not(line[0].isnumeric()):
            continue
        space = line.find(' ')
        cardname = line[space + 1:]
        quantity = line[:space] 
        if inMain:
            main[cardname] = int(quantity)
        else:
            if not cardname in side:
                side[cardname] = int(quantity)
    return main, side

def aggregate(lis, N):
    aggre = {}
    for deck in lis:
        for card in deck:
            for i in range(1, deck[card] + 1):
                aggre_name = card + '_' + str(i)
                if not aggre_name in aggre:
                    aggre[aggre_name] = 1
                else:
                    aggre[aggre_name] += 1
    firstN = {}
    sorted_aggregate = sorted(list(aggre.items()), key=lambda x: x[1], reverse=True)
    print(sorted_aggregate)
    print()
    print(sorted_aggregate[:N])
    for card, _ in sorted_aggregate[:N]:
        underline = card.find('_')
        cardname = card[:underline]
        if not cardname in firstN:
            firstN[cardname] = 1
        else:
            firstN[cardname] += 1
    return firstN

def writer(f, main, side):
    f.write('Deck\n')
    for card in main:
        f.write(str(main[card]) + ' ' + card + '\n')
    f.write('\nSideboard\n')
    for card in side:
        f.write(str(side[card]) + ' ' + card + '\n')
    f.close

archetype = 'Esper Doom Foretold'
decklists = os.listdir(archetype)
mains = []
sides = []
for deck in decklists:
    main, side = parse(open(archetype + '/' + deck))
    # for _ in range(int(deck[0])):
    mains.append(main)
    sides.append(side)
main_aggregate = aggregate(mains, 80)
print()
side_aggregate = aggregate(sides, 15)
final = open(archetype + '.txt', 'w')
writer(final, main_aggregate, side_aggregate)