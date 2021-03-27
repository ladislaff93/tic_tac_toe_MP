#print the board for game here as list
board = [' ' for x in range(10)]

#Function that asks player to choose the character with he want to play
def character():
    while True:
        chs = int(input('What letter would you like to choose? (1-X, 2-O):\n'))
        if chs in (1,2):
            if chs == 1:
                return 'X'
            elif chs== 2:
                return 'O'
        else:
            print('Try Again Wrong Choice!')

#If player choose the X give the computer O and vice versa
def character2(letter):
  if letter=='X':
      return 'O'
  else:
      return 'X' 

#function that will insert the letter player choose onto position on board  
def insertletter(letter, pos):
  board[pos]=letter

#check if the position that player choose is free
def spaceisfree(pos):
    return board[pos]==' '

#function is going to check if there is winner. Mean. If there are three rows with the same letter
def iswinner(board,letter):
  return letter == board[1] and letter in board[2] and letter in board[3] or letter in board[4] and letter in board[5] and letter in board[6] or letter in board[7] and letter in board[8] and letter in board[9] or letter in board[1] and letter in board[5] and letter in board[9] or letter in board[3] and letter in board[5] and letter in board[7] or letter in board[1] and letter in board[4] and letter in board[7] or letter in board[2] and letter in board[5] and letter in board[8] or letter in board[3] and letter in board[6] and letter in board[9]

#funtion that check if the board is full and return either True or False
def isboardfull(board):
  if board.count(' ') > 1:
    return False
  else:
    return True

#just print the board
def printboard(board):
  print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
  print('-------')
  print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
  print('-------')
  print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')

#function for player move
def playermove(board, letter):
  run = True
  while run:
    pos = int(input('Your letter is {}. Choose a move from 1-9!'.format(letter)))
    try:
      if pos < 10 and pos > 0:
        if spaceisfree(pos):
          run = False
          insertletter(letter, pos)
        else:
          print('Position occupied!')
      else:
        print('Invalid number.')
    except:
      print('Type Number')

def selectRandom(moves):
  import random 
  ln = len(moves)
  r = random.randrange(0,ln)
  return moves[r]


def computermove(board, letter2, letter):
  possiblemoves=[x for x, letter in enumerate(board) if x!=0 and letter==' ']
  move = False 


  for letters in [letter2, letter]:
    for i in possiblemoves:
      boardcopy= board[:]
      boardcopy[i]=letters
      if iswinner(board, letters):
         move = i
         return move


  cornersopen = []
  for i in possiblemoves:
    if i in [1,3,7,9]:
      cornersopen.append(i)
  if len(cornersopen)>0:
    move = selectRandom(cornersopen)
    return move
  if 5 in possiblemoves:
    move = 5
    return 5


  edgesopen=[]
  for i in possiblemoves:
    if i in [2,4,6,8]:
      edgesopen.append(i)
  if len(edgesopen)>0:
    move = selectRandom(edgesopen)
    return move

def choosegame():
    inp=int(input('Choose the type of game?\n 1.Singleplayer \n 2.Multiplayer: \n '))
    if inp == 1:
        return True
    else:
        return False

#function where the game 'run'
def main():
  #print out the welcome message
  print('Welcome in Tic Tac Toe!')

  #print out the dialog message for choosing the letter for a player
  #this part is going to inform player what letter he choose and give him the move options
  letter = character()
  letter2 = character2(letter)
  game = choosegame()
  #print out the board
  printboard(board)


  #until the board is full we are going to execute the game and if board is full return tie game message
  
  while True:
    #first player go 
    if not (iswinner(board, letter2)):
      if not isboardfull(board):
        playermove(board, letter)
        printboard(board)
      else:
        print('It\'s a tie game!')
        break
    else:
      print('Sorry {} win!'.format(letter2))
      break
    
    #second player go computer or human     
    if not (iswinner(board, letter)):
        if not isboardfull(board):
            if game == True:
                move = computermove(board, letter2, letter) 
                if move == False:
                    print('It\'s a tie game!')
                    break
                else:
                    insertletter(letter2, move)
                    print('{} place a move on {}'.format(letter2, move))
                    printboard(board)
            else:
                if not (iswinner(board, letter2)):
                    if not isboardfull(board):
                        playermove(board, letter2)
                        printboard(board)
                    else:
                        print('It\'s a tie game!')
                        break
    else:
        print('Sorry {} win!'.format(letter2))
        break  

main()


