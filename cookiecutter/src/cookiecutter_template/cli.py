"""Console script for cookiecutter_template."""
import cookiecutter_template

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for cookiecutter_template."""
    console.print("Replace this message by putting your code into "
               "cookiecutter_template.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
