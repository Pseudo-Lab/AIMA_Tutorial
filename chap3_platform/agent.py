# AIMA Tutorial: From Book to Code
# Written by Mincheol Moon

class Agent:
  # 0 ~ 5번까지의 도시가 있으며, initial_state에서 desired_state까지 이동하는 것이 목표
  
  turn = 0 # 매 틱당 1 증가
  cost = 0 # 현재까지 소비한 Cost
  initial_state = 0 # 초기 위치 (상태)
  current_state = 0 # 현재 위치 (상태)
  desired_state = 5 # 목표 위치 (상태)
  action = -1 # 이동하려는 위치. 매 턴마다 0~5 중 1개 선택
  terminate = False # 이 값이 True면 에이전트의 행동 중지
  
  # Real Map Data, -1은 이동 불가, 양수는 Cost
  # mapdata[x][y]는 x지점에서 y지점으로 가기 위한 실제 Cost
  # 예를 들어, 0번 지점에서 1번 지점까지 가기 위한 Cost는 mapdata[0][1] = 56
  mapdata = [[-1,56,-1,-1,-1,-1],
             [56,-1,153,267,-1,-1],
             [-1,153,-1,-1,-1,-1],
             [-1,267,-1,-1,98,-1],
             [-1,-1,-1,98,-1,178],
             [-1,-1,-1,-1,178,-1]]
  
  # Heuristic을 위한 각 지점의 2차원 좌표
  locationdata = [(0,0),(30,40),(67,92),(121,78),(154,101),(220,151)]
  
  def __init__(self):
    self.cost = 0
    self.initial_state = 0
    self.current_state = 0
    self.desired_state = 5
  
  def sense(self):
    # 부분 관찰 환경을 위한 빌드업. 3장에서는 사용될 일이 없으며, mapdata, locationdata를 사용하면 됨
    pass
  
  def process_action(self):
    print("==================================================")
    # Check to Goal
    if self.current_state == self.desired_state:
      print("Arrive to Destination")
      self.terminate = True
      
    # Process Action (Move)
    self.turn += 1
    if self.mapdata[self.current_state][self.action] == -1:
      print('Invalid Movement!')
    else:
      self.cost += self.mapdata[self.current_state][self.action]
      self.current_state = self.action
    
    print("Turn: ", self.turn)
    print("Location: ", self.current_state)
    print("Goal: ", self.desired_state)
    print("Cost: ", self.cost)
    
  
  def choose_action(self):
    # 여기만 구현하면 됨.
    if self.current_state == 0:
      self.action = 1
    elif self.current_state == 1:
      self.action = 3
    elif self.current_state == 2:
      self.action = 1
    elif self.current_state == 3:
      self.action = 4
    elif self.current_state == 4:
      self.action = 5
    elif self.current_state == 5:
      self.action = 4
    