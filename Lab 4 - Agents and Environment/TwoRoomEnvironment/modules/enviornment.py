# Python code for the abstract Environment

from abc import abstractmethod
class Environment:

    @abstractmethod
    def __init__(self, n):
        self.n = n
    def executeStep(self,n=1): 
        raise NotImplementedError('action must be defined!')
    def executeAll(self): 
        raise NotImplementedError('action must be defined!')
    def delay(self,n=100): 
        self.delay = n
 
