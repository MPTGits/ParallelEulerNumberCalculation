from unittest import TestCase
from unittest.mock import patch

from argument_parser import ArgumentParser, time
from cmd_arguments_const import DefaultArgumentsValuesConst, CLIArgumentsConst


class ArgumentParserTest(TestCase):

    @patch.object(time, 'strftime')
    def test_default_arguments(self, time_mock):
        time_mock.return_value = '20201012-010243'
        args = ArgumentParser()
        expected_file_name = "{output_file}_{timestamp}.txt".format(
            output_file=DefaultArgumentsValuesConst.OUTPUT_FILE_NAME,
            timestamp=time.strftime("%Y%m%d-%H%M%S"))
        self.assertEqual(args.save_to_file, expected_file_name)
        self.assertEqual(args.num_processors, DefaultArgumentsValuesConst.PROCESSORS)
        self.assertEqual(args.precision, DefaultArgumentsValuesConst.PRECISION)
        self.assertEqual(args.granularity, DefaultArgumentsValuesConst.GRANULARITY)
        self.assertEqual(args.quiet_output, False)

    def test_when_arguments_are_passed(self):
        values = {
            CLIArgumentsConst.PRECISION: "99",
            CLIArgumentsConst.NUM_OF_PROCESSORS: "8",
            CLIArgumentsConst.RESULT_FILE: "test_file",
            CLIArgumentsConst.QUIET_OUTPUT: '',
            CLIArgumentsConst.GRANULARITY: 10
        }
        args = ArgumentParser(**values)
        self.assertEqual(args.save_to_file, values[CLIArgumentsConst.RESULT_FILE])
        self.assertEqual(args.num_processors, 8)
        self.assertEqual(args.precision, 99)
        self.assertEqual(args.granularity, 10)
        self.assertEqual(args.quiet_output, True)
