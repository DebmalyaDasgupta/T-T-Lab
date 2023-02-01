# Count no of vowels in a string using sets

# Function to count vowel
def vowel_count(str):
    # Initializing count variable to 0
    count = 0
    vowel = set("aeiouAEIOU")

    for alphabet in str:
        if alphabet in vowel:
            count = count + 1

    print("No. of vowels :", count)

str = "DebmalyaDasgupta"



vowel_count(str)


