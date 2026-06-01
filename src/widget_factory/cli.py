"""CLI entry point."""

import click


@click.group()
def main():
    """Widget factory CLI."""
    pass


@main.command()
@click.option("--output-dir", default="dist")
def build(output_dir):
    """Build widgets."""
    click.echo(f"Building to {output_dir}")


@main.command()
@click.option("--port", default=8000)
def serve(port):
    """Serve widgets."""
    click.echo(f"Serving on port {port}")


@main.command()
def lint():
    """Lint widget definitions."""
    click.echo("Linting...")
