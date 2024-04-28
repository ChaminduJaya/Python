def start_game():
    global total_runs 
    total_runs=0
    global wickets 
    wickets = 0
    global ball
    ball=0
    global over
    over=0
def overs_in_match():
    global over
    while over<5 :
        balls_in_over() 
        if wickets == 4:
            break
        over+=1
    
    
def balls_in_over():
    global ball  
    ball=0
    while ball<6 and wickets <4 :
        print_score()
        ball +=1
        score_off_balls()
       
        

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
        if wickets == 4:
            game_over()
    else :
        print('invalid')

def print_score():
    print(f'{total_runs}/{wickets}  overs :{over}.{ball}')

def game_over():
    print_score()
start_game()
overs_in_match()