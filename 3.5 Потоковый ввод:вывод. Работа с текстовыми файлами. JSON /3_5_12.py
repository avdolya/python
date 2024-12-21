gr_1 = input()
gr_2 = input()
gr_3 = input()
gr_4 = input()
s = []
even = []
odd = []
eq = []
chet = nechet = 0
with open(gr_1) as file_in_1:
    for line in file_in_1:
        res_even = []
        res_odd = []
        res_eq = []


        for i in line.split():
            for letter in '02468':
                chet += i.count(letter)
            for letter in '13579':
                nechet += i.count(letter)
            if chet > nechet:
                res_even.append(i)
            elif chet < nechet:
                res_odd.append(i)
            else:
                res_eq.append(i)
            chet = nechet = 0


        even.append(' '.join(res_even) + '\n')
        odd.append(' '.join(res_odd) + '\n')
        eq.append(' '.join(res_eq) + '\n')
with open(gr_2, "w", encoding="UTF-8") as file_out:
    file_out.writelines(even)
with open(gr_3, "w", encoding="UTF-8") as file_out:
    file_out.writelines(odd)
with open(gr_4, "w", encoding="UTF-8") as file_out:
    file_out.writelines(eq)