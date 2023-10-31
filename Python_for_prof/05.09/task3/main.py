order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
ind, letter in enumerate(order)
d[letter] = ind
key=lambda x: d[x]
