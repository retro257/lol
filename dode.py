import random
g = int(input())

h = 0
while h < g:
    znak = random.randint(0, 1)
    first = random.randint(10, 35)

    second = random.randint(0, 35)

    if znak >= 1:
        print(str(first)+" + "+str(second)+" = ")
        while True:
        
            finish = int(input())
            if finish == first+second:
                h += 1
                break
            else:
                print("no")
    else:
        if first < second:
            continue
        print(str(first)+" - "+str(second)+" = ")
        while True: 
            finish = int(input())
            if finish == first-second:
                h += 1
                break
            else:
                print("no")
        

