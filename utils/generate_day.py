import requests
from bs4 import BeautifulSoup
from models.config import Config

config = Config()


def create_file_from_template(template_path, new_file_path, day):
    with open(template_path) as template_file:
        content = template_file.read()
    content = content.replace("template", f"day_{day}").replace("solution_", "")
    with open(new_file_path, "w") as new_file:
        new_file.write(content)


def scrape_instructions(day):
    url = f"https://adventofcode.com/2024/day/{day}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article", class_="day-desc")
        if article:
            return article.text
    return None


def main():
    day = input("Enter the puzzle day (X, integer): ")
    try:
        day = int(day)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    solution_file = config.solutions_dir / f"day_{day}.py"
    test_file = config.tests_dir / f"solutions/test_day_{day}.py"
    instructions_file = config.instructions_dir / f"day_{day}.txt"

    if not solution_file.exists():
        create_file_from_template(config.template_solution, solution_file, day)
        print(f"Created {solution_file}")
    else:
        print(f"{solution_file} already exists.")

    if not test_file.exists():
        create_file_from_template(config.template_test, test_file, day)
        print(f"Created {test_file}")
    else:
        print(f"{test_file} already exists.")

    if not instructions_file.exists():
        instructions = scrape_instructions(day)
        if instructions:
            config.instructions_dir.mkdir(parents=True, exist_ok=True)
            with open(instructions_file, "w") as f:
                f.write(instructions)
            print(f"Scraped and saved instructions to {instructions_file}")
        else:
            print(f"Failed to scrape instructions for day {day}.")
    else:
        print(f"{instructions_file} already exists.")


if __name__ == "__main__":
    main()
