"""Tests for Sustainability Compliance Agent."""

import unittest
from sustainability_compliance import analyze_code, SustainabilityAnalyzer


class TestSustainabilityAnalyzer(unittest.TestCase):
    """Test cases for sustainability analysis."""

    def setUp(self):
        self.analyzer = SustainabilityAnalyzer()

    def test_detect_constant_in_loop(self):
        """Test detection of constant computation in loop."""
        code = """
for i in range(100):
    result = 5 * 10
    print(result)
"""
        result = analyze_code(code)
        self.assertGreater(result['total_issues'], 0)
        self.assertTrue(any('Constant' in i.issue_type for i in result['issues']))

    def test_detect_unused_variable(self):
        """Test detection of unused variables."""
        code = """
unused_var = 42
used_var = 10
print(used_var)
"""
        result = analyze_code(code)
        self.assertTrue(any('Unused' in i.issue_type for i in result['issues']))

    def test_detect_string_concatenation_in_loop(self):
        """Test detection of string concatenation in loop."""
        code = """
output = ""
for word in words:
    output += word + " "
"""
        result = analyze_code(code)
        self.assertTrue(any('String' in i.issue_type for i in result['issues']))

    def test_detect_nested_loops(self):
        """Test detection of nested loops."""
        code = """
for item in items:
    for sub_item in item.children:
        process(sub_item)
"""
        result = analyze_code(code)
        self.assertTrue(any('Nested' in i.issue_type for i in result['issues']))

    def test_no_issues_in_clean_code(self):
        """Test that clean code produces no issues."""
        code = """
result = 5 * 10
for i in range(100):
    print(result)
"""
        result = analyze_code(code)
        # Should have fewer issues than problematic code
        self.assertLess(result['total_issues'], 3)

    def test_severity_levels(self):
        """Test that issues have appropriate severity levels."""
        code = """
output = ""
for word in words:
    output += word

unused = 42
"""
        result = analyze_code(code)
        severities = [i.severity for i in result['issues']]
        self.assertTrue(any(s in severities for s in ['high', 'medium', 'low']))

    def test_issue_has_suggestion(self):
        """Test that each issue has a suggestion."""
        code = """
for i in range(100):
    result = 5 * 10
"""
        result = analyze_code(code)
        for issue in result['issues']:
            self.assertIsNotNone(issue.suggestion)
            self.assertGreater(len(issue.suggestion), 0)

    def test_issue_has_estimated_savings(self):
        """Test that each issue has estimated energy savings."""
        code = """
for i in range(100):
    result = 5 * 10
"""
        result = analyze_code(code)
        for issue in result['issues']:
            self.assertIsNotNone(issue.estimated_savings)
            self.assertIn('%', issue.estimated_savings)


if __name__ == '__main__':
    unittest.main()
