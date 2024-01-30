def find_longest_consecutive_sequence(input_list):
    num_set = set(input_list)
    longest_streak = 0
    best_sequence_start = None

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak
                best_sequence_start = num

    return [best_sequence_start + i for i in range(longest_streak)]

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
longest_sequence = find_longest_consecutive_sequence(input_list)
print(', '.join(map(str, longest_sequence)))
