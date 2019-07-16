"""Entrypoint Unit Tests.

The chain test file ensures that we are being able to create a new chain that can
execute the basic desired methods.

"""
import chain

from pytest import main
from sys import argv
from faker import Faker
from unittest.mock import patch, MagicMock
from chain.tests.helpers import DependencyMocker

file_path = "chain"
dependencies = DependencyMocker(file_path)


@patch.multiple(file_path, **dependencies.to_dict())
def test_call(fake: Faker, Decorator: MagicMock = None, **kwargs) -> None:
    """Test the Entrypoint Call.

    Ensures that when we call the entrypoint it will automatically redirect
    to the creation of a decorator, passing args and kwargs.

    """
    # Given
    args = fake.word()
    kwargs = fake.pydict()

    # When
    created_chain = chain(*args, **kwargs)

    # Then
    Decorator.assert_called_once_with(*args, **kwargs)


@patch.multiple(file_path, **dependencies.to_dict())
def test_state(fake: Faker, State: MagicMock = None, **kwargs) -> None:
    """Test the State Creation.

    Ensures that when we call the state method it is creating and returning a
    new chain state.

    """
    # Given
    kwargs = fake.pydict()

    # When
    state = chain.state(**kwargs)

    # Then
    State.assert_called_once_with(**kwargs)


if __name__ == "__main__":
    args = [__file__] + [arg for arg in argv[1:]]
    main(args)
