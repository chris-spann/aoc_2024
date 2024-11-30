# from unittest.mock import MagicMock, mock_open, patch

# import pytest

# from utils.config import Config
# from utils.generate_day import create_file_from_template, main, scrape_instructions


# @pytest.fixture
# def mock_config():
#     with patch("utils.generate_day.Config", autospec=True) as mock_config:
#         mock_config = Config()
#         yield mock_config

# def test_create_file_from_template(mock_config):
#     template_content = "This is a template for day_template."
#     expected_content = "This is a template for day_1."
#     with patch("builtins.open", mock_open(read_data=template_content)) as mock_file:
#         create_file_from_template(mock_config.template_solution, mock_config.solutions_dir / "day_1.py", 1)
#         mock_file.assert_called_with(mock_config.template_solution)
#         mock_file().write.assert_called_with(expected_content)

# def test_scrape_instructions_success(mock_config):
#     day = 1
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.text = '<article class="day-desc">Instructions for day 1</article>'
#     with patch("requests.get", return_value=mock_response):
#         instructions = scrape_instructions(day)
#         assert instructions == "Instructions for day 1"

# def test_scrape_instructions_failure(mock_config):
#     day = 1
#     mock_response = MagicMock()
#     mock_response.status_code = 404
#     with patch("requests.get", return_value=mock_response):
#         instructions = scrape_instructions(day)
#         assert instructions is None

# def test_main_create_files(mock_config):
#     day = 1
#     solution_file = mock_config.solutions_dir / f"day_{day}.py"
#     test_file = mock_config.tests_dir / f"test_day_{day}.py"
#     instructions_file = mock_config.instructions_dir / f"day_{day}.txt"

#     with patch("builtins.input", return_value="1"), \
#          patch("generate_day.create_file_from_template") as mock_create_file, \
#          patch("generate_day.scrape_instructions", return_value="Instructions for day 1"), \
#          patch("builtins.open", mock_open()) as mock_file, \
#          patch("pathlib.Path.exists", return_value=False), \
#          patch("pathlib.Path.mkdir") as mock_mkdir:

#         main()

#         mock_create_file.assert_any_call(mock_config.template_solution, solution_file, day)
#         mock_create_file.assert_any_call(mock_config.template_test, test_file, day)
#         mock_mkdir.assert_called_with(parents=True, exist_ok=True)
#         mock_file().write.assert_called_with("Instructions for day 1")

# def test_main_files_exist(mock_config):
#     day = 1
#     with patch("builtins.input", return_value="1"), \
#          patch("pathlib.Path.exists", return_value=True), \
#          patch("generate_day.create_file_from_template") as mock_create_file, \
#          patch("generate_day.scrape_instructions") as mock_scrape_instructions:

#         main()

#         mock_create_file.assert_not_called()
#         mock_scrape_instructions.assert_not_called()
