import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_activities_state():
    original_state = copy.deepcopy(activities)

    # Arrange: start each test from the same in-memory dataset.
    activities.clear()
    activities.update(copy.deepcopy(original_state))

    yield

    activities.clear()
    activities.update(copy.deepcopy(original_state))
