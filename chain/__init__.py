"""Chain Module.

This module contains all the relevant methods for the chain module. It holds a shortcut
for the most used functions in order to make it easier for developers to import and
use our packages.

"""
from sys import modules
from types import ModuleType
from chain.core.domains.state import State
from chain.core.domains.chain import Decorator

__version__ = "1.0.2"


class Chain(ModuleType):
    """Default Chain Class.

    The Chain class is the entrypoint to use our lib. It holds all the logic
    to use the core packages of this library.

    """

    def __call__(self, *args, **kwargs):
        return Decorator(*args, **kwargs)

    def state(self, **kwargs):
        """Generate New State.

        This method will generate a new state given kwargs, using their keys
        as the state key attribute with respective values.

        """
        return State(**kwargs)


modules[__name__].__class__ = Chain
