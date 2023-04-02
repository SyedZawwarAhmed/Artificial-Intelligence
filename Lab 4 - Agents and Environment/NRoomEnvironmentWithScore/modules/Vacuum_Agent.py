from modules.agent import Agent
class VaccumAgent(Agent):
    def __init__(self):
        pass
    def sense(self,env):
        self.environment = env
    def act(self): 
        if self.environment.currentRoom.status == 'dirty': 
            self.environment.score -= 10
            return 'clean'
        if self.environment.currentRoom.location == 0: 
            return 'right'
        if self.environment.currentRoom.location > 0 and self.environment.currentRoom.location != len(self.environment.rooms) - 1:
            if self.environment.previousRoom.location < self.environment.currentRoom.location:
                return 'right' 
            elif self.environment.previousRoom.location > self.environment.currentRoom.location:
                return 'left'
        return 'left'