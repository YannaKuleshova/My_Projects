#########################
#Author: Kuleshova Yana
#Date: 23/11/2021
#Task: 5_3
#########################

# Игра в крестики нолики с компьютером

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Enter your move: " + player_token)
      try:
         player_answer = int(player_answer)
      except:
         print("Error. The number must be valid.")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("This cage is already occupied!")
      else:
        print("Error. The number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "won!")
              win = True
              break
        if counter == 9:
            print("A draw!")
            break
    draw_board(board)
main(board)

input("Press Enter to exit!")