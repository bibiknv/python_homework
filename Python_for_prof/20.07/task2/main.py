
from datetime import datetime
import json

with open('pools.json', encoding='utf-8') as file:

    data_js = json.load(file)
    print(sorted(data_js, key=lambda x: (x['DimensionsSummer']['Length']), (x['DimensionsSummer']['Width'])))
    # for key, value in data_js[0].items():
    #     if key == 'DimensionsSummer':
    #         max_lenght = value['Length']
    #         max_width = value['Width']
    #
    #
    # for object_js in data_js:
        # for key, value in object_js.items():
        #     if key == 'WorkingHoursSummer':
        #         print
        #     # if key == 'DimensionsSummer':
        #     #     if value['Length'] > max_lenght:
        #     #         max_lenght = value['Length']
        #     #     if value['Width'] > max_width:
        #     #         max_width = value['Width']

print(key=lambda x: (x['DimensionsSummer']['Length']), x['DimensionsSummer']['Width']))



    # for dict_dj in data_js:
    #     for key, value in dict_dj.items():
    #         print(key, value)
    # start_time = datetime(2000, 1, 1, 10)
    # end_time = datetime(2000, 1, 1, 12)
    #
    # max_len
    # print(start_time)
