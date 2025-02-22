datasets
========

This section is auto-generated from the help text for the parsec command
``datasets``.


``download_dataset`` command
----------------------------

**Usage**::

    parsec datasets download_dataset [OPTIONS] DATASET_ID

**Help**

Download a dataset to file or in memory. If the dataset state is not 'ok', a ``DatasetStateException`` will be thrown, unless ``require_ok_state=False``.


**Output**


    If a ``file_path`` argument is not provided, returns a dict containing the file content.
            Otherwise returns nothing.
    
**Options**::


      --file_path TEXT        If this argument is provided, the dataset will be
                              streamed to disk at that path (should be a directory
                              if ``use_default_filename=True``). If the file_path
                              argument is not provided, the dataset content is
                              loaded into memory and returned by the method (Memory
                              consumption may be heavy as the entire file will be in
                              memory).
    
      --use_default_filename  If ``True``, the exported file will be saved as
                              ``file_path/%s``, where ``%s`` is the dataset name. If
                              ``False``, ``file_path`` is assumed to contain the
                              full file path including the filename.  [default:
                              True]
    
      --require_ok_state      If ``False``, datasets will be downloaded even if not
                              in an 'ok' state, issuing a ``DatasetStateWarning``
                              rather than raising a ``DatasetStateException``.
                              [default: True]
    
      --maxwait FLOAT         Total time (in seconds) to wait for the dataset state
                              to become terminal. If the dataset state is not
                              terminal within this time, a
                              ``DatasetTimeoutException`` will be thrown.  [default:
                              12000]
    
      -h, --help              Show this message and exit.
    

``get_datasets`` command
------------------------

**Usage**::

    parsec datasets get_datasets [OPTIONS]

**Help**

Provide a list of all datasets. Since this may be very large, ``limit`` and ``offset`` parameters should be used to specify the desired range.


**Output**


    Return a list of dataset dicts.
    
**Options**::


      --limit INTEGER   Maximum number of datasets to return.  [default: 500]
      --offset INTEGER  Return datasets starting from this specified position. For
                        example, if ``limit`` is set to 100 and ``offset`` to 200,
                        datasets 200-299 will be returned.
    
      -h, --help        Show this message and exit.
    

``show_dataset`` command
------------------------

**Usage**::

    parsec datasets show_dataset [OPTIONS] DATASET_ID

**Help**

Get details about a given dataset. This can be a history or a library dataset.


**Output**


    Information about the HDA or LDDA
    
**Options**::


      --deleted        Whether to return results for a deleted dataset
      --hda_ldda TEXT  Whether to show a history dataset ('hda' - the default) or
                       library dataset ('ldda').  [default: hda]
    
      -h, --help       Show this message and exit.
    
