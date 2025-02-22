import click
from parsec.commands.datasets.download_dataset import cli as download_dataset
from parsec.commands.datasets.get_datasets import cli as get_datasets
from parsec.commands.datasets.show_dataset import cli as show_dataset


@click.group()
def cli():
    pass


cli.add_command(download_dataset)
cli.add_command(get_datasets)
cli.add_command(show_dataset)
