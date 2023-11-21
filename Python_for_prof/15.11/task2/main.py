def parse_ranges(ranges):
    result_lst = []

    lst = ranges.split(',')
    generator = (i.split('-') for i in lst)

    for i in list(generator):
        for j in range(int(i[0]), int(i[1]) + 1):
            result_lst.append(j)

    for num in result_lst:
        yield num

print(*parse_ranges('1-10,2-10'))




# def parse_ranges(ranges):
#     result_lst = []
#
#     lst = ranges.split(',')
#     generator = (i.split('-') for i in lst)
#
#     for i in list(generator):
#         for j in i:
#             result_lst.append(int(j))
#
#     result_lst = list(set(result_lst))
#     for num in range(min(result_lst), max(result_lst) + 1):
#         yield num
#
# print(*parse_ranges('1-10,2-10'))

# def parse_ranges(ranges):
    # result_lst = []
    #
    # lst = ranges.split(',')
    # generator = (i.split('-') for i in lst)
    #
    # for i in list(generator):
    #     for j in range(int(i[0]), int(i[1]) + 1):
    #         result_lst.append(j)
    #
    # result_lst = list(set(result_lst))
    # for num in result_lst:
    #     yield num

