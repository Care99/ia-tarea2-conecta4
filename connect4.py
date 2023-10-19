import random;
import math;
class player:
  number=0;
  def __init__(self,player_number):
    self.number = player_number;

class connect:
  width=0;
  height=0;
  ammount=0;
  max_ammount=0;

  def __init__(self):
    self.width = 7;
    self.height = 6;
    self.max_ammount=42;
    self.board = [[0]*self.width for i in range(self.height)];
    self.filled_height = [0 for i in range(self.width)];

  def check_horizontal(self,x,y,player):
    i=y;
    j=x;
    score=0;
    #Check left
    for j in range(x-1,x-4,-1):
        if(j>=0):
          if(self.board[i][j]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    #Check right
    i=y;
    j=x;
    for j in range(x+1,x+4):
        if(j<=6):
          if(self.board[i][j]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    return score;

  def check_vertical(self,x,y,player):
    i=y;
    j=x;
    score=0;
    #Check up
    for i in range(y-1,y-4,-1):
        if(i>=0):
          if(self.board[i][j]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    #Check down
    i=y;
    j=x;
    for i in range(y+1,y+4):
        if(i<=5):
          if(self.board[i][j]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    return score;

  def check_diagonal_1(self,x,y,player):
    i=y;
    j=x;
    iteration=0
    score=0;
    #Check north west
    for iteration in range(1,4):
        if(i-iteration>=0 and j-iteration>=0):
          if(self.board[i-iteration][j-iteration]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    #Check south east
    i=y;
    j=x;
    for iteration in range(1,4):
        if(i+iteration<=5 and j+iteration<=6):
          if(self.board[i+iteration][j+iteration]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    return score;

  def check_diagonal_2(self,x,y,player):
    i=y;
    j=x;
    iteration=0;
    score=0;
    #Check north east
    for iteration in range(1,4):
        if(i-iteration>=0 and j+iteration<=6):
          if(self.board[i-iteration][j+iteration]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    #Check south west
    i=y;
    j=x;
    for iteration in range(1,4):
        if((i+iteration<=5) and (j-iteration>=0)):
          if(self.board[i+iteration][j-iteration]==player.number):
            score = score + 1;
          else:
            break;
        else:
          break;
    return score;

  def is_filled(self,x):
    y = self.filled_height[x];
    filled_condition = 0;
    if( self.filled_height[x] == self.height):
      filled_condition = 1;
    return filled_condition;

  def place_in(self,x,player):
    y = 5-self.filled_height[x];
    if( self.is_filled(x) ):
      return -1;
    self.board[y][x] = player.number;
    self.filled_height[x] = self.filled_height[x] + 1;
    self.ammount=self.ammount+1;
    return y;

  def check_victory(self,x,y,player):
    victory = 0;
    score_horizontal = self.check_horizontal(x,y,player);
    score_vertical = self.check_vertical(x,y,player);
    score_diagonal_1 = self.check_diagonal_1(x,y,player);
    score_diagonal_2 = self.check_diagonal_2(x,y,player);
    if( score_horizontal >= 3 or score_vertical >= 3 or score_diagonal_1 >= 3 or score_diagonal_2 >= 3 ):
      victory = 1;
    return victory;

  def score(self,x,y,player):
    score = 0;
    score_horizontal = self.check_horizontal(x,y,player);
    score_vertical = self.check_vertical(x,y,player);
    score_diagonal_1 = self.check_diagonal_1(x,y,player);
    score_diagonal_2 = self.check_diagonal_2(x,y,player);
    score = score_horizontal + score_vertical + score_diagonal_1 + score_diagonal_2
    return score;
  def print_board(self):
    i=0;
    for i in range(self.height):
      print(self.board[i]);

  # ... (previous code)

  def is_valid_move(self, x):
      return not self.is_filled(x)

  def evaluate(self, player,x):
      y = self.filled_height[x]-1;
      if self.check_victory(x, y, player):
        score = 20  # AI wins
      else:
        score = self.score(x,y,player);
      return score

  def minimax(self, depth, maximizing, alpha, beta, player, x):
      if depth == 0 or self.ammount == self.max_ammount:
          return self.evaluate(player,x)

      if maximizing:
          max_eval = -math.inf
          for x in range(self.width):
              if self.is_valid_move(x):
                  y = self.place_in(x, player)
                  eval = self.minimax(depth - 1, False, alpha, beta, player, x)
                  self.board[y][x] = 0
                  self.filled_height[x] -= 1
                  self.ammount -= 1
                  max_eval = max(max_eval, eval)
                  alpha = max(alpha, eval)
                  if beta <= alpha:
                      break
          return max_eval
      else:
          min_eval = math.inf
          for x in range(self.width):
              if self.is_valid_move(x):
                  y = self.place_in(x, player)
                  eval = self.minimax(depth - 1, True, alpha, beta, player, x)
                  self.board[y][x] = 0
                  self.filled_height[x] -= 1
                  self.ammount -= 1
                  min_eval = min(min_eval, eval)
                  beta = min(beta, eval)
                  if beta <= alpha:
                      break
          return min_eval

  def ai_move(self, player):
      best_eval = -math.inf
      best_move = None
      alpha = -math.inf
      beta = math.inf
      for x in range(self.width):
          if self.is_valid_move(x):
              y = self.place_in(x, player)
              eval = self.minimax(9, True, alpha, beta, player,x)
              self.board[y][x] = 0
              self.filled_height[x] -= 1
              self.ammount -= 1
              if eval > best_eval:
                  best_eval = eval
                  best_move = x
      return best_move
  def ai_move_prune(self, player):
      best_eval = -math.inf
      best_move = None
      alpha = -math.inf
      beta = math.inf
      for x in range(self.width):
          if self.is_valid_move(x):
              y = self.place_in(x, player)
              eval = self.minimax(1, True, alpha, beta, player,x)
              self.board[y][x] = 0
              self.filled_height[x] -= 1
              self.ammount -= 1
              if eval > best_eval:
                  best_eval = eval
                  best_move = x
              alpha = max(alpha, eval)
              if beta <= alpha:
                  break
      return best_move

#Begin main
board = connect();
player1 = player(1);
player2 = player(2);
turn = 0;
x=0;
y=0;

while( board.ammount < board.max_ammount ):
  turn = (turn+1)%2;
  if( turn == 0 ):
    x = board.ai_move(player1)
    y = board.place_in(x,player1);
    print("Turn number: " + str(board.ammount) + "\tx: " + str(x) + "\ty: " + str(y));
    board.print_board();
    if(board.check_victory(x,y,player1)):
      print("Player 1 has won!");
      break;
  else:
    x = board.ai_move_prune(player2);
    y = board.place_in(x,player2);
    print("Turn number: " + str(board.ammount) + "\tx: " + str(x) + "\ty: " + str(y));
    board.print_board();
    if(board.check_victory(x,y,player2)):
      print("Player 2 has won!");
      break;
  print("------------------------------");
