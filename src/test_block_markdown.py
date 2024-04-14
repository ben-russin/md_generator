import unittest
from block_markdown import markdown_to_blocks  # Adjust the import based on your project structure

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        markdown = "This is a single paragraph without any special markdown."
        expected = ["This is a single paragraph without any special markdown."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_paragraphs(self):
        markdown = """This is the first paragraph.

This is the second paragraph with **bold** and *italic* markdown.

This is the third paragraph."""
        expected = [
            "This is the first paragraph.",
            "This is the second paragraph with **bold** and *italic* markdown.",
            "This is the third paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_paragraphs_with_excessive_whitespace(self):
        markdown = """
        
        This paragraph has excessive leading and trailing whitespace.
        
        
        """
        expected = ["This paragraph has excessive leading and trailing whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_blocks(self):
        markdown = "This is a paragraph.\n\n\n\nThis is another paragraph."
        expected = [
            "This is a paragraph.",
            "This is another paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_list_blocks(self):
        markdown = """* This is a list item
* This is another list item

* This is a new list start"""
        expected = [
            "* This is a list item\n* This is another list item",
            "* This is a new list start"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == '__main__':
    unittest.main()
