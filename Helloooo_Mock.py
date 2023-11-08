"""Helloooo"""
def main():
    """Demo"""
    word = list(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    check_vowels = [i for i in word if i in vowels]
    last_vowel = str(check_vowels[-1]) if check_vowels else False
    word.reverse()
    for i in range(len(word)):
        if word[i] == last_vowel:
            word[i] = last_vowel*4
            break
    word.reverse()
    print(*word, sep='')
main()
