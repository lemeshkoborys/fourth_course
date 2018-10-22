from dataclasses import dataclass

@dataclass
class ExceptionManager:

    critical_exceptions_count: int = 0
    non_critical_exceptions_count: int = 0
    """
    ExceptionManager class handles Exception type
    """

    def is_critical(self, e: Exception):
        if isinstance(e, TypeError):
            return True
        else:
            return False

    def handle_manger(self, e: Exception):
        e = self.is_critical(e)
        if e:
            self.critical_exceptions_count += 1
        else:
            self.non_critical_exceptions_count += 1
