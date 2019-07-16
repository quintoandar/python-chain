"""State Package.

The state creates a Chain state that will store all the current chain state and also
create some useful methods to be used during a chain.

"""
from typing import ClassVar
from chain.core.domains.context import Context


class State:
    """State Class.

    This class is responsible for storing all the data from a given chain and allowing
    to insert new data and run specific methods.

    """

    def __init__(self, **initial_state: dict) -> ClassVar:
        self.__dict__.update(initial_state)

    def __gt__(self, next) -> any:
        return Context(state=self, origin=next)

    def clear(self) -> None:
        """Clear the Current State.

        This method will remove everything from the current state.

        """
        self.__dict__.clear()

    def get_state(self) -> any:
        """Get the Current State.

        Get all the data from the current state.

        """
        return self.__dict__
