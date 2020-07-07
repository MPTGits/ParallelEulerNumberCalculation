import time
from cmd_arguments_const import CLIArgumentsConst, DefaultArgumentsValuesConst


class ArgumentParser:

    def __init__(self, **kwargs):
        self.num_processors = int(kwargs.get(CLIArgumentsConst.NUM_OF_PROCESSORS, DefaultArgumentsValuesConst.PROCESSORS))
        self.precision = int(kwargs.get(CLIArgumentsConst.PRECISION, DefaultArgumentsValuesConst.PRECISION))
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        default_output_file = "{output_file}_{timestamp}.txt".format(
            output_file=DefaultArgumentsValuesConst.OUTPUT_FILE_NAME,
            timestamp=timestamp)
        self.save_to_file = kwargs.get(CLIArgumentsConst.RESULT_FILE, default_output_file)
        self.granularity = int(kwargs.get(CLIArgumentsConst.GRANULARITY, DefaultArgumentsValuesConst.GRANULARITY))
        self.quiet_output = True if CLIArgumentsConst.QUIET_OUTPUT in kwargs else False

    def __repr__(self):
        return f"""
        Number of processors:{self.num_processors}
        Precision:{self.precision}
        File to save to:{self.save_to_file}
        Granularity is: {self.granularity}
        Is quiet mode:{self.quiet_output}
        """

    def __eq__(self, other):
        return self.quiet_output == other.quiet_output \
                and self.save_to_file == other.save_to_file \
                and self.precision == other.precision \
                and self.num_processors == other.num_processors \
                and self.granularity == other.granularity

    def __ne__(self, other):
        return not self.__eq__(other)
