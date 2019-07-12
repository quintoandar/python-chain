"""Context Package.

The context is the result of a given operation between two chains. It has a bunch of
methods that can be used to extract data from the chain result.

"""
from typing import ClassVar
from copy import deepcopy


class Context:
    """Context Class.

    This class is responsible for storing all the data from a given chain output and
    allowing to perform specific transformations with it.

    """

    def __init__(self, state: ClassVar, origin: ClassVar) -> ClassVar:
        self.origin = origin
        self.current = deepcopy(state)
        self.__initial_state = deepcopy(state)

        self.merge_context(origin.initial_state)
        self.__autorun()

    def __gt__(self, next) -> any:
        return next.execute(context=self)

    def __autorun(self) -> None:
        self.output = self.origin.function(context=self.current)

    def merge_context(self, state) -> None:
        """Merge Context with State.

        This method will merge the current context with a given state. It can be used
        before executing a chain.

        """
        self.current.__dict__.update(state.__dict__)
