import random

points = 0
rounds = 1
words = []
computer_word = "apple"
computer_word_length = random.randint(3, 10)

with open('dict_test_utf8.txt', 'r', encoding='utf-8') as file:
    dict = []

    for line in file:
        a = line.split()[0]
        if a[-1] == ".":
            a = a[:-1]
        dict.append(a)

while rounds < 10:

    print("{} round".format(rounds))

    print("컴퓨터: {} {}".format(computer_word, computer_word_length))

    user_input = input(f"{computer_word_length}글자의 단어와 글자수를 입력하세요: ")
    user_word, user_number = user_input.split()

    if computer_word[-1] == user_word[0] and user_word in dict and len(user_word) == computer_word_length and user_word not in words:
        points += 1
        print("1전 흭득. 현재 점수 {}점".format(points))
        words.append(user_word)
    else:
        points -= 1
        if user_word in words:
            print("이미 나온 단어입니다(-1) 현재 점수 {}점".format(points))
        elif user_word not in dict:
            print("사전에 없는 단어입니다(-1). 현재 점수 {}점".format(points))
        elif len(user_word) != computer_word_length:
            print("wrong length")
        else:
            print(user_word, user_number)
            print("끝말잇기가 안됩니다(-1)현재 점수 {}점".format(points))

    for new_word in dict:
        if user_word[-1] == new_word[0] and len(new_word) == int(user_number):
            computer_word = new_word
            computer_word_length = random.randint(3, 10)
            break


    #move on to the next round
    rounds += 1

    #if the user has played for 10 rounds, it will display the following message
    if rounds == 10:
        print("게임 끝났습니다.")
        break