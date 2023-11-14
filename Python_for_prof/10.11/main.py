def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    new_list_mast = []

    for i in card_mast:
        if i != suit:
            new_list_mast.append(i)

    while True:
        for i in range(len(new_list_mast)):
            k = new_list_mast[i]
            for j in card_values:
                yield ' '.join([j, k])


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)


# решил так: в бесконечном цикле while проходил
# по мастям и обнулял счетчик при достижение длинны списка мостей а в цикле for
#     проходил по номиналу и возвращал значение=))
generator = card_deck('пик')

#
# print(next(generator))
# print(next(generator))
# print(next(generator))
