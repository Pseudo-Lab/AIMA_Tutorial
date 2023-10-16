import copy
import random
# nqueen problem with hill-climb search
# 8-Queen을 가정

# 한 열의 하나의 퀸의 존재. 퀸의 열들을 배열로 저장. chessboard_current는 다음과 같음.
# Q-------
# -Q------
# --Q-----
# ---Q----
# ----Q---
# -----Q--
# ------Q-
# -------Q
chessboard_current = [0,1,2,3,4,5,6,7]
chessboard_next = [0,0,0,0,0,0,0,0]
terminate = False

def random_initialize():
  global chessboard_current
  for i in range(8):
    temp = random.randrange(8)
    chessboard_current[i] = temp
    

# score: 퀸이 잡을 수 있는 퀸의 수
def calculate_score(chessboard_array):
  score = 0
  # row
  for i in range(8):
    for j in range(8):
      if i == j: continue
      if chessboard_array[i] == chessboard_array[j]: score += 1
  # diagonal
  for i in range(8):
    for j in range(8):
      if i == j: continue
      if chessboard_array[i] + i == chessboard_array[j] + j: score += 1
      if chessboard_array[i] - i == chessboard_array[j] - j: score += 1
      
  return score
      
def find_min_next():
  global chessboard_current, chessboard_next, terminate
  current_score = calculate_score(chessboard_current)
  if current_score == 0:
    terminate = True
    return 1
  next_score = []
  for i in range(8): # i번쨰 말을
    for j in range(8): # j 위치로 이동시켰을 떄
      chessboard_next = copy.deepcopy(chessboard_current)
      chessboard_next[i] = j
      temp_score = calculate_score(chessboard_next)
      next_score.append(temp_score)
  
  min_index = next_score.index(min(next_score))
  min_i = min_index // 8
  min_j = min_index % 8
  
  chessboard_next = copy.deepcopy(chessboard_current)
  chessboard_next[min_i] = min_j
  return 0

# Start!
random_initialize()
while True:
  # Display State
  print(chessboard_current)
  print(calculate_score(chessboard_current))
  find_min_next()
  if chessboard_next == chessboard_current: break
  chessboard_current = copy.deepcopy(chessboard_next)
  