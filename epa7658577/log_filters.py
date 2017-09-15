from logging import Filter
from pprint import pprint


class ManagementFilter(Filter):

    def filter(self, record):
        # 9/15/17 this seems to be working on localhost
        if "heroku" in record.getMessage():
          return False
        return True 

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
