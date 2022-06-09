
from question import Question


q1 = Question("What is the capital of Illinois?\n(a)Springfield \n(b)Chicago \n(c)Romeoville \n(d)Champagne \n", "B")
q2 = Question("How many days are in December?\n(a)30 \n(b)28 \n(c)31 \n(d)29 \n", "C")
q3 = Question("How many months are in the first quarter of the year?\n(a)8 \n(b)2 \n(c)4 \n(d)5 \n", "C")
q4 = Question("Who invented the light bulb? \n(a)Benjamin Franklin\n(b)Issac Newton \n(c)George Washington \n(d)Thomas Edison \n", "D")
q5 = Question("Finish the quote: \"What goes up must come ____:\" \n(a)Around \n(b)Down \n(c)Directly Below \n(d)Full Swing \n", "B")

lives = 3

correct = 0

questionArray = [q1, q2, q3, q4, q5]


while lives > 0:

    for i in questionArray:
        
        if lives == 0:
            break
            
        else:
            quest = i.prompt
            answer = i.answer

            print(quest)
            
            guess = input('Your answer choice? ')
            
            if guess.upper() == answer:
                correct += 1
                print('Correct!')

            else:
                lives -= 1
                
                if lives > 1:
                    print('Wrong answer given. ' + str(lives) + ' lives remaining.')
                    
                elif lives == 1:
                    print('Wrong answer given. ' + str(lives) + ' life remaining.')
                    
                else:
                    print('Wrong answer! Out of lives!')


print('Game Over! Amount Correct: ' + str(correct) + '. Try to beat your score!')
