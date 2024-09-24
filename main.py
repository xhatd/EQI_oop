import argparse
from UML_INTERFACE.uml_interface import UMLInterface  # Update the import as necessary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the UML Management Interface.")
    parser.add_argument("--cli", action="store_true", help="Run in command-line interface mode")

    args = parser.parse_args()

    if args.cli:
        interface = UMLInterface()
        interface.run()  # This will start the CLI
    else:
        print("GUI mode is not implemented yet.")
