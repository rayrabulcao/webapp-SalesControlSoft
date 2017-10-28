import os

from bios_setup import app


def runbios_setup():
    port = int(os.environ.get('PORT', 5555))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    runbios_setup()
