s = int(input())
output = ""
with open("public.txt", "r", encoding="UTF-8") as file:
    input = file.read()
    for symbol in input:
        if 65 <= ord(symbol) <= 90:
            output += chr(65 + (ord(symbol) - 65 + s) % (90 - 65 + 1))
        elif 97 <= ord(symbol) <= 122:
            output += chr(97 + (ord(symbol) - 97 + s) % (122 - 97 + 1))
        else:
            output += symbol
with open("private.txt", "w") as file_out:
    print(output, file=file_out)


