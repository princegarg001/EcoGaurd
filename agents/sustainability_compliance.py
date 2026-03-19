"""Sustainability Compliance Agent for EcoGuard.

Analyzes code for energy-inefficient patterns and suggests optimizations.
"""

import re
import ast
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Issue:
    """Represents a sustainability issue found in code."""
    line_number: int
    issue_type: str
    description: str
    suggestion: str
    severity: str  # 'low', 'medium', 'high'
    estimated_savings: str  # e.g., "2-5% energy reduction"


class SustainabilityAnalyzer:
    """Analyzes code for sustainability issues."""

    def __init__(self):
        self.issues: List[Issue] = []
        self.code_lines: List[str] = []

    def analyze(self, code: str) -> List[Issue]:
        """Analyze code and return list of issues."""
        self.issues = []
        self.code_lines = code.split('\n')

        # Run all analysis passes
        self._detect_inefficient_loops(code)
        self._detect_unused_variables(code)
        self._detect_redundant_computations(code)

        return sorted(self.issues, key=lambda x: x.line_number)

    def _detect_inefficient_loops(self, code: str) -> None:
        """Detect inefficient loop patterns."""
        # Pattern 1: Constant computation inside loop
        pattern1 = r'for\s+\w+\s+in\s+.*?:\s*\n\s+.*?=\s*[\w.]+\s*\*\s*\d+'
        matches = re.finditer(pattern1, code, re.MULTILINE)
        for match in matches:
            line_num = code[:match.start()].count('\n') + 1
            self.issues.append(Issue(
                line_number=line_num,
                issue_type='Inefficient Loop - Constant Computation',
                description='Computing constant value inside loop wastes CPU cycles',
                suggestion='Move constant computation outside the loop',
                severity='medium',
                estimated_savings='5-15% energy reduction'
            ))

        # Pattern 2: Nested loops that could be optimized
        pattern2 = r'for\s+\w+\s+in\s+.*?:\s*\n\s+for\s+\w+\s+in\s+.*?:'
        matches = re.finditer(pattern2, code, re.MULTILINE)
        for match in matches:
            line_num = code[:match.start()].count('\n') + 1
            self.issues.append(Issue(
                line_number=line_num,
                issue_type='Nested Loop',
                description='Nested loops can have high computational cost',
                suggestion='Consider using list comprehension or vectorization',
                severity='medium',
                estimated_savings='10-20% energy reduction'
            ))

        # Pattern 3: Loop with string concatenation
        pattern3 = r'for\s+\w+\s+in\s+.*?:\s*\n\s+.*?\+=\s*["\']'
        matches = re.finditer(pattern3, code, re.MULTILINE)
        for match in matches:
            line_num = code[:match.start()].count('\n') + 1
            self.issues.append(Issue(
                line_number=line_num,
                issue_type='Inefficient Loop - String Concatenation',
                description='String concatenation in loops creates new objects repeatedly',
                suggestion='Use list.append() and join() instead of += in loops',
                severity='high',
                estimated_savings='20-30% energy reduction'
            ))

    def _detect_unused_variables(self, code: str) -> None:
        """Detect unused variables."""
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return

        # Find all variable assignments
        assigned_vars = {}
        used_vars = set()

        for node in ast.walk(tree):
            # Track assignments
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        line = getattr(node, 'lineno', 0)
                        assigned_vars[target.id] = line
            # Track usage
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_vars.add(node.id)

        # Find unused variables
        for var_name, line_num in assigned_vars.items():
            if var_name not in used_vars and not var_name.startswith('_'):
                self.issues.append(Issue(
                    line_number=line_num,
                    issue_type='Unused Variable',
                    description=f'Variable "{var_name}" is assigned but never used',
                    suggestion=f'Remove unused variable or prefix with underscore if intentional',
                    severity='low',
                    estimated_savings='1-2% memory reduction'
                ))

    def _detect_redundant_computations(self, code: str) -> None:
        """Detect redundant or wasteful computations."""
        # Pattern: Multiple calls to same expensive function
        pattern = r'(\w+\.\w+\([^)]*\)).*\1'
        matches = re.finditer(pattern, code, re.MULTILINE)
        for match in matches:
            line_num = code[:match.start()].count('\n') + 1
            self.issues.append(Issue(
                line_number=line_num,
                issue_type='Redundant Computation',
                description='Same function called multiple times with same arguments',
                suggestion='Cache the result in a variable and reuse it',
                severity='medium',
                estimated_savings='5-10% energy reduction'
            ))

        # Pattern: Excessive logging
        pattern_logging = r'(print|logger\.\w+)\([^)]*\)'
        matches = list(re.finditer(pattern_logging, code))
        if len(matches) > 10:
            self.issues.append(Issue(
                line_number=1,
                issue_type='Excessive Logging',
                description=f'Found {len(matches)} logging statements - excessive I/O',
                suggestion='Reduce logging frequency or use conditional logging',
                severity='low',
                estimated_savings='2-5% energy reduction'
            ))


def format_issue(issue: Issue) -> str:
    """Format an issue for display."""
    return f"""
**Line {issue.line_number}: {issue.issue_type}** [{issue.severity.upper()}]

{issue.description}

**Suggestion:** {issue.suggestion}

**Estimated Savings:** {issue.estimated_savings}
"""


def analyze_code(code: str) -> Dict[str, Any]:
    """Main entry point for code analysis."""
    analyzer = SustainabilityAnalyzer()
    issues = analyzer.analyze(code)

    return {
        'total_issues': len(issues),
        'issues': issues,
        'summary': {
            'high_severity': len([i for i in issues if i.severity == 'high']),
            'medium_severity': len([i for i in issues if i.severity == 'medium']),
            'low_severity': len([i for i in issues if i.severity == 'low']),
        },
        'formatted_output': '\n'.join([format_issue(issue) for issue in issues])
    }


if __name__ == '__main__':
    # Example usage
    sample_code = """
for i in range(100):
    result = 5 * 10  # Constant computation in loop
    print(result)

unused_var = 42

for item in items:
    for sub_item in item.children:
        process(sub_item)

output = ""
for word in words:
    output += word + " "  # String concatenation in loop
"""

    result = analyze_code(sample_code)
    print(f"Found {result['total_issues']} issues:")
    print(f"  High: {result['summary']['high_severity']}")
    print(f"  Medium: {result['summary']['medium_severity']}")
    print(f"  Low: {result['summary']['low_severity']}")
    print(result['formatted_output'])
