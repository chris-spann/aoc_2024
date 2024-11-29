from pathlib import Path

from pydantic import BaseModel, Field


class Config(BaseModel):
    base_dir: Path = Field(default_factory=lambda: Path(__file__).resolve().parent.parent)
    template_solution: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent
        / "solutions"
        / "solution_template.py"
    )
    template_test: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent
        / "tests"
        / "test_solution_template.py"
    )
    instructions_dir: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "instructions"
    )
    solutions_dir: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "solutions"
    )
    tests_dir: Path = Field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "tests"
    )
