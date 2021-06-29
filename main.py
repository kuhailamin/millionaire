QUESTIONS=["What is the capital of the UAE?","What is the boiling temperature of water?"]
OPTIONS=[["Abu Dhabi","Dubai","Sharjah","RAK"],["60","85","100","70"]]
ANSWERS=[0,2]
Q1_AMOUNT=100
Q2_AMOUNT=200
Q3_AMOUNT=300
Q4_AMOUNT=500
Q5_AMOUNT=1000
Q6_AMOUNT=Q5_AMOUNT*2 #2000
Q7_AMOUNT=Q6_AMOUNT*2 #4000
Q8_AMOUNT=Q7_AMOUNT*2 #8000
Q9_AMOUNT=Q8_AMOUNT*2 #16000
Q10_AMOUNT=Q9_AMOUNT*2 #32000
Q11_AMOUNT=Q10_AMOUNT*2 #64000
Q12_AMOUNT=125000
Q13_AMOUNT=Q12_AMOUNT*2 #250000
Q14_AMOUNT=Q13_AMOUNT*2 #500000
Q15_AMOUNT=Q14_AMOUNT*2
AMOUNTS=[Q1_AMOUNT,Q2_AMOUNT,Q3_AMOUNT,Q4_AMOUNT,Q5_AMOUNT,Q6_AMOUNT,Q7_AMOUNT,Q8_AMOUNT,Q9_AMOUNT,Q10_AMOUNT,Q11_AMOUNT,Q12_AMOUNT,Q13_AMOUNT,Q14_AMOUNT,Q15_AMOUNT]


print("I'm George Gherdahi. Welcome to Who Wants to Be a Millionare.")
name=input("Introduce yourself to the audience")
print("Welcome "+name+" to the show! We are excited to have you!")
answer=input("So, tell us. What will you do if you win the million dirhams? 1: Invest it, 2: Buy one million meals and feed the hungry, 3: Travel the world, 4: Buy a fancy car, 5: Save it in the bank")
if answer=="1":
    print("Wow! smart idea! Good luck")
elif answer=="2":
    print("You are a rare gem! Very generous! We need people like you! God bless you")
elif answer=="3":
    print("Nice! But, do you need 1M Drhs for that? Interesting")
elif answer=="4":
    print("I'm sure you will enjoy it, but really 1 Mh Drhs for a car? Why? You can rent it for a month for much less money")
elif answer=="5":
    print('You should reconsider! Because money loses value as time passes by. Besides, money is either digits in the bank or a piece of paper')

for index in range(len(QUESTIONS)):
    Q=QUESTIONS[index]
    print(Q)
    Options=OPTIONS[index]
    print("Option 1:",Options[0])
    print("Option 2:", Options[1])
    print("Option 3:", Options[2])
    print("Option 3:", Options[3])
    answer=int(input("What is the answer? 1-4"))
    answer=answer-1
    if answer==ANSWERS[index]:
        print("Well done! You got ",AMOUNTS[index])
    else:
        print("Sorry. You lost")
        break

