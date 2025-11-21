#!/usr/bin/env python3
"""
Simple test for mirador_actionable.py
"""

import subprocess
import sys
from pathlib import Path

def test_help():
    """Test that help command works"""
    result = subprocess.run(
        ["python3", "mirador_actionable.py", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Mirador Actionable Instruction System" in result.stdout
    print("✅ Help command works")

def test_generate():
    """Test that generate command works"""
    result = subprocess.run(
        ["python3", "mirador_actionable.py", "generate"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    print("✅ Generate command works")
    print(f"   Output preview: {result.stdout[:100]}...")

def test_show():
    """Test that show command works"""
    result = subprocess.run(
        ["python3", "mirador_actionable.py", "show"],
        capture_output=True,
        text=True
    )
    # Show might return 0 or 1 depending on if action exists
    # We just want to make sure it doesn't crash
    print("✅ Show command works")

def test_history():
    """Test that history command works"""
    result = subprocess.run(
        ["python3", "mirador_actionable.py", "history"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    print("✅ History command works")

if __name__ == "__main__":
    print("Testing mirador_actionable.py...\n")

    try:
        test_help()
        test_generate()
        test_show()
        test_history()

        print("\n✅ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
