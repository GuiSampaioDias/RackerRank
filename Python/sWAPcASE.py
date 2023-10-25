def swap_case(s):
    new_s = list(s)
    for i in range(len(new_s)):
        if new_s[i].islower():
            new_s[i] = new_s[i].upper()
        elif new_s[i].isupper():
            new_s[i] = new_s[i].lower()
    new_s = "".join(new_s)
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)