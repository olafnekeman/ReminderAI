"""Dashboard Streamlit application."""


def main() -> None:
    """Entry point for the dashboard CLI."""
    import subprocess
    import sys
    from pathlib import Path

    # Get the path to the app.py file
    app_path = Path(__file__).parent / "main.py"

    # Build the command with the app path and any additional arguments
    # sys.argv[1:] contains all arguments passed after the command name
    cmd = ["streamlit", "run", str(app_path), *sys.argv[1:]]

    # Run streamlit with the app.py file and forwarded arguments
    sys.exit(subprocess.call(cmd))


def dev() -> None:
    """Run development server with hot reload."""
    main()
