from copy import copy
import time
start_time = time.time()

from test import counte
from test2 import generat
from keys_gen import gen
from gen_sqrt import gen_sqrt
import math
from sys import stdout

def find(arg, result):
   ended = []
   fn = 0
   comds = generat(arg)

   cd = gen(len(arg)- 1)

   all = len(comds) * len(cd)

   for i in comds:
      l = ""
      for t in range(0, len(i)):
         if t == len(i)-1:

            l = l + i[t]
         else:
            l = l + i[t] + " "
      

      for t in cd:
         copy_l = l
         a = 0
         for t2 in range(0, len(l)):
            if l[t2] == " ":
               copy_l = copy_l[0:t2]+t[a]+copy_l[t2+1:len(l)]
               a += 1
         
         l_with_sqrt = gen_sqrt(copy_l)
         if i == comds[0] and t == cd[0]:
            all *= len(l_with_sqrt)+1

         ended.append(copy_l)
         ended.append(counte(copy_l))

         fn += 1
         for i1 in l_with_sqrt:
            ended.append(i1)
            ended.append(counte(i1))
            fn += 1
            if float(counte(i1)) == float(result):
               None
         w = str(fn/all*100)
      print(w[0:6]+" %") 

   return(ended)   
         
         #if float(counte(copy_l)) == float(result):
         #   print(copy_l, counte(copy_l))
      

   
#find(["8", "1", "3", "7", "2", "6", "9"], "28")

print("--- %s seconds ---" % (time.time() - start_time))