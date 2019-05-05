def get_index_different_char(chars):
    alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    count_alfa = 0
    count_other = 0
    for n, x in enumerate(chars):
        if (str(x) in alphanumeric) and (str(x) != ""):
            count_alfa += 1
            alfa_char_id = n
            if (count_alfa > 1) and (count_other == 1):
                return other_char_id
        else:
            count_other += 1
            other_char_id = n
            if (count_other > 1) and (count_alfa == 1):
                return alfa_char_id
        if n == len(chars) - 1: return n