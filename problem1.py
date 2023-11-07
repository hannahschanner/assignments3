
while True:
    f = open('dict_test_utf8.txt', 'r', encoding='utf-8')

    word = input("Word to translate? ")

    if word == '0':
        break

    for line in f:
        parts = line.split(' :')
        if word == parts[0].strip():
            print(line)

    f.close()