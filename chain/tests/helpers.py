"""Test Helpers.

This file contains all the helpers that are being used by multiple test files.

"""
from typing import ClassVar
from unittest.mock import DEFAULT
from chain.tests import constants


class DependencyMocker:
    def __init__(
        self,
        file_path: str,
        hash_table: dict = constants.DEPEDENCIES_HASH_TABLE,
        mocked_values=tuple(DEFAULT for _ in constants.DEPEDENCIES_HASH_TABLE),
    ) -> ClassVar:
        dependencies = zip(hash_table.get(file_path), mocked_values)

        self.file_path: file_path
        self.dependencies = tuple(dependencies)

    def to_dict(self, ignore: tuple = (None,)) -> dict:
        """Extract dependencies to a dict.

        This method will extract all the class dependencies to a dict,
        ignoring some if the user has asked us to do so.

        """
        to_mock = dict((k, v) for k, v in self.dependencies if k not in ignore)
        return to_mock


class FakeChain:
    pass


class FakeState:
    pass
