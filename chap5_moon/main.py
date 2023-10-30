import copy
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
    pass
  
  def calculate_score(self):
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
    
    # print
    print(self.current_state[0])
    print(self.current_state[0])
    print(self.current_state[0])
    
    if self.is_my_turn == True:
      for i in range(3):
        for j in range(3):
          if self.current_state[i][j] == '-': # 여기에 'O'를 찍을 수 있음
            # 찍고 재귀함수 호출
            self.current_state[i][j] = 'O'
            self.is_my_turn = False
            self.calculate_score()
            self.current_state[i][j] = '-'
    
    if self.is_my_turn == False:
      for i in range(3):
        for j in range(3):
          if self.current_state[i][j] == '-': # 여기에 'X'를 찍을 수 있음
            # 찍고 재귀함수 호출
            self.current_state[i][j] = 'X'
            self.is_my_turn = True
            self.calculate_score()
            self.current_state[i][j] = '-'
  

playerA = PlayerA()
playerA.calculate_score()
    
