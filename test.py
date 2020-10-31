

str_ = "My Name is Sakthi"

print(str_[::-1]) 

letter_list = list()

for letter in range(len(str_)-1,-1,-1):
    #import pdb;pdb.set_trace()
    letter_list.append(str_[letter])
print letter_list

print ("".join(letter_list))

class A(object):
    def __init__(self):
        if getattr(self.__class__, '_has_instance', False):
            raise RuntimeError('Cannot create another instance')
        self.__class__._has_instance = True
        print ("hi i ma boy")


obj1 = A()

obj2 = A()














