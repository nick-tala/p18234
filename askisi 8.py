import random


#----------------------------------------------------------
# return random integer between 0 and 7
def random_number():
    return random.randint(1, 4)
#----------------------------------------------------------

def play_me():
    x=0
    y=0
    counter=0
    athroisma=0
    while True:
        movement=random_number()

        if movement == 1:
            x=x+1
            
        if movement == 2:
            x=x-1   
        if movement == 3:
            y=y-1
        if movement == 4:
            y=y+1     
        counter = counter+1
        athroisma=athroisma+movement
        
        print('x:', x, 'y:', y)

        if (x==0 and y==0):
            print('rounds:', counter)
            average=athroisma/counter
            print('average:', average)
            break
if __name__ == "__main__":
    play_me()
