class CricketMatch():
    def start_game(self):
        #global total_runs,wickets,ball,over 
        self.total_runs=0
        self.wickets = 0
        self.ball=0
        self.over=0
    def overs_in_match(self):
        #global over,ball
        while self.over<2 and self.wickets <4 :
            self.balls_in_over() 
            self.over+=1
        
        else:
            self.game_over() 
            

        
    def balls_in_over(self):
        #global ball  
        self.ball=0
        while self.ball<6 and self.wickets <4 :
            self.print_score()
            self.ball +=1
            self.score_off_balls()
        
            

    def score_off_balls (self):
        #global total_runs
        #global wickets
        score = input('Score :')
        if score.isdigit() :        #validation
            score = int(score)
            #if 0 <= score <5 or score ==6:
            if score in (0,1,2,3,4,6):
                runs = score 
                self.total_runs += runs
        elif score.lower() == 'w':
            self.wickets+=1
            #if wickets == 4:
                #game_over()
                #print_score()
        else :
            print('invalid')

    def print_score(self):
        print(f'{self.total_runs}/{self.wickets}  overs :{self.over}.{self.ball}')

    def game_over(self):
        #global ball,over
        if self.wickets==4 :
                    if self.ball==6:
                        self.ball=0
                    else:
                        self.over -=1
        elif self.over==2:
                self.ball=0
        self.print_score()
        print ('Game Over!')

class T20 :
     pass

def main():
     firstBat = CricketMatch() #instance (object)
     secondBat = CricketMatch()
     firstBat.start_game()
     firstBat.overs_in_match()
     secondBat.start_game()
     secondBat.overs_in_match()

if __name__ == "__main__":
    main()
