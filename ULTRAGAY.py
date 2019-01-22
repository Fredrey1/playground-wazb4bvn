import random
def main():
    lines = open('STD.txt').read().splitlines()
    myline = random.choice(lines)
    if myline == ('Homeless attacking farmers 3-5 homeless 2-4 farmers'):
        rhe = (random.randint(2, 6))
        rfe = (random.randint(1, 5))
        print("You see", rhe, "homeless people attacking ", rfe, "farmers");
        if myline != ('Homeless attacking farmers 3-5 homeless 2-4 farmers'):
            print(myline);

            if myline == ('Guy asks for you to hold onto expensive vase (stolen)'):
                 print("A man asks you to hold  onto a rather expensive looking vase. Do you take it?")
                 answer = str(input('  Do you? (y/n) '))
                 if answer == 'y':
                     b = (random.randint(75, 100))
                     print(" 'Alright, thanks, I'll be back, if anyone asks you about that vase, you don't know me, OK?' ")
                     input();
                     a = (random.randint(1, 2))
                     if a == (1):
                         print ("    The police seem to be quite interestind in the vase, and accuse you of stealing it!");
                         if a == (2):
                             print ("    After a while, the man returns, seeking his vase. n/    'Do ya' still have my vase?' n/ Do you?   ")
                             answer = str(input('  Do you? (y/n) '))
                             if answer == 'y':
                                 b = (random.randint(75, 100))
                                 print(" 'Ah! Thank you mate! Here, for your troubles.' The man hands you ", b, "in return for the vase.")
                                 input();
                                 if answer == 'n':
                                    c = (random.randint(100, 120))
                                    print(" 'Well I gotta make my money somehow! Pay up or I spray up! Give me ", c, " dollars!'");
                                    input();
    else: print(myline)
input()
if __name__ == '__main__':
    main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
