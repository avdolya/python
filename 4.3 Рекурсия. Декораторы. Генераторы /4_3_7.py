def same_type(func):
    def nums(*args):
        t = type(args[0])
        if all(isinstance(i, t) for i in args[1:]):
            return func(*args)
        else:
            print('Обнаружены различные типы данных')
    return nums