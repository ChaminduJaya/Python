def initialize_game():
    global total,wickets,overs,ball,player_A,player_B,batsman, player_A_run, player_B_run, player_A_star, player_B_star
    total=0
    wickets =0
    overs=0
    ball=0
    player_A = 'Hasaranga'
    player_B = 'Shehan'
    batsman = player_A
    player_A_run =0
    player_B_run = 0
    player_A_star = '*'
    player_B_star = ' '

def over():
    global overs
    while game_over():
        ball_in_over()
        overs += 1

def ball_in_over():
    global ball
    ball=0
    while game_over() and ball<6:
        print_score()
        ball +=1
        runs()

def runs():
    global total,wickets
    run=input('runs =')
    if run.isdigit() :
        run= int(run)
        if (0 <= run < 7)  and (run !=5) :
            total += run
            batsman_run(run)
            if run ==3 or run ==1:
                player_change()

        else :
            print ('Invalid Input')
    else:
        if run.lower() == 'w':
            wickets +=1
            if wickets ==5:
                return
            player_change_wickets()



def player_change():
    global batsman,player_B,player_A,player_A_star,player_B_star
    if batsman== player_A :
        batsman = player_B
        player_B_star = '*'
        player_A_star = ' '
    else :
        batsman = player_A
        player_A_star = '*'
        player_B_star = ' '
def batsman_run(run):
    global batsman, player_B, player_A,player_A_run,player_B_run,player_A_star,player_B_star
    if batsman == player_A:
        player_A_run += run
        player_A_star = '*'
        player_B_star = ' '
    else:
        player_B_run += run
        player_B_star = '*'
        player_A_star = ' '

def player_change_wickets():
     global batsman, player_B, player_A,player_A_run,player_B_run

     if batsman == player_A:
         print (f'{player_A} run is {player_A_run}')
         player_A = input('New Batsman:')
         batsman = player_A
         player_A_run =0
     else:
         print(f'{player_B} run is {player_B_run}')
         player_B = input('New Batsman:')
         batsman = player_B
         player_B_run =0

def print_score():
    global overs,ball,total,wickets,player_A,player_B,player_A_run,player_B_run,player_A_star,player_B_star
    print(f'{total}/{wickets}', end='  ')
    print(f'overs {overs}.{ball}',end='  ')
    print(f'{player_A} : {player_A_run}{player_A_star}  {player_B} : {player_B_run}{player_B_star}')

def game_over():
    global wickets,overs,ball
    return wickets == 5 or (overs ==4 and ball==7 )

def main():
    initialize_game()
    over()

if __name__ == "__main__":
    main()