import logging

from prettytable import PrettyTable

logger = logging.getLogger()


def print_table(header, *rows):
    table = PrettyTable(header)
    for row in rows:
        table.add_row(row)
    for line in table.__unicode__().split('\n'):
        logger.info(line)
