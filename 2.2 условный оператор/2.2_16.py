def main():
    pass
a = 43872 / int(input())
b = 43872 / int(input())
c = 43872 / int(input())
if a < b < c:
    print('          Петя          ')
    print('  Вася  ')
    print('                  Толя  ')
    print('   II      I      III   ')
if c < b < a:
    print('          Толя          ')
    print('  Вася  ')
    print('                  Петя  ')
    print('   II      I      III   ')
if c < a < b:
    print('          Толя          ')
    print('  Петя  ')
    print('                  Вася  ')
    print('   II      I      III   ')
if b < a < c:
    print('          Вася          ')
    print('  Петя  ')
    print('                  Толя  ')
    print('   II      I      III   ')
if a < c < b:
    print('          Петя          ')
    print('  Толя  ')
    print('                  Вася  ')
    print('   II      I      III   ')
if b < c < a:
    print('          Вася          ')
    print('  Толя  ')
    print('                  Петя  ')
    print('   II      I      III   ')

if __name__ == '__main__':
    main()
