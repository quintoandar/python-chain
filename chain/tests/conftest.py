"""Chain Fixtures.

This script will handle the creation of all Pytest fixtures of Chain's
application.

"""
from pytest import fixture
from faker import Faker


@fixture(scope="session")
def fake():
    """Build a new fake data provider.

    This fixture will build a new fake data provider using Faker lib.

    """
    fake = Faker()

    fake.add_provider("python")

    return fake
