import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app, activities


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team practicing drills and games",
            "schedule": "Mondays, Wednesdays, 4:00 PM - 6:00 PM",
            "max_participants": 15,
            "participants": ["tyler@mergington.edu", "nina@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Laps, stroke improvement, and swim meets",
            "schedule": "Tuesdays and Thursdays, 5:00 PM - 6:30 PM",
            "max_participants": 20,
            "participants": ["liam@mergington.edu", "ava@mergington.edu"]
        },
        "Art Club": {
            "description": "Drawing, painting, and mixed-media workshops",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu", "jack@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting, stagecraft, and production for school plays",
            "schedule": "Fridays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["lucy@mergington.edu", "sam@mergington.edu"]
        },
        "Debate Team": {
            "description": "Competitive debating, research, and public speaking",
            "schedule": "Tuesdays, Thursdays, 4:30 PM - 6:00 PM",
            "max_participants": 16,
            "participants": ["oliver@mergington.edu", "mia@mergington.edu"]
        },
        "Robotics Club": {
            "description": "Design, build, and program robots for competitions",
            "schedule": "Mondays and Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 12,
            "participants": ["ethan@mergington.edu", "grace@mergington.edu"]
        }
    }
    
    yield
    
    # Reset activities after test
    activities.clear()
    activities.update(original_activities)
