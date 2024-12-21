text = text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
print({i: text.lower().count(i) for i in sorted(text.lower()) if i.isalpha()})
