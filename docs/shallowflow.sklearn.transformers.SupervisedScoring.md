# SupervisedScoring

## Name
shallowflow.sklearn.transformers.SupervisedScoring

## Synopsis
Applies the supervised estimator from storage to the incoming dataset.

## Flow input/output
input: shallowflow.sklearn.datasets.Dataset

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

* storage_name (StorageName)

  * The name of the storage item that represents the estimator or estimator container
  * default: 'storage'

* predictions (bool)

  * Whether to generate predictions
  * default: True

* probabilities (bool)

  * Whether to generate probabilities
  * default: False

