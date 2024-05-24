"""Unit tests for cron parser"""

import pytest

from cron_parser.constants import FieldName
from cron_parser.cron_expression import CronExpression
from cron_parser.cron_field import CronField
from cron_parser.exceptions import InvalidCronExpression, InvalidCronField, InvalidRange

"""Fixtures defining valid and invalid expressions"""
@pytest.fixture
def valid_cron_expression():
    return ["*/15 0 1,15 * 1-5", "/usr/bin/find"]

@pytest.fixture
def invalid_cron_expression():
    return ["*/15 0 1,15 * 1-5 extra_field", "/usr/bin/find"]


"""Tests"""
def test_cron_field_parse_any_with_step():
    field = CronField(FieldName.DAY_OF_WEEK, "*/2")
    field.parse()
    assert field.values == [1, 3, 5, 7]

def test_cron_field_parse_range():
    field = CronField(FieldName.HOUR, "1-3")
    field.parse()
    assert field.values == [1, 2, 3]

def test_cron_field_parse_list():
    field = CronField(FieldName.DAY_OF_MONTH, "1,15")
    field.parse()
    assert field.values == [1, 15]

def test_cron_field_parse_step():
    field = CronField(FieldName.MONTH, "1-6/2")
    field.parse()
    assert field.values == [1, 3, 5]

def test_cron_expression_parse_valid(valid_cron_expression):
    """Checks if cron expression contains supported number of cron fields"""
    expression = CronExpression(valid_cron_expression[0], valid_cron_expression[1])
    expression.parse()
    assert len(expression.fields) == len(FieldName)

def test_cron_expression_parse_invalid(invalid_cron_expression):
    """Raises 'InvalidCronExpression' exception"""
    expression = CronExpression(invalid_cron_expression[0], invalid_cron_expression[1])
    with pytest.raises(InvalidCronExpression):
        expression.parse()

def test_cron_field_parse_invalid():
    """Raises 'InvalidCronField' exception"""
    field = CronField(FieldName.DAY_OF_WEEK, "1-*")
    with pytest.raises(InvalidCronField):
        field.parse()

def test_cron_field_range_parse_invalid():
    """Raises 'InvalidRange' exception"""
    field = CronField(FieldName.DAY_OF_WEEK, "1-8")
    with pytest.raises(InvalidRange):
        field.parse()