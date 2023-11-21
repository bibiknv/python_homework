def filter_names(names, ignore_char, max_names):
    result = []
    generator_names = (i.lower() for i in names)
    generator_word = (i for i in generator_names if i.isalpha())
    generator_lst = (i for i in generator_word)
    for i in generator_lst:
        if i[:1:].upper() != ignore_char.upper():
            result.append(i)
    generator_result = [i for i in enumerate(result, 1)]

    try:
        for i in range(max_names):
            yield generator_result[i][1].title()
    except
        StopIteration


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))
