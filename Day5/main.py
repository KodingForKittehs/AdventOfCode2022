import re


def empty_line(input):
    for i, c in enumerate(input):
        if not c.strip():
            return i
    return -1


def get_list_num(line):
    last = line.split()[-1]
    return int(last)


def move_items(lists, num, start, end):
    tmp = []
    for i in range(num):
        item = lists[start - 1].pop()
        tmp.append(item)
    lists[end - 1].extend(reversed(tmp))


def read_state():
    input = [line for line in open('Day5/input.txt')]

    empty = empty_line(input)
    list_num = get_list_num(input[empty - 1])
    lists = [[] for i in range(list_num)]

    for i in range(empty - 2, -1, -1):
        for j in range(list_num):
            try:
                item = input[i][j * 4 + 1].strip()
                if item:
                    lists[j].append(item)
            except IndexError:
                pass

    moves = []
    for i in range(empty + 1, len(input)):
        vals = re.findall('\d+', input[i])
        moves.append((int(vals[0]), int(vals[1]), int(vals[2])))
    return lists, moves


def problem1():
    lists, moves = read_state()
    for move in moves:
        for i in range(move[0]):
            move_items(lists, 1, move[1], move[2])
    result = ''
    for lst in lists:
        result += lst[-1]
    return result


def problem2():
    lists, moves = read_state()
    for move in moves:
        move_items(lists, move[0], move[1], move[2])
    result = ''
    for lst in lists:
        result += lst[-1]
    return result


print(f'Problem 1: {problem1()}')
print(f'Problem 2: {problem2()}')
