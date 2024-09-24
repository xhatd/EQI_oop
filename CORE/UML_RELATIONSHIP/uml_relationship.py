"""
Author: Israel Gonzalez
Created: September 23, 2024

Description:
    A module to manage relationships between UML classes.
"""

# Import necessary modules
from CORE.UML_CLASS.uml_class import ClassManager

class RelationshipManager:
    def __init__(self, class_manager: ClassManager):
        """Initialize RelationshipManager with an empty relationship list and a ClassManager instance."""
        self.relationship_list = []
        self.class_manager = class_manager  # Store the ClassManager instance

    def add_relationship(self, class_name_a: str, class_name_b: str, relationship_type: str) -> bool:
        """Add a relationship between two classes."""
        if not self.check_class_name_exist(class_name_a) or not self.check_class_name_exist(class_name_b):
            return False
        
        if self.check_relationship_exists(class_name_a, class_name_b, relationship_type):
            print(f"\nRelationship '{relationship_type}' between '{class_name_a}' and '{class_name_b}' already exists!")
            return False
        
        relationship = {
            "class_a": class_name_a,
            "class_b": class_name_b,
            "relationship_type": relationship_type
        }
        
        self.relationship_list.append(relationship)
        print(f"\nRelationship '{relationship_type}' added between '{class_name_a}' and '{class_name_b}'!")
        return True

    def delete_relationship(self, class_name_a: str, class_name_b: str, relationship_type: str) -> bool:
        """Delete a relationship between two classes."""
        for relationship in self.relationship_list:
            if (relationship["class_a"] == class_name_a and 
                relationship["class_b"] == class_name_b and 
                relationship["relationship_type"] == relationship_type):
                self.relationship_list.remove(relationship)
                print(f"\nRelationship '{relationship_type}' deleted between '{class_name_a}' and '{class_name_b}'!")
                return True
        print(f"\nRelationship '{relationship_type}' between '{class_name_a}' and '{class_name_b}' not found!")
        return False

    def check_relationship_exists(self, class_name_a: str, class_name_b: str, relationship_type: str) -> bool:
        """Check if a relationship exists between two classes."""
        for relationship in self.relationship_list:
            if (relationship["class_a"] == class_name_a and 
                relationship["class_b"] == class_name_b and 
                relationship["relationship_type"] == relationship_type):
                return True
        return False

    def check_class_name_exist(self, class_name: str) -> bool:
        """Check if a class name exists in the class manager."""
        for cls in self.class_manager.get_classes():
            if cls["name"] == class_name:
                return True
        print(f"\nClass '{class_name}' not found!")
        return False

# Usage example
if __name__ == "__main__":
    class_manager = ClassManager()  # Create a ClassManager instance
    relationship_manager = RelationshipManager(class_manager)  # Pass it to RelationshipManager
