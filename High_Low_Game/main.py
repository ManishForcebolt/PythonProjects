import random
import logo_art
WIN_COUNTER=0


print(logo_art.logo)
n1 = random.randint(1,100)
n2 = random.randint(1,100)
print(f"Computer has selected a number {n1} \n")
print(f"Your number is {n2}")

def highlow(a,b):
    if b <= a:
        return "low"
    else:
        return "high"

#output=highlow(n1, n2)
#print(output)

End_of_Game = False

while not End_of_Game:
    #print(f"n1={n1},n2={n2}")
    output=highlow(n1, n2)
    user_input=input("Enter High or Low\n").lower()
    #print(user_input)
    if (user_input==output):
        WIN_COUNTER+=1
        print(f"Your guess was {user_input} You Win\n")
        #n1=n2
        n1=random.randint(1, 100)
        #print(n2)
    else:
        End_of_Game=True
        print(f"Your guess {user_input} is incorrect. You Loose! \n") 
        print(f"Numbers were {n1} & {n2}")  


print(f"Your win counts are {WIN_COUNTER}")