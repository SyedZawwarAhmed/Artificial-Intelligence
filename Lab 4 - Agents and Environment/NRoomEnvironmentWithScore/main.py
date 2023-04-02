from modules.Vacuum_Agent import VaccumAgent
from modules.Vacuum_Cleaner import NRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = NRoomVaccumCleanerEnvironment(vcagent, 5) 
env.executeStep(50)