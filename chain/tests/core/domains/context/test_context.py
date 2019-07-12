"""Context Unit Tests.

The state test file ensures that we are being able to create a new context that we can
use inside a chain.

"""
from pytest import main
from sys import argv
from faker import Faker
from unittest.mock import MagicMock
from chain.tests.helpers import FakeChain, FakeState
from chain.core.domains.context.context import Context


def test_initialize(fake: Faker, **kwargs) -> None:
    """Test the Initialization of a Context.

    Ensures that we can initialize a context, storing all desired args and running the
    startup methods.

    """
    # Given
    class MutatedContext(Context):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    fake_state = fake.pydict()
    mocked_merge_context = MagicMock()
    mocked_autorun = MagicMock()

    fake_origin = FakeChain()
    fake_origin.initial_state = fake.word()

    MutatedContext.merge_context = mocked_merge_context
    MutatedContext._Context__autorun = mocked_autorun

    # When
    context = MutatedContext(fake_state, fake_origin)

    # Then
    mocked_merge_context.assert_called_once_with(fake_origin.initial_state)
    mocked_autorun.assert_called_once()

    assert context.origin.initial_state == fake_origin.initial_state
    assert context.current == fake_state
    assert context._Context__initial_state == fake_state


def test_gt(fake: Faker, **kwargs) -> None:
    """Test the Override of the Greater Than Method.

    Ensures that we are overriding the greater than builtin function.

    """
    # Given
    fake_state = MagicMock()
    fake_origin = MagicMock()
    mocked_execute = MagicMock()

    fake_next = FakeChain()
    fake_next.execute = mocked_execute

    expected = fake.word()
    mocked_execute.return_value = expected

    context = Context(fake_state, fake_origin)

    # When
    result = context > fake_next

    # Then
    mocked_execute.assert_called_once_with(context=context)

    assert result == expected


def test_autorun(fake: Faker, **kwargs) -> None:
    """Test the Autorun.

    Ensures that we can trigger the autorun function.

    """
    # Given
    context = Context(MagicMock(), MagicMock())
    fake_chain = FakeChain()
    mocked_function = MagicMock()

    fake_current_context = fake.pydict()
    context.origin = fake_chain
    context.current = fake_current_context
    fake_chain.function = mocked_function

    expected = fake.word()
    mocked_function.return_value = expected

    # When
    context._Context__autorun()

    # Then
    mocked_function.assert_called_once_with(context=fake_current_context)

    assert context.output == expected


def test_merge_context(fake: Faker, **kwargs) -> None:
    """Test the Merge Context Method.

    Ensures that we can merge the current context with a new given state.

    """
    # Given
    context = Context(MagicMock(), MagicMock())

    state = fake.pydict()
    current = fake.pydict()

    fake_state = FakeState()
    fake_current_context = FakeState()

    context.current = fake_current_context
    fake_state.__dict__ = state
    fake_current_context.__dict__ = current

    # When
    context.merge_context(fake_state)

    # Then
    assert all(s in context.current.__dict__.items() for s in state.items())
    assert all(c in context.current.__dict__.items() for c in current.items())


if __name__ == "__main__":
    args = [__file__] + [arg for arg in argv[1:]]
    main(args)
