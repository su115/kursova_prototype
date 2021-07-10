#import 
import unittest
import Subject as S
import Group as G
import Board as B
import Profession as P
import random
import copy

PROFESSIONS_AND_IDS = "src/professions"


class Profession:
    l_sbj = []
    l_grp = []
    parent = None
    board = None
    def __init__(self,name="@",_id=0,l_sbj=[], l_grp=[],empty=False ,parent=None,board=None):
        self.name = name
        self._id = _id
        self.board = board
        #set parent
        self.parent = parent
        if not empty:
            # for l_sbj and l_grp
            def set_list(C,l,sl):
                if type(l) == type(int()) and l >= 0:
                    for i in range(l):
                        sl.append(C.crt_rand(parent=self,board=board ) )
                elif type(l) != type(list()):
                    print(l)
                    raise Exception("class Profession:__init__() l_%%% not int or list")
                elif type(l) == type(list()):              
                    # нема перевірки типу просто на список
                    for i in l:
                        sl.append(i)
            


            def rep_l(sl):
                # шукає предмети із однаковими назвами і видаляє їх в 1 Profession усі предмети мають бути унікальні
                # це особливо важливо коли предмети створені рандомом
                # Group аналогічно
                
                l_name =[]
                l_obj = []
                for i in sl:
                    if not i.name in l_name:
                        l_obj.append(i)
                    l_name.append(i.name)
                sl.clear()
                for i in l_obj:
                    sl.append(i)
    
            set_list(S.Subject,l_sbj,self.l_sbj)
            set_list(G.Group,l_grp,self.l_grp)
            rep_l(self.l_sbj)
            rep_l(self.l_grp)
            
        elif empty:
            self.l_sbj = []
            self.l_grp = []

    def print_name(self):
        print("Profession: ",self._id,self.name)
        def printL(l):
            for i in l:
                i.print_name()
                print("="*14)
        printL(self.l_sbj)
        printL(self.l_grp)

    def print_all(self):
        print("Profession name:\t",self.name)
        print("Profession id:\t\t",self._id)
        print("="*14) 
        def print_list(l):
            print(l)
            # for i in l:
           #     i.print_all()
           #     print("="*14)
        print_list(self.l_sbj)
        print_list(self.l_grp)
        

    
    def __eq__(self,other):
        if self.name != other.name:
            return False
        
       
        # check if lists are eq
        def list_eq(l1,l2):
            for i in l1:
                if not i in l2:
                    return False
            return True

        if not list_eq(self.l_sbj,other.l_sbj) and list_eq(self.l_grp,other.l_grp):
                    return False
        if not ( len(self.l_sbj)==len(other.l_sbj) and len(self.l_grp)==len(other.l_grp) ):
            return False
        return True
 
    @classmethod
    def crt_rand(self,g_count=0,s_count=0,simple=True,parent=None,empty=False,board=None):
        # In process
        if simple:
            with open(PROFESSIONS_AND_IDS) as f:
                soup = f.readlines()
            soup = [x.strip() for x in soup]
            _id,name = random.choice(soup).split(' ')
            #print("class Profesion",parent,board)
            return Profession(name,_id,s_count,g_count,parent=parent,board=board)
        return Profession("*",99,[],[],parent=parent,empty=empty,board=board)
    

    def terminal_input(self):
        # NEED PARENT (PARENT=BOARD)

        def id_stability(_id):
            for i in self.parent.l_prf:
                if int(i._id) == _id:
                    raise Exception("class Profession: id is occupied by another Profesion.")
            return _id
        self.name = str(input("Profession\nprofession name:\t"))


        line = ""
        #print("len of parent.l_prf:",len(self.parent.l_prf))
        for i in self.parent.l_prf:
            line += str(i._id)+" "+str(i.name)+"\t"
            if len(line) > 100:
                print(line)
                line = ""


        self._id = id_stability(int(input("profession id:\t\t")))
        self.l_sbj = []
        self.l_grp = []




    def help_type(func):
        def wrapper(self,soup):
            wrap = str(type(soup))
            #print("class Profession:wrap=",wrap)

            if wrap == "<class 'Subject.Subject'>" or wrap == "<class '__main__.Subject'>":
                func(self,self.l_sbj,soup)
            elif wrap == "<class 'Group.Group'>" or wrap == "<class '__main__.Group'>":
                func(self,self.l_grp,soup)
        return wrapper

    @help_type
    def add(self,c,obj):
        
        c.append(obj)
#        print("Group was append:",c)


    @help_type
    def remove(self,c,obj):
        c.remove(obj)

    #@classmethod

    @staticmethod
    def is_in(c,obj):
        return  obj in c
        


class TestProfession(unittest.TestCase):
    def test_simple(self):
        # __init__() print_all()
        try:
            l_s = []
            l_g = []
            def l_append_rand(l,C):
                for i in range(4):
                    l.append(C.crt_rand())
            
            l_append_rand(l_s,S.Subject)
            l_append_rand(l_g,G.Group)
            
            p = Profession("ITIS",1,l_s,l_g)
            p = Profession("ISM",2,4,5)
            #p.print_all()
        except:
            self.assertTrue(False,"class Profession:")

    def test_crt_rand(self):
        # crt_rand()  __init__()
        try:
#            for i in range(100): 
                p1 = Profession.crt_rand(3,3)
                p2 = copy.deepcopy(p1)
                p3 = Profession.crt_rand(4,3)

                # однакові p3 i p1 дуже часто
 #               if p1 != p2 or p1 == p3:
  #                  raise Exception("class Profession:__eq__ or crt_rand ERROR !!!")
        except:
            self.assertTrue(False,"class Profesion: ERROR plese check test_crt_rand() to find error.")
    
    def test_init(self):
        # crt_rand() __init__() x5
        try:
            for i in range(5):
                Profession.crt_rand()
            Profession.crt_rand(20,20)

        except:
            self.assertTrue(False,"class Profession: ANOMALY was found !!!")

    
    def test_help_type(self):
        # add() @help_type remove()
        b = B.Board()
        p = Profession(parent=b)
        g = G.Group.crt_rand
        s = S.Subject.crt_rand
        g1 = g()
        p.add(g1)
        p.add(g())
        p.remove(g1)
        p.add(s())
        s1 = s()
        p.add(s1)
        p.remove(s1)


    def test_is_in(self):
        # is_in() add() __init__()
        b = B.Board()
    
        p = Profession(1,1,parent=b)
        b.add(p)
        g = G.Group.crt_rand()
        #g.print_all()
        p.add(g)

        if not p.is_in(p.l_grp,g):
           raise Exception("class Profession: is_in() don`t work")


    

#    def test_terminal_input(self):
#        b = B.Board()
#        for i in range(20):
#            p1 =Profession.crt_rand(1,1)
#            print(p1.name)
#            b.add(p1)

#        b.print_all()
            
#        p = Profession(parent=b)
#        p.terminal_input()
#        p.print_all()



    def test_empty_profession(self):
        b = B.Board()
        p = P.Profession(empty=True)
        #p.print_all()



if "__main__" == __name__:
    unittest.main()
