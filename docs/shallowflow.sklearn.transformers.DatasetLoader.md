# DatasetLoader

## Name
shallowflow.sklearn.transformers.DatasetLoader

## Synopsis
Dummy, just passes through the data.

## Flow input/output
input: shallowflow.api.io.File

## Options
* debug (bool)

  * If enabled, outputs some debugging information
  * default: False

* skip (bool)

  * Whether to skip this actor during execution
  * default: False

* annotation (str)

  * For adding documentation to the actor
  * default: ''

* name (str)

  * The name to use for this actor, leave empty for class name
  * default: ''

* stop_flow_on_error (bool)

  * Whether to stop the flow in case of an error
  * default: True

* loader (AbstractDatasetLoader)

  * Loads the dataset from the incoming file
  * default: shallowflow.sklearn.transformers.datasetloaders.ArffLoader

