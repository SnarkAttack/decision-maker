from abc import ABC, abstractmethod
from .state import BaseState
from .action import BaseAction

class BaseAgent(ABC):

    @abstractmethod
    def get_move(self, inital_state: BaseState) -> BaseAction:
        """
        Return an action to take given the current state
        """
        raise NotImplementedError()