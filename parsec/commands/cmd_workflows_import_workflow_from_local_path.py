import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_import_workflow_from_local_path')
@options.galaxy_instance()
@click.argument("file_local_path", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, file_local_path):
    """Imports a new workflow given the path to a file containing a previously exported workflow.
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path)
