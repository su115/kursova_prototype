import unittest
from Board import Board as B
from Profession import Profession as P
from Subject import Subject as S
from Activity import Activity as A
from Group import Group as G
from Teacher import Teacher as T
import random


class MainTerminalLogic:

    


    
    def __init__(self,board=B(empty=True)):
        self.board = board
        self.b = board # alias
        self.PATH = 'src/board.pickle'


    def sub_menu(self,action):

        #for  Techer,Group,Subject triger to create)
        p_nempty = len(self.b.l_prf)>0
        p_count = len(self.b.l_prf)
        t_count = len(self.b.l_tch)
        s_count = 0
        g_count = 0
        a_count = 0

        # for Activity triger to create)
        tg_nempty = False
#        self.b.print_all()
        if p_nempty:
            for i in self.b.l_prf:
                if len(i.l_grp)>0  and len(self.b.l_tch)>0:
                    tg_nempty=True
                s_count += len(i.l_sbj)
                g_count += len(i.l_grp)
                for j in i.l_sbj:
                    a_count += len(j.l_activity)
                    
        def smenu():
            print('__________'+action+'_Sub Menu_______________')
            print(action+' New Profession:     '+str(p_count)+'\t     P/p')
            if p_nempty:
                print(action+' New Teacher:        '+str(t_count)+'\t    T/t') 
                print(action+' New Group:          '+str(g_count)+'\t    G/g')
                if tg_nempty:
                    print(action+' New Subject:        '+str(s_count)+'\t    S/s')
                    print(action+' New Activity:       '+str(a_count)+'\t    A/a')
                    if action=="Print@":
                        print("Analize Teacher Activity            H/h")
            print('Repeat Menu                         M/m')
            print('Quit:                               Q/q')
        smenu()
        raw = ' '
        obj = ''
        triger = True
        while triger:
            # Input 
            if raw == ' ':
                raw = input()
                if raw == '':
                    raw = ' ' 

            # Profession
            if raw[0]=='P' or raw[0]=='p':
                obj = P
            
            if p_nempty:
                # Teacher
                if raw[0]=='t' or raw[0]=='t':
                    obj = T

                if tg_nempty:
                    # Subject
                    if raw[0]=='S' or raw[0]=='s':
                        obj = S
                    # Action
                    if raw[0]=='A' or raw[0]=='a':
                        obj = "activity"
                    #Analize
                    if action == "Print@":
                        if raw[0]=='H' or raw[0]=='h':
                            self.Tprint()
                            raw = ' ' 
                            return True
                # Group
                if raw[0]=='G' or raw[0]=='g':
                    obj = G
            # Repeat Memu
            if raw[0]=='M' or raw[0]=='m':
                return True
                raw = ' '
                continue

            # Quit
            if raw[0]=='Q' or raw[0]=='q':
                triger = False
                return False
            if obj:
                self.Action(obj,action)
                obj = ''
                return True
            else:
                print('Your choice was:'+raw+' please enter another.')
            raw = ' '




    def Action(self,obj,action):
        if action == 'Create':
            self.create(obj)
        if action == 'Print@':
            self._print(obj)
        return False
    
    def help_type_print(func):
        def choice_list(l,line,Activity_=False):
            print(line)
            for i in range(len(l)):
                if Activity_:
                    print('\t',str(i),'\t',l[i].type_act)
                else:
                    print('\t'+str(i)+'\t'+l[i].name)
            resa = int( input("Choice:") )
            return l[resa]

        
        


        def wrapper(self,obj):
            if type(obj)==type("sdf"):
                wrap=obj
            else:
                wrap = str(type(obj()))
            parent = board = None


            # Teacher and Profession
            if wrap == "<class 'Profession.Profession'>":
                obj = choice_list(self.b.l_prf,"\n\n\tChoice from Professions:\n\n")
            
            if wrap == "<class 'Teacher.Teacher'>":
                obj = choice_list(self.b.l_tch,"\tChoice from Teacher list:\n\n")

            # Subject and Group
            if wrap == "<class 'Subject.Subject'>" :
                prof = choice_list(self.b.l_prf,"\n\n\tChoice from Professions:\n\n")
                obj = choice_list(prof.l_sbj,"\n\n\tChoice from Subjects:\n\n")


            
            if wrap == "<class 'Group.Group'>":
                prof = choice_list(self.b.l_prf,"\n\n\tChoice from Professions:\n\n")
                obj = choice_list(prof.l_grp,"\n\n\tChoice from Groups:\n\n")
           

            # Activity
            if wrap == "activity":
                prof = choice_list(self.b.l_prf,"\n\n\tChoice from Professions:\n\n")
                subj = choice_list(prof.l_sbj,"\n\n\tChoice from Subjects:\n\n")
                obj = choice_list(subj.l_activity,"\n\n\tChoice Activity:\n",True)

            func(self,obj)
        return wrapper


    @help_type_print
    def _print(self,obj):
        obj.print_all()


    def Tprint(self):
        for i in range(len(self.b.l_tch)):
            print(str(i)+'\t'+self.b.l_tch[i].name+'\t'+self.b.l_tch[i].s_name+'\t'+self.b.l_tch[i].l_name )
        resa = int(input("Enter choice:\t"))
        self.b.l_tch[resa].calc_hours()

    def help_type_create(func):
        def wrapper(self,obj):
            if type(obj)==type("sdf"):
                wrap=obj
            else:
                wrap = str(type(obj()))
            parent = board = None




            def find_profession_parent():
                    for i in self.b.l_prf:
                        print( str(i._id) + "\t"  + i.name )
                    resa = int( input( "Choice id:\t" ) )
                    for i in self.b.l_prf:
                        if resa == int(i._id):
                            return i
                    print("You enter not valid id.")





            # Teacher and Profession
            if wrap == "<class 'Profession.Profession'>" or wrap == "<class 'Teacher.Teacher'>":
                parent = board = self.b   #parent = board = '<class 'Board.Board'>' 

            # Subject and Group
            if wrap == "<class 'Subject.Subject'>" or wrap == "<class 'Group.Group'>":
                parent = find_profession_parent()
                board = self.b
           

            # Activity
            if wrap == "activity":
                prof = find_profession_parent()
                print("\n\n\nNow please choice Subject:")
                for i in range( len( prof.l_sbj ) ):
                    print( '\t' + str(i) +"\t" + prof.l_sbj[i].name )
                resa=int( input( "Your choice:" ) )
                parent = prof.l_sbj[resa]
                board = self.b
        
                #print("parent:",type(parent) )
                #o = A(parent=parent,board=board)
                
                
                #parent.add(o)
                parent.terminal_add_activity(parent)

            else:
                func(self,obj,parent,board)

        return wrapper

    @help_type_create
    def create(self,obj,parent,board):
        print( "obj:" , type(obj()), "parent:",type(parent) )
        o = obj(parent=parent,board=board)
        parent.add(o)
        o.terminal_input()
    
    def main_menu_terminal(self):
        raw = ' '
        action = ''

        def menu():
            print('Welcome to terminal version, prototype of program "Інформаційна система навантаження вчителів"!!! ')
            print('=================MAIN MENU==============')
            print('Actions:                         command')
            print('Create                            C/c')
            print('Print@                            P/p')
            print("Remove                            R/r")
            print('Edit#%                            E/e')
            print('Load BOARD:                       L/l')
            print('Make BackUP:                      B/b')
            print('Repeat MENU                       M/m')
            print('Quit:                             Q/q')
            
        menu()  
        triger = True
        while triger:
            if raw == ' ':
                raw = input("Your choice:\t\t")
                if raw =='':
                    raw = ' '
            # Create
            if raw[0]=='C' or raw[0]=='c':
                action = 'Create'

            # Print
            if raw[0]=='P' or raw[0]=='p':
                action = 'Print@'

            # Remove
            if raw[0]=='R' or raw[0]=='r':
                action = 'Remove'

            # Edit
            if raw[0]=='E' or raw[0]=='e':
                action = 'Edit%#'

            # Load Board
            if raw[0]=='L' or raw[0]=='l':
                print("Defauil path is "+self.PATH+"\t Enter new path? [Enter] or N/n:",end='')
                path=input()
                if len(path)>0 and ( path[0] != 'N' or path[0] != 'n'):
                    self.PATH=path
                self.b.load(self.PATH)
                raw = ' '
                print('Loading COMPLETE!!!')
                menu()

            # Make BackUP
            if raw[0]=='B' or raw[0]=='b':
                 print("Defauil path is "+self.PATH+"\t Enter new path? [Enter] or N/n:",end='')
                 path=input()
                 if len(path)>0 and ( path[0] != 'N' or path[0] != 'n'):
                    self.PATH=path
                 self.b.backup(self.PATH,debug=True)
                 raw = ' '
                 print("BackUP COMPLETE!!!")
                 menu()

            # Repeat Menu
            if raw[0]=='M' or raw[0]=='m':
                menu()
                raw = ' ' 

            # Quit
            if raw[0]=='Q' or raw[0]=='q':
                triger = False
                return False
            
            # Make Action or repeat input
            if  action:
                
                while True:
                    if not self.sub_menu(action):
                        break

                action = ''
                raw = ' '
                menu()
            else:
                print('Your choice was:'+raw+' please enter another.')

       

    def create_random_BOARD(self):
        b = self.b
#        p1 = P("ICM","999",parent=b)
#        b.add(p1)
#        t1 = T("Nazar","Chervonuy","Petrovuch",prof=p1,parent=b)
#        b.add(t1)
        for i in range(20):
            p=P.crt_rand(parent=b,board=b) 
            self.b.add(p)
        for i in range(50):
            t = T.crt_rand(prof=random.choice(self.b.l_prf),parent=b) 
            self.b.add(t)
        
        for i in self.b.l_prf:
            for z in range(7):
                    i.add(S.crt_rand(parent=i,board=b))
                    if z%3==0:
                        i.add(G.crt_rand(parent=i,board=b))
        
    def choice_random(self):
        print("DEBUG!!!")
        print("Warning!!! if your Board is empty you can generate Random Board  with random thing!!!")
        print("Please enter Y/y to generate or empty. Y/y")
        choice = input("Your choice:\t")
        if choice == '' or choice == '\n' or choice[0] == 'y' or choice[0] == 'Y':
            self.create_random_BOARD()
            print("RANDOM BOARD was generated!!!")

class TestMainLogic(unittest.TestCase):
    def test_main_menu_terminal(self):
        m = MainTerminalLogic()
        m.choice_random()
#        m.create_random_BOARD()
    #    m.b.l_tch[0].calc_hours()
        m.main_menu_terminal()
    
if __name__ == "__main__":
    unittest.main()
