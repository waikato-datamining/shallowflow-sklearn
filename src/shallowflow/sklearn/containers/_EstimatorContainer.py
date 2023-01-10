from shallowflow.api.container import AbstractContainer
from shallowflow.sklearn.datasets import Dataset
from sklearn.base import BaseEstimator


class EstimatorContainer(AbstractContainer):
    VALUE_ESTIMATOR = "estimator"

    VALUE_DATASET = "dataset"

    def __init__(self, estimator, dataset=None):
        """
        Initializes the container.

        :param estimator: the estimator to store
        :type estimator: BaseEstimator
        :param dataset: the training data
        """
        super().__init__()
        self.set(self.VALUE_ESTIMATOR, estimator)
        self.set(self.VALUE_DATASET, dataset)

    def _init_help(self):
        """
        Populates the help strings for the values.
        """
        super()._init_help()
        self._add_help(self.VALUE_ESTIMATOR, "The estimator object", cls=BaseEstimator)
        self._add_help(self.VALUE_DATASET, "The (optional) training data", cls=Dataset)

    def names(self):
        """
        Returns the names of the values that can be stored.

        :return: the list of names
        :rtype: list
        """
        return [self.VALUE_ESTIMATOR, self.VALUE_DATASET]
