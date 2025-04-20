"""Project pipelines."""

from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    return {}
