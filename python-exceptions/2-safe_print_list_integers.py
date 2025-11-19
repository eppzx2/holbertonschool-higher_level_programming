#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x): #listin indexi qeder dovr
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError): #element int deyilse kec
                pass
    except IndexError: #mylistin indeksinden coxdursa problem eleme
        pass
    print()
    return count
