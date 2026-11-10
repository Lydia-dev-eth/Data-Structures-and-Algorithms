def merge_bookings(B1, B2):
    '''
    Input:  B1, B2 | booking schedules (lists of triples (k, s, t))
    Output: B      | booking schedule for the union of their requests
    '''
    ###########################
    # Part (a): Implement me! #
    ###########################
    n1, n2 = len(B1), len(B2)
    p1, p2 = 0, 0   # p1, p2: next booking in B1, B2 that ends after time x
    x = 0           # B covers the merged schedule up to time x
    B = []

    while p1 < n1 or p2 < n2:
        if p2 == n2:                      # only B1 has bookings left
            k, s, t = B1[p1]
            B.append((k, max(x, s), t))
            x = t
            p1 += 1
        elif p1 == n1:                    # only B2 has bookings left
            k, s, t = B2[p2]
            B.append((k, max(x, s), t))
            x = t
            p2 += 1
        else:                             # both have bookings left
            k1, s1, t1 = B1[p1]
            k2, s2, t2 = B2[p2]
            x = max(x, min(s1, s2))       # skip empty time before next booking
            if t1 <= s2:                  # B1's booking ends before B2's starts
                B.append((k1, x, t1))
                x = t1
                p1 += 1
            elif t2 <= s1:                # B2's booking ends before B1's starts
                B.append((k2, x, t2))
                x = t2
                p2 += 1
            elif x < s2:                  # only B1 is active until B2 starts
                B.append((k1, x, s2))
                x = s2
            elif x < s1:                  # only B2 is active until B1 starts
                B.append((k2, x, s1))
                x = s1
            else:                         # both active until the first one ends
                end = min(t1, t2)
                B.append((k1 + k2, x, end))
                x = end
                if t1 == end: p1 += 1
                if t2 == end: p2 += 1

    # Join neighbouring bookings that touch and have the same number of rooms
    joined = []
    for k, s, t in B:
        if joined and joined[-1][0] == k and joined[-1][2] == s:
            k0, s0, t0 = joined.pop()
            s = s0
        joined.append((k, s, t))
    return joined


def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ###########################
    # Part (c): Implement me! #
    ###########################
    if len(R) == 0:
        return tuple(B)
    if len(R) == 1:  # base case: one talk needs one room
        s, t = R[0]
        return ((1, s, t),)

    m = len(R) // 2
    B1 = satisfying_booking(R[:m])  # conquer left half
    B2 = satisfying_booking(R[m:])  # conquer right half
    B = merge_bookings(B1, B2)      # combine

    return tuple(B)
