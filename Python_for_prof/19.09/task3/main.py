def sourcetemplate(url):
    def load(**kwargs):
        nonlocal url
        sorted(kwargs)
        result_list = []

        for key, value in kwargs.items():
             url += '?' + str(key) + '=' + str(value) + '&'
        return url[:-1]
    return load
# https://stepik.org/lesson/651459/step/14?thread=solutions&?unit=648165&
# https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165
# url = 'https://stepik.org/lesson/651459/step/14'
# load = sourcetemplate(url)
# print(load(thread='solutions', unit=648165))
url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

