"""Chain Decorator Unit Tests.

The decorator test file ensures that we are being able to create a new decorator on an
existing function.

"""
from pytest import main
from sys import argv
from unittest.mock import patch, MagicMock
from chain.tests.helpers import DependencyMocker
from chain.core.domains.chain import decorator
from chain.core.domains.chain import Chain

file_path = "chain.core.domains.chain.decorator"
dependencies = DependencyMocker(file_path)


@patch.multiple(file_path, **dependencies.to_dict())
def test_add_new_function(**kwargs) -> None:
    """Test the Creation of a New Chain.

    Ensures that we can create a new chain using the declared decorator.

    """
    # Given
    func = MagicMock()
    decorated_class = decorator.Decorator

    # When
    result = decorated_class(func)

    # Then
    assert result.function == func


@patch.multiple(file_path, **dependencies.to_dict())
def test_update_wrapper(update_wrapper: MagicMock = None, **kwargs) -> None:
    """Test the Call of Update Wrapper.

    Ensures that we are calling the update wrapper function on init.

    """
    # Given
    func = MagicMock()
    decorated_class = decorator.Decorator

    # When
    result = decorated_class(func)

    # Then
    update_wrapper.assert_called_once_with(result, func)


@patch.multiple(file_path, **dependencies.to_dict(ignore=("Chain",)))
def test_super(**kwargs) -> None:
    """Test the Super of Decorator.

    Ensures that the generated class has a super Chain class.

    """
    # When
    decorated_class = decorator.Decorator

    # Then
    assert issubclass(decorated_class, Chain)


if __name__ == "__main__":
    args = [__file__] + [arg for arg in argv[1:]]
    main(args)
