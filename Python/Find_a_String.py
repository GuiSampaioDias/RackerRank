def count_substring(string, sub_string):
    size_string = len(string) + 1
    size_sub = len(sub_string)
    numb_of_equals = 0
    if size_string == size_sub and sub_string in string:
        return 1
    for i in range(size_string - size_sub):
        if string[i:i+size_sub] == sub_string:
            numb_of_equals += 1
    return numb_of_equals   

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)