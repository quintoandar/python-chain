"""Behave Environment Configuration.

This module configures the Behave environment, setting some fixtures and also setting up
everything that must run on the test lifecycle.

"""
from behave import fixture, use_fixture
from behave.__main__ import main
from faker import Faker
from sys import argv


@fixture
def fake_data_provider(context: dict, *args, **kwargs) -> None:
    """Create a new fake data provider.

    This fixture will create a new fake data provider to be used during the test steps
    and attach it on the context.

    """
    fake = Faker()
    fake.add_provider("python")
    fake.add_provider("address")

    context.fake = fake


def before_all(context: dict) -> None:
    """Execute actions before all features.

    This lifecycle method will execute a series of actions and functions before any
    feature runs.

    """
    use_fixture(fake_data_provider, context)


if __name__ == "__main__":
    main([arg for arg in argv[1:]])
