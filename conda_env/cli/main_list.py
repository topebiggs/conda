from argparse import RawDescriptionHelpFormatter

from conda.cli import common
from conda.cli.conda_argparse import add_parser_json

description = """
List the Conda environments
"""

example = """
examples:
    conda env list
    conda env list --json
"""


def configure_parser(sub_parsers):
    list_parser = sub_parsers.add_parser(
        'list',
        formatter_class=RawDescriptionHelpFormatter,
        description=description,
        help=description,
        epilog=example,
    )

    add_parser_json(list_parser)

    list_parser.set_defaults(func=execute)


def execute(args, parser):
    info_dict = {'envs': []}
    common.handle_envs_list(info_dict['envs'], not args.json)

    if args.json:
        common.stdout_json(info_dict)
