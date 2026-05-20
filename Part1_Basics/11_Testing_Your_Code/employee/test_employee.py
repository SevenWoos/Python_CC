from employee import Employee
import pytest

@pytest.fixture
def test_employee():
  """A employee for use in all test functions."""
  employee1 = Employee('Nathan', 'Drake', 1000)
  return employee1

def test_give_default_raise(test_employee):
  """Test that the default raise is added to the annual salary."""
  test_employee.give_raise()
  assert test_employee.annual_salary == 6000

def test_give_custom_raise(test_employee):
  """Test that the default raise is added to the annual salary."""
  test_employee.give_raise(10000)
  assert test_employee.annual_salary == 11000

