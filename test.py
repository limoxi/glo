# coding: utf8
import sys
from pprint import pprint

from click.testing import CliRunner
from glo.core.cli import add

from glo.core.helper import get_plural_for_word


def main():
    runner = CliRunner()
    f = sys.argv[1]
    if f == 'add':
        resource_name = sys.argv[2]
        result = runner.invoke(add, [resource_name])
        pprint(result)
        assert result.exit_code == 0
    elif f == 'plural':
        letter = sys.argv[2]
        plural_letter = get_plural_for_word(letter)
        print(plural_letter)

if __name__ == '__main__':
    main()