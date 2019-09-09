""" `
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
 """


def persistence(n):
    fpass = True
    itterations = 0
    tres = 1
    while len(str(tres)) != 1 or fpass:
        cres = 1
        if fpass:
            fpass = False
            split_num = [int(d) for d in str(n)]

            if len(split_num) == 1:
                return itterations

            for num in split_num:
                tres = tres*num
            itterations +=1

        
        else:
            split_num = [int(d) for d in str(tres)]

            if len(str(tres)) == 1:
                return itterations

            for num in split_num:
                cres = cres * num
             
            itterations +=1
            tres = cres
    return (itterations)


print(persistence(999)) 