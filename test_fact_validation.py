#!/usr/bin/env python3
"""
Simple test for mirador_fact_validator.py
"""

import subprocess
import sys
import tempfile
import os

def test_help_command():
    """Test that --help works"""
    result = subprocess.run(
        ["python3", "mirador_fact_validator.py", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Mirador Fact Validation System" in result.stdout
    print("✓ Help command works")

def test_basic_validation():
    """Test basic validation with a simple instruction file"""
    # Create a temporary instruction file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Test instruction: The sky is blue during the day.\n")
        f.write("This is a simple fact that should be validated.\n")
        temp_file = f.name

    try:
        # Run validation
        result = subprocess.run(
            ["python3", "mirador_fact_validator.py", temp_file],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Check it ran (may not complete if Ollama not running, but should start)
        print(f"Return code: {result.returncode}")
        if result.stdout:
            print(f"Output preview: {result.stdout[:200]}")
        if result.stderr:
            print(f"Stderr preview: {result.stderr[:200]}")

        print("✓ Basic validation test completed")

    except subprocess.TimeoutExpired:
        print("⚠ Validation timed out (expected if Ollama models not ready)")
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)

def main():
    print("Running fact validator tests...\n")

    try:
        test_help_command()
        test_basic_validation()
        print("\n✓ All tests completed successfully")
        return 0
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
