import click
from parsec.commands.jobs.get_jobs import cli as get_jobs
from parsec.commands.jobs.get_metrics import cli as get_metrics
from parsec.commands.jobs.get_state import cli as get_state
from parsec.commands.jobs.report_error import cli as report_error
from parsec.commands.jobs.rerun_job import cli as rerun_job
from parsec.commands.jobs.search_jobs import cli as search_jobs
from parsec.commands.jobs.show_job import cli as show_job


@click.group()
def cli():
    pass


cli.add_command(get_jobs)
cli.add_command(get_metrics)
cli.add_command(get_state)
cli.add_command(report_error)
cli.add_command(rerun_job)
cli.add_command(search_jobs)
cli.add_command(show_job)
