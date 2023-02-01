def vowel_count(str):
    # Initializing count variable to 0
    count = 0
    vowel = set("aeiouAEIOU")

    for alphabet in str:
        if alphabet in vowel:
            count = count + 1

    print("No. of vowels :", count)

str = input('Enter the string : ')

vowel_count(str)
