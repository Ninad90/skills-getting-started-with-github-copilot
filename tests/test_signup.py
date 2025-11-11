"""Tests for signing up for activities"""


def test_signup_for_activity_success(client, reset_activities):
    """Test successfully signing up for an activity"""
    response = client.post(
        "/activities/Chess Club/signup?email=newstudent@mergington.edu"
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Signed up" in data["message"]
    assert "newstudent@mergington.edu" in data["message"]


def test_signup_adds_participant(client, reset_activities):
    """Test that signup actually adds the participant to the list"""
    # Get initial count
    response = client.get("/activities")
    initial_count = len(response.json()["Chess Club"]["participants"])
    
    # Sign up new participant
    client.post("/activities/Chess Club/signup?email=newstudent@mergington.edu")
    
    # Check participant was added
    response = client.get("/activities")
    new_count = len(response.json()["Chess Club"]["participants"])
    assert new_count == initial_count + 1
    assert "newstudent@mergington.edu" in response.json()["Chess Club"]["participants"]


def test_signup_nonexistent_activity(client, reset_activities):
    """Test signing up for a non-existent activity returns 404"""
    response = client.post(
        "/activities/Nonexistent Club/signup?email=student@mergington.edu"
    )
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_already_signed_up(client, reset_activities):
    """Test signing up when already signed up returns 400"""
    # Try to sign up someone already in Chess Club
    response = client.post(
        "/activities/Chess Club/signup?email=michael@mergington.edu"
    )
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_multiple_activities(client, reset_activities):
    """Test signing up for multiple different activities"""
    new_email = "versatile@mergington.edu"
    
    # Sign up for Chess Club
    response1 = client.post(f"/activities/Chess Club/signup?email={new_email}")
    assert response1.status_code == 200
    
    # Sign up for Programming Class
    response2 = client.post(f"/activities/Programming Class/signup?email={new_email}")
    assert response2.status_code == 200
    
    # Verify both signups worked
    response = client.get("/activities")
    data = response.json()
    assert new_email in data["Chess Club"]["participants"]
    assert new_email in data["Programming Class"]["participants"]
