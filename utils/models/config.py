from pathlib import Path

from pydantic import BaseModel, Field


class Config(BaseModel):
    """
    Model for path pattern in automation scripts.
    """

    base_dir: Path = Field(default_factory=lambda: Path(__file__).resolve().parent.parent.parent)
    template_solution: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent.parent
        / "templates"
        / "solution_template.py"
    )
    template_test: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent.parent
        / "templates"
        / "test_solution_template.py"
    )
    instructions_dir: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent.parent / "instructions"
    )
    solutions_dir: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent.parent / "solutions"
    )
    tests_dir: Path = Field(default_factory=lambda: Path(__file__).resolve().parent.parent.parent / "tests")
    readme: Path = Field(default_factory=lambda: Path(__file__).resolve().parent.parent.parent / "README.md")
