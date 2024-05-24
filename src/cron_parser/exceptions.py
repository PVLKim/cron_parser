"""
cron_parser.exceptions
~~~~~~~~~~~~~~~~~~~

Custom exceptions
"""

class InvalidCronExpression(Exception):
    """Cron expression has invalid format"""
    pass

class InvalidCronField(Exception):
    """Cron field has non-supported characters or invalid format"""
    pass

class InvalidRange(Exception):
    """Numerical values fall outside allowed range"""
    pass