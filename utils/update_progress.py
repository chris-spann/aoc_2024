import re
import subprocess

from models.config import Config

# Adjusted markers to match the README content
PROGRESS_TABLE_HEADER = "| Day | Part 1 | Part 2 |"
PROGRESS_TABLE_SEPARATOR = "| :----: | :----: | :----: |"
PROGRESS_TABLE_END = "---"

config = Config()


def get_git_commits():
    """Get a list of commit messages from the Git log."""
    result = subprocess.run(["git", "log", "--pretty=format:%s"], capture_output=True, text=True)
    return result.stdout.splitlines()


def get_latest_commit_message():
    """Get the latest commit message."""
    result = subprocess.run(["git", "log", "-1", "--pretty=%s"], capture_output=True, text=True)
    return result.stdout.strip()


def parse_progress_from_commits(commits):
    """Parse commits to extract progress for each day and part."""
    progress = {day: [False, False] for day in range(1, 26)}
    pattern = re.compile(r"Completed Day (\d+) Part (\d)")
    has_solved_commits = False

    for commit in commits:
        match = pattern.search(commit)
        if match:
            has_solved_commits = True
            day, part = int(match.group(1)), int(match.group(2))
            if day in progress and 1 <= part <= 2:
                progress[day][part - 1] = True

    return progress, has_solved_commits


def build_progress_table(progress):
    """Build the progress table based on solved days/parts."""
    table_rows = [PROGRESS_TABLE_HEADER, PROGRESS_TABLE_SEPARATOR]
    for day, parts in progress.items():
        solution_file = config.solutions_dir / f"day_{day}.py"
        # Only include days with an existing solution file
        if solution_file.exists():
            row = f"|   {day:2}   |   {'✅' if parts[0] else '❌'}   |   {'✅' if parts[1] else '❌'}   |"
            table_rows.append(row)
    return "\n".join(table_rows)


def update_readme(progress):
    """Update the README.md file with the current progress."""
    readme_content = config.readme.read_text()

    # Build the new progress table
    new_progress_table = build_progress_table(progress)

    # Find the start and end of the progress table
    if PROGRESS_TABLE_HEADER in readme_content and PROGRESS_TABLE_END in readme_content:
        start_idx = readme_content.index(PROGRESS_TABLE_HEADER)
        # Find the line after the PROGRESS_TABLE_END marker
        end_idx = readme_content.index(PROGRESS_TABLE_END, start_idx) + len(PROGRESS_TABLE_END)

        # Extract the unchanged parts of the README
        before_table = readme_content[:start_idx]
        after_table = readme_content[end_idx:].lstrip("\n")

        # Ensure no extra characters are lost
        updated_readme = f"{before_table}{new_progress_table}\n{after_table}"
        config.readme.write_text(updated_readme)
    else:
        print("Progress table markers not found in README.md")


def main():
    # Check the current commit message for progress
    latest_commit = get_latest_commit_message()
    solve_pattern = re.compile(r"Completed Day (\d+) Part (\d)")

    if solve_pattern.search(latest_commit):
        # Fetch all commit history for a full progress update
        commits = get_git_commits()
        progress, should_update_progress = parse_progress_from_commits(commits)

        if should_update_progress:
            update_readme(progress)
            print("README progress updated successfully.")
        else:
            print("No updates needed. No solved commits found.")
    else:
        print("Latest commit does not indicate progress. No update performed.")


if __name__ == "__main__":
    main()
