"""
cron_parser.cli
~~~~~~~~~~~~~~~~~~~

Entrypoint for defining CLI interface implemented by Typer and allowed commands.
"""

import typer

from cron_parser.cron_expression import CronExpression
from cron_parser.exceptions import InvalidCronExpression

app = typer.Typer()

@app.command()
def cron_parser(expression: str):
    """
    The parsing CLI command which takes single parameter `expression`.
    
    :param expression The cron expression followed by "command"

    Usage:
    $ cron_parser "*/15 0 1,15 * 1-5 /usr/bin/find"

    Output:
    minute        1 16 31 46
    hour          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    day of month  1 15 18 19 20
    month         1
    day of week   2 4 6
    command       /usr/bin/find

    """
    fields = expression.rsplit(" ", 1)
    if len(fields) != 2:
        raise InvalidCronExpression("Expression contains no spaces")
    cron_expression = CronExpression(fields[0], fields[1])
    cron_expression.parse().format_output()