
word = input("Please enter a word: ")
word_lower = word.lower()
forward_letters = []
backward_letters = []

def letters_forward(word_lower):
    for index in range(0,len(word_lower)):
      forward_letters.append(word_lower[index])

def letters_backward(word_lower):
    for index in range((len(word_lower) - 1), -1, -1):
      backward_letters.append(word_lower[index])

def is_palindrome(forward_letters, backward_letters):
    if forward_letters == backward_letters:
        palindrome = f'{word} is a palindrome.'
    else:
        palindrome = f'{word} is not a palindrome.'
    return palindrome

letters_forward(word_lower)
letters_backward(word_lower)


print(is_palindrome(forward_letters, backward_letters))
