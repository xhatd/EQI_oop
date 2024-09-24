"""
Author: Israel Gonzalez
Created: September 23, 2024

Description:
    Manager for UML classes and attributes, facilitating operations
    such as adding, deleting, renaming classes and attributes, and displaying them.
"""

# Import necessary modules
from CORE.UML_CLASS.uml_class import ClassManager
from CORE.UML_ATTRIBUTE.uml_attribute import AttributeManager
from CORE.UML_RELATIONSHIP.uml_relationship import RelationshipManager  # Import RelationshipManager

class UMLManager:
    def __init__(self):
        """Initialize UMLManager with ClassManager, AttributeManager, and RelationshipManager."""
        self.class_manager = ClassManager()
        # Pass the class manager to the attribute manager
        self.attribute_manager = AttributeManager(self.class_manager)
        self.relationship_manager = RelationshipManager(self.class_manager)  # Initialize RelationshipManager

    def add_class(self, class_name: str) -> bool:
        """Add a class to the UML model."""
        return self.class_manager.add_class(class_name)

    def delete_class(self, class_name: str) -> bool:
        """Delete a class from the UML model."""
        return self.class_manager.delete_class(class_name)

    def rename_class(self, old_class_name: str, new_class_name: str) -> bool:
        """Rename a class in the UML model."""
        return self.class_manager.rename_class(old_class_name, new_class_name)

    def add_attribute(self, class_name: str, attr_name: str) -> bool:
        """Add an attribute to a class in the UML model."""
        return self.attribute_manager.add_attr(class_name, attr_name)

    def delete_attribute(self, class_name: str, attr_name: str) -> bool:
        """Delete an attribute from a class in the UML model."""
        return self.attribute_manager.delete_attr(class_name, attr_name)

    def rename_attribute(self, class_name: str, old_attr_name: str, new_attr_name: str) -> bool:
        """Rename an attribute in a class of the UML model."""
        return self.attribute_manager.rename_attr(class_name, old_attr_name, new_attr_name)

    def add_relationship(self, class_name_a: str, class_name_b: str, relationship_type: str) -> bool:
        """Add a relationship between two classes in the UML model."""
        return self.relationship_manager.add_relationship(class_name_a, class_name_b, relationship_type)

    def delete_relationship(self, class_name_a: str, class_name_b: str, relationship_type: str) -> bool:
        """Delete a relationship between two classes in the UML model."""
        return self.relationship_manager.delete_relationship(class_name_a, class_name_b, relationship_type)

    def display_classes(self):
        """Display all classes managed by the UML model."""
        print("Classes:")
        for cls in self.class_manager.get_classes():
            print(f"  - {cls['name']}")  # Updated from 'class_name' to 'name'

    def display_attributes(self, class_name: str):
        """Display all attributes for a specific class."""
        attr_list = self.attribute_manager.get_attr_list(class_name)
        print(f"Attributes for class '{class_name}':")
        for attr in attr_list:
            print(f"  - {attr['name']}")  # Updated from 'attr_name' to 'name'

if __name__ == "__main__":
    manager = UMLManager()

