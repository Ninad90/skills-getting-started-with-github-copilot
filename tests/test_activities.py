"""Tests for getting activities"""
import pytest


def test_get_activities(client, reset_activities):
    """Test retrieving all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert len(data) == 9  # Should have 9 activities


def test_get_activities_contains_required_fields(client, reset_activities):
    """Test that activities have all required fields"""
    response = client.get("/activities")
    data = response.json()
    
    for activity_name, activity_details in data.items():
        assert "description" in activity_details
        assert "schedule" in activity_details
        assert "max_participants" in activity_details
        assert "participants" in activity_details
        assert isinstance(activity_details["participants"], list)


def test_get_activities_contains_initial_participants(client, reset_activities):
    """Test that activities have initial participants"""
    response = client.get("/activities")
    data = response.json()
    
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
    assert "emma@mergington.edu" in data["Programming Class"]["participants"]
