"""
cron_parser.constants
~~~~~~~~~~~~~~~~~~~

Represent valid cron field types and corresponding allowed value ranges for each.
"""

from enum import StrEnum, unique

@unique
class FieldName(StrEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY_OF_MONTH = "day of month"
    MONTH = "month"
    DAY_OF_WEEK = "day of week"

# Each field range is lower-bound-inclusive and upper-bound-exclusive.
FIELD_RANGES = {
    FieldName.MINUTE: (0, 60),
    FieldName.HOUR: (0, 24),
    FieldName.DAY_OF_MONTH: (1, 32),
    FieldName.MONTH: (1, 13),
    FieldName.DAY_OF_WEEK: (1, 8),
}
