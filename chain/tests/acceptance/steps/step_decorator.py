"""Decorator Behave Steps.

This script contains all the steps to behavior tests of the decorator feature.

"""
import chain

from behave import given, then
from unittest.mock import MagicMock


@given("a mocked decorated chain function")
def step_create_mocked_decorated_function(context: dict) -> None:
    """Declare a New Decorated Function.

    This step will declare a new decorated chain function and assign it to
    the current test context.

    """
    nb_functions = context.fake.pyint()
    dirt = [chain(context.dummy_function) for _ in range(nb_functions)]

    context.mock = MagicMock()
    context.chain = [chain(context.mock)] + dirt


@then("the mocked should have been called")
def step_check_if_mock_was_called(context: dict) -> None:
    """Check if the mock was called.

    This step will check if the mock from our current test context was called.

    """
    context.mock.assert_called_once()
