import click
import github3

TOKEN_FILE = 'token'


def _log_from_token():
    with open(TOKEN_FILE) as f:
        token = f.readline().strip()

    return github3.login(token=token)


def _ask_for_token():
    click.echo("Please enter your Github credential. They will not be "
               "recorded.")
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True)

    auth = github3.authorize(
        username, password,
        ['user', 'repo'],
        note="Inbox application"
    )

    with open(TOKEN_FILE, 'w+') as f:
        f.write("{}\n{}".format(auth.token, auth.id))


def login():
    """
    Log the user using a token. Request the token if necessary.

    returns: :class:`GitHub <github3.github.GitHub>`
    """
    for _ in range(10):
        try:
            return _log_from_token()
        except (IOError):
            _ask_for_token()

    raise click.ClickException("Unable to log-in. Aborting.")
