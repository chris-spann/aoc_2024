import re
import subprocess
import sys
from pathlib import Path


# Assuming 'config.readme' is the path to the README.md
class Config:
    readme = Path("README.md")  # Adjust the path to your README file


config = Config()


# Step 1: Get the current commit message
def get_commit_message():
    """Get the current commit message."""
    result = subprocess.run(["git", "log", "-1", "--pretty=%B"], capture_output=True, text=True)
    return result.stdout.strip()


# Step 2: Parse commits to extract progress for each day and part
def parse_progress_from_commit(commit_message):
    """Parse a single commit message to extract progress."""
    progress = {day: [False, False] for day in range(1, 26)}  # Initialize progress as not done (False)
    pattern = re.compile(r"Completed Day (\d+) Part (\d)")

    match = pattern.search(commit_message)
    if match:
        day, part = int(match.group(1)), int(match.group(2))
        if day in progress and 1 <= part <= 2:
            progress[day][part - 1] = True  # Mark the part as completed

    return progress


# Step 3: Build the updated progress table
def build_progress_table(progress):
    """Build the new progress table based on the current progress."""
    progress_table = ["| Day | Part 1 | Part 2 |", "| :----: | :----: | :----: |"]
    for day, parts in progress.items():
        part1 = "✅" if parts[0] else "❌"
        part2 = "✅" if parts[1] else "❌"
        progress_table.append(f"| {day} | {part1} | {part2} |")
    return "\n".join(progress_table)


# Step 4: Update the README.md file with the new progress table
def update_readme(progress):
    """Update the README.md file with the current progress."""
    readme_content = config.readme.read_text()

    # Build the new progress table
    new_progress_table = build_progress_table(progress)

    # Use a regex to find and replace the progress table
    table_pattern = re.compile(
        r"(<!-- START PROGRESS TABLE -->)(.*?)(<!-- END PROGRESS TABLE -->)", re.DOTALL
    )

    # Check if the progress table markers exist
    if table_pattern.search(readme_content):
        # Replace the existing progress table with the new one
        updated_readme = table_pattern.sub(
            r"\1\n" + new_progress_table + r"\3",  # keep the markers intact
            readme_content,
        )
        # Write the updated README back
        config.readme.write_text(updated_readme)
        print("README updated with progress.")
    else:
        print("Progress table markers not found in README.md")
        # Optionally, handle the case where the table is missing
        # You can add an error message or even insert the markers automatically


# Main function that runs everything
def main():
    commit_message = get_commit_message()  # Get the current commit message

    # Check if the commit message matches the solved pattern
    if "Completed Day" in commit_message:
        print(f"Commit message detected: {commit_message}")

        # Parse the commit message and update the progress table
        progress = parse_progress_from_commit(commit_message)
        update_readme(progress)  # Update the README file with the new progress

        # Exit successfully
        sys.exit(0)  # Pre-commit hook passes

    else:
        print("No progress found in commit message, skipping README update.")
        sys.exit(0)  # Pre-commit hook passes


# Run the script
if __name__ == "__main__":
    main()
