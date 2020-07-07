import unittest

from cmd_arguments_const import CLIArgumentsConst
from general_utils import get_commands_arguments_dict


class GeneralUtilsTest(unittest.TestCase):

    def test_get_commands_arguments_dict_when_valid_cmd_commands_are_passed(self):
        passed_commands = ['some_program.py', '-t', '200', '-p', '10', '-g', '10']
        parsed_commands = get_commands_arguments_dict(passed_commands)
        expected = {CLIArgumentsConst.NUM_OF_PROCESSORS: '200',
                    CLIArgumentsConst.PRECISION: '10',
                    CLIArgumentsConst.GRANULARITY: '10'}
        self.assertEqual(parsed_commands, expected)

    def test_get_commands_arguments_dict_when_INVALID_cmd_commands_are_passed(self):
        passed_commands = ['some_program.py', '-fake', '200', 'another_fake']
        parsed_commands = get_commands_arguments_dict(passed_commands)
        expected = {}
        self.assertEqual(parsed_commands, expected)

    def test_get_commands_arguments_dict_when_argument_without_value_is_passed(self):
        passed_commands = ['some_program.py', '-p']
        self.assertRaises(IndexError, get_commands_arguments_dict, passed_commands)