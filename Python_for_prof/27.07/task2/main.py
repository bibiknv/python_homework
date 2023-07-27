import pickle
def filter_dump(filename, object, typename):
    lst = [*filter(lambda x: type(x) == typename, object)]

    with open('numbers.pkl', 'wb') as file:
        pickle.dump(lst, file)

typename = int
object = [1,2,3,"d"]
filename = "some_file"

filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
