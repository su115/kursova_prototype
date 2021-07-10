import names
import unittest
import random
import Board as B
import Profession as P


class Teacher:
    parent = None
    board = None
    def __init__(self,name="*",s_name="*",l_name="*",prof=0,parent=None,board=None):    
        self.name=name
        self.s_name=s_name
        self.l_name=l_name
        self.prof = prof
        self.board = board
        self.parent = parent
        if board:
            #set board
            self.board = board   
            #check prof with exists Subject _id 
            typ = str( type(prof) )
            if typ == "<class 'Profession.Profesion'>":
                if not prof in board.l_prf:
                        raise Exception("class Teacher:prof dont exist in parent!!!")


    def terminal_input(self):
        # need PARENT !!!!(parent = BOARD)!!!

        print("Teacher:\nname:\t\t",end='')
        self.name = str(input())
        print("secound name:\t",end='')
        self.s_name = str(input())
        print("last name:\t",end='')
        self.l_name = str(input())
        print("choice profession id:")
        def menu_profesion():
            for i in self.parent.l_prf:
                print(str(i._id)+" "+str(i.name))
            print("\nEnter Teacher Profession:\t",end='')    
            return int(input())
        self.prof = menu_profesion()

    def print_name(self):
        print("Teacher:",self.name,self.s_name,self.l_name,self.prof)


    def print_all(self):
        print("name:\t\t",self.name)
        print("s_name:\t\t",self.s_name)
        print("l_name:\t\t",self.l_name)
        print("profession:\t",self.prof)
        # print("hours",self.hours) # not now

    def __eq__(self,other):
        if (self.name != other.name):
            return False
        if (self.s_name != other.s_name):
            return False
        if (self.l_name != other.l_name):
            return False
        if (self.prof != other.prof):
            return False
        return True
    
    @classmethod
    def crt_rand(self,simple=True,prof=None,parent=None):
        if simple:
            if parent:
                if prof:
                    n=names
                    return Teacher(n.get_first_name(),n.get_first_name(),n.get_last_name(),prof=prof,parent=parent)

                n = names
                return Teacher(n.get_first_name(),n.get_first_name(),n.get_last_name(),int(random.choice(parent.l_prf)._id),parent)
            return Teacher(names.get_first_name(),names.get_first_name(),names.get_last_name(),random.randint(1,100),parent)
        return Teacher("*","*","*",99)
    
    def get_str_name(self):
        if type( self.prof )==type(int()):
            return self.name+self.s_name+self.l_name+"\t"+str(self.prof)
        #print("Not int!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return self.name+self.s_name+self.l_name+'\t'+str(self.prof._id)

    def calc_hours(self):
        
        def get_Teacher_List_Activity():
            
            
            t_str = self.get_str_name()
            list_act = []
            for x in self.parent.l_prf:
               for i in x.l_sbj:
                    for j in i.l_activity:
                        tmp = j.teacher.get_str_name()
        #                print("tmp\t",tmp,end='\t\t\t')
        #                print("t_str\t:",t_str)
                        if tmp == t_str:
                            list_act.append(j)

            print("All in OK!!!",len(list_act))
            return list_act
        
        
        #need parent
        print("Calculate hours: for teacher:\t",self.name,self.s_name,self.l_name)

        l_active = {"лекція":0,"лабораторна":0, "практична":0, "самостійна":0,"контрольні":0, "екзамен":0,"консультація":0}
        l_current ={"лекція":0,"лабораторна":0, "практична":0, "самостійна":0,"контрольні":0, "екзамен":0,"консультація":0}
        l_type = list( l_active.keys() )
        


        list_act = get_Teacher_List_Activity()
        for act in list_act:
            tmp=act.type_act
#            print("type:activity:\t",tmp)
#            print("act_hours:\t",act.act_hours)
#            print("current_hours:\t",act.cur_hours)
            l_active[tmp] += act.act_hours
            l_current[tmp]+= act.cur_hours
        self.print_name()
        print("Active hours:",l_active)
        print("Current hours:",l_current)








        # UnitTests
class TestTeacher(unittest.TestCase):
    def test_simple(self):
        # __init__() print_all()
        try:
            a = Teacher("Petro","Pertovich","Ivanenkiv","ICM")
            #a.print_all()
        except:
            self.assertTrue(False,"Проблеми з Teacher:__init__ or print_all")
    
    def test_eq(self):
        # __eq__() crt_rand()
        try:
            a = b = Teacher.crt_rand()
            c = Teacher.crt_rand()
            if (a !=b or a == c):
                raise("Some problems with crt_random() or __eq__()")
        except:
            self.assertTrue(False,"Teacher:__eq__() or crt_rand() !!!")


    def test_init(self):
        #crt_rand() __init() X5
        for i in range(5):
            try:
                g = Teacher.crt_rand()
            except:
                self.assertTrue(False,"Anomal 2")

#Because somebody must input from keyboard :(
#    def test_terminal(self):
#        b = B.Board() 
#        p = P.Profession.crt_rand
#        for i in range(20):
#            b.add(p())
#        t = Teacher(board=b,parent=b)
#        t.terminal_input()  
#        t.print_all()





    def test_calc_hour(self):
        b = B.Board()
        b.load('src/board.pickle')
        t = random.choice(b.l_tch)
        t.calc_hours()

if "__main__"==__name__:
    unittest.main()

