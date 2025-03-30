from abc import ABC, abstractmethod
from .action import BaseAction
from collections.abc import Iterable

class BaseState(ABC):
    """
    Base class for game state 
    """

    @abstractmethod
    def get_current_player(self) -> int:
        """
        Returns id for player whose turn it is
        """
        raise NotImplementedError()

    @abstractmethod
    def get_valid_actions(self) -> Iterable[BaseAction]:
        """
        Return a list of all valid actions from this state
        """
        raise NotImplementedError()
    
    @abstractmethod
    def take_action(self, action: BaseAction) -> 'BaseState':
        """
        Return the state that follows this one after taking a specific action
        """
        raise NotImplementedError()

    @abstractmethod
    def get_reward(self, player_id: int) -> float:
        """
        Return the reward for a given player id in the current state
        """
        raise NotImplementedError()