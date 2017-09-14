from logging import Filter
from pprint import pprint


class ManagementFilter(Filter):

    def filter(self, record):
        LOGS_TO_SUPPRESS = [
            'heroku',
            'whatever'
        ]
        return not any([word in record.getMessage() for word in LOGS_TO_SUPPRESS])
        """
        return not record.getMessage().contains('heroku')
        if (hasattr(record, 'funcName')
                and record.funcName == 'execute'):
            return False
        else:
            return True
        """
