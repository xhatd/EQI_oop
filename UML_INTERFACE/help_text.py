import subprocess
import platform

help_text = """
NAME
    UML Management Interface - A tool for managing UML classes and attributes.

DESCRIPTION
    This program allows users to manage UML classes and their attributes.
    Commands are available to add, delete, and rename classes and attributes.

COMMANDS

    Add and Manage Classes:
        add_class <class_name>
            Add a new class with the specified name.

        delete_class <class_name>
            Delete the specified class.

        list_class
            Display the list of all created class(es).

        rename_class <old_class_name> <new_name>
            Rename a class from the old name to the new name.

        class_detail <class_name>
            Show the detail of the specified class.

    Manage Attributes:
        add_attr <class_name> <attr_name>
            Add a new attribute to the specified class.

        delete_attr <class_name> <attr_name>
            Delete the specified attribute from the chosen class.

        rename_attr <class_name> <current_attribute_name> <new_name>
            Rename an attribute within the specified class.

    Manage Relationships:
        add_rel <source_class> <destination_class_name> <relationship_level>
            Add a relationship from the source class to the destination class with the specified relationship level.

        delete_rel <chosen_class_name> <destination_class_name>
            Delete the relationship between the chosen class and the specified destination class.

    File Operations:
        clear_data
            Delete all data in the current storage.

        delete_saved
            Delete a saved file.

        load
            Load data from saved files.

        saved_list
            Show the list of saved files.

        save
            Save current data.

        default
            Go back to a blank program state.

    Miscellaneous:
        class_rel
            Display the relationships between class(es).

        help
            Display this help text.

        sort
            Sort the class list in alphabetical order.

        exit
            Quit the program.

SEE ALSO
    For more information, refer to the README.md documentation on our github.

"""

def show_help():
    """Display the help text directly."""
    print(help_text)

def show_manual():
    """Display the manual with pagination depending on the platform."""
    # Create a header message
    header_message = "Press 'q' to exit manual.\n\n"
    # Combine the header with the help text
    manual_text = header_message + help_text

    # Get the operating system
    current_os = platform.system()

    try:
        # Check if the system is Linux or macOS
        if current_os in ["Linux", "Darwin"]:
            # Use 'less' for pagination
            with subprocess.Popen(['less'], stdin=subprocess.PIPE) as proc:
                proc.communicate(input=manual_text.encode('utf-8'))

        # Check if the system is Windows
        elif current_os == "Windows":
            # Use 'more' for pagination
            with subprocess.Popen(['more'], stdin=subprocess.PIPE, shell=True) as proc:
                proc.communicate(input=manual_text.encode('utf-8'))

        else:
            # If the OS is not recognized, just print the help text
            print(manual_text)

    except Exception as e:
        # In case of any errors, print the manual without pagination
        print(f"Error displaying manual: {e}")
        print(manual_text)

# Usage example
if __name__ == "__main__":
    show_manual()
