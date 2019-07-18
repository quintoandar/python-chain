"""Decorator Behave Steps.

This script contains all the steps to behavior tests of the decorator feature.

"""
import chain

from behave import given, when, then
from itertools import count
from unittest.mock import MagicMock
from chain.core.domains.state import State


@given("a random number of static chains")
def step_create_random_static_chains(context: dict) -> None:
    """Create a Random Number of Static Chains.

    This step will generate a random number of static chains.

    """
    nb_chains = context.fake.pyint()
    context.chain = [chain(context.dummy_function) for _ in range(nb_chains)]


@given("an odd random number of static chains")
def step_create_odd_random_static_chains(context: dict) -> None:
    """Create an Odd Random Number of Static Chains.

    This step will generate an odd random number of static chains.

    """

    def dummy(context: State) -> None:
        pass

    nb_chains = context.fake.pyint(min=1, step=2)
    context.chain = [chain(dummy) for _ in range(nb_chains)]


@given("a single static chain")
def step_create_single_random_static_chain(context: dict) -> None:
    """Create a Random Number of Static Chains.

    This step will generate a random number of static chain.

    """

    def dummy(context: State) -> None:
        pass

    context.chain = [chain(dummy)]


@given("a new chain with mocked function")
def step_create_mocked_chain(context: dict) -> None:
    """Create a Chain with Mocked Function.

    This step will generate a new chain with mocked function and append it on the end
    of the created chain.

    """
    if "chain" not in context:
        context.chain = list()

    context.mocked_function = MagicMock(return_value=None)
    context.chain.append(chain(context.mocked_function))


@given("add a return value to the mocked function")
def step_add_return_value(context: dict) -> None:
    """Add a Return Value to the Mocked Function.

    This step will generate a new return value to the mocked function on the chain.

    """
    context.expected_output = context.fake.pydict()
    context.mocked_function.return_value = context.expected_output


@given("add an arg return value to the mocked function")
def step_add_return_value_as_args(context: dict) -> None:
    """Add a Return Value to the Mocked Function as Args.

    This step will generate a new return value as args to be passed to the next function
    on the chain.

    """
    context.expected_args = context.fake.pytuple()
    context.expected_kwargs = context.fake.pydict()

    context.mocked_function.return_value = (
        context.expected_args,
        context.expected_kwargs,
    )


@given("a new chain returning random autoincremented data")
def step_create_autoincrementing_chain(context: dict) -> None:
    """Create a Autoincrementing Chain.

    This step will generate a new chain with a function that will always return an
    autoincremented data.

    """
    if "chain" not in context:
        context.chain = list()

    context.initial_state.count = count()

    def autoincrement(context: State) -> tuple:
        counted = next(context.count)

        return (counted,), dict()

    context.chain.append(chain(autoincrement))


@given("a decorated chain function with output")
def step_create_decorated_function_with_output(context: dict) -> None:
    """Create a New Decorated Chain Function With Output.

    This step will generate a new decorated chain function.

    """
    expected_output = context.fake.pydict()

    @chain
    def dummy(context: State, expected_output=expected_output) -> None:
        return expected_output

    if 'chain' not in context:
        context.chain = list()

    context.expected_output = expected_output
    context.chain.append(dummy)


@given("a decorated chain function without output")
def step_create_decorated_function_without_output(context: dict) -> None:
    """Create a New Decorated Chain Function Without Output.

    This step will generate a new decorated chain function without adding an output.

    """
    expected_output = context.fake.pydict()

    @chain
    def bar(context: State) -> None:
        context.bar = 'bar'

    if 'chain' not in context:
        context.chain = list()

    context.expected_output = expected_output
    context.chain.append(bar)


@when("I reverse the chain")
def step_revese_chain(context: dict) -> None:
    """Reverse the Generated Chain.

    This step will reverse the current chain.

    """
    context.chain = context.chain[::-1]


@when("I add a counter on the current state")
def step_add_counter_to_state(context: dict) -> None:
    """Add Counter on Current State.

    This step will add a counter on the current initial state.

    """
    context.initial_state.count = count()


@then("the mocked function should have been called with correct data")
def step_check_args_chain(context: dict) -> None:
    """Check if We Are Passing Args.

    This step will check if, during a chain, we are passing args between the chained
    functions.

    """
    calls = context.mocked_function.call_args_list
    last_call = calls[-1]

    args = last_call[0]
    kwargs = last_call[1]

    context.expected_kwargs.update({"context": kwargs["context"]})

    assert args == context.expected_args
    assert kwargs == context.expected_kwargs
    assert kwargs["context"].get_state() == context.initial_state.get_state()


@then("the context should not persist data")
def step_check_reversed_chain(context: dict) -> None:
    """Check the Result of the Reversed Chain.

    This step will check the result of the reversed chain to see if it has runned
    ignoring the previous state.

    """
    calls = context.mocked_function.call_args_list
    last_call = calls[-1]

    args = last_call[0]
    kwargs = last_call[1]

    assert args[0] == 0
