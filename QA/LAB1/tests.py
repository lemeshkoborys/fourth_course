import unittest
import vars
from exception_manager import ExceptionManager

class TestIsCritical(unittest.TestCase):

    def test_is_critical_true(self):
        e = TypeError()
        e_manager = ExceptionManager()
        self.assertTrue(e_manager.is_critical(e))

    def test_is_critical_false(self):
        e_manager = ExceptionManager()
        self.assertFalse(e_manager.is_critical(ConnectionError))
        self.assertFalse(e_manager.is_critical(EnvironmentError))
        self.assertFalse(e_manager.is_critical(EOFError))


class TestHandleManager(unittest.TestCase):

    def test_is_handled(self):
        e_manager = ExceptionManager()
        e = TypeError()
        e_manager.handle_manger(e)
        self.assertEqual(vars.critical_count, e_manager.critical_exceptions_count)
        self.assertEqual(vars.non_critical_count, e_manager.non_critical_exceptions_count)

    def test_not_handled(self):
        e_manager = ExceptionManager()
        e = IndentationError()
        e_manager.handle_manger(e)
        self.assertNotEqual(vars.critical_count, e_manager.critical_exceptions_count)
        self.assertNotEqual(vars.non_critical_count, e_manager.non_critical_exceptions_count)


if __name__ == '__main__':
    unittest.main()
