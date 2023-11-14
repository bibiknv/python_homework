# def all_together(*iterable):
#     for args in iterable:
#         for i in args:
#             yield i
#
# print(list(all_together()))
#

def all_together(*iterable):
    for args in iterable:
        yield from args

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))
