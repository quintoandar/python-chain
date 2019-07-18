"""State Unit Tests.

The state test file ensures that we are being able to create a new state that we can
use inside a chain.

"""
from pytest import main
from sys import argv
from faker import Faker
from unittest.mock import patch, MagicMock
from chain.tests.helpers import DependencyMocker
from chain.core.domains.state.state import State

file_path = "chain.core.domains.state.state"
dependencies = DependencyMocker(file_path)


@patch.multiple(file_path, **dependencies.to_dict())
def test_store_data(fake: Faker, **kwargs) -> None:
    """Test the Storage of Data on State.

    Ensures that we can store any data on a given state.

    """
    # Given
    fake_string = fake.word()
    fake_tuple = fake.pytuple()
    fake_dict = fake.pydict()

    state = State()

    # When
    state.string = fake_string
    state.tuple = fake_tuple
    state.dict = fake_dict

    # Then
    assert state.string == fake_string
    assert state.tuple == fake_tuple
    assert state.dict == fake_dict


@patch.multiple(file_path, **dependencies.to_dict())
def test_multiple_stores(fake: Faker, **kwargs) -> None:
    """Test the Creation of Multiple Stores.

    Ensures that we can create multiple stores and those would not impact on each other.

    """
    # Given
    fake_string_one = fake.word()
    fake_string_two = fake.word()

    state_one = State()
    state_two = State()

    # When
    state_one.string = fake_string_one
    state_two.string = fake_string_two

    # Then
    assert state_one.string == fake_string_one
    assert state_two.string == fake_string_two
    assert state_one.string != state_two.string


@patch.multiple(file_path, **dependencies.to_dict())
def test_initial_state(fake: Faker, **kwargs) -> None:
    """Test the Creation of a Initial State.

    Ensures that we can set a initial state on the creation of the chain.

    """
    # Given
    fake_string = fake.word()
    fake_tuple = fake.pytuple()
    fake_dict = fake.pydict()

    initial_state = {"string": fake_string, "tuple": fake_tuple, "dict": fake_dict}

    # When
    state = State(**initial_state)

    # Then
    assert state.string == fake_string
    assert state.tuple == fake_tuple
    assert state.dict == fake_dict


@patch.multiple(file_path, **dependencies.to_dict())
def test_method_clear(fake: Faker, **kwargs) -> None:
    """Test the Clear Method.

    Ensures that we can clear the current state.

    """
    # Given
    fake_string = fake.word()
    state = State(string=fake_string)

    # When
    state.clear()

    # Then
    assert not hasattr(state, "string")


@patch.multiple(file_path, **dependencies.to_dict())
def test_chain_rshift_return(fake: Faker, Context: MagicMock = None, **kwargs) -> None:
    """Test if State is Chainable.

    Ensures that we can insert the state in a chain.

    """
    # Given
    next = fake.word()
    state = State()

    # When
    result = state >> next

    # Then
    Context.assert_called_once_with(state=state, origin=next)

    assert result == Context()


@patch.multiple(file_path, **dependencies.to_dict())
def test_get_state(fake: Faker, **kwargs) -> None:
    """Test if we Can Get The State.

    Ensures that we can get the current state.

    """
    # Given
    expected_string = fake.word()
    state = State(string=expected_string)

    # When
    result = state.get_state()

    # Then
    assert result == {"string": expected_string}


if __name__ == "__main__":
    args = [__file__] + [arg for arg in argv[1:]]
    main(args)
