"""
Author: Israel Gonzalez
Created: September 23, 2024

Description:
    Manager for UML attributes, facilitating operations
    such as adding, deleting, renaming attributes, and retrieving them.
"""

class AttributeManager:
    def __init__(self, class_manager):
        self.class_manager = class_manager  # Reference to ClassManager

    def add_attr(self, class_name: str, attr_name: str) -> bool:
        """Add an attribute to a class in the UML model."""
        if class_name in self.class_manager.classes:
            self.class_manager.classes[class_name]['attributes'].append({'name': attr_name})
            print(f"Attribute '{attr_name}' added to class '{class_name}'.")
            return True
        else:
            print(f"Class '{class_name}' does not exist. Cannot add attribute.")
            return False

    def delete_attr(self, class_name: str, attr_name: str) -> bool:
        """Delete an attribute from a class in the UML model."""
        if class_name in self.class_manager.classes:
            attributes = self.class_manager.classes[class_name]['attributes']
            for attr in attributes:
                if attr['name'] == attr_name:
                    attributes.remove(attr)
                    print(f"Attribute '{attr_name}' removed from class '{class_name}'.")
                    return True
            print(f"Attribute '{attr_name}' does not exist in class '{class_name}'.")
            return False
        else:
            print(f"Class '{class_name}' does not exist.")
            return False

    def rename_attr(self, class_name: str, old_attr_name: str, new_attr_name: str) -> bool:
        """Rename an attribute in a class of the UML model."""
        if class_name in self.class_manager.classes:
            attributes = self.class_manager.classes[class_name]['attributes']
            for attr in attributes:
                if attr['name'] == old_attr_name:
                    attr['name'] = new_attr_name
                    print(f"Attribute '{old_attr_name}' renamed to '{new_attr_name}' in class '{class_name}'.")
                    return True
            print(f"Attribute '{old_attr_name}' does not exist in class '{class_name}'.")
            return False
        else:
            print(f"Class '{class_name}' does not exist.")
            return False

    def get_attr_list(self, class_name: str) -> list:
        """Get the list of attributes for a specific class."""
        if class_name in self.class_manager.classes:
            return self.class_manager.classes[class_name]['attributes']
        return []

# Example usage (comment this out in production):
if __name__ == "__main__":
    from CORE.UML_CLASS.uml_class import ClassManager
    class_manager = ClassManager()
    attribute_manager = AttributeManager(class_manager)
    class_manager.add_class("Car")
    attribute_manager.add_attr("Car", "color")
    attribute_manager.rename_attr("Car", "color", "paint_color")
    attribute_manager.delete_attr("Car", "paint_color")
