import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_categories')
@click.option(
    "--deleted",
    help="whether to show deleted categories",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, deleted=False):
    """Returns a list of dictionaries that contain descriptions of the repository categories found on the given Tool Shed instance.

Output:

    A list of dictionaries containing information about
          repository categories present in the Tool Shed.
          For example::

            [{'deleted': False,
              'description': 'Tools for manipulating data',
              'id': '175812cd7caaf439',
              'model_class': 'Category',
              'name': 'Text Manipulation',
              'url': '/api/categories/175812cd7caaf439'}]

        .. versionadded:: 0.5.2
    """
    return ctx.gi.categories.get_categories(deleted=deleted)
