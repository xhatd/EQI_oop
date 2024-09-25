"""
Author: Israel Gonzalez
Created: September 24, 2024

Description:
    Module for listing UML classes, their attributes, and relationships.
"""

from CORE.UML_CLASS.uml_class import ClassManager
from CORE.UML_ATTRIBUTE.uml_attribute import AttributeManager
from CORE.UML_RELATIONSHIP.uml_relationship import RelationshipManager

class UMLListing:
    def __init__(self, class_manager: ClassManager, attribute_manager: AttributeManager, relationship_manager: RelationshipManager):
        """Initialize UMLListing with ClassManager, AttributeManager, and RelationshipManager."""
        self.class_manager = class_manager
        self.attribute_manager = attribute_manager
        self.relationship_manager = relationship_manager

    def truncate(self, text: str, length: int) -> str:
        """Truncate text to a specified length and add ellipsis if necessary."""
        return text if len(text) <= length else text[:length - 3] + '...'

    def list_classes(self):
        """List all UML classes along with their attributes and relationships side by side."""
        classes = self.class_manager.get_classes()  # Get classes from the class manager

        if not classes:
            print("No classes found.")
            return

        # Prepare a list of class boxes
        boxes = []
        for cls in classes:
            class_name = self.truncate(cls.get('name', 'Unknown Class'), 20)  # Truncate class name
            attributes = cls.get('attributes', [])  # Get attributes from the class

            # Create a box for the class
            box_lines = [
                "|==========================|",
                f"|  {class_name:<18}      |",  # Align class name
                "|==========================|"
            ]

            # Add attributes section
            if attributes:
                box_lines.append(" |   Attributes:          |")
                box_lines.append("|--------------------------|")

                for attr in attributes:
                    attr_name = self.truncate(attr['name'], 15)  # Truncate attribute name
                    box_lines.append(f" |      - {attr_name:<15} |")  # Align attribute names
            else:
                box_lines.append(" |   No attributes found.   |")

            # Add relationships section
            relationships = self.relationship_manager.get_relationships_for_class(cls.get('name', 'Unknown Class'))

            if relationships:
                box_lines.append("|==========================|")
                box_lines.append(" |   Relationships:       |")
                box_lines.append("|--------------------------|")

                for rel in relationships:
                    target_class = self.truncate(rel['class_b'], 15)  # Class the relationship is pointing to
                    rel_type = self.truncate(rel['relationship_type'], 10)  # Type of relationship
                    box_lines.append(f" |  {rel_type} -> {target_class:<10} |")
            else:
                box_lines.append(" |   No relationships found.|")

            box_lines.append("|==========================|")
            boxes.append(box_lines)

        # Print boxes side by side
        for i in range(max(len(box) for box in boxes)):  # Get max height of boxes
            for box in boxes:
                # Print the current line of each box if it exists
                if i < len(box):
                    print(box[i], end="  ")  # Add space between boxes
                else:
                    print(" " * 20, end="  ")  # Empty space for alignment
            print()  # New line after each row of boxes

# Usage example
if __name__ == "__main__":
    class_manager = ClassManager()
    attribute_manager = AttributeManager()
    relationship_manager = RelationshipManager()
    listing = UMLListing(class_manager, attribute_manager, relationship_manager)
    listing.list_classes()  # Call the listing function
