"""Chain Package.

The chain creates a Chain class that will handle the core methods to create chainable
functions using our lib.

"""
from typing import ClassVar, Callable
from injectable import autowired
from copy import deepcopy
from chain.core.domains.state import State
from chain.core.domains.context import Context


class Chain:
    """Chain Class.

    This class is responsible for executing the core methods to allow functions to
    be chained.

    """

    @autowired
    def __init__(self, function: Callable, *, initial_state: State) -> ClassVar:
        self.initial_state = deepcopy(initial_state)
        self.function = function

    def __call__(self, *args, **kwargs) -> any:
        return self.function(context=self.initial_state, *args, **kwargs)

    def __split_output(self, output: any) -> tuple:
        return output if type(output) == tuple else (tuple(), dict())

    def execute(self, context: Context) -> any:
        """Execute the Current Chain Based on Context.

        This method will execute the current chain considering the current context that
        we are running into.

        """
        args, kwargs = self.__split_output(context.output)

        context.merge_context(self.initial_state)
        context.output = self.function(*args, **kwargs, context=context.current)

        return context
