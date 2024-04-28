def start_game():
    global total_runs 
    total_runs=0
    global wickets 
    wickets = 0
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
        print(f'{total_runs}/{wickets}  overs :{over}.{ball}')
        score_off_balls()
        
        ball +=1

def score_off_balls ():
    global total_runs
    global wickets
    score = input('Score :')
    if score.isdigit() :        #validation
        score = int(score)
        #if 0 <= score <5 or score ==6:
        if score in (0,1,2,3,4,6):
            runs = score 
            total_runs += runs
    elif score.lower() == 'w':
        wickets+=1
    else :
        print('invalid')

def print_score():
    pass

start_game()
overs_in_match()