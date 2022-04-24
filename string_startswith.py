def count_substring(string, sub_string):
    res = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(res)
#checks for all occurences of substring in string and returns count of occurences


if __name__ == '__main__':
    print(count_substring('ABCDCDC', 'CDC'))
    