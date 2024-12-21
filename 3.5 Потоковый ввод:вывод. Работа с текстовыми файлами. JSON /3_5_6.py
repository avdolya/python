d = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 
     'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
     'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh',
     'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'Ь': '', 'Ъ': ''}
st = ''
with open("/Users/olaavduhina/Desktop/lms/3.5 Потоковый ввод:вывод. Работа с текстовыми файлами. JSON /transliteration.txt", 'w', encoding="UTF-8") as file_res:
    with open("/Users/olaavduhina/Desktop/lms/3.5 Потоковый ввод:вывод. Работа с текстовыми файлами. JSON /cyrillic.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        for line in lines:
            line = line.rstrip("\n")
            for s in line:
                if s.isupper():
                    st += d.get(s, s)
                else:
                    st += d.get((s.upper()), s).lower()

            print(st, file = file_res)
            st = ''

