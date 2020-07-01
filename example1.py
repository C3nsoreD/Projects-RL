import random

class Environment:
    def __init__(self):
        self.steps_left = 10

    # -> List[float] is an example of type annotaions
    def get_observation(self) -> List[float]:
        # Returns the current env's observation to the agent
        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> List[int]:
        # method that allows the agent to query the set of actions 
        # to execute
        return [0, 1]

    def is_done(self) -> bool:
        # Signals the end of the episode to the agent.
        return self.steps_left == 0
    
    # central piece of this environment
    def action(self, action: int) -> float:
        # Handles the agent's action and returns the reward for this action
        # in this case the reward is random
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()
