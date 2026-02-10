import pickle



hp,ehp=0,0
print('''You open your eyes to see a realm of darkness.
You are unable to figure out where you are.
Slowly you recall your name...
''')
input('''(Press enter to continue)
 ''')
def pdetails():
    global name
    name=input("Enter your Player Name :- ")
    print()
    if name.isdigit()==True:
        c1=True
        print(name+"...","..perhaps its a roll number.")

    else:
        print(name+"...","hmm... sounds about right.")
    print('''
You soon recall other details about yourself...
You realize that this unfamiliar place that you arrived
at is actually your school, and this realization causes
some of the darkness to clear...
    ''')
    input('''(Press enter to continue)
    ''')
    print("1 - WIZARD")
    #https://ascii.co.uk/art/wizard
    print('''
                                   .   . +  * .o   o.* `.`. +.
                                  '   *  . ' ' |\^/|  `. * .  * 
                                                \V/  
                                                /_\ 
                                               _/ \_
    ''')

    print('''
You are studious, well versed in the arts and sciences.
You prefer careful thought and analysis as opposed to
a more direct, physical approach..
(The Wizard uses magic spells for attacks and can utilize
enemy weaknesses.)
    ''')
    input('''(Press enter to continue)
 ''')

    print("2 - KNIGHT")
    print('''              
                       _.--.    .--._
                     ."  ."      ".  ".
                    ;  ."    /\    ".  ;
                    ;   ._,-/  \-,_.`  ;
                    \  ,`  / /\ \  `,  /
                     \/    \/  \/    \/
                     ,=_    \/\/    _=,
                     |  "_   \/   _"  |
                     |_   '"-..-"'   _|
                     | "-.        .-" |
                     |    "\    /"    |
                     |      |  |      |
             ___     |      |  |      |     ___
         _,-",  ",   '_     |  |     _'   ,"  ,"-,_
       _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
     ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
    !     \  \  \   \                  /   /  /  /     !
    :      \  \  \   \                /   /  /  /      :
    ''')
    print('''You never cared much for studies. You prefer
to act first and ask questions later.
(The Knight uses Physical Attacks)
    ''')
    input('''(Press enter to continue)
 ''')
    global char
    charT=False
    while charT==False:
        char=input("Choose your character (1 or 2) :- ")
        if char=="1":
            char="Wizard"
            charT=True
        elif char=="2":
            char="Knight"
            charT=True
        else:
            print("Invalid character")
    print()
    print("Name:-",name)
    print("Character:-",char)
    print()


import random
global ohp,di,mor
ohp=100
hp=ohp
mor=0
def magic():
    print("1. FLAME - Send a powerful flame from your staff")
    print("2. FREEZE - Unleash a chill blast of ice ")
    print("3. Starlight - Shine Burning Light from your staff")
    print("4. Wind - Unleash a gust of wind from your staff")
    print("5. Lightning - Send out a Lightning Bolt from your staff")
    print("6. Staff Bash - Hit the enemy with your staff")
    while True:
        print()
        op=input("Enter Attack Choice :- ")
        if op=="1":
            atk="flame"
            break
        elif op=="2":
            atk="freeze"
            break
        elif op=="3":
            atk="starlight"
            break
        elif op=="4":
            atk="wind"
            break
        elif op=="5":
            atk="lightning"
            break
        elif op=="6":
            atk="staff bash"
            break
        else:
            print("Invalid choice, enter again")
            continue
    return atk


def code():
    print('''You spot a door with a 4 - digit number
lock.
''')
    input('''(Press enter to continue)
 ''')
    while True:
        print("(Enter 'l' to abandon the door and move on.)")
        print()
        print('''There's a note on the door that reads -
            'There are No herbivores left, except the
             Quad-legged Pentphalia, of which there are
             only One left'
''')
        num=input("What do you enter? :- ")
        print()
        
        dr=False
        if num.lower()=="l":
            print("You decide to leave it")
            break

        elif num.isnumeric()==True:
            if num=="0451":
                print('''...........
                ''')
                input('''(Press enter to continue)
 ''')
                print("The door unlocks!")
                dr=True
                break
            else:
                print("......")
                print()
                print("Its the wrong code")
                continue
        if dr==True:
            return dr
            break  
        else:
            print("Invalid Input, try again")
            continue
    return dr




def metal():
    print('''You peek into the room
to the door's window. All you see is
a furnace.''')
    input('''(Press enter to continue)
 ''')
    print('''But before you try to ponder about why a 
school would have a furnace, your'''+weapon+'''glows.
So you decide to enter the room
''')
    input('''(Press enter to continue)
 ''')
    print('''You peer into the furnace. You back up
as you realize something is moving about in it.
''')
    input('''(Press enter to continue)
 ''')
    print('''Suddenly, a huge, moving lump of 
metal blurts out of the furnace onto the floor.
'..BLHAAARGHHH!!..', it says. ''')
    if mor>0:
        print('''You figure that it won't
be as conversational as some of the other enemies .
''')
    else:
        print('''You don't feel you'll be
able to reason with it, not that you would care..''')
    input('''(Press enter to continue)
 ''')
    enemy(MetalMonster,[])




def sword():

    print("1. Light Thrust  ")
    print("2. Heavy Thrust  ")
    print("3. Light Slash  ")
    print("4. Heavy Slash  ")
    print("5. Blade Flurry - Most Damage, Takes away some of your health")
    print()
    print('''(Thrusts do more damage while
Slashes have higher change of knocking
down the enemy)''')
    while True:
        print()
        op=input("Enter Attack Choice :- ")
        if op=="1":
            atk="lt"
            break
        elif op=="2":
            atk="ht"
            break
        elif op=="3":
            atk="ls"
            break
        elif op=="4":
            atk="hs"
            break
        elif op=="5":
            atk="flurry"
            break
        else:
            print("Invalid choice, enter again")
            continue
    return atk
#EnemyName=["Displayed name",ehp,"Weakness","(Un/)Reasonable","(No/) Escape","'Unreasonable Dialogue'","'No Escape Dialogue'",Latk,Hatk,"Latktext","Hatktext","power",hi,di]
Werewolf=["DARK WEREWOLF",100,"Starlight","Unreasonable","No Escape","'GRRR! No talk, only die!!'","'GRRRR! Get back here!!!'",20,35,"The Werewolf lashes out at you","The Werewolf deals a fearsome blow!","weak",5,10]
Werewolf2=["DARK WEREWOLF BROTHER",120,"Starlight","Unreasonable","No Escape","'GRRR! No talk, only die!!'","'GRRRR! Get back here!!!'",25,40,"The Werewolf lashes out at you","The Werewolf deals a fearsome blow!","weak",7,13]
LWerewolf=["DARK WEREWOLF RULER",150,"Starlight","Rmor","No Escape","'GRRR..Talk?..'","'GRRRR! You must pay for killing my subordinates!!!'",28,45,"The Werewolf lashes out at you","The Werewolf deals a fearsome blow!","strong",8,14]
King=["GOLD ARMOURED KING, BMON",520,"no weakness","Unreasonable","No Escape","'There is no time to talk! Fight and face your death!'","'I'm afraid there is no escape from me!'",40,49,"The King strikes you with his sceptre","The king fires a devastating beam of magic at you!","strong",10,10]
FireDragon=["FIERY DRAGON OF THE COURTYARD",300,"Freeze","RWizard","No Escape",''''Foolish mortal!! To converse
with the likes of you?!
I would rather incinerate'
you!''',''''Trying to escape?! HAH!!'
(The Dragon creates a wall of fire
around you, preventing your escape)''',35,44,"The Dragon swipes at you with it's claws","The Dragon unleashes its fiery breath on you!!","strong",10,14]
IceMonster=["SHARP ICY MONSTER",212,"Flame","Reasonable","No Escape","'..Converse?'","'..Hmm, no wait!'",30,40,"The Monster (reluctantly) swipes a sharp icicle at you",
"The Monster (looking away) releases it's chilly breath on you!","strong",9,13]
MetalMonster=["MONSTER OF METAL",300,"Lightning","Unreasonable","No Escape","'..BLHAAARGHHH..'","'GLRHAAAAA!!!'",32,42,"The Monster forms a fist and punches you","The Monster creates a blade and swipes at you",
"strong",15,15]
MWiz=["WIZARD OF MATH",350,"Staff Bash","RWizard","No Escape","'Converse!? Why, you wouldn't be able to keep up with me!'",''''Trying to Escape?'
The wizard flies his broomstick around to your
back, preventing your escape.''',35,48,'''The Wizard fires a magic bolt at you
(You notice mathematical symbols all
around you, as you get hit)''',"The Wizard, indeed, divides up your health!","weak",16,16]
DKnight=["KNIGHT OF DARKNESS",320,"Starlight","RKnight","No Escape","'Why converse, when we can FIGHT!'","'I'm afraid there's NO escape from me!'",
35,45,"The Knight strikes you with his shield.","The Knight thrusts his sword at you!","weak",16,16]



file=open("reason.dat","wb")
D={}
D["FireDragon"]=["Wizard","'Ahh, an intellectual like myself, sure, let us converse'","'What is your opinion on the injust imprisonment of dragons'",
"'Excellent!, it is good that we see eye to eye on this situation","WHAT?! I should have incinerated you in the beginning!!'",
"'Indifference? I am a beast of fire, I cannot stand indifference!'",
''' 'Do you see dragons as untamed and unintelligent common
beasts, or are you familiar with our artistic and literary works?' ''',
"'Hmph! I should've incinerated you in the beginning!'",
'''Your Response :-
    1. Just as you said, I believe that it
    is extremely injust that magnificient
    creatures such as yourself are imprisoned.
    
    2. I think such terrifying and untamed
    beasts only belong behind strong solid bars!
    
    3. I'm indifferent to the sufferings of dragons
    I'm just trying to get out of this place!
    ''',
'''Your Response :-
    1. Of course! Most of the world's greatest
    artistic and literary minds were of dragon
    origin. Morgaloth's 'Burning a Village' is
    a personal favourite.
    
    2. Dragon literature is the worst kind! Such
    monsters have no concept of style and literary
    cohesion.
    
    3. What're you talking about?! I didnt even know
    they were real, let alone that they have art and
    literature!
    ''',
'''
I'm not feeling particularly hungry today,
so I will give you another chance
''',"1","2","3"]
pickle.dump(D,file)
D.clear()

D["IceMonster"]=["Both","'You wan't to talk? Hmm.. I guess I can do that.'","'...What do you think about ice? In general.' ",
"Yeah..I feel the same way","..Oh, it looks like you're not as understanding as I thought",
"The Ice Monster doesn't laugh",
"'Do you think I look too intimidating?'",
"..Well, It looks like this didn't amount to much",
'''Your Response :-
    1. I couldn't trust something so lifeless and cruel!
    
    2. Hmm.. some people think ice is hostile and threatening
    but I personally think ice is calm and serene. 
    
    3. I think ice is 'Really cool!'
    ''',
'''Your Response :-
    1. Definitely! I wouldn't wan't to be anywhere near
    those sharp icicles!
    
    2. Not Really. Even if those sharp points are probably
    dangerous, I can tell you're kind underneath. 
    
    3. Yeah.. All those sharp icicles make you look like
    some cool robot!
    ''',
'''
'I've got another question'
''',"2","1","3"]
pickle.dump(D,file)
D.clear()
D["KWerewolf"]=["Both","'..Talk?..Grrr, Fine!!'","'Why you kill two of my wulves HRMHH?!'","'Grr! I told all of them 'talk before fight!' but it looks like they no listen!'\n'HRMHH..I will let you go now'",
"'GRRR!! I KILL YOU NOW!!'","'HRMHH, Me understand, but that still no excuse for killing!'","'Me keep hearing 'Wulves have no grammar' and me just don't think is true!!'\n 'What you think?!'",
"'GRRR!! ME KILL YOU NOW!!'",
'''Your Response :-
    1. I saw those dark, terrifying abominations, and knew
    they had to die!
    
    2. Excuse me, but, I have no idea how I got here or
    why I have a weapon, but the first thing I see is two 
    werewolves that seemingly want to kill me, so I think
    my actions are justified.  
    
    3. Well, I tried to reason with them, but they just
    wouldn't listen!
    ''',
'''Your Response :-
    1. Judging by the three I just met, I think that rumour
    is safely true.
    
    2. Umm..actually it's 'I keep hearing that 'Wulves' have 
    no grammar and I don't think that's true.'
    
    3. A completely baseless rumour! I have never heard more
    eloquent beasts.
    ''',
'''
'Me will give one more chance...'
''',"3","1","2"]
pickle.dump(D,file)
D.clear()

D["MWizard"]=["Wizard","'Oh.. A fellow Wizard! Let us converse indeed..'",''''But let me begin with a simple Mathematical question.
What is 9 added to (3 times 12)?' ''',''''Indeed it is!' ''','''The wizard becomes furious and recites some formulas to calm down
It's clear you can reason no further''',"Errhmm.. not exactly, but an honest mistake","'If x^2 - x - 2 is equal to 0, what is x?'",
"'UGHH, Nevermind..'",
'''Your Response :-
    1. That would be ...45!
    
    2. Ummm....21?
    
    3. You know... Isn't it just witches that use flying
    broomsticks?
    ''',
'''Your Response :-
    1. Let's see... take x as common....., x can be 1 or 2.
    
    2. ..... x is equal to 12..or 7?
    
    3. Solve for x? HOW ABOUT I DON'T?!
    ''',
'''
'How about this one...'
''',"1","3","2"]
pickle.dump(D,file)
D.clear()


D["DKnight"]=["Knight","'Ah..A worthy sparring partner! Sure, let us converse!'","'When attacking an enemy, what is your primary objective?'",
"'Ah, you are indeed a fine warrior!'","'Escape?! Escape is a coward's way!'","'I appreciate your aggressive spirit, but such an approach is inneffective'",
"'Even before your first attack, what should you consider?'","'Incorrect!'",
"'UGHH, Nevermind..'",
'''Your Response :-
    1. I would try to knock the enemy down, for a special attack
    
    2. ..Try to escape?
    
    3. I would thrust my blade with vigour!
    ''',
'''Your Response :-
    1. If I can reason with the enemy?
    
    2. Nothing. I just attack!
    
    3. If I have enough health?
    ''',
'''
'One more question...'
''',"1","2","3"]

pickle.dump(D,file)
D.clear()


file.close()
def get_dlg():
    file=open("reason.dat","rb")
    LR=[]
    try:
        while True:
            L=pickle.load(file)
            for k,v in L.items():
                LR+=v,
    except EOFError:
            pass
    file.close()
    return LR


LR=get_dlg()
L=LR[0]
L2=LR[1]
KW=LR[2]
MW=LR[3]
DK=LR[4]
LR=L



def reason(LR):
    
    anger=False
    if LR[0]=="Both":
        print(LR[1])
        print()
        input('''(Press enter to continue)
 ''')
        print(LR[2])
        print()
        input('''(Press enter to continue)
 ''')
        print(LR[-6])
        
        while True:
            op=input("Enter your choice :- ")
            if op==LR[-3]:
                print(LR[3])
                break
            elif op==LR[-2]:
                anger=True
                print(LR[4])
                break
            elif op==LR[-1]:
                print(LR[5])
                print(LR[-4])
                print(LR[6])

                print()
                print(LR[-5])
                input('''(Press enter to continue)
 ''')
                opn=input("Enter your choice :- ")
                while True:
                    if opn==LR[-3]:
                        print(LR[3])
                        anger=False
                        break
                    elif opn==LR[-2] or opn==LR[-1]:
                        print(LR[7])
                        anger=True
                        break
                    else:
                        print("Invalid input, Try again")
                        continue
                break    
            else:
                print("Invalid input, Try again")
                continue

    elif char!=LR[0]:
            print("The enemy will only reason with")
            print("a",LR[0])
            anger=True
    else:
        print(LR[1])
        print()
        print(LR[2])
        print()
        print(LR[-6])
        
        while True:
            op=input("Enter your choice :- ")
            if op==LR[-3]:
                print(LR[3])
                break
            elif op==LR[-2]:
                anger=True
                print(LR[4])
                break
            elif op==LR[-1]:
                print(LR[5])
                print(LR[-4])
                print(LR[6])
                print()
                print(LR[-5])
                opn=input("Enter your choice :- ")
                while True:
                    if opn==LR[-3]:
                        print(LR[3])
                        anger=False
                        break
                    elif opn==LR[-2] or opn==LR[-1]:
                        print(LR[7])
                        anger=True
                        break
                    else:
                        print("Invalid input, Try again")
                        continue
                break    
            else:
                print("Invalid input, Try again")
                continue
    return anger




def eattack(L):
    attp=random.randrange(1,5)
    if L[-3]=="strong":
        if attp==1 or attp==3 or attp==4:
            atk=L[8]
            atd=L[-4]
        else:
            atk=L[7]
            atd=L[-5]
    else:
        if attp==1 or attp==3 or attp==4:
            atk=L[7]
            atd=L[-5]
        else:
            atk=L[8]
            atd=L[-4]
    return [atk,atd]

di,hi=0,0

def retry():
    while True:
        retry=input('''
    Would you like to try again? (y or n) :- ''')
        if retry.lower()=="y":
            retrc=True
            break
        elif retry.lower()=="n":
            retrc=False
            break
        else:
            print("Invalid choice, enter again")
            continue
    if retrc==True:
        return retrc
    else:
        return retrc

def game_over(hp,ohp):
    
    r=False
    if hp!=0:
        return "not dead"
    if hp==0:
        print("YOU HAVE DIED")
        r=retry()
    if r==True:
        return True
    else:
        return False
    

    
def enemy(L,LR):
    print(L[0].center(20," "))
    global hp,ohp,mor,si
    escape=False
    Reasoned=False
    print()
    global ehp
    global di
    global hi
    ehp=L[1]
    ma=0
    si=0
    if char=="Wizard":
        while ehp>0 and hp>0:
            print()
            print("(A) - Attack")
            print("(B) - Attempt to reason")
            print("(C) - Attempt to flee")
            
            dmg=0
            while True:
                miss=random.randrange(0,15)
                emiss=random.randrange(0,10)
                print()
                print("ENEMY HEALTH :- ",ehp,"/",L[1])
                print("PLAYER HEALTH :- ",hp,"/",ohp)
                print()
                op=input("Enter choice :- ")
                print()
                if op.lower()=="a":
                    atk=magic()
                    wk=False
                    if atk==L[2].lower():
                        wk=True
                        dmg=43+di
                    elif atk!="staff bash":
                        dmg=23+di
                    else:
                        dmg=10+di
                    if miss!=4:
                        ehp-=dmg
                        print("You have successfully attacked the enemy")
                        si+=5
                        if ehp<=0:
                            ehp=0
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                            si+=5
                            print("Enemy Vanquished")
                            break
                        else:
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                        
                        
                        if wk==True:
                            print()
                            si+=10
                            print("You have even discovered its weakness,",L[2])
                            print("You now have the opportunity for a special attack")
                            
                            while True:
                                fin=input("Would you like to perform it (y or n) :- ")
                                if fin.lower()=="y":
                                    si+=10
                                    dmg2=100
                                    if dmg2>ehp:
                                        ehp=0
                                        break
                                    else:
                                        ehp-=dmg2
                                    break
                                elif fin.lower()=="n":
                                    break
                                else:
                                    print("Invalid choice, enter again")
                                    continue
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                            print("PLAYER HEALTH :- ",hp,"/",ohp)
                        
                        if ehp==0:
                            print("ENEMY VANQUISHED!!")

                            print('''
You feel stronger after overcoming such a powerful foe.
You have even regained some of your health.''')
                            di+=L[-1]
                            hi+=L[-2]
                            ohp+=10+hi
                            if ohp-hp<30:
                                hp=ohp
                            else:
                                hp+=30    
                            
                            break
                    else:
                        print("Unfortunately, your attack didn't land")
                        si-=5
                    if emiss!=4:
                        E=eattack(L)
                        print(E[1])
                        eatk=E[0]
                        if eatk>hp:
                            hp=0
                        else:
                            hp-=eatk
                        if hp==0:
                            print("The Enemy Defeated You")
                            break
                    else:
                        print("Fortunately, the enemy's attack missed")
                        si+=5

                elif op.lower()=="b":
                    if ma<1:
                        ma+=1
                    if L[3]=="Unreasonable" or L[3]=="RKnight":
                        print(L[5])
                        print("You can't reason with this enemy.")
                    elif L[3]=="RWiz":
                        if reason(LR)==False:
                            Reasoned=True
                            ma+=2
                        else:
                            Reasoned=False



                    elif L[3]=="Rmor":
                        if mor<2:
                            print(L[5])
                        else:
                            if reason(LR)==False:
                                Reasoned=True
                                ma+=2
                            else:
                                Reasoned=False


                    else:
                        if reason(LR)==False:
                            Reasoned=True
                            ma+=2
                        else:
                            Reasoned=False

                    
                    break
                elif op.lower()=="c":
                    if random.randrange(1,6)!=4:
                        print(L[6])
                        print("You are unable to escape")
                    else:
                        escape=True
                    break
                else:
                    print("Invalid choice, enter again")
                    continue
            if Reasoned==True:
                print("You have successfully reasoned with the enemy")
                mor+=ma
                break
            if escape==True:
                mor+=ma
                print("You were able to evade the enemy!")
                break
            if ehp==0:
                mor+=ma
                break
            if hp==0:
                print("Lost")
                break
    else:
        #Character is Knight
        while ehp>0 and hp>0:
            
            dmg=0
            while True:
                print("(A) - Attack")
                print("(B) - Attempt to reason")
                print("(C) - Attempt to flee")
            
                miss=random.randrange(0,15)
                emiss=random.randrange(0,10)
                print()
                print("ENEMY HEALTH :- ",ehp,"/",L[1])
                print("PLAYER HEALTH :- ",hp,"/",ohp)
                print()
                op=input("Enter choice :- ")
                print()
                if op.lower()=="a":
                    atk=sword()
                    wk=False
                    fl=False
                    if atk[1]=="s":
                        sc=random.randrange(1,5)
                        if sc==1 or sc==3 or sc==4:
                            wk=True
                        if atk[0]=="l":
                            dmg=30+di
                        else:
                            dmg=45+di
                    elif atk[1]=="t":
                        sc=random.randrange(1,6)
                        if sc==2:
                            wk=True
                        if atk[0]=="l":
                            dmg=40+di
                        else:
                            dmg=50+di
                    elif atk=="flurry":
                        dmg=55+di
                        if hp>30:
                            hp-=30
                        else:
                            hp-=10
                        fl=True
                    if miss!=4:
                        si+=5
                        ehp-=dmg
                        print("You have successfully attacked the enemy")
                        if ehp<=0:
                            ehp=0
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                            
                        else:
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                        if fl==True:
                            print()
                            si+=15
                            print("The Blade Flurry Attack was exhausting")
                            print("You lost some health")
                        
                        if wk==True:
                            print()
                            si+=10
                            print("You managed to knock the enemy down")
                            print("You now have the opportunity for a special attack")
                            
                            while True:
                                fin=input("Would you like to perform it (y or n) :- ")
                                if fin.lower()=="y":
                                    si+=10
                                    dmg2=100
                                    if dmg2>ehp:
                                        ehp=0
                                        break
                                    else:
                                        ehp-=dmg2
                                    break
                                elif fin.lower()=="n":
                                    break
                                else:
                                    print("Invalid choice, enter again")
                                    continue
                            print("ENEMY HEALTH :- ",ehp,"/",L[1])
                            print("PLAYER HEALTH :- ",hp,"/",ohp)
                        
                        if ehp==0:
                            print("ENEMY VANQUISHED!!")
                            print('''
    You feel stronger after overcoming such a powerful foe.
    You have even regained some of your health.''')
                            di+=L[-1]
                            hi+=L[-2]
                            ohp+=10+hi
                            if ohp-hp<30:
                                hp=ohp
                            else:
                                hp+=45    
                            
                            break
                    else:
                        print("Unfortunately, your attack didn't land")
                        si-=5
                    if emiss!=4:
                        E=eattack(L)
                        print(E[1])
                        eatk=E[0]
                        if eatk>hp:
                            hp=0
                        else:
                            hp-=eatk
                        if hp==0:
                            print("The Enemy Defeated You")
                            break
                    else:
                        print("Fortunately, the enemy's attack missed")
                        si+=5

                elif op.lower()=="b":

                    if ma<1:
                        ma+=1
                    if L[3]=="Unreasonable" or L[3]=="RWizard":
                        print(L[5])
                        print("You can't reason with this enemy.")
                    elif L[3]=="RKnight":
                        if reason(LR)==False:
                            Reasoned=True
                            si+=25
                            ma+=2
                        else:
                            Reasoned=False


                    elif L[3]=="Rmor":
                        if mor<2:
                            print(L[5])
                        else:
                            if reason(LR)==False:
                                Reasoned=True
                                ma+=2
                            else:
                                Reasoned=False


                    else:
                        if reason(LR)==False:
                            Reasoned=True
                            si+=25
                            ma+=2
                        else:
                            Reasoned=False

                    break

                elif op.lower()=="c":
                    if random.randrange(1,6)!=4:
                        print(L[6])
                        print("You are unable to escape")
                    else:
                        escape=True
                else:
                    print("Invalid choice, enter again")
                    continue
            if Reasoned==True:
                print("You have successfully reasoned with the enemy")
                mor==ma
                break
            if escape==True:
                print("You were able to evade the enemy!")
                si+=10
                mor+=ma
                break

            if ehp==0:
                mor+=ma
                break
            if hp==0:
                print("The Enemy Defeated You!")
                break
            input('''(Press enter to continue)
    ''')
        
while hp!=0:
    
    global score
    score=0    
    pdetails()
    ncheck=input("Is this acceptable? (y or n) :- ")
    while ncheck!="y":
        pdetails()
        ncheck=input("Is this acceptable? (y or n) :- ")
    input('''(Press enter to continue)
 ''')
    print('''
You get up and begin to get your bearings.
The darkness fully lifts to finally reveal 
that you are in....''')
    input('''(Press enter to continue)
 ''')
    print('''....your own school.

But something's off. No-one is there
    ''' )
    if char=="Knight":
        weapon="Sword"
    else:
        weapon="Magic Staff"
    print("You glance down at your right hand, and to your")
    print("surprise, you see that you are holding a",weapon+".")
    print("It feels oddly familiar in your hands")
    print()
    input('''(Press enter to continue)
 ''')
    print('''But before you can try to figure out what's going on,
A shadowy figure appears...
It's a Werewolf! With dark fur and long sharp claws.

It growls as it approaches you, but the light from a nearby
lamppost burns its skin, so it steps back
It's unlikely that you can escape it.

So you approach it.''')
    input('''(Press enter to continue)
        ''')


    enemy(Werewolf,[])
    print("MOR","=",mor)
    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    print()
    input('''(Press enter to continue)
    ''')
    score+=si
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass
    
    print('''
Another one appears!!
    ''')
    input('''(Press enter to continue)
    ''')
    enemy(Werewolf2,[])
    score+=si
    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass

    print("MOR","=",mor)
    print('''
A third, larger one appears!!
    ''')
    input('''(Press enter to continue)
    ''')
    enemy(LWerewolf,KW)
    score+=si
    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass
    print("MORALITY POINTS","=",mor)
    print('''
It seems that was the last of them''')
    input('''(Press enter to continue)
    ''')
    print('''You look around at your deserted school.
It's the same place but the lack of anyone
there makes it feel like a nightmare.
You try to remember how you got here, but
nothing comes to mind.''')
    print()
    input('''(Press enter to continue)
 ''')
    
    print('''So you decide to explore the area
''')
    input('''(Press enter to continue)
    ''')
    while True:
        op=input('''Two paths await you :- 
        1. To the Courtyard
        2. To the entrance of the
        first building of classrooms.
        
        Which do you take? :-''')
        if op=="1":
            print('''You walk towards the courtyard.
It seems as deserted as everywhere else...

But suddenly a huge Red Dragon swoops into the
courtyard!!
It has dangerous, fiery breath and long, sharp, claws.''')
            input('''(Press enter to continue)
 ''')
            enemy(FireDragon,LR)
            score+=si
            #print(mor)
            break
        elif op=="2":
            print('''You walk towards the first
school building.
There is an odd puddle of water, just outside the entrance.

But slowly, the puddle freezes, and out of it emerges
a Monster of ice!

It's covered in sharp icicles and has a chilling breath..
But it's face has an almost sad and thoughtful expression
unlike the werewolves you just fought''')
            input('''(Press enter to continue)
 ''')
            enemy(IceMonster,L2)
            score+=si
            #print(mor)
            break
        else:
            print("Invalid input, Try again")
            print()
            continue

    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass
    input('''(Press enter to continue)
 ''')
 


    print("MORALITY POINTS","=",mor)
    print('''You make your way towards the final hallway 
of the school, just before the exit, or at least, 
what you think is the exit.
''')
    input('''(Press enter to continue)
 ''')
    print('''But before you enter, an enemy appears,
A Knight Clothed in Darkness!!''')
    input('''(Press enter to continue)
    ''')
    enemy(DKnight,DK)

    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass

#HALFWAY POINT

    while True:
        ex=input('''You are at the halfway point
of the game, would you like to exit? (y or n) :- ''')
        ext=False
        if ex.lower()=="y":
            progress="Half Game"
            ext=True
            break
        elif ex.lower()=="n":
            ext=False
            break
        else:
            print("Invalid Input, Try again")
            continue

    if ext==True:
        print("Exiting the game")
        fl2=open("lbrd.dat","wb")
        PD={}
        PD[name]=[char,score,progress]
        pickle.dump(PD,fl2)
        PD.clear()
        fl2.close()
        break



    print("MORALITY POINTS","=",mor)
    input('''You, finally, enter the hallway

    (Press enter to continue)
    ''')

    print('''You see two rooms in the hallway.''')
    while True:
        r=input('''You decide to check them out

    1. The First Room
    2. The Second Room

Which do you go to first? :- ''')
        if r=="1":
            metal()

            while True:
                op=input("Do you check the other room? ('y' or 'n') :- ")
                if op.lower()=="y":

                    if code()==True:
                        if hp+50<ohp:
                            print('''The chest contains some food!

        As you eat it, you regain some health
        ''')
                            input('''(Press enter to continue)
        ''')
                            hp+=60
                            print("PLAYER HEALTH :- ",hp,"/",ohp)
                        else:
                            print('''The chest contains a blue orb, 

        It jumps out of the chest and gets absorbed by your '''+weapon+"!!")
                            input('''(Press enter to continue)
        ''')
                            di+=20
                            print("It appears that it has gained power!")
                        print("You decide to leave the room.")
                    else:
                        print('''You decide to abandon that room.
        ''')

                    break
                elif op.lower()=="n":
                    print('''You decide to move on..
''')

            break
        elif r=="2":
            if code()==True:
                if hp+50<ohp:
                    print('''The chest contains some food!

As you eat it, you regain some health
''')
                    input('''(Press enter to continue)
 ''')
                    hp+=60
                    print("PLAYER HEALTH :- ",hp,"/",ohp)
                else:
                    print('''The chest contains a blue orb, 

It jumps out of the chest and gets absorbed by your '''+weapon+"!!\n")
                    input('''(Press enter to continue)
 ''')
                    di+=20
                    print("It appears that it has gained power!")
                print("You decide to leave the room.")
            else:
                print('''You decide to abandon that room.
''')
            while True:
                op=input("Do you check the other room? ('y' or 'n') :- ")
                if op.lower()=="y":
                    metal()
                    break
                elif op.lower()=="n":
                    print('''You decide to move on..
''')
                    break
            break
        else:
            print("Invalid Input, try again")
            continue

    print("MORALITY POINTS","=",mor)

    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass
    input('''(Press enter to continue)
 ''')

    print('''The exit is in sight, but before you get there
an enemy, materializes out of thin air...
''')
    print('''It's a Wizard!! It floats midair upon a 
magical broomstick..''')
    input('''(Press enter to continue)
 ''')
    print(''''I am the WIZARD of MATH! And I am here to DIVIDE
you out of existence!!'

''')
    enemy(MWiz,MW)
    print('''You make your way through to the school exit,
whose gate, as you now realize, is shut...

but an ominous room catches your eye..
''')
    input('''(Press enter to continue)
 ''')


    print('''Its door has a plaque, but the letters are worn
out and you can only make out

        'T#E P##N#####'# O##I##'.

''')
    input('''(Press enter to continue)
 ''')
    print('''
Seeing that there's nowhere else to proceed, you
decide to enter it.
''')
    input('''(Press enter to continue)
 ''')
    print('''As you enter, the room suddenly
expands, almost to the size of a stadium.
In it is one gigantic being.
    
It wears a crown and is clothed in Golden 
Armour, and it sits on a throne, a sceptre
is in it's hand.
''')
    input('''(Press enter to continue)
 ''')
    print('''It speaks to you, in a loud
booming voice.
'Ah, so YOU are the trespasser that my
subjects have told me about. I am the 
king of this kingdom, and it's time
you face the consequences!'
    
The King steps down from his throne
and charges up his magic sceptre
''')
    input('''(Press enter to continue)
 ''')
    print("MORALITY POINTS","=",mor)
    if mor>7:
        score+=40
        print('''The King raises his sceptre
to strike you!
But just before the hit lands, he
is shot down by a barrage of arrows!

'The King is Down! CHAAAARGE!!!!'
''')
        input('''(Press enter to continue)
 ''')

        print('''An army of soldiers charge at the knocked down
King. They Defeat him and hoist a flag in victory.

One of them, who appears to be their leader approaches you.

'Warrior, we have been watching you, and the way, you've been
dealing with the creatures of this land. We have noticed that
you tried to resolve things peacefully, as much as you could.'
''')
        input('''(Press enter to continue)
 ''')
        print(''''We had planned before to deal with the kingafter the king would 
defeat you, but your actions greatly impressed us, so we decided 
to save you.'
''')
        input('''(Press enter to continue)
 ''')
        print('''
'Thank you for showing kindness to our people
while we were opressed by this horrible king.
Now, I believe it's time for you to leave this place.
We wish you good luck for your future endeavours!'
''')
    else:
        enemy(King,[])
        score+=si
    
    if hp>ohp:
        hp=ohp
    print("PLAYER HEALTH :- ",hp,"/",ohp)
    go=game_over(hp,ohp)
    if go==True:
        hp=100
        continue
    elif go==False:
        break
    else:
        pass
    score+=mor*5
    print('''All of a sudden, that familiar darkness
returns..
Your eyelids feel heavy, and you go to sleep.''')
    input('''(Press enter to continue)
 ''')
    print('''You wake up in your bed at home. It was
all just a dream. You glance at your alarm clock and
realize, to your surprise, that you are late for school.
So you get up and move on with your day.
''')
    print("You don't even notice that under your bed is")
    print("a",weapon,"glowing with power...")
    print()
    print("SCORE =",score)
    progress="Full Game"
    fl3=open("lbrd.dat","wb")
    PD={}
    PD[name]=[char,score,progress]
    pickle.dump(PD,fl3)
    PD.clear()
    fl3.close()
    break

fl=open("lbrd.dat","rb")
D=pickle.load(fl)
for k,v in D.items():
    print(k,"Character :-",v[0],"Score :-",v[1],"Progress :-",v[2])
fl.close()

print('''
By Ben Mathew
QA Tester - Gautam

ASCII Art - https://ascii.co.uk/art/wizard
            https://ascii.co.uk/art/knights''')