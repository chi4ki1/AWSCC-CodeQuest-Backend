import time
import sys 

print("◤━━━━━━━━━━━━━━━━━━━━◥")
print("      STORY GAME       ")
print("◤━━━━━━━━━━━━━━━━━━━━◥")
time.sleep(1)

print("A man is asking you for a shelter.")
time.sleep(1)
yes_no = int(input ("Will you let him in?(1 for YES, 0 for NO): "))

if yes_no == 1:
    print("A police officer arrived and showed you a picture of a man you just let in. HE IS A WANTED SUSPECT!")
    time.sleep(1)
    decide = int(input("Would you tell him?(1 for YES, 0 for NO): "))

    if decide == 1:
        print("The police arrested the suspect!")
        time.sleep(1)
        print("YOU WON!🌟")
        sys.exit()
    elif decide == 0:
        print("After the police left, the suspect killed you with a knife.")
        time.sleep(1)
        print("GAME OVER! ☠︎︎")
        sys.exit()
elif yes_no == 0:
    print("He suddenly attacked you!")
    fight = int(input("Will you knock him down? (1 for YES, 0 for NO): "))

    if fight == 1:
        print("You knocked him out, leaving him unconcious. You immediately escaped from him.")
        time.sleep(1)
        print("YOU WON!🌟")
        sys.exit()
    elif fight == 0:
        print("You let him attack you and suddenly slit your throat with a knife")
        time.sleep(1)
        print("GAME OVER! ☠︎︎")
        sys.exit()
else:
    print("ENTER A VALID INPUT! (1 for YES, 0 for NO)")
    sys.exit()