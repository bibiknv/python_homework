def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char == vowels:
            char.upper()
        swapped_string += char

    return print(swapped_string)


