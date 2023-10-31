### https://stepik.org/lesson/594680/step/5?unit=589701

Линеаризация — это процесс преобразования списка, который может содержать несколько уровней вложенных списков, в список, содержащий все те же элементы без какой-либо вложенности.


Например, список:


[1, [2, 3], [4, [5, 6, [7, 8, 9]]]] после линеаризации будет иметь вид:


[1, 2, 3, 4, 5, 6, 7, 8, 9]


Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:


nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.