import unittest
import random
import Activity as A
import Board as B
import Profession as P  
import Teacher as T
import Group as G
import Subject as S
# Variables
PATH_TO_S_NAMES = "src/subjects"

class Subject:
    parent = None
    board = None
    _is = False
    def check_l_activity(self,l_activity):
        tmp_type = type(A.Activity.crt_rand())
        for i in l_activity:
            if type(i) != tmp_type:
                raise("class Subject: get rubbish in l_activity !!!")
        return True


    def __init__(self,name="@#$%",l_activity=[],board=None, parent=None):
        self.name = name

        #set parent
        self.parent = parent
        self.board = board
        if board:
            if  parent:
                    if not self.parent in self.board.l_prf:
                        raise Exception("class Subject:Profession isn`t exists on Board!!!")
            
        if  (self.check_l_activity(l_activity)):
            self.l_activity = l_activity
        else:
            self.l_activity = []
        self.rep_l_activity()

    def terminal_input(self):
        # Need BOARD TO choice parent!!!
        self.name=input("Subject:\nsubject name:\t")
        
        #for j in range(len( self.board.l_prf)):
        #    i=self.board.l_prf[j]
        #    print(str(j)+"<-- id:\t"+ str(i._id)+"\t"+str(i.name))
            
        #resa = int(input("Choice Profesion for subject:\t\t"))
        #self.parent = self.board.l_prf[resa]


    @staticmethod
    def terminal_add_activity(self):

        #print("Do you want add Activity^?  y/n")
        #tmp = input()
        #if tmp[0]=='N' or tmp[0]=='n':
        #    print("::::::::::::::::off:::::::::::::::::::")
        #    return False
        l = {"лекція":64,"лабораторна":32, "практична":32, "самостійна":40,"контрольні":6, "екзамен":4,"консультація":2}
        ll = list(l.keys())
        line=""

        # Buffer Overflow~!!!!!!!
        for i  in range(len(ll)):
            print(str(i)+" "+ll[i],end='\t')

        print("\nPlease choice type of activity:",end='\t' )

        resa = int(input())
       
        type_activity=ll[resa]
        act_hours =l[ ll[resa]]
        print("Active hours:\t",str(act_hours),end='\t')
        cur_hours= int(input("Please input current hours:"))
        print("\nPlease choice Teacher:")
        
        #Teacher
        #for i in range(len(self.board.l_tch)):
         #   if self.board.l_tch[i] == self.parent:
          
        i = [int(x.prof) for x in self.board.l_tch].index(self.parent._id)
        print('\t'+str(i)+"\t"+self.board.l_tch[i].name+"\t"+self.board.l_tch[i].s_name)

        resa =int( input("Your chice:\t\t") )
        teacher = self.board.l_tch[resa]

        
        #Group
        print("Groups")
        for i in range(len( self.parent.l_grp)):
            # print("Subject parent--->",type(self.parent))
            print(i, self.parent.l_grp[i].g_name)
        resa = int( input("Choice Group please:\t") )
        group = self.parent.l_grp[resa]

        a = A.Activity(type_activity,act_hours,cur_hours,teacher=teacher,group=group,parent=self,board=self.board)
        self.add(a)

            


            




    def add(self,a):
        if (type(a)==A.Activity):
            self.l_activity.append(a)
        else:
            raise("class Subject: add get rubbish !!!")

    @staticmethod
    def is_in(c,obj):
        return obj in c

    def remove(self,a):
        self.l_activity.remove(a)


    def print_name(self):
        print("Subject name:\t",self.name)
        for i in self.l_activity:
            i.print_name()

    def print_all(self):
        print("subject name:\t",self.name)
        print(self.l_activity)
        #print("="*14)
        #for i in self.l_activity:
        #    i.print_all()
        #    print("-"*14)
        #print("="*14)
    
    @classmethod
    def get_rand_S_name(self):
        with open(PATH_TO_S_NAMES) as f:
            l_name = f.readlines()
        l_name = [x.strip() for x in l_name]
        #name = l_name[random.randint(0,len(l_name)-1)]
        name = random.choice(l_name)
        return name


    @classmethod
    def crt_rand(self,sing=5,board=None,parent=None):
        name = self.get_rand_S_name()
        l_act = []
        
        if type(sing)==type(int() and sing > 0):
            for i in range(sing):
                l_act.append(A.Activity.crt_rand(board=board,parent=self))      

 
        if type(sing)==type([]) and check_l_activity(sing):
            l_act = sing

        return Subject(name,l_act,board=board,parent=parent)
        
    def __eq__(self,other):
        if self.name != other.name or len(self.l_activity) != len(other.l_activity):
            return False
        for i in self.l_activity:
            if not i in other.l_activity:
                return False
        return True

    def rep_l_activity(self):
        # Ця функція повинна навусти лад з Activities щоб не було повторів по типу активності
        tmp =[]
        tmp_l_type=[]
        for i in self.l_activity:
            if i.type_act not in tmp_l_type:
                tmp.append(i)
                tmp_l_type.append(i.type_act)
        self.l_activity = tmp

#UnitTest
class TestSubject(unittest.TestCase):
    def test_simple(self):
        # __init__() print_all() get_rand_S_name() check_l_activity() rep_l_activity()
        try:
            l = []
            l.append(A.Activity.crt_rand())
            l.append(A.Activity.crt_rand())
            l.append(A.Activity.crt_rand())
            Subject(Subject.get_rand_S_name(),l)
        except:
            self.assertTrue(False,"class Subject:ERROR in __init__() or print_all() or get_rand_S_name() !!!")


    def test_crt_rand(self):
        # crt_rand() __eq__() 
        try:
            s1 = s2 = Subject.crt_rand()
            l = []
            l.append(A.Activity.crt_rand())
            l.append(A.Activity.crt_rand())
            l.append(A.Activity.crt_rand())
            s3 = Subject(Subject.get_rand_S_name(),l)
            if s1 != s2 and s3 == s1:
                raise("class Subject:__eq__() or crt_rand() ERROR !!!")
        except:
            self.assertTrue(False,"class Subject:__eq__() or crt_rand()")

    def test_init_anomaly(self):
        # __init__() get_rand_S_name() check_l_activity() rep_l_activity() __del__()  X50
        try:
            
            for i in range(50):
                g = Subject(Subject.get_rand_S_name(),[])
        except:
            self.assertTrue(False,"Catch Anomaly!")


    def test_is_in(self):
        b = B.Board(empty=True)
        p = P.Profession(empty=True,parent=b)
        b.add(p)
        s = Subject(parent=p,board=b)
        t = T.Teacher.crt_rand(parent=b)
        b.add(t)
        a = A.Activity.crt_rand(parent=s,board=b)
        s.add(a)
        if not s.is_in(s.l_activity,a):
            raise Exception("class Subject:is_in dont work~~!!")

    #def test_terminal_input(self):
    #    b = B.Board()
    #    for i in range(10):
    #        b.add(P.Profession.crt_rand(parent=b,empty=True))
    #    p = random.choice(b.l_prf)
    #    #print(b.print_name())
    #    for i in range(10):
    #        b.add(T.Teacher.crt_rand(parent=b,prof=random.choice(b.l_prf)  ))
    #    s = S.Subject(board=b)#,parent=p)
    #    s.terminal_input()
    #    s.terminal_add_activity()
    #    s.print_all()
        

if "__main__"==__name__:
    unittest.main()
