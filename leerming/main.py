import multiprocessing
import sys

import granian
from granian.constants import Interfaces


def main() -> None:
    run_func = None
    if len(sys.argv) > 1:
        run_func = COMMANDS.get(sys.argv[1])

    if run_func:
        run_func(sys.argv)
    else:
        run_granian(sys.argv)


def run_qcluster(argv: list) -> None:
    """Run Django-q cluster."""
    from django.core.management import execute_from_command_line

    execute_from_command_line(argv[2:])


def run_manage(argv: list) -> None:
    """Run Django's manage command."""
    from django.core.management import execute_from_command_line

    execute_from_command_line(argv[1:])


def run_granian(argv: list) -> None:
    """Run the web server."""
    workers = multiprocessing.cpu_count() * 2 + 1
    granian.Granian(
        "leerming.wsgi:application",
        interface=Interfaces.WSGI,
        workers=workers,
        address="0.0.0.0",
        port=8000,
    ).serve()


COMMANDS = {"qcluster": run_qcluster, "manage": run_manage}


if __name__ == "__main__":
    main()
