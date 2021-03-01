import sys
from flask.cli import FlaskGroup
from src import create_app
from src.adapters.run_adapters import RequestAndBuild
import click

app = create_app()
cli = FlaskGroup(create_app=create_app)

days=1
limit=10

@cli.command('build_games')
@click.argument('record_start')
@click.argument('days')
@click.argument('limit')
def build_games(record_start, days, limit):
    # "2020-12-20", 1, 10
    runner = RequestAndBuild()
    runner.run(record_start, int(days), int(limit))
    print(record_start, days, limit)


if __name__ == "__main__":
    cli()