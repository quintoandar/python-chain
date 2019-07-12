"""Decorator Package.

The decorator exposes the possibility to create a new decorator to an existing function.

"""
from functools import update_wrapper
from typing import Callable, ClassVar
from injectable import autowired
from chain.core.domains.state import State
from chain.core.domains.chain import Chain


class Decorator(Chain):
    """Decorator Class.

    This class is responsible for allowing external functions to use our Chain as a
    decorator on their functions.

    """

    @autowired
    def __init__(self, function: Callable, *, initial_state: State) -> ClassVar:
        super().__init__(function, initial_state=initial_state)
        update_wrapper(self, function)
