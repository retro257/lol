def gen_sqrt(input_ex):
    
    input_ex = input_ex+" "
    pattern = "1234567890."
    
    len_sqrt = 1
    
    finish = []
    m = 0
    for i in input_ex:
        if i not in pattern:
            m += 1
    while len_sqrt != m+1:
        now_len = 0
        can = False
        MIN = 0
        MAX = 0
        
        i = 0
        while i < len(input_ex):
            
            if input_ex[i] in pattern:
                if i == 0:
                    if can == False:
                        
                        MIN = i
                        k = 0
                        
                        can = True
                else:
                    if input_ex[i-1] not in pattern:
                        if can == False:
                        
                            MIN = i
                            k = 0
                            
                            can = True

            else:
                if can:
                    
                        
                    
                    now_len += 1
                    
                    if now_len % len_sqrt == 0:
                        MAX = i
                        can = False
                        finish.append(input_ex[0:MIN]+"s("+input_ex[MIN:MAX]+")"+input_ex[MAX:len(input_ex)])

                        
                        i -= MAX-MIN-1
                        
            i += 1
        
        len_sqrt += 1
        
            
    return(finish)
#print(gen_sqrt("1254+20.0-21*8-12-4"))