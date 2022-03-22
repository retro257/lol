def counte(a):
    from decimal import Decimal
    import decimal
    import math
    numbers = "1234567890."
    i = 0

    while i < len(a):
        
        if a[i] == "s":
            MIN = 0
            pr = ""
            for t in range(i+2, len(a)):
                if a[t] != ")":
                    pr = pr+a[t]
                else:
                    MIN = t+1
                    break
            r = counte(pr)
            try:
                red = math.sqrt(float(r))
                if "." in str(red):
                    red = str(red)[0:str(red).index(".")+2]
            except ValueError:
                return 0
            a = a[0:i]+str(red)+a[MIN:len(a)]
        i += 1
    i = 0
    while i < len(a):
        
        if a[i] == "*":
            MAX = len(a)
            MIN = 0
            s = i-1

            for i2 in range(i+1, len(a)):

                if a[i2] not in numbers:

                    MAX = i2
                    break

            while s > 0:
                if a[s] not in numbers:

                    MIN = s+1
                    break
                s -= 1
            d2 = len(a[MIN:i])

            l = i
            i = i - d2 -1
            try:
                a = a[0:MIN]+str(float(a[MIN:l]) * float(a[l+1:MAX]) )+a[MAX:len(a)]
                
            except decimal.DivisionByZero:
                return 0
            except ZeroDivisionError:
                return 0

        elif a[i] == "/":
            MAX = len(a)
            MIN = 0
            s = i-1

            for i2 in range(i+1, len(a)):

                if a[i2] not in numbers:

                    MAX = i2
                    break

            while s > 0:
                if a[s] not in numbers:

                    MIN = s+1
                    break
                s -= 1
            d2 = len(a[MIN:i])

            l = i
            i = i - d2 -1
            
            try:
                a = a[0:MIN]+str(float(a[MIN:l]) // float(a[l+1:MAX]) )+a[MAX:len(a)]
                
            except decimal.DivisionByZero:
                return 0
            except ZeroDivisionError:
                return 0
            
        i += 1
    i = 0
            
    while i < len(a):
        
        if a[i] == "+":
            MAX = len(a)
            MIN = 0
            s = i-1

            for i2 in range(i+1, len(a)):

                if a[i2] not in numbers:

                    MAX = i2
                    break

            while s > 0:
                if a[s] not in numbers:

                    MIN = s+1
                    break
                s -= 1
            d2 = len(a[MIN:i])

            l = i
            i = i - d2 -1
          
            try:
                a = a[0:MIN]+str(float(a[MIN:l]) + float(a[l+1:MAX]) )+a[MAX:len(a)]
                
            except decimal.DivisionByZero:
                return 0
            except ZeroDivisionError:
                return 0
 
        elif a[i] == "_":
            MAX = len(a)
            MIN = 0
            s = i-1

            for i2 in range(i+1, len(a)):

                if a[i2] not in numbers:

                    MAX = i2
                    break

            while s > 0:
                if a[s] not in numbers:

                    MIN = s+1
                    break
                s -= 1
            d2 = len(a[MIN:i])

            l = i
            i = i - d2 -1
            
            try:
                a = a[0:MIN]+str(float(a[MIN:l]) - float(a[l+1:MAX]) )+a[MAX:len(a)]
                
            except decimal.DivisionByZero:
                return 0
            except ZeroDivisionError:
                return 0

        i += 1
    return a

#print(counte("8+1/9*s(5+2)/3"))