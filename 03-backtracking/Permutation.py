def permutation(input_list, partial, used):
    if len(partial) == len(input_list):
        print(partial)
    else:
        for i in range(0, len(input_list)):
            if not used[i] and not (input_list[i] == input_list[i - 1] and not used[i - 1]):
                used[i] = True
                partial.append(input_list[i])
                permutation(input_list, partial, used)
                used[i] = False
                partial.pop(len(partial) - 1)


nums = [1, 2, 3, 4, 5]
used = [False for _ in range(0, len(nums))]
permutation(nums, [], used)
