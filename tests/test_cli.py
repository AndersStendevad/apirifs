from apirifs import __version__ as VERSION
from apirifs.cli import apirifs


def test_apirifs(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(apirifs, ["--version"])
        assert not result.exception
        assert result.output == f"{VERSION}\n"
