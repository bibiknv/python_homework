def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    dict_result = {}
    list_result = sorted(grades['grades'])
    name = grades['name']

    dict_result.setdefault('name', name)
    dict_result.setdefault('top_grade', list_result[-1])

    return dict_result

annotations = top_grade.__annotations__

print(annotations['grades'])
