n = int(input("Tell length of your stars\n"))
b = bool(int(input("Write 0 for high to low STARS, OR 1 for low to high STARS\n")))
e = 1
def function1(d):
    while d > 0:
        print(" * ", end="")
        d -= 1
    print()
while n > 0 and b == False:
    function1(n)
    n -= 1
while e <= n and b == True:
    function1(e)
    e += 1
print("Thanks to come here, GOD BLESS ALL YOUR STARS")



