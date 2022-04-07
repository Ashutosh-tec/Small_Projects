n = 18
b = 9
c = 0
print("Welcome! to the Game of..\nGUESS or DIE.\n##ALERT!! You have", b, "chances only\n","Save yourself and remember if you won there is a joke for you. Just laugh.")
try:
    while b > 0:
        b = b-1

        a = input("Guess The Number\n")
        a = int(a)
        if a > n:
            c = c + 1
            print("Not such high, go down....")
            print("Chances left", b)

            continue

        elif a == n:
            c = c+1
            print("You won!! ")
            print("You have guessed the number in try of", c, "times")
            print("YOU ARE VERY INTELLIGENT.")
            break
        elif a < n:
            c = c + 1
            print("Think high man")
            print("Chances left", b)

            continue
    while b == 0:
        print("Wrong guess limit exceeded.")
        break
except:
    print("Invalid input")
