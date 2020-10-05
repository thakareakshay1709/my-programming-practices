def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_vowels_score = 0
    stuart_score = 0
    str_len = len(string)
    for i, j in enumerate(string):
        # print(i, j)
        if j in vowels:
            kevin_vowels_score = kevin_vowels_score + (str_len - i)
        else:
            stuart_score = stuart_score + (str_len - i)
    # print(stuart_score, kevin_vowels_score)
    if kevin_vowels_score == stuart_score:
        print('DRAW')
    elif kevin_vowels_score > stuart_score:
        print('KEVIN {}'.format(kevin_vowels_score))
    elif kevin_vowels_score < stuart_score:
        print(f'STUART {stuart_score}')


if __name__ == '__main__':
    print(__name__)
    s = 'BANANA'  # input()
    minion_game(s)
