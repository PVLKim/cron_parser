"""
cron_parser.cron_expression
~~~~~~~~~~~~~~~~~~~

This module defines class representing a cron expression followed by a command.
"""

from typing import Self

from cron_parser.cron_field import CronField
from cron_parser.exceptions import InvalidCronExpression
from cron_parser.constants import FieldName

class CronExpression:
    """
    A simple cron expression class that contains a cron expression with a 
    command, list of valid cron fields and a `command` attribute. 

    :param expr:    cron expression
    :param command: command
    """

    def __init__(self, expr: str, command: str) -> None:
        self.expr: str = expr
        self.command: str = command
        self.fields: list[CronField] = []

    def parse(self) -> Self:
        """
        Parses each cron field and populates `fields` attribute with a list 
        of parsed objects.
        """
        fields = self.expr.split()
        if len(fields) != len(FieldName):
            raise InvalidCronExpression(f"Invalid number of arguments for cron expression: must be {len(FieldName)}, found {len(fields)}.")
        
        for (f_name, expr) in zip(FieldName.__members__.values(), fields):
            cron_field = CronField(f_name, expr)
            cron_field.parse()
            self.fields.append(cron_field)
        return self
        
    def format_output(self) -> None:
        """
        Prints formatted output to console, where first 14 columns represent
        field name and the remainder are space-separated valid values for 
        each cron field given its parsed expression.
        """
        for cf in self.fields:
            field_name, values = cf.name, cf.values
            field_name = field_name + (" " * (14-len(field_name)))
            values = " ".join(list(map(str, values)))
            print(field_name + values)
        print("command" + (" " * (14-len("command"))) + self.command)
