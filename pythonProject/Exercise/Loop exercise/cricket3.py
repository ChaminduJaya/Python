
class CricketGame():

    def __init__(self):

        self.total=0
        self.wickets =0
        self.overs=0
        self.ball=0
        self.player_a_run =0
        self.player_b_run = 0
        self.player_a_ball = 0
        self.player_b_ball = 0
        self.player_a_star = '*'
        self.player_b_star = ' '
        self.batsman = ''
        self.player_a = ''
        self.player_b = ''
        self.player={}
        self.bowler={}

    def initialize_game(self):
        for i in range(1,6):
            player_name = input(f'Player {i}: ')

            self.player[player_name]={'runs': 0, 'balls': 0, "4's": 0, "6's": 0}
            #self.player[player_name] ={}
            if i==1:
                self.player_a = player_name
                self.batsman = self.player_a
            elif i==2:
                self.player_b = player_name

    def over(self):

        while  self.game_over():
            bowler_name = input('Bowler name: ')
            if not bowler_name in self.bowler :
                self.bowler[bowler_name] = {'wickets': 0 ,'runs': 0, 'overs': 0, }
                print (self.bowler)
            self.ball_in_over()
            self.overs += 1

    def ball_in_over(self):
        self.ball=0
        if self.overs != 0:
            self.player_change()
        while self.game_over() and self.ball<6:
            self.print_score()
            self.ball +=1
            self.runs()

    def runs(self):

        run=input('runs =')
        if run.isdigit() :
            run= int(run)
            if run in (0,1,2,3,4,6) :
                self.total += run
                self.batsman_run(run)
                if run in (1,3):
                    self.player_change()

            else :
                self.ball -= 1
                print ('Invalid Input')
        else:
            if run.lower() == 'w':
                self.wickets += 1
                self.player_change_wickets()


    def player_change(self):

        if self.batsman== self.player_a :

            self.batsman = self.player_b
            self.player_b_star = '*'
            self.player_a_star = ' '
        else :
            self.batsman = self.player_a
            self.player_a_star = '*'
            self.player_b_star = ' '

    def batsman_run(self,run):

        if self.batsman == self.player_a:
            self.player_a_update(run)

        else:
            self.player_b_update(run)

    def player_change_wickets(self):
        if self.wickets < 4:
             if self.batsman == self.player_a:
                self.player_a_initial_update()

             else:
                 self.player_b_initial_update()
             print (f'{self.batsman} is a new batsman!')

    def player_a_initial_update(self):
        self.player_a=list(self.player.keys())[self.wickets+1]
        #self.player_a_details={'runs': 0, 'balls': 0, "4's": 0, "6's": 0}
        self.player_a_run = 0
        self.player_a_ball= 0
        self.player_a_star = '*'
        self.player_b_star = ' '
        self.batsman= self.player_a

    def player_b_initial_update(self):
        self.player_b = list(self.player.keys())[self.wickets + 1]
        self.player_b_run = 0
        self.player_b_ball =0
        self.player_b_star = '*'
        self.player_a_star = ' '
        self.batsman = self.player_b

    def player_a_update(self,run):
        self.player_a_run += run
        self.player_a_ball += 1
        self.player_a_star = '*'
        self.player_b_star = ' '
    def player_b_update(self,run):
        self.player_b_run += run
        self.player_b_ball += 1
        self.player_b_star = '*'
        self.player_a_star = ' '

    def player_a_final_update(self):
        player_a_details = {'runs': self.player_a_run, 'balls': self.player_a_ball, "4's": 0, "6's": 0}
        self.player[self.player_a] = player_a_details

    def player_b_final_update(self):
        player_b_details = {'runs': self.player_b_run, 'balls': self.player_b_ball, "4's": 0, "6's": 0}
        self.player[self.player_b] = player_b_details
    def print_score(self):

        print(f'{self.total}/{self.wickets}', end='  ')
        print(f'overs {self.overs}.{self.ball}',end='  ')
        print(f'{self.player_a} : {self.player_a_run}{self.player_a_star}  {self.player_b} : {self.player_b_run}{self.player_b_star}')
        print (self.player)

    def game_over(self):
        if self.wickets == 4 or self.overs ==2:
            self.print_score()
            print('Game over!')
            return False
        return True
def main():
    first_batting = CricketGame()
    first_batting.initialize_game()
    first_batting.over()


if __name__ == "__main__":
    main()