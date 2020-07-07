from cmd_arguments_const import CLIArgumentsConst

SUPPORTED_COMMANDS = {'-p': CLIArgumentsConst.PRECISION,
                      '-t': CLIArgumentsConst.NUM_OF_PROCESSORS,
                      '-o': CLIArgumentsConst.RESULT_FILE,
                      '-q': CLIArgumentsConst.QUIET_OUTPUT,
                      '-g': CLIArgumentsConst.GRANULARITY}


def get_commands_arguments_dict(argv):
    commands = {}
    for idx, arg in enumerate(argv):
        if arg in SUPPORTED_COMMANDS:
            try:
                commands[SUPPORTED_COMMANDS[arg]] = argv[idx + 1]
            except IndexError as _:
                raise IndexError('Supplied argument has no value provided!')
    return commands