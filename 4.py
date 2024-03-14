def slidingwindow(s):
    window = {}

    left, right = 0, 0
    while right < len(s):
        c = s[right]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1
        right += 1

        while left < right and window needs shrink:
            d = s[left]
            left += 1
            