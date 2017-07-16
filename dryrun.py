"""
Load app and run it.
"""
from brmflask.app import create_app

if __name__ == "__main__":
    runapp = create_app(
        config_override={'DEBUG': True},
        template_folder='tests/dryrun/templates'
    )
    runapp.run()
