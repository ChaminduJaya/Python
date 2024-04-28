def start_game():
    pass
def overs_in_match():
    
    over =0
    while over<5 :
    
        balls_in_over(over) #passing argument
        over+=1
    else :
        print(f'overs :{over}.0')
    
def balls_in_over(over):
    ball = 0
    while ball<6 :
        print(f'overs :{over}.{ball}')
        ball +=1

   

def print_score():
    pass

overs_in_match()