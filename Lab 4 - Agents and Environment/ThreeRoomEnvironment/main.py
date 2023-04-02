from modules.Vacuum_Agent import VaccumAgent
from modules.Vacuum_Cleaner import ThreeRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = ThreeRoomVaccumCleanerEnvironment(vcagent) 
env.executeStep(50)