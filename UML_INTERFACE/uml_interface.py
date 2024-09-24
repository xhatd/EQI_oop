"""
Author: Israel Gonzalez
Date: Updated Date

Description:
    This module provides a command-line interface for managing UML classes 
    and their attributes, allowing users to add, delete, rename classes 
    and attributes, and manage relationships between classes.
"""

from CORE.UML_CLASS.uml_class import ClassManager
from CORE.UML_ATTRIBUTE.uml_attribute import AttributeManager
from UML_UTILS.save_load import save_data_to_json, load_data_from_json
from UML_INTERFACE.help_text import show_help, show_manual
from UML_MANAGER.uml_manager import UMLManager
from CORE.UML_LISTING.uml_listing import UMLListing

class UMLInterface:
    def __init__(self):
        self.manager = UMLManager()  # Initialize the UMLManager
        self.uml_listing = UMLListing(self.manager.class_manager, self.manager.attribute_manager)
        self.display_banner()  # Display the banner upon initialization

    def display_banner(self):
        banner = r"""
        ▗▖ ▗▖▗▖  ▗▖▗▖       ▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
        ▐▌ ▐▌▐▛▚▞▜▌▐▌       ▐▌   ▐▌  █  █    █ ▐▌ ▐▌▐▌ ▐▌
        ▐▌ ▐▌▐▌  ▐▌▐▌       ▐▛▀▀▘▐▌  █  █    █ ▐▌ ▐▌▐▛▀▚▖
        ▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖    ▐▙▄▄▖▐▙▄▄▀▗▄█▄▖  █ ▝▚▄▞▘▐▌ ▐▌
                                             
        Welcome to the UML Management Interface!
    For more information on commands, type "help" for the manual.
        """
        print(banner)

    def save_data(self, filename=None):
        """Save the current UML data to a JSON file with a user-specified filename."""
        if not filename:
            filename = input("Enter filename to save (default: uml_data.json): ") or 'uml_data.json'
        
        # Ensure the filename ends with .json
        if not filename.endswith('.json'):
            filename += '.json'
        
        uml_data = {
            "classes": [
                {
                    "name": cls["name"],
                    "attributes": cls["attributes"]  # Ensure attributes are included
                }
                for cls in self.manager.class_manager.get_classes()
            ],
            "relationships": []  # Populate this later as needed
        }
        save_data_to_json(uml_data, filename)

    def load_data(self, filename=None):
        """Load UML data from a JSON file with a user-specified filename if it exists."""
        if not filename:
            filename = input("Enter filename to load (default: uml_data.json): ") or 'uml_data.json'
        
        # Ensure the filename ends with .json
        if not filename.endswith('.json'):
            filename += '.json'

        uml_data = load_data_from_json(filename)
        if uml_data:
            for cls in uml_data.get('classes', []):
                self.manager.class_manager.add_class(cls["name"])  # Load classes through manager
                for attr in cls.get("attributes", []):
                    self.manager.attribute_manager.add_attr(cls["name"], attr["name"])  # Add attributes
            print("Data loaded successfully.")
        else:
            print("No data found or the file is empty.")

    def run(self):
        while True:
            command = input("=> ")

            # Parse command
            parts = command.split()
    
            if not parts:
                continue
            
            main_command = parts[0]

            if main_command == "help":
                show_manual()  # Call the show_manual function
            
            elif main_command == "exit":
                print("Exiting the UML Management Interface. Goodbye!")
                break
            
            elif main_command == "save":
                self.save_data()  # Save the UML data
            
            elif main_command == "load":
                self.load_data()  # Load the UML data
            
            elif main_command.startswith("add_class") and len(parts) == 2:
                class_name = parts[1]
                self.manager.add_class(class_name)
                
            elif main_command.startswith("delete_class") and len(parts) == 2:
                class_name = parts[1]
                self.manager.delete_class(class_name)

            elif main_command.startswith("rename_class") and len(parts) == 3:
                old_name = parts[1]
                new_name = parts[2]
                self.manager.rename_class(old_name, new_name)

            elif main_command.startswith("add_attr") and len(parts) == 3:
                class_name = parts[1]
                attr_name = parts[2]
                self.manager.add_attribute(class_name, attr_name)
                
            elif main_command.startswith("delete_attr") and len(parts) == 3:
                class_name = parts[1]
                attr_name = parts[2]
                self.manager.delete_attribute(class_name, attr_name)
                
            elif main_command.startswith("rename_attr") and len(parts) == 4:
                class_name = parts[1]
                old_attr_name = parts[2]
                new_attr_name = parts[3]
                self.manager.rename_attribute(class_name, old_attr_name, new_attr_name)

            elif main_command == "list_classes":
                self.uml_listing.list_classes()  # Call the listing function

            elif main_command.startswith("add_relationship") and len(parts) == 4:
                class_name_a = parts[1]
                class_name_b = parts[2]
                relationship_type = parts[3]
                self.manager.add_relationship(class_name_a, class_name_b, relationship_type)
                
            elif main_command.startswith("delete_relationship") and len(parts) == 4:
                class_name_a = parts[1]
                class_name_b = parts[2]
                relationship_type = parts[3]
                self.manager.delete_relationship(class_name_a, class_name_b, relationship_type)

            else:
                print("Invalid command. Please try again or type 'help' for assistance.")

if __name__ == "__main__":
    interface = UMLInterface()
    interface.run()
