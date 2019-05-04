def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    delka = len(string)
    seznam =list(range(delka))
    if n > delka:
        n = n % delka
    i = 0
    n = -n
    for c in string:
        if (i + n) < delka:
           seznam[i + n] = c
        else:
            seznam[- delka + i + n] = c
        i += 1
    return "".join(seznam)



