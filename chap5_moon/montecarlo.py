import copy
import random
# '-': None, 'O': Player1, 'X': Player2
board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

def is_finished():
  global board
  # return 1: Player 1의 승리, return 2: player 2의 승리, return 0: 계속 플레이
  for i in range(3):
    if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O': return 1
    if board[i][0] == 'O' and board[i][2] == 'O' and board[i][2] == 'O': return 1
    if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X': return 2
    if board[i][0] == 'X' and board[i][2] == 'X' and board[i][2] == 'X': return 2
  
  if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O': return 1
  if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X': return 2
  
  return 0

# need to minimax tree search
class PlayerA:
  global board
  current_state = copy.deepcopy(board)
  is_my_turn = True
  is_searching_finished = True # 재귀함수 구현을 위하여 사용
  searching_result = 0.0
  
  def __init__(self):
    self.current_state = copy.deepcopy(board)
    
  def print_board(self):
    print('----------')
    print(board[0])
    print(board[1])
    print(board[2])
    
  def check_finished(self):
    for i in range(3):
      if self.current_state[0][i] == 'O' and self.current_state[1][i] == 'O' and self.current_state[2][i] == 'O': return 1
      if self.current_state[i][0] == 'O' and self.current_state[i][2] == 'O' and self.current_state[i][2] == 'O': return 1
      if self.current_state[0][i] == 'X' and self.current_state[1][i] == 'X' and self.current_state[2][i] == 'X': return 2
      if self.current_state[i][0] == 'X' and self.current_state[i][2] == 'X' and self.current_state[i][2] == 'X': return 2
  
    if self.current_state[0][0] == 'O' and self.current_state[1][1] == 'O' and self.current_state[2][2] == 'O': return 1
    if self.current_state[0][0] == 'X' and self.current_state[1][1] == 'X' and self.current_state[2][2] == 'X': return 2
    
    cnt = 0
    for i in range(3):
      for j in range(3):
        if self.current_state[i][j] == '-':
          cnt += 1
    if cnt == 0: return -1 # draw
    return 0
  
  def calculate_score(self):
    self.current_state = copy.deepcopy(board)
    self.is_searching_finished = False
    # Searching Start
    if self.is_searching_finished == True:
      return self.searching_result
    
    if is_finished() == 1:
      self.is_searching_finished = True
      self.searching_result = 1
      return 1 # 승리 확률: 1
    
    if is_finished() == 2:
      self.searching_result = 0
      return 0 # 승리 확률: 0
    
    if is_finished() == -1:
      self.searching_result = 0.5
      return 0.5 # 승리 확률: 0
    
    score = 0.0
    for n in range(100):
      self.current_state = copy.deepcopy(board)
      self.is_searching_finished = False
      # 몬테카를로 방법 사용. 100번 랜덤 추출
      #print(n,'th Turn')
      while True:
        # print
        # print('########################')
        # print(self.current_state[0])
        # print(self.current_state[1])
        # print(self.current_state[2])
        
        # 끝났으면, 점수 얻고 다음 추출 실행
        if self.check_finished() == 1:
          score += 1.0
          break
        if self.check_finished() == 2:
          score += 0.0
          break
        
        if self.check_finished() == -1:
          score += 0.5
          break
        
        if self.is_my_turn == True:
          while True:
            x = random.randrange(3)
            y = random.randrange(3)
            if self.current_state[x][y] == '-':
              self.current_state[x][y] = 'O'
              self.is_my_turn = False
              break
            
        elif self.is_my_turn == False:
          while True:
            x = random.randrange(3)
            y = random.randrange(3)
            if self.current_state[x][y] == '-':
              self.current_state[x][y] = 'X'
              self.is_my_turn = True
              break
    
    return score
  
  def choose_best_move(self):
    if self.is_my_turn == True:
      # max
      max_i = -1
      max_j = -1
      max_score = -1000
      score = 0
      for i in range(3):
        for j in range(3):
          if board[i][j] != '-': continue
          board[i][j] = 'O'
          score = self.calculate_score()
          if score > max_score:
            max_score = score
            max_i = i
            max_j = j
          board[i][j] = '-'
    
      board[max_i][max_j] = 'O'
      self.is_my_turn = False
      
    elif self.is_my_turn == False:
      # min
      min_i = -1
      min_j = -1
      min_score = 1000
      score = 0
      for i in range(3):
        for j in range(3):
          if board[i][j] != '-': continue
          board[i][j] = 'X'
          score = self.calculate_score()
          if score < min_score:
            min_score = score
            min_i = i
            min_j = j
          board[i][j] = '-'
    
      board[min_i][min_j] = 'X'
      self.is_my_turn = True

playerA = PlayerA()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
playerA.choose_best_move()
playerA.print_board()
    
