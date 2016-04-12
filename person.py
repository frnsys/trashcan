class Person():
    """ a person is stateful and
    makes individual decisions based on
    personal utility functions and state"""
    def __init__(self, utilities=None, state=None, impatience=0):
        # utilities are 3-arity functions that take as input:
        # (property value, personal state, world state)
        self.utilities = utilities or {}
        self.state = state or {}

        self.impatience = impatience

    def evaluate(self, option, world):
        """scores an option based on utility functions and state"""
        score = 0
        for property, func in self.utilities.items():
            try:
                value = getattr(option, property)
            except AttributeError:
                continue

            # property value may depend on the world state
            if callable(value):
                value = value(world)
            score += func(value, self.state, world)
        return score

    def hyperbolic_discount(self, delay):
        return 1/(1 + delay * self.impatience)