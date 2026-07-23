import copy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_api_state():
    """Reset the in-memory FastAPI activity store before and after each test."""
    original_state = copy.deepcopy(app_module.activities)

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_state))
    yield

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_state))
