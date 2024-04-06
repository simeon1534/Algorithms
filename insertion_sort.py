inp = [12, 11, 13, 5, 6]

sorted_inp = []
for i in inp:
    if not sorted_inp:
        sorted_inp.append(i)

    else:
        for j in range(len(sorted_inp) - 1, -1, -1):

            if i > sorted_inp[j]:
                sorted_inp.insert(j + 1, i)
                break
        else:  # sledovatelno i e po malko ot nai malkoto chislo v sorted_arr
            sorted_inp.insert(0, i)

print(sorted_inp)

