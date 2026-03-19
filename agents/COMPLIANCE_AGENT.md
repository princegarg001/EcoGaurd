# Sustainability Compliance Agent

This directory contains the Sustainability Compliance Agent implementation.

## Files

- `sustainability_compliance.py` - Core analysis engine
- `gitlab_integration.py` - GitLab API integration
- `test_compliance.py` - Unit tests

## Features

### Detections

1. **Inefficient Loops**
   - Constant computation inside loops
   - Nested loops
   - String concatenation in loops

2. **Unused Variables**
   - Variables assigned but never used
   - Helps reduce memory waste

3. **Redundant Computations**
   - Duplicate function calls
   - Excessive logging

### Output

Each issue includes:
- Line number
- Issue type and description
- Actionable suggestion
- Estimated energy savings
- Severity level (high/medium/low)

## Usage

### Standalone Analysis

```python
from sustainability_compliance import analyze_code

code = """
for i in range(100):
    result = 5 * 10
    print(result)
"""

result = analyze_code(code)
print(f"Found {result['total_issues']} issues")
print(result['formatted_output'])
```

### GitLab Integration

```python
from gitlab_integration import ComplianceAgent

agent = ComplianceAgent(project_id='80410036')
agent.analyze_merge_request(mr_iid=1, files={
    'src/main.py': code_content
})
```

## Testing

```bash
python -m pytest test_compliance.py
```

## Next Steps

- Add more pattern detection (e.g., inefficient algorithms)
- Integrate with GitLab CI/CD pipeline
- Add support for more programming languages
- Implement caching for repeated analyses
