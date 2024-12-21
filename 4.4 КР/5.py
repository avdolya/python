def rabbit(start, finish, length):
    results = []
    def jump(current_position, remaining_jumps, path):
        if remaining_jumps == 0:
            if current_position == finish:
                results.append(path)
            return
        for next_position in (current_position - 1, current_position + 1, current_position + 2, current_position - 2):
            if next_position not in path:
                jump(next_position, remaining_jumps - 1, path + [next_position])
    jump(start, length, [start])
    return results
result = rabbit(13, 17, 4)
print(*result, sep="\n")
