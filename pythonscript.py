import random
## Random Number will choose 1 thru 9 then print corresponding answer to screen
random_number = random.randint(1, 9)

name = "Truby"

question = "Is this real life?"


## Core Logic
if random_number < 4:
    pre = "Number is less than 4, the answer is- "
    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
elif random_number < 10:
    pre = "Number is 4 or greater, the answer is- "
    if random_number == 4:
        answer = "Reply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful."
else: answer == "Error."

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + pre + answer)