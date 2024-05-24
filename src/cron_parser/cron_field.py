"""
cron_parser.cron_field
~~~~~~~~~~~~~~~~~~~

This module defines class representing a valid cron field and corresponding access and parsing methods.
"""

from cron_parser.exceptions import InvalidCronField, InvalidRange
from cron_parser.constants import FIELD_RANGES, FieldName


class CronField:
    """
    A cron time field class. 

    Used to store data about the cron field, implement `parse()` method to
    produce the list of valid time values given the allowed range. 

    :param name: The field name representing time field. In standard cron
        expression format has 5 fields: minute, hour, day of month, month and
        day of week
    :param expr: Expression of the field. Can currently contain 4 special
        characters (,-*/) and can contain any number of sub-expressions
        separated by commas.
    """
    def __init__(self, name: FieldName, expr: str) -> None:
        self._name: FieldName = name
        self._expr: str = expr
        self._values: list[int] = [] # populated by calling `parse()` method

    def parse(self) -> None:
        values = set()
        lower, upper = FIELD_RANGES[self._name][0], FIELD_RANGES[self._name][1]
        expressions = self._expr.split(",")
        """
        Produces valid values given the cron field expression and allowed 
        range for the field type. 
        """

        for e in expressions:
            step = 1
            if e == "":
                raise InvalidCronField(f"Empty expression for field {self._name}")
            
            if e == "*":
                values.update(list(range(lower, upper)))
                continue
            elif e.isdigit():
                if lower <= int(e) < upper:
                    values.update([int(e)])
                    continue
                else:
                    raise InvalidRange(f"Number outside allowed range for field {self._name}: {e}")

            if "/" in e:
                tokens = e.split("/")

                if len(tokens) > 2:
                    raise InvalidCronField(f"Multiple '/' operators are not allowed, found {len(tokens)} for field {self._name}.")
                if not tokens[1].isdigit() or int(tokens[1]) < 1:
                    raise InvalidCronField(f"Step value for field {self._name} has invalid format: {tokens[1]}")
                
                step = int(tokens[1])
                e = tokens[0]

            if "-" in e:
                tokens = e.split("-")
                if len(tokens) > 2:
                    raise InvalidCronField(f"Multiple '-' operators are not allowed, found {len(tokens)} for field {self._name}.")
                try:
                    start, end = int(tokens[0]), int(tokens[1])
                except ValueError:
                    raise InvalidCronField(f"Range boundaries for field {self._name} are not numbers: {tokens}")
                if not (lower <= start < upper) or not (lower <= end < upper) or start > end:
                    raise InvalidRange(f"Range boundaries for field {self._name} fall outside of range {lower}-{upper-1}, found {start}-{end}.")
                
                result = [x for x in range(start, end+1, step)]
            else:
                if e == "*":
                    result = [x for x in range(lower, upper, step)]
                elif e.isdigit() and lower <= int(e) < upper:
                    result = [x for x in range(int(e), upper, step)]
                else:
                    raise InvalidCronField(f"Invalid character or value outside range for field {self._name}: {e}")
            values.update(result)
        self._values = sorted(list(values))
    
    
    @property
    def name(self) -> FieldName:
        """Read method for the cron field name."""
        return self._name
    
    @property
    def values(self) -> list[int]:
        """Read method for the values produced from parsed cron field."""
        return self._values
    

    

