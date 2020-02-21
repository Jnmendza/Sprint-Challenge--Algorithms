'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    word_len = len(word)
    # Base case
    if word_len < 2:
        return 0
    # 0 - 2
    elif word[:2] == 'th':
        # +1 will keep a count without resetting
        return count_th(word[1:]) + 1
    else:
        # 1 - to the end
        return count_th(word[1:])

    # TBC

count_th('d;fkthenandnowdfd')
