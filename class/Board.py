import Teacher as T 
import Profession as P
import unittest
import pickle
import os
import Board as B


TEST_BL_PATH = "src/test_board.pickle"
BL_PATH = "src/board.pickle"


class Board:
    l_tch = []
    l_prf = []
    def __init__(self,l_tch=None,l_prf=None,empty=False):
        if not empty:
            def rep_l(l):
                l_name = []
                l_obj = []
                for i in l:
                    if not i.name in l_name:
                        l_obj.append(i)
                        l_name.append(i.name)
                return l_obj
            if  l_tch:
                self.l_tch=rep_l(l_tch)
            if  l_prf:
                self.l_prf=rep(l_prf)
        elif empty:
            l_prf = []
            l_tch = []
    
    #decorator
    def type_help(func):
        def wrapper(self,soup):
            wrap = str(type(soup))
            #print('Board type_help:wrap',wrap,str(type(self)))
            if wrap == "<class 'Profession.Profession'>" or wrap == "<class '__main__.Profession'>":
                #print("IN type help Prafession",wrap)
                func(self,self.l_prf,soup)
            elif wrap == "<class 'Teacher.Teacher'>" or wrap == "<class '__main__.Teacher'>":
                func(self,self.l_tch,soup)
        return wrapper


    @type_help
    def add(self,c,obj):
        #print("add",type(obj),type(c))
        c.append(obj)

    @type_help
    def remove(self,c,obj):
        c.remove(obj)
   
    #@classmethod

    @staticmethod
    def is_in(c,obj):
        # print("IS_IN")
        return obj in c


    def print_name(self):
        def p(l):
            for i in l:
                i.print_name()
        p(self.l_tch)
        p(self.l_prf)

    def print_all(self):
        def prnt(l):
            print(l)
            #print("="*14)
            #for i in l:
            #    i.print_all()
            #print("="*14)

        print("+"*7, "BOARD","+"*7)
        print(len(self.l_tch),"l_tch")
        prnt(self.l_tch)
        prnt(self.l_prf)

    def crt_rand(self,simple=True):
        if simple:
            return Board([T.Teacher.crt_rand()],[P.Profession.crt_rand()])
        return Board([T.Teacher.crt_rand(simple=False)],[P.Profession.crt_rand(simple=False)])


    def backup_manager(func):
        def wrapper(self,path,debug=False):
            if os.path.exists(path):
                if not debug:
                    raise Exception("class Board: backup(): file ",path," already exist!")
                os.remove(path)
            func(self,path)
        return wrapper
    
    def load_manager(func):
        def wrapper(self,path):
            if not os.path.exists(path):
                raise Exception("class Board: backup(): file ", path," not found!")
            func(self,path)
        return wrapper

    @backup_manager
    def backup(self,path):
        # path with filename
        profs_g=[]
        profs_s=[]

        for i in self.l_prf:
            profs_g.append(i.l_grp)
            profs_s.append(i.l_sbj)

        with open(path,"wb") as f:

            data = [self.l_tch, self.l_prf,profs_g,profs_s]
            pickle.dump(data,f)

    @load_manager
    def load(self,path):
        with open(path,"rb") as f:
            data = pickle.load(f)
            def put_l(l,sl):
                sl.clear()
                for i in l:
                    sl.append(i)
            put_l(data[0],self.l_tch)
            put_l(data[1],self.l_prf)
            profs_g = data[2]
            profs_s = data[3]
            for i in self.l_prf:
                i.l_grp =profs_g[ self.l_prf.index(i)]
                i.l_sbj =profs_s[self.l_prf.index(i)]

    def __eq__(self,other):
        def l_eq(l1,l2):
            if len(l1) != len(l2):
                return False
            for i in l1:
                if not i in l2:
                    return False
            return True
        if not l_eq(self.l_tch,other.l_tch):
            return False
        if not l_eq(self.l_prf,other.l_prf):
            return False
        return True








class TestBoard(unittest.TestCase):
    def test_decorator(self):
        # add() remove() __init__() 
        b = Board()
        p = P.Profession.crt_rand()
        t = T.Teacher.crt_rand()
        b.add(t)
        b.add(p)
        #b.print_all()

    
    def test_init(self):
        # add() remove() __init__() crt_rand()
        b = Board()
        t = T.Teacher.crt_rand
        b.add(t())
        b.add(t())
        b.add(t())

    def test_backup(self):
        # add() __init__() crt_rand() backup() load() __eq__()
        b = Board()
        #b.print_name()

        t = T.Teacher.crt_rand
        p = P.Profession.crt_rand
        b.add(t())
        b.add(t())
        b.add(t())
        b.add(p())
        b.add(p())
        b.add(p())

        b.backup(TEST_BL_PATH,debug=True)
        z = Board()
        z.load(TEST_BL_PATH)
        #b.backup(TEST_BL_PATH)
        if z != b:
            raise Exception("Backup or load function dont work as must!")


    def test_is_in(self):
        b =B.Board(empty=True)
        #b1.print_all()
        p = P.Profession(empty=True)
        b.add(p)
        #b.print_name()
        t1=T.Teacher(parent=b,prof=p)
        b.add(t1)
        #b.print_all()
        if not b.is_in(b.l_tch,t1):
            raise Exception("class Board:is_in() dont work")

if "__main__"==__name__:
    unittest.main()



