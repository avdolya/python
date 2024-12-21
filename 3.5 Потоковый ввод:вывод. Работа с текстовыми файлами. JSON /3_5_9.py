a = input()
b = input()
with open(a, "r", encoding="UTF-8") as input_file:
        with open(b, "w", encoding="UTF-8") as output_file:
                for l in input_file:
                        l = l.strip().replace("\t", "")
                        word_list = l.split()
                        if len(word_list) != 0:
                            print(*word_list, file=output_file)
                