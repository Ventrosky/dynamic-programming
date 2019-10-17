def choose(input_list, target):
    input_list = sorted(input_list)
    combination(input_list, target, 0, [], 0)


def combination(input_list, target, sum, comb, start):
    if sum == target:
        print(comb)
        return
    if start == len(input_list):
        return
    for i in range(start, len(input_list)):
        cand = input_list[i]
        if sum + cand > target or (i > start and cand == input_list[i - 1]):
            continue
        comb.append(cand)
        combination(input_list, target, sum + cand, comb, i + 1)
        comb.pop()


input_list = [10, 1, 2, 7, 6, 1, 5]
choose(input_list, 8)
