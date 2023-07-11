### https://stepik.org/lesson/518491/step/20?unit=510939

Рассмотрим следующий текстовый фрагмент:

ball,color,purple

ball,size,4

ball,notes,it's round

cup,color,blue

cup,size,1

cup,notes,none


Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта, значение свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно purple. Также у объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно. Помимо объекта ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название object и сгруппируем строки данного текстового фрагмента по первому столбцу:


object,color,size,notes

ball,purple,4,it's round

cup,blue,1,none


Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих — значения соответствующих свойств этого объекта.


Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:


filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
id_name — общее название для объектов
Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.