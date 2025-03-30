import random

from decision_maker.base import BaseAction, BaseAgent, BaseState
from decision_maker.utils import logger as lg


class RandomAgent(BaseAgent):

    def __init__(self, seed=None):
        random.seed(seed)
        
    def get_move(self, inital_state: BaseState) -> BaseAction:

        valid_actions = inital_state.get_valid_actions()

        if len(valid_actions):
            lg.error("No valid actions returned")
            raise ValueError()

        next_move = random.shuffle(valid_actions)[0]

        return next_move