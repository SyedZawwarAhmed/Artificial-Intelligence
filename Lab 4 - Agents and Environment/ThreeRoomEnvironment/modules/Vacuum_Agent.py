from modules.agent import Agent
class VaccumAgent(Agent):
    def __init__(self):
        pass
    def sense(self,env):
        self.environment = env
    def act(self): 
        if self.environment.currentRoom.status == 'dirty': return 'clean'
        if self.environment.currentRoom.location == 'A': 
            return 'right'
        if self.environment.currentRoom.location == 'B':
            if self.environment.previousRoom.location == 'A':
                return 'right' 
            elif self.environment.previousRoom.location == 'C':
                return 'left'
        return 'left'