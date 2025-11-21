#!/usr/bin/env python3
"""
Simple test suite for mirador_action_prioritizer.py
"""

import subprocess
import sys
import os
from pathlib import Path

def test_help_command():
    """Test that --help works"""
    result = subprocess.run(
        [sys.executable, "mirador_action_prioritizer.py", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Help command failed: {result.stderr}"
    assert "Mirador Action Prioritization System" in result.stdout
    print("✓ Help command works")

def test_database_initialization():
    """Test that database is created properly"""
    # Import the module
    import mirador_action_prioritizer

    # Create instance (should initialize DB)
    prioritizer = mirador_action_prioritizer.MiradorActionPrioritizer()

    # Check that database file exists
    assert prioritizer.tracking_db.exists(), "Database file not created"
    print("✓ Database initialization works")

    # Check that tables exist
    import sqlite3
    conn = sqlite3.connect(prioritizer.tracking_db)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]

    assert 'action_opportunities' in tables, "action_opportunities table missing"
    assert 'daily_action_log' in tables, "daily_action_log table missing"

    conn.close()
    print("✓ Database tables created correctly")

def test_add_opportunity():
    """Test adding an opportunity"""
    import mirador_action_prioritizer

    prioritizer = mirador_action_prioritizer.MiradorActionPrioritizer()

    # Add a test opportunity
    opportunity_data = {
        'title': 'Test Opportunity',
        'description': 'Testing the system',
        'financial_impact': 5,
        'time_efficiency': 7,
        'strategic_value': 6,
        'feasibility': 8,
        'urgency': 4,
        'learning_value': 5,
        'estimated_time_minutes': 30,
        'potential_income': 100.0
    }

    opportunity_id, scores = prioritizer.add_opportunity(opportunity_data)

    assert opportunity_id is not None, "Failed to add opportunity"
    assert 'total_priority_score' in scores, "Scores missing total_priority_score"
    print(f"✓ Added opportunity with ID: {opportunity_id}, Score: {scores['total_priority_score']:.2f}")

def test_top_opportunities():
    """Test retrieving top opportunities"""
    import mirador_action_prioritizer

    prioritizer = mirador_action_prioritizer.MiradorActionPrioritizer()

    # Get top opportunities
    top = prioritizer.get_top_opportunities(limit=5)

    # Should be a list (might be empty if this is first run)
    assert isinstance(top, list), "get_top_opportunities didn't return a list"
    print(f"✓ Retrieved {len(top)} top opportunities")

def run_all_tests():
    """Run all tests"""
    print("Running mirador_action_prioritizer tests...\n")

    try:
        test_help_command()
        test_database_initialization()
        test_add_opportunity()
        test_top_opportunities()

        print("\n✓ All tests passed!")
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
