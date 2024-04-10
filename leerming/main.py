import sys
import subprocess


def _run_granian():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "granian",
            "--interface",
            "wsgi",
            "leerming.wsgi:application",
            "--port",
            "8000",
        ]
    )


def _run_manage(*args):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manage",
            *args,
        ]
    )


def main():
    if len(sys.argv) > 1:
        _run_manage(*sys.argv[1:])
    else:
        _run_granian()


if __name__ == "__main__":
    main()

