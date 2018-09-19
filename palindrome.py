letter_array =[]
word = input("Please enter a word: ")
def separate_letters():

    for index in range(0,len(word)):
      letter_array.append(word[index])

separate_letters()

def is_palindrome():
    for index in range(0, len(letter_array)):
        while True:
            if letter_array[index] == letter_array[(len(letter_array)-1)-(index)]:
                return(F'{word} is a palindrome')
            else:
                break

        return(F'{word} is not a palindrome')


print(is_palindrome())
