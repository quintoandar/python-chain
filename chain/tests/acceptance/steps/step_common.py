"""Common Behave Steps.

This script contains all the common steps to behavior chain.tests. Those steps are
being used by multiple features.

"""
import chain

from behave import given, when, then
from functools import reduce
from chain.core.domains.state import State


@given("a dummy chain function")
def step_create_dummy_chain_function(context: dict) -> None:
    """Create a Dummy Chain Function.

    This step will create a new dummy function, compatible with chaining, and attach
    it to the context.

    """

    def dummy(context: State) -> None:
        pass

    context.dummy_function = dummy


@given("a new empty state")
def step_create_empty_state(context: dict) -> None:
    """Create an Empty State.

    This step will generate a new empty state to be used inside a given chain.

    """
    context.initial_state = chain.state()


@given("a new dirty state")
def step_create_dirty_state(context: dict) -> None:
    """Create an Dirty State.

    This step will generate a new state with contents to be used inside a
    given chain.

    """
    context.initial_state = chain.state(**context.fake.pydict())


@when("I run the chain")
def step_run_chain(context: dict) -> None:
    """Run the Generated Chain.

    This step will run the generated chain with the desired initial state.

    """
    to_execute = [context.initial_state] + context.chain

    if "results" not in context:
        context.results = list()

    result = reduce(lambda a, b: a >> b, to_execute)
    context.results.append(result)


@when("I run the first function on the chain directly")
def step_run_first_chain_directly(context: dict) -> None:
    """Run the First Function in the Chain.

    This step will run the first function in the chain directly.

    """
    result = context.chain[0]()

    if 'results' not in context:
        context.results = list()

    context.results.append(result)


@when("I reset the state")
def step_reset_state(context: dict) -> None:
    """Reset the Current State.

    This step will reset the current state.

    """
    context.initial_state.clear()


@then("the first result context must be my initial state")
def step_check_dummy_result(context: dict) -> None:
    """Check if Result is Same as Initial State.

    This step will check if the result is the same as the initial state.

    """
    assert context.results[0].current.get_state() == context.initial_state.get_state()


@then("the first result must have the desired output")
def step_check_output(context: dict) -> None:
    """Check if We Can Get the Chain Output.

    This step will check if the first result are with the desired output.

    """
    assert context.results[0].output == context.expected_output


@then("the direct call result must match the output")
def step_check_output_of_direct_call(context: dict) -> None:
    """Check if We Can Get the Function Output Directly.

    This step will check if, when running the function directly, we can get the
    desired output.

    """
    assert context.results[0] == context.expected_output
