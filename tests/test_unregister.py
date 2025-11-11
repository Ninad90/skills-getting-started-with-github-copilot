"""Tests for unregistering from activities"""


def test_unregister_from_activity_success(client, reset_activities):
    """Test successfully unregistering from an activity"""
    response = client.post(
        "/activities/Chess Club/unregister?email=michael@mergington.edu"
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Unregistered" in data["message"]


def test_unregister_removes_participant(client, reset_activities):
    """Test that unregister actually removes the participant"""
    # Get initial count
    response = client.get("/activities")
    initial_count = len(response.json()["Chess Club"]["participants"])
    
    # Unregister participant
    client.post("/activities/Chess Club/unregister?email=michael@mergington.edu")
    
    # Check participant was removed
    response = client.get("/activities")
    new_count = len(response.json()["Chess Club"]["participants"])
    assert new_count == initial_count - 1
    assert "michael@mergington.edu" not in response.json()["Chess Club"]["participants"]


def test_unregister_nonexistent_activity(client, reset_activities):
    """Test unregistering from a non-existent activity returns 404"""
    response = client.post(
        "/activities/Nonexistent Club/unregister?email=student@mergington.edu"
    )
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_not_signed_up(client, reset_activities):
    """Test unregistering when not signed up returns 400"""
    response = client.post(
        "/activities/Chess Club/unregister?email=notregistered@mergington.edu"
    )
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_then_signup_again(client, reset_activities):
    """Test that a participant can sign up again after unregistering"""
    email = "changeable@mergington.edu"
    
    # Sign up
    client.post(f"/activities/Chess Club/signup?email={email}")
    response = client.get("/activities")
    assert email in response.json()["Chess Club"]["participants"]
    
    # Unregister
    client.post(f"/activities/Chess Club/unregister?email={email}")
    response = client.get("/activities")
    assert email not in response.json()["Chess Club"]["participants"]
    
    # Sign up again
    response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert response.status_code == 200
    
    # Verify re-signup worked
    response = client.get("/activities")
    assert email in response.json()["Chess Club"]["participants"]
