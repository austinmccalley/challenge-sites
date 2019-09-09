def find_next_square(sq):
    import math
    this_root = math.sqrt(sq)

    if this_root % 1 == 0:
        return (this_root + 1) * (this_root + 1)
    else:
        return -1

