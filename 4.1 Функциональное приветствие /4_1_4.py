def month(a, b):
    eng_month = ['January', 'February', 'March', ' April', 'May', 
                 'June', ' July', 'August', 'September', 'October', 'November', 'December']
    rus_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 
                 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    if b == 'en':
        return eng_month[a - 1]
    else:
        return rus_month[a - 1]
print(month(7,'ru'))
