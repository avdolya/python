'''values = []
chet = nechet = ln1 = ln2 = 0


def enter_results(*new_values):
    global values, chet, nechet, ln1, ln2
    values.extend(new_values)
    for i in range(len(values)):
        if i % 2 == 0:
            chet += values[i]
            ln1 +=1
        else:
            nechet += values[i]
            ln2 += 1


def get_sum():
    return (nechet, chet)


def get_average():
    avg_nechet = nechet / ln2 if ln2 != 0 else 0
    avg_chet = chet / ln1 if ln1 != 0 else 0
    return (avg_nechet, avg_chet)'''
chet = nechet = ln1 = ln2 = 0
values = []


def enter_results(*new_values):
    global chet, nechet, ln1, ln2
    values.extend(new_values)
    chet = nechet = ln1 = ln2 = 0
    for i in range(len(values)):
        if i % 2 == 0:
            chet += values[i]
            ln1 +=1
        else:
            nechet += values[i]
            ln2 += 1

    
def get_sum():
    return (round(chet, 2), round(nechet, 2))

    
def get_average():
    avg_nechet = nechet / ln2 if ln2 != 0 else 0
    avg_chet = chet / ln1 if ln1 != 0 else 0
    return (round(avg_chet, 2), round(avg_nechet, 2))

enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())