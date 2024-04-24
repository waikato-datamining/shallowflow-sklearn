# TrainSupervisedEstimator

## Name
shallowflow.sklearn.transformers.TrainSupervisedEstimator

## Synopsis
Trains the specified sklearn estimator on the incoming dataset.

## Flow input/output
input: shallowflow.sklearn.datasets.SupervisedDataset

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

* estimator (AbstractEstimatorConfiguration)

  * The estimator configuration to use
  * default: shallowflow.sklearn.estimators.GenericConfiguration

