import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('invoke_workflow')
@click.argument("workflow_id", type=str)
@click.option(
    "--inputs",
    help="A mapping of workflow inputs to datasets and dataset collections. The datasets source can be a LibraryDatasetDatasetAssociation (``ldda``), LibraryDataset (``ld``), HistoryDatasetAssociation (``hda``), or HistoryDatasetCollectionAssociation (``hdca``).",
    type=str
)
@click.option(
    "--params",
    help="A mapping of non-datasets tool parameters (see below)",
    type=str
)
@click.option(
    "--history_id",
    help="The encoded history ID where to store the workflow output. Alternatively, ``history_name`` may be specified to create a new history.",
    type=str
)
@click.option(
    "--history_name",
    help="Create a new history with the given name to store the workflow output. If both ``history_id`` and ``history_name`` are provided, ``history_name`` is ignored. If neither is specified, a new 'Unnamed history' is created.",
    type=str
)
@click.option(
    "--import_inputs_to_history",
    help="If ``True``, used workflow inputs will be imported into the history. If ``False``, only workflow outputs will be visible in the given history.",
    is_flag=True
)
@click.option(
    "--replacement_params",
    help="pattern-based replacements for post-job actions (see below)",
    type=str
)
@click.option(
    "--allow_tool_state_corrections",
    help="If True, allow Galaxy to fill in missing tool state when running workflows. This may be useful for workflows using tools that have changed over time or for workflows built outside of Galaxy with only a subset of inputs defined.",
    is_flag=True
)
@click.option(
    "--inputs_by",
    help="Determines how inputs are referenced. Can be \"step_index|step_uuid\" (default), \"step_index\", \"step_id\", \"step_uuid\", or \"name\".",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id, inputs="", params="", history_id="", history_name="", import_inputs_to_history=False, replacement_params="", allow_tool_state_corrections="", inputs_by=""):
    """Invoke the workflow identified by ``workflow_id``. This will cause a workflow to be scheduled and return an object describing the workflow invocation.

Output:

    A dict containing the workflow invocation describing the
          scheduling of the workflow. For example::

            {'history_id': '2f94e8ae9edff68a',
             'id': 'df7a1f0c02a5b08e',
             'inputs': {'0': {'id': 'a7db2fac67043c7e',
                              'src': 'hda',
                              'uuid': '7932ffe0-2340-4952-8857-dbaa50f1f46a'}},
             'model_class': 'WorkflowInvocation',
             'state': 'ready',
             'steps': [{'action': None,
                        'id': 'd413a19dec13d11e',
                        'job_id': None,
                        'model_class': 'WorkflowInvocationStep',
                        'order_index': 0,
                        'state': None,
                        'update_time': '2015-10-31T22:00:26',
                        'workflow_step_id': 'cbbbf59e8f08c98c',
                        'workflow_step_label': None,
                        'workflow_step_uuid': 'b81250fd-3278-4e6a-b269-56a1f01ef485'},
                       {'action': None,
                        'id': '2f94e8ae9edff68a',
                        'job_id': 'e89067bb68bee7a0',
                        'model_class': 'WorkflowInvocationStep',
                        'order_index': 1,
                        'state': 'new',
                        'update_time': '2015-10-31T22:00:26',
                        'workflow_step_id': '964b37715ec9bd22',
                        'workflow_step_label': None,
                        'workflow_step_uuid': 'e62440b8-e911-408b-b124-e05435d3125e'}],
             'update_time': '2015-10-31T22:00:26',
             'uuid': 'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
             'workflow_id': '03501d7626bd192f'}

        The ``params`` dict should be specified as follows::

          {STEP_ID: PARAM_DICT, ...}

        where PARAM_DICT is::

          {PARAM_NAME: VALUE, ...}

        For backwards compatibility, the following (deprecated) format is
        also supported for ``params``::

          {TOOL_ID: PARAM_DICT, ...}

        in which case PARAM_DICT affects all steps with the given tool id.
        If both by-tool-id and by-step-id specifications are used, the
        latter takes precedence.

        Finally (again, for backwards compatibility), PARAM_DICT can also
        be specified as::

          {'param': PARAM_NAME, 'value': VALUE}

        Note that this format allows only one parameter to be set per step.

        For a ``repeat`` parameter, the names of the contained parameters needs
        to be specified as ``<repeat name>_<repeat index>|<param name>``, with
        the repeat index starting at 0. For example, if the tool XML contains::

          <repeat name="cutoff" title="Parameters used to filter cells" min="1">
              <param name="name" type="text" value="n_genes" label="Name of param...">
                  <option value="n_genes">n_genes</option>
                  <option value="n_counts">n_counts</option>
              </param>
              <param name="min" type="float" min="0" value="0" label="Min value"/>
          </repeat>

        then the PARAM_DICT should be something like::

          {...
           "cutoff_0|name": "n_genes",
           "cutoff_0|min": "2",
           "cutoff_1|name": "n_counts",
           "cutoff_1|min": "4",
           ...}

        At the time of this writing, it is not possible to change the number of
        times the contained parameters are repeated. Therefore, the parameter
        indexes can go from 0 to n-1, where n is the number of times the
        repeated element was added when the workflow was saved in the Galaxy UI.

        The ``replacement_params`` dict should map parameter names in
        post-job actions (PJAs) to their runtime values. For
        instance, if the final step has a PJA like the following::

          {'RenameDatasetActionout_file1': {'action_arguments': {'newname': '${output}'},
                                            'action_type': 'RenameDatasetAction',
                                            'output_name': 'out_file1'}}

        then the following renames the output dataset to 'foo'::

          replacement_params = {'output': 'foo'}

        see also `this email thread
        <http://lists.bx.psu.edu/pipermail/galaxy-dev/2011-September/006875.html>`_.

        .. warning::
          Historically, the ``run_workflow`` method consumed a ``dataset_map``
          data structure that was indexed by unencoded workflow step IDs. These
          IDs would not be stable across Galaxy instances. The new ``inputs``
          property is instead indexed by either the ``order_index`` property
          (which is stable across workflow imports) or the step UUID which is
          also stable.
    """
    return ctx.gi.workflows.invoke_workflow(workflow_id, inputs=inputs, params=params, history_id=history_id, history_name=history_name, import_inputs_to_history=import_inputs_to_history, replacement_params=replacement_params, allow_tool_state_corrections=allow_tool_state_corrections, inputs_by=inputs_by)
