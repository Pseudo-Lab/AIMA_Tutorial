from agent import Agent

agent1 = Agent()

# main loop
while True:
  if agent1.terminate == True: break
  agent1.choose_action()
  agent1.process_action()