def checkString(str):
    flag_letter = False
    flag_number = False

    for i in str:
        if i.isalpha():
            flag_letter = True

        elif i.isdigit():
            flag_number = True

        else:
            print("No valid answer!!")

    return flag_letter and flag_number

Sentence = input('Enter the sentence: ')

print(checkString(Sentence))