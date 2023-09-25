# 8-Puzzle
# Action: up, down, left, right

from puzzle_agent import PuzzleAgent

puzzleagent1 = PuzzleAgent()

# main loop
while True:
  if puzzleagent1.terminate == True: break
  puzzleagent1.choose_action()
  puzzleagent1.process_action()