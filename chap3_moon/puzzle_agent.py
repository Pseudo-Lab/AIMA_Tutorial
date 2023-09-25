# AIMA Tutorial: From Book to Code
# Written by Mincheol Moon

import copy
import random

class PuzzleAgent:
  # 8-Puzzle 문제를 해결하는 Agent
  
  turn = 0 # 매 틱당 1 증가
  cost = 0 # 현재까지 소비한 Cost
  space_x = 0 # current_state의 빈 칸 '0'의 위치 (x좌표)
  space_y = 0 # current_state의 빈 칸 '0'의 위치 (y좌표)
  initial_state = [[0,1,3],
                   [4,2,5],
                   [7,8,6]]
  desired_state = [[1,2,3],
                   [4,5,6],
                   [7,8,0]]
  current_state = copy.deepcopy(initial_state)
  
  action = 0 # 1: up, 2: down, 3: left, 4: right. 빈 칸을 이동한다고 생각하면 됨
  terminate = False
  
  def __init__(self):
    self.turn = 0
    self.cost = 0
    self.initial_state = [[1,2,3],
                          [4,5,6],
                          [7,0,8]]
    self.desired_state = [[1,2,3],
                          [4,5,6],
                          [7,8,0]]
    self.current_state = copy.deepcopy(self.initial_state)
    
  def find_xy(self, to_find):
    for i in range(3):
      for j in range(3):
        if self.current_state[i][j] == to_find:
          self.space_x = j
          self.space_y = i
          return
  
  def sense(self):
    # 부분 관찰 환경을 위한 빌드업. 3장에서는 사용될 일이 없으며, mapdata, locationdata를 사용하면 됨
    pass
  
  def process_action(self):
    print("==================================================")
    # Check to Goal
    if self.current_state == self.desired_state:
      print("8-Puzzle Completed")
      self.terminate = True
      return
      
    # Process Action (Move)
    self.turn += 1
    self.cost += 1
    self.find_xy(0) # 빈 공간의 좌표 획득
    if self.action == 1: # Up
      if self.space_y == 0:
        print('Invalid Movement')
      else: # swap
        temp = self.current_state[self.space_y][self.space_x]
        self.current_state[self.space_y][self.space_x] = self.current_state[self.space_y - 1][self.space_x]
        self.current_state[self.space_y - 1][self.space_x] = temp
        
    elif self.action == 2: # Down
      if self.space_y == 2:
        print('Invalid Movement')
      else: # swap
        temp = self.current_state[self.space_y][self.space_x]
        self.current_state[self.space_y][self.space_x] = self.current_state[self.space_y + 1][self.space_x]
        self.current_state[self.space_y + 1][self.space_x] = temp
    
    elif self.action == 3: # Left
      if self.space_x == 0:
        print('Invalid Movement')
      else: # swap
        temp = self.current_state[self.space_y][self.space_x]
        self.current_state[self.space_y][self.space_x] = self.current_state[self.space_y][self.space_x - 1]
        self.current_state[self.space_y][self.space_x - 1] = temp
    
    elif self.action == 4: # Down
      if self.space_x == 2:
        print('Invalid Movement')
      else: # swap
        temp = self.current_state[self.space_y][self.space_x]
        self.current_state[self.space_y][self.space_x] = self.current_state[self.space_y][self.space_x + 1]
        self.current_state[self.space_y][self.space_x + 1] = temp
        
    print("Turn: ", self.turn)
    print("Action: ", self.action)
    print("Current Puzzle State")
    print(self.current_state[0])
    print(self.current_state[1])
    print(self.current_state[2])
  
  def estimation_distance(self, array_a, array_b):
    for i in range(1,9):
      self.find_xy(array_a, i)
    
  
  def choose_action(self):
    # 여기만 구현하면 됨.
    self.action = random.randint(1,4)
    
    