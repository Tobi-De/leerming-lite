import multiprocessing
import subprocess
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
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manage",
            "qcluster",
            *argv[2:],
        ],
        check=False,
    )


def run_manage(argv: list) -> None:
    """Run Django's manage command."""
    subprocess.run([sys.executable, "-m", "manage", *argv[2:]], check=False)


def run_granian(argv: list) -> None:
    """Run the web server."""
    workers = multiprocessing.cpu_count() * 2 + 1
    granian.Granian(
        "leerming.wsgi:application",
        interface=Interfaces.WSGI,
        workers=workers,
        port=8000,
    ).serve()


COMMANDS = {"qcluster": run_qcluster, "manage": run_manage}
