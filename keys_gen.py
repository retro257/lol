

def gen(sol):
    finish = []
    
    result = {}
    for i in range(0, sol):
        result[i] = 0
    keys = ("+", "_", "*", "/")
    max = 4**sol
    now_num = 0

    for i in range(0, max):
        rs = []
        for t in range(0, sol):
            if result[t] == 4 and t != sol-1:
                result[t] = 0
                result[t+1] += 1
        for t in range(0, len(result)):
            rs.append(keys[result[t]])
        finish.append(rs)
        result[0] += 1
    return finish
