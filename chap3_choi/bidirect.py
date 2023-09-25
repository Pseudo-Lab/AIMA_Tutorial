class State_BFS:
    def __init__(self, board, moves=0):
        self.board = board
        self.moves = moves
        # self.goal = goal

    # i1가 i2를 교환하여 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State_BFS(new_board, moves)

    # 자식 노드를 확정하여서 리스트에 저장하여서 반환한다.
    def expand(self, moves):
        result = []
        i = self.board.index(0)         # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 1, 2]:          # UP 연산자
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:          # LEFT 연산자
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:          # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:          # DOWN 연산자
            result.append(self.get_new_board(i, i+3, moves))
        return result

    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return str(self.board[:3]) + "\n" + \
        str(self.board[3:6]) + "\n" + \
        str(self.board[6:]) + "\n" + \
        "-------------------"

    def __eq__(self, other):
        return self.board == other.board

############################################################

turn = 0

# start_node = [1, 2, 3,
#           0, 4, 6,
#           7, 5, 8]
start_node = [2, 0, 3,
          1, 4, 6,
          7, 5, 8]

# 목표 상태
end_node = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

## 시작 노드 관리
# open 리스트
start_open_queue = []
start_open_queue.append(State_BFS(start_node))

start_closed_queue = []
start_moves = 0

## 종점 노드 관리
end_open_queue = []
end_open_queue.append(State_BFS(end_node))

end_closed_queue = []
end_moves = 0


def queue_empty_or_not(queue):
    if len(queue) != 0:
        return True
    else:
        print("탐색 실패")
        return False

def is_equal_board(start_open_queue, end_open_queue):
    for i in start_open_queue:
        for j in end_open_queue:
            if i==j:
                print("탐색 성공")
                print(i)
                return True
    return False

while queue_empty_or_not(start_open_queue) or queue_empty_or_not(end_open_queue):
    
    turn += 1

    ## 시작 노드 관리
    start_open_current = start_open_queue.pop(0)             # OPEN 리스트의 뒤에서 상태 가져오기
    print("현재 노드 (시작)")
    print(start_open_current)

    start_moves = start_open_current.moves + 1
    start_closed_queue.append(start_open_current)
    
    for state in start_open_current.expand(start_moves):
        if (state in start_closed_queue) or (state in start_open_queue):        # 이미 거쳐간 노드이면 or 깊이 제한
            continue                                   # 노드를 버린다.
        else:
            start_open_queue.append(state)                  # OPEN 리스트의 끝에 추가
            print("자식 노드", start_moves, ", and state moves: ", state.moves)
            print(state)
    
    if is_equal_board(start_open_queue, end_open_queue):
        # print("탐색 성공")
        print("탐색 횟수: ", turn)
        print("start node moves: ", start_moves)
        print("end node moves: ", end_moves)
        break

    turn += 1

    ## 종점 노드 관리
    end_open_current = end_open_queue.pop(0)             # OPEN 리스트의 뒤에서 상태 가져오기
    print("현재 노드 (종점)")
    print(end_open_current)

    end_moves = end_open_current.moves + 1
    end_closed_queue.append(end_open_current)
    
    for state in end_open_current.expand(end_moves):
        if (state in end_closed_queue) or (state in end_open_queue):    # 이미 거쳐간 노드이면 or 깊이 제한
            continue                                # 노드를 버린다.
        else:
            end_open_queue.append(state)            # OPEN 리스트의 끝에 추가
            print("자식 노드", end_moves, ", and state moves: ", state.moves)
            print(state)
    
    if is_equal_board(start_open_queue, end_open_queue):
        # print("탐색 성공")
        print("탐색 횟수: ", turn)
        print("start node moves: ", start_moves)
        print("end node moves: ", end_moves)
        break