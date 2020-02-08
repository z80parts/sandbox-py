def show_wordlist(file):
    word_list = []
    file_date = open(file)
    for line in file_date:
        tmp_list = line.split()

        for word in tmp_list:
            word = word.rstrip('.,:!?)"')
            word = word.lstrip('("')
            word_list.append(word)

    return word_list


if __name__ == '__main__':
    file_name = input('file name:')
    list = show_wordlist(file_name)
    for word in list:
        print(word)
