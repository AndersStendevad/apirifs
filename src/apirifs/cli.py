"""apirifs CLI"""


import click
from apirifs import __version__ as VERSION


@click.command()
@click.option("--version", is_flag=True, help="Shows the version of apirifs")
def apirifs(version):
    """The main way to engange with apirifs is with this cli"""
    if version:
        click.echo(f"{VERSION}")
