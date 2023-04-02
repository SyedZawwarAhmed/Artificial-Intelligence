from modules.Vacuum_Agent import VaccumAgent
from modules.Vacuum_Cleaner import TwoRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = TwoRoomVaccumCleanerEnvironment(vcagent) 
env.executeStep(50)