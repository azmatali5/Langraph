                              #     type anotation 

# Typed Dictionary
from typing import TypedDict 
import random
class movies(TypedDict):
      name :str
      age : int

movies=movies(name='boss',age=206)

 
 # union 

# from typing import any , Optional,Union

                                 #  lambda function   
#  with one argument 

summ= lambda summ: summ *summ 
summ(10)
                                
# with two agument 

sum2=lambda y,z: y*z
print(sum2(2,3))


pr = lambda a,b: print(a,b)
pr('ali',"az")

