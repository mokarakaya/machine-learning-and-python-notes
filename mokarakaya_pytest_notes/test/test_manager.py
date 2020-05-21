import mock
import pytest
from pytest_mock import mocker
from mokarakaya_pytest_notes.source import manager



def test_update_jobs_fleet_capacity(mocker):
  mocker.patch.object(manager, 'sub_method')
  manager.sub_method.return_value = 120
  result = manager.method_under_test()
  manager.sub_method.assert_called_with('somestring', 1, 120)
  assert result == 121