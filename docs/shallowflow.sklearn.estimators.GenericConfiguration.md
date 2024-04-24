# GenericConfiguration

## Name
shallowflow.sklearn.estimators.GenericConfiguration

## Synopsis
Generic estimator configuration, using classname and options for constructor.

## Options
* debug (bool)

  * If enabled, outputs some debugging information
  * default: False

* class_name (str)

  * The class name of the estimator to instantiate.
  * default: 'sklearn.ensemble.RandomForestClassifier'

* options (dict)

  * The dictionary to supply to the constructor of the estimator.
  * default: {}

