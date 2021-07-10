# Imports^:
import Teacher as T
import unittest
import Group as G
import random
import Profession as P
import Board as B
import Subject as S

class Activity:
    parent = None
    board = None
    def __init__(self, type_activity="$#!@", act_hours=0, cur_hours=0, group=None,teacher=None, profession=None,parent=None,board=None):

        # set parent        
        self.parent = parent
        self.board = board

        self.type_act = type_activity
        self.act_hours = act_hours
        self.cur_hours = cur_hours

        self.group = group   
        self.teacher = teacher
        
        

    def print_name(self):
        print("type of activity:\t",self.type_act)

    def print_all(self):
        print("type of activity:\t",self.type_act)
        print("activity hours:\t\t",self.act_hours)
        print("current hours:\t\t",self.cur_hours)
        print("group:\t\t\t",self.group.g_name)
        print('teacher:\t\t',self.teacher.name,self.teacher.s_name)
        #Group.print_all() 
        #print("="*14,"\nGroup:")
        #self.group.print_all()
        #print("="*14)

        #Teacher.print_all()
        #print("="*14,"\nTeacher:")
        #self.teacher.print_all()
        #print("="*14)

    def __eq__(self,other):
        if (self.type_act != other.type_act):
            return False
        if (self.act_hours != other.act_hours):
            return False
        if (self.cur_hours != other.cur_hours):
            return False
        if (self.group != other.group):
            return False
        if (self.teacher != other.teacher):
            return False
        return True

    @classmethod
    def crt_rand(self,teacher=None,group=None,profession=None,board=None,parent=None):
        # Трохи складніший рандом
        l = {"лекція":64,"лабораторна":32, "практична":32, "самостійна":40,"контрольні":6, "екзамен":4,"консультація":2}
        choice = random.choice(list(l.keys()))
        if (not teacher):
            #print("class Activity:Board!!!--->",board)
            if not board :
                teacher = T.Teacher.crt_rand()
            else:
                teacher = random.choice(board.l_tch)
        if (not group):
            if  profession:
                group = random.choice(profession.l_grp)
            else:
                group = G.Group.crt_rand()

        act_hours = random.randint(l[choice]/2,l[choice])
        cur_hours = random.randint(0,act_hours)
        return Activity(choice,act_hours, cur_hours,group,teacher,profession,parent=parent,board=board)


# Юніт тести
class TestActivity(unittest.TestCase):
    def test_simple(self):
        # To test "print_all" and "__init__"
        try:
            b = B.Board()
            
            p = P.Profession(parent=b)
            b.add(p)
            s = S.Subject(parent=p,board=b)
            p.add(s)
            a = Activity(parent=s,profession=p,board=b)
        except:
            self.assertTrue(False,"Є проблеми в __init__ або print_all класу Activity!!!")
    def test_parent(self):
        # __init__() parent,board,
        b = B.Board()
        p = P.Profession.crt_rand(parent=b)
        b.add(p)
        t = T.Teacher(parent=b,prof=p)
        b.add(t)
        s = S.Subject.crt_rand(1,board=b,parent=p)
        a = Activity(parent=s,board=b,teacher=t,profession=p)




if __name__=='__main__':
    unittest.main()

