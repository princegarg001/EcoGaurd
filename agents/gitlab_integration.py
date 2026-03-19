"""GitLab integration for Sustainability Compliance Agent.

Handles interaction with GitLab API for MR comments and issue creation.
"""

import os
import json
from typing import List, Dict, Any, Optional
from sustainability_compliance import analyze_code, Issue


class GitLabIntegration:
    """Handles GitLab API interactions."""

    def __init__(self, project_id: str, token: Optional[str] = None):
        self.project_id = project_id
        self.token = token or os.getenv('GITLAB_TOKEN')
        self.api_url = os.getenv('CI_API_V4_URL', 'https://gitlab.com/api/v4')

    def post_mr_comment(self, mr_iid: int, comment: str) -> bool:
        """Post a comment on a merge request."""
        # In real implementation, would use requests library
        # For MVP, just log the action
        print(f"[MR {mr_iid}] Comment: {comment}")
        return True

    def create_issue(self, title: str, description: str, labels: List[str]) -> bool:
        """Create a new issue in the project."""
        # In real implementation, would use requests library
        print(f"[Issue] {title}")
        print(f"Description: {description}")
        print(f"Labels: {labels}")
        return True


class ComplianceAgent:
    """Main agent for sustainability compliance checking."""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.gitlab = GitLabIntegration(project_id)

    def analyze_merge_request(self, mr_iid: int, files: Dict[str, str]) -> None:
        """Analyze code changes in a merge request."""
        all_issues = []
        file_issues = {}

        # Analyze each file
        for file_path, code in files.items():
            if not self._should_analyze(file_path):
                continue

            result = analyze_code(code)
            if result['total_issues'] > 0:
                file_issues[file_path] = result['issues']
                all_issues.extend(result['issues'])

        if not all_issues:
            comment = "✅ **EcoGuard Sustainability Check**: No efficiency issues found!"
            self.gitlab.post_mr_comment(mr_iid, comment)
            return

        # Generate MR comment
        comment = self._generate_mr_comment(file_issues, all_issues)
        self.gitlab.post_mr_comment(mr_iid, comment)

        # Create issues for high-severity problems
        high_severity = [i for i in all_issues if i.severity == 'high']
        for issue in high_severity:
            self._create_sustainability_issue(issue)

    def _should_analyze(self, file_path: str) -> bool:
        """Check if file should be analyzed."""
        analyzable_extensions = ('.py', '.js', '.ts', '.java', '.cpp', '.c', '.go')
        return file_path.endswith(analyzable_extensions)

    def _generate_mr_comment(self, file_issues: Dict[str, List[Issue]], 
                            all_issues: List[Issue]) -> str:
        """Generate a formatted MR comment."""
        summary = f"""## 🌱 EcoGuard Sustainability Check

**Summary:** Found {len(all_issues)} efficiency issues
- 🔴 High: {len([i for i in all_issues if i.severity == 'high'])}
- 🟡 Medium: {len([i for i in all_issues if i.severity == 'medium'])}
- 🟢 Low: {len([i for i in all_issues if i.severity == 'low'])}

### Issues by File
"""

        for file_path, issues in file_issues.items():
            summary += f"\n#### {file_path}\n"
            for issue in issues:
                severity_emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}[issue.severity]
                summary += f"\n{severity_emoji} **Line {issue.line_number}:** {issue.issue_type}\n"
                summary += f"- {issue.description}\n"
                summary += f"- **Fix:** {issue.suggestion}\n"
                summary += f"- **Savings:** {issue.estimated_savings}\n"

        summary += "\n---\n"
        summary += "💡 **Tip:** Fixing these issues can reduce energy consumption and improve performance!\n"
        summary += "See [Green Software Foundation](https://greensoftware.foundation/) for more tips."

        return summary

    def _create_sustainability_issue(self, issue: Issue) -> None:
        """Create a GitLab issue for a high-severity problem."""
        title = f"[Sustainability] {issue.issue_type}"
        description = f"""
## Issue
{issue.description}

## Suggestion
{issue.suggestion}

## Estimated Impact
{issue.estimated_savings}

## Reference
Detected by EcoGuard Sustainability Compliance Agent
"""
        labels = ['sustainability', 'efficiency', 'green-code']
        self.gitlab.create_issue(title, description, labels)


def main():
    """Main entry point for the agent."""
    # Get environment variables
    project_id = os.getenv('CI_PROJECT_ID', '80410036')
    mr_iid = os.getenv('CI_MERGE_REQUEST_IID')

    if not mr_iid:
        print("Not running in MR context")
        return

    # Sample files for testing
    sample_files = {
        'src/processor.py': """
for i in range(100):
    result = 5 * 10
    print(result)

unused_var = 42
""",
        'src/utils.py': """
output = ""
for word in words:
    output += word + " "
"""
    }

    agent = ComplianceAgent(project_id)
    agent.analyze_merge_request(int(mr_iid), sample_files)


if __name__ == '__main__':
    main()
