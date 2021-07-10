import unittest
import random
import Board as B
import Profession as P
import string


class Group:
    parent = None
    board = None
    def __init__(self,g_name="#@$$%",course=0,num_student=0,board=None,parent=None):
        self.g_name=g_name
        self.course=course
        self.num_student=num_student
        
        #set parent
        self.parent = parent
        self.board = board
        if board:
            if parent:
                if not parent in board.l_prf:
                    raise Exception("class Group:Profession is not exists in Board!")
            
        # спроба створити alias для self.g_name -> self.name
        self.name = self.g_name
    
    def terminal_input(self):
        # Nead Board to choice Parent
        self.g_name=input("Group:\ngroup name:\t\t")
        self.course=int(input("course:\t\t\t"))
        self.num_student=int(input("number of student:\t"))
#        print(type(self.board))
        for i in self.board.l_prf:
            print(str(i._id)+" "+ str(i.name)+'\t\t')

        #parent = int(input("Choice group profession:\t"))
        #for i in self.board.l_prf:
        #    if int(i._id)==parent:
        #        self.parent=i

    def print_name(self):
        print("Group name:",self.g_name)

    def print_all(self):
        print("group name:\t\t",self.g_name)
        print("course:\t\t\t",self.course)
        print("number of student:\t",self.num_student)
        print("profession id:\t\t",self.parent._id)
    def __eq__(self,other):
        if (self.g_name != other.g_name):
            return False
        if (self.course != other.course):
            return False
        if (self.num_student != other.num_student):
            return False
        return True

    @classmethod
    def crt_rand(self,parent=None,board=None):
        #Too simple to unittest
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(2))
        return Group(result_str.upper()+"-"+str(random.randint(10,500)),random.randint(1,5),random.randint(8,40),parent=parent,board=board)

# UnitTests
class TestGroup(unittest.TestCase):
    def test_simple(self):
        # __init__() and print_all()
        try:
            g = Group("IT-23",2,8)
            #g.print_all()
        except:
            self.assertTrue(False,"Є проблеми в Group:__init__ or print_all !!!")

    def test_eq(self):
        #__eq__()
        try:
            a = Group("IT-33",2,40)
            b = Group("IT-33",2,40)
            c = Group("ii",6,6)
            if (a == c or a != b):
                raise("__eq__ don`t work !!!")
        except:
            self.assertTrue(False,"class Group:__eq__ don`t work !!!")

#    def test_terminal_input(self):
#        b = B.Board()
#        p = P.Profession.crt_rand
#        for i in range(10):
#            tmp = p(parent=b,board=b)
#            b.add(tmp)
#        g = Group(board=b)
#        g.terminal_input()
#        g.print_all()

if __name__=='__main__':
    unittest.main()
