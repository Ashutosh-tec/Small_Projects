#This is basic game project on python. This game is similar like the game Stone-paper-scissors.
D = {"S": 1, "W": 2, "G": 3 }
i = 0
c = 0
K = 4000
D2 = {1: "SNAKE", 2: "WATER", 3: "GUN"}
print("WELCOME!! to the GAME\n\n$#$ SNAKE WATER GUN $#$ ")
start = bool(input("\nEnter any key to Start"))
while K != 0:
    try:
        while i < 10:
            import random
            lst = [1, 2, 3]
            A = random.choice(lst)
            n = input("\nPlease Enter\nS for SNAKE\nW for WATER\nG for GUN\n")
            if A == D[n]:
                print("\nYou Clashed!!\n", "Computer Chosen:", D2[A])
                i -= 1
            elif A == 1 and D[n] ==2 or  A == 2 and D[n] ==3 or A == 3 and D[n] ==1:
                print("\nYou LOOSE!!,", "Computer Chosen:", D2[A])
                c -= 1
            elif A == 1 and D[n] ==3 or A == 2 and D[n] == 1 or A == 3 and D[n] ==2:
                print("\nYou WON!!", "Computer Chosen:", D2[A])
                c += 1
            i = i+1
            print("\nLIFE LINE ->", 10-i)
        if c > 0:
            print("\nYou  are  the     W I N N E R !!!!!   :)\nYour Score is", c)
        elif c < 0:
            print("\nG A M E     O V E R")
        else:
            print("\nYou Tied")
        a = bool(int(input("Press 1 to replay AND 0 for EXIT.\n")))
        if a == True:
            i = 0
            c = 0
        elif a == False:
            K = 0
            print("ACHCHHA CHALTA HU, DUAOO ME YAAD RAKHNA.")
    except Exception as e:
        print("Invalid Input")
