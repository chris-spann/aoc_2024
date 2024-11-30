import re
import subprocess

from models.config import Config

PROGRESS_TABLE_START = "| :----: |:----:|:----: |"
PROGRESS_TABLE_END = "---"

config = Config()


def get_git_commits():
    """Get a list of commit messages from the Git log."""
    result = subprocess.run(["git", "log", "--pretty=format:%s"], capture_output=True, text=True)
    return result.stdout.splitlines()


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


def update_readme(progress):
    """Update the README.md file with the current progress."""
    readme_content = config.readme.read_text()

    # Build the new progress table
    progress_table = [PROGRESS_TABLE_START]
    for day, parts in progress.items():
        solution_file = config.solutions_dir / f"day_{day}.py"
        if solution_file.exists():
            row = f"| {day:<4} | {'✅' if parts[0] else '❌'} | {'✅' if parts[1] else '❌'} |"
            progress_table.append(row)

    # Replace the progress table in the README
    start_idx = readme_content.index(PROGRESS_TABLE_START)
    end_idx = readme_content.index(PROGRESS_TABLE_END, start_idx) + len(PROGRESS_TABLE_END)
    updated_readme = readme_content[:start_idx] + "\n".join(progress_table) + readme_content[end_idx:]

    config.readme.write_text(updated_readme)


def main():
    commits = get_git_commits()
    # only update readme if a solved commit has been found
    progress, should_update_progress = parse_progress_from_commits(commits)
    if should_update_progress:
        update_readme(progress)


if __name__ == "__main__":
    main()
