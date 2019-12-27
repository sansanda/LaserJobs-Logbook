from abc import ABC, abstractmethod
from Logic.LaserJob import LaserJob

class IFilter():
    @abstractmethod
    def satisfies(self,laserJob):
        pass
    def getName(self):
        pass

