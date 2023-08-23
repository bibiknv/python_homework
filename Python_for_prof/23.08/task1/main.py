def is_good_password():
    pass

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))

try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

