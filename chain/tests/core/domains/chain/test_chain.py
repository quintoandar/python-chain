"""Chain Unit Tests.

The chain test file ensures that we are being able to create a new chain that can
execute the basic desired methods.

"""
from pytest import main
from sys import argv
from faker import Faker
from itertools import count
from unittest.mock import patch, MagicMock, PropertyMock
from chain.tests.helpers import DependencyMocker
from chain.core.domains.chain.chain import Chain

file_path = "chain.core.domains.chain.chain"
dependencies = DependencyMocker(file_path)


@patch.multiple(file_path, **dependencies.to_dict())
def test_split_output(fake: Faker, **kwargs) -> None:
    """Test the Split Result Method.

    Ensures that our chain can split the previous result from the current context if
    it is a tuple. If it is not, it should return an default arg tuple.

    """
    # Given
    chain = Chain(lambda: None)

    args = fake.pytuple()
    kwargs = fake.pydict()

    # When
    with_args = chain._Chain__split_output((args, kwargs))
    without_args = chain._Chain__split_output(fake.pydict())

    # Then
    assert with_args == (args, kwargs)
    assert without_args == (tuple(), dict())


@patch.multiple(file_path, **dependencies.to_dict())
def test_execute(fake: Faker, Context: MagicMock = None, **kwargs) -> None:
    """Test the Execution of a Chain.

    Ensures that we can execute a chain given a specific context.

    """
    # Given
    context = Context()
    prev_args, prev_kwargs = (tuple(), dict())

    function = MagicMock(return_value=None)
    context_merge = MagicMock()
    chain_split_output = MagicMock(return_value=(prev_args, prev_kwargs))
    chain = Chain(function)

    prop_context_merge = PropertyMock(return_value=context_merge)
    prop_context_output = PropertyMock(return_value=fake.word())

    chain.initial_state = fake.word()
    chain._Chain__split_output = chain_split_output

    type(context).output = prop_context_output
    type(context).merge_context = prop_context_merge

    # When
    result = chain.execute(context=context)

    # Then
    chain_split_output.assert_called_once_with(context.output)
    context_merge.assert_called_once_with(chain.initial_state)
    function.assert_called_once_with(*prev_args, **prev_kwargs, context=context.current)

    assert result == context


if __name__ == "__main__":
    args = [__file__] + [arg for arg in argv[1:]]
    main(args)
