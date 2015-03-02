import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('jobs_search_jobs')
@options.galaxy_instance()
@click.argument("job_info", type=dict)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, job_info):
    """Return jobs for current user based payload content
    """
    return ctx.gi.jobs.search_jobs(job_info)
