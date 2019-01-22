import random
yes = input('y')
no = input('n')
print("    You see the man creeping over to you. He motions for you to come a bit closer, and asks 'Do you have it?'")
input('  Do you? (y/n) ')
if yes == 'y':
    b = (random.randint(75, 100))
    print(" 'Ah! Thank you mate! Here, for your troubles.' The man hands you ", b, "in return for the vase.")
    input();
if no == 'n':
    c = (random.randint(100, 120))
    print(" 'Well I gotta make my money somehow! Pay up or I spray up! Give me ", c, " dollars!'");
    input();
