def mutate_string(string, position, character):
    new_string = list(string)
    new_string[position] = character
    new_string = ''.join(new_string)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)