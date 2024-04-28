
class CricketGame():

    def __init__(self):

        self.total=0
        self.wickets =0
        self.overs=0
        self.ball=0


        self.player_A_run =0
        self.player_B_run = 0
        self.player_A_ball = 0
        self.player_B_ball = 0
        self.player_A_star = '*'
        self.player_B_star = ' '
        self.player_details = []
        for i in range(5):
            self.player_details.append({'name':'','runs': 0, 'balls': 0, "4's": 0, "6's":0})
            self.player_details[i]['name'] = input(f'player {i+1} :')
        self.player_A = self.player_details[0]['name']
        self.player_B = self.player_details[1]['name']
        self.batsman = self.player_A
        self.player_no = 2
        self.player_a_no =0
        self.player_b_no =1
    def over(self):

        while not self.game_over():
            self.bowler = input('Bowler name: ')
            self.ball_in_over()
            self.overs += 1

    def ball_in_over(self):
        self.ball=0
        if self.over != 0:
            self.player_change()
        while not self.game_over() and self.ball<6:
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
        if self.batsman== self.player_A :
            self.batsman = self.player_B
            self.player_B_star = '*'
            self.player_A_star = ' '
        else :
            self.batsman = self.player_A
            self.player_A_star = '*'
            self.player_B_star = ' '
    def batsman_run(self,run):

        if self.batsman == self.player_A:
            self.player_details[self.player_a_no]['runs'] += run
            self.player_details[self.player_a_no]['balls'] += 1
            self.player_A_star = '*'
            self.player_B_star = ' '


        else:
            self.player_details[self.player_b_no]['runs'] += run
            self.player_details[self.player_b_no]['balls'] += 1
            self.player_B_star = '*'
            self.player_A_star = ' '

    def player_change_wickets(self):
        if self.wickets < 5:
             if self.batsman == self.player_A:
                print(self.player_details[self.player_a_no])
                self.player_A = self.player_details[self.player_no]['name']
                self.batsman = self.player_A
                self.player_A_run =0
                self.player_A_ball = 0
                self.player_a_no = self.player_no

             else:
                print(self.player_details[self.player_b_no])
                self.player_B = self.player_details[self.player_no]['name']
                self.batsman = self.player_B
                self.player_B_run =0
                self.player_B_ball = 0
                self.player_b_no = self.player_no
             print (f'{self.batsman} is a new batsman!')
        self.player_no +=1
    def print_score(self):

        print(f'{self.total}/{self.wickets}', end='  ')
        print(f'overs {self.overs}.{self.ball}',end='  ')
        print(f'{self.player_A} : {self.player_A_run}{self.player_A_star}  {self.player_B} : {self.player_B_run}{self.player_B_star}')


    def game_over(self):
        return self.wickets == 5 or (self.overs ==4 and self.ball==7 )

def main():
    first_batting = CricketGame()
    first_batting.over()

if __name__ == "__main__":
    main()