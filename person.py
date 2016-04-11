class Person():
    """ a person is stateful and
    makes individual decisions based on
    personal utility functions and state"""
    def __init__(self, utilities=None, state=None):
        self.utilities = utilities or {}
        self.state = state or {}

    def evaluate(self, option, state):
        """scores an option based on utility functions and state"""
        score = 0
        for property, func in self.utilities.items():
            value = getattr(option, property)
            if callable(value):
                value = value(state)
            score += func(value, self.state)
        return score