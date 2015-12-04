import click

from inbox.github import login


@click.command()
def inbox():
    gh = login()
    user = gh.user()

    click.echo("Hello {}!".format(user.name))


if __name__ == '__main__':
    inbox()
