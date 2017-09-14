from logging import Filter
from pprint import pprint


class ManagementFilter(Filter):

    def filter(self, record):
        if "heroku" in record.getMessage():
          return True
        return False

        """
        LOGS_TO_SUPPRESS = [
            'heroku',
            'whatever'
        ]
        return not any([word in record.getMessage() for word in LOGS_TO_SUPPRESS])
        if (hasattr(record, 'funcName')
                and record.funcName == 'execute'):
            return False
        else:
            return True
        """
