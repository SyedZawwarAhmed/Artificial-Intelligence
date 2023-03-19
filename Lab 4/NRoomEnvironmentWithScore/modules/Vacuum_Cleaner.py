# For the Two Room Vacuum Cleaner Environment
from modules.enviornment import Environment
from modules.Room import Room


class NRoomVaccumCleanerEnvironment():
    def __init__(self, agent, n):
        self.rooms = [Room(i, 'dirty') for i in range(n)]
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.previousRoom = None
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score = 0

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
                self.score += 25
            elif res == 'right':
                self.previousRoom = self.currentRoom
                self.currentRoom = self.rooms[self.currentRoom.location + 1]
                self.score -= 1
            elif res == 'left':
                self.previousRoom = self.currentRoom
                self.currentRoom = self.rooms[self.currentRoom.location - 1]
                self.score -= 1
            self.displayAction()
            self.displayScore()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action))

    def displayScore(self):
        print(
            "------- Score at step %d is [%s]" % (self.step, self.score))

    def delay(self, n=100):
        self.delay = n
