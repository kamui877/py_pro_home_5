import datetime


list_1 = ['', '', 'c', 'd', 'e', 'f']
list_2 = ['a', 'b', 'c', '', 'e', '']


def decorator(path):
    def _decorator(function):
        def func(arg1, arg2):
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'\nВремя вызова функции: {datetime.datetime.now()}\n'
                           f'Название функции: {function.__name__}\n'
                           f'Аргументы функции: {arg1, arg2}\n'
                           f'Результат работы функции: {function(arg1, arg2)}\n')
            return function(arg1, arg2)
        return func
    return _decorator


@decorator('log.txt')
def delete_doubles(d1, d2):
    #Объединяет списки с дублями в один
    list_res = []
    for val, key in zip(d1, d2):
        if val == key:
            list_res.append(val)
        elif val == '':
            list_res.append(key)
        elif key == '':
            list_res.append(val)
    return list_res


print(delete_doubles(list_1, list_2))