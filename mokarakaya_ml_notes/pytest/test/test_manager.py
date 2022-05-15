"""
pytest and pytest_mock examples.

gets mocker from;
from pytest_mock import mocker
"""

from mokarakaya_ml_notes.pytest.source import manager
import pytest


@pytest.fixture()
def my_manager(mocker):
    my_manager = manager.Manager(10)
    mocker.patch.object(my_manager, "get_test_value")
    my_manager.get_test_value.return_value = 15
    return my_manager


def test_update_jobs_fleet_capacity(mocker):
    mocker.patch.object(manager, "sub_method")
    manager.sub_method.return_value = 120
    result = manager.method_under_test()
    manager.sub_method.assert_called_with("somestring", 1, 120)
    assert result == 121


@pytest.mark.parametrize("var1, var2, expect", [(1, 2, 3), (4, 5, 9)])
def test_add(mocker, var1, var2, expect):
    print("running for:", var1, var2, expect)
    assert manager.add(var1, var2) == expect


def test_failure():
    with pytest.raises(ValueError):
        manager.failure()


def test_call_with_mock(my_manager):
    value = manager.add_to_manager(my_manager)
    assert value == 16
