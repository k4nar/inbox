import click


@click.command()
def inbox():
    click.echo("Hello World!")


if __name__ == '__main__':
    inbox()
