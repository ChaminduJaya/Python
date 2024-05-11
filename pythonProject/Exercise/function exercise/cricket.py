class CricketMatch():
    def start_game():
        global total_runs,wickets,ball,over 
        total_runs=0
        wickets = 0
        ball=0
        over=0
    def overs_in_match():
        global over,ball
        while over<2 and wickets <4 :
            balls_in_over() 
            over+=1
        
        else:
        game_over() 
            

        
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
            #if wickets == 4:
                #game_over()
                #print_score()
        else :
            print('invalid')

    def print_score():
        print(f'{total_runs}/{wickets}  overs :{over}.{ball}')

    def game_over():
        global ball,over
        if wickets==4 :
                    if ball==6:
                        ball=0
                    else:
                        over -=1
        elif over==2:
                ball=0
        print_score()
        print ('Game Over!')

class T20 :
     pass

def main():
     firstBat = CricketMatch() #instance (object)
     secondBat = CricketMatch()
    
start_game()

overs_in_match()