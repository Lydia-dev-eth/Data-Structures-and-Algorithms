def letter_index(c):
    '''Map a lowercase letter to 0..25.'''
    return ord(c) - ord('a')


def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    k = len(S[0])

    # counts[tuple of 26 letter counts] = number of length-k windows of T
    # with exactly those letter counts (i.e. anagrams of each other)
    counts = {}
    freq = [0] * 26  # letter counts of the current window

    for i in range(len(T)):
        freq[letter_index(T[i])] += 1          # letter enters the window
        if i >= k:
            freq[letter_index(T[i - k])] -= 1  # letter leaves the window
        if i >= k - 1:                         # window is full: record it
            key = tuple(freq)
            counts[key] = counts.get(key, 0) + 1

    # answer each S_i with one lookup of its own letter counts
    for word in S:
        freq = [0] * 26
        for c in word:
            freq[letter_index(c)] += 1
        A.append(counts.get(tuple(freq), 0))

    return tuple(A)
