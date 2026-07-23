from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete(
        "/activities/Chess Club/participants?email=michael@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    chess_club = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in chess_club["participants"]


def test_unregister_participant_for_unknown_activity_returns_404():
    response = client.delete(
        "/activities/Unknown Activity/participants?email=student@example.com"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
