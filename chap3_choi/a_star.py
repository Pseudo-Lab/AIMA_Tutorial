class State_Astar:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    # i1과 i2를 교환하여서 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State_Astar(new_board, self.goal, moves)

    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    def expand(self, moves):
        result = []
        i = self.board.index(0)     # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 1, 2]:      # UP 연산자
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [2, 5, 8]:      # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:      # DOWN 연산자
            result.append(self.get_new_board(i, i+3, moves))
        return result

    # f(n) = h(n) + g(n)
    def f(self):
        return self.h() + self.g()

    # h(n): 휴리스틱 함수
    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    # g(n): 시작 노드로부터 떨어진 경로 수
    def g(self):
        return self.moves

    # def __eq__(self, other):
    #     return self.board == other.board

    # 상태와 상태를 비교하기 위하여 lt(less than) 연산자 정의
    # 우선순위 큐 정렬 기준 재정의
    def __lt__(self, other):
        return self.f() < other.f()

    # def __gt__(self, other):
    #     return self.f() > other.f()

    # 객체 출력
    def __str__(self):
        return "-------------------- f(n)=" + str(self.f()) + "\n"+ \
        "-------------------- h(n)=" + str(self.h()) + "\n" + \
        "-------------------- g(n)=" + str(self.g()) + "\n" + \
        str(self.board[:3]) + "\n" + \
        str(self.board[3:6]) + "\n" + \
        str(self.board[6:]) + "\n" + \
        "--------------------"


import queue

# 초기 상태
puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

# 목표 상태
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

# open 리스트는 우선순위 큐로 생성
open_queue = queue.PriorityQueue()
open_queue.put(State_Astar(puzzle, goal))

closed_queue = []
moves = 0
turn = 0

while not open_queue.empty():

    turn += 1
    current = open_queue.get()
    print(current)
    if current.board == goal:
        print("탐색 성공")
        print("탐색 횟수: ", turn)
        print("moves: ", moves)
        break
    moves = current.moves + 1
    for state in current.expand(moves):
        if state not in closed_queue:
            open_queue.put(state)   # 우선순위 큐 정렬
    closed_queue.append(current)