def choose(input_list, k):
    combination(input_list, set(), 0, k)


def combination(input_list, comb, start, k):
    if len(comb) == k:
        print(comb)
        return
    if start == len(input_list):
        return
    for i in range(start, len(input_list)):
        comb.add(input_list[i])
        combination(input_list, comb, i + 1, k)
        comb.remove(input_list[i])


def combination_alternative(input_list, comb, i, k):
    if len(comb) == k:
        print(comb)
        return
    if i == len(input_list):
        return
    comb.add(input_list[i])
    combination_alternative(input_list, comb, i + 1, k)
    comb.remove(input_list[i])
    combination_alternative(input_list, comb, i + 1, k)


choose(input_list=[1, 2, 3, 4, 5], k=3)
