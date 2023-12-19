from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def from_dict(self):
        pass
