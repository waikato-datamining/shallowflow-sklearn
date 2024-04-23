from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "shallowflow.api.actor.Actor": [
            "shallowflow.sklearn.sinks",
            "shallowflow.sklearn.sources",
            "shallowflow.sklearn.transformers",
        ],
        "shallowflow.api.container.AbstractContainer": [
            "shallowflow.sklearn.containers",
        ],
        "shallowflow.sklearn.estimators.AbstractEstimatorConfiguration": [
            "shallowflow.sklearn.estimators",
        ],
    }
