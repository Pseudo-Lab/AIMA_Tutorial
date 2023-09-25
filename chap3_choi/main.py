from bidirect import State_BFS

agent1 = State_BFS()

# main loop
while len(agent1.open_queue) != 0:
  if agent1.terminate == True: break
  agent1.choose_action()
  agent1.process_action()