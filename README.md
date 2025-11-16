# Candidate Fitness Assessment Skill (Alpha)

A Claude skill that automates candidate fitness assessment by systematically comparing resumes against job descriptions to generate structured, evidence-based evaluation reports.

## Overview

This skill helps hiring managers conduct initial candidate screening by:
- Extracting all requirements from job descriptions
- Matching resume content to each requirement with direct evidence
- Generating standardized markdown reports with fitness scores
- Ensuring compliance with equal employment opportunity guidelines

## Features

- **Structured Analysis**: Generates consistent markdown reports with requirements tables, summaries, and calculated fitness scores
- **Evidence-Based**: Uses only direct quotes from resumes (no paraphrasing or editorializing)
- **Compliance-Focused**: Excludes protected class considerations (race, color, religion, sex, national origin, age, disability, genetic information)
- **Referral Tracking**: Includes bonus scoring for employee referrals
- **Copy-Ready Output**: Produces markdown format for easy integration into your workflows

## Installation

1. Download the `candidate-fitness.skill` file
2. In Claude, navigate to Settings → Skills
3. Click "Add Skill" and upload the `.skill` file
4. The skill will be available immediately for use

## Usage

### Basic Usage

Upload both a resume and job description to Claude, then use any of these triggers:

```
Compare this resume to this job description
Check this candidate's fitness
Review this candidate against the provided position
Evaluate candidate qualifications
```

### Workflow

1. **Upload Documents**: Provide both resume and job description
2. **Referral Question**: Claude will ask if the candidate is an employee referral
3. **Assessment Generation**: Claude analyzes and generates the report
4. **Copy Output**: The markdown report is ready to paste into your documents

### Example Output

```markdown
## Candidate Fit Analysis

| Position Requirement | Evidence |
| -------------------- | -------- |
| 5+ years Python development experience | "Senior Python Developer at TechCorp (2018-2023)" |
| Bachelor's degree in Computer Science | "B.S. Computer Science, State University, 2018" |
| Experience with AWS cloud services | No direct evidence of requirement found |
| Strong communication skills | "Led weekly technical presentations for 20+ stakeholders" |

## Summary

The candidate demonstrates strong technical experience with 5 years of Python development and relevant educational background. Notable strengths include proven leadership in technical communication and project management. The resume does not provide direct evidence of AWS cloud services experience, though general cloud technologies are mentioned.

**Candidate Fitness Score**: 75.0
```

## Scoring System

The fitness score is calculated based on:

```
Base Score = (Satisfied Requirements / Total Requirements) × 100
Final Score = Base Score + Referral Bonus (if applicable)
```

- **Referral Bonus**: +10 points for employee referrals
- **Maximum Score**: 100.0 (capped)

## Requirements

- Claude with skills support
- Resume document (any format supported by Claude)
- Job description document (any format supported by Claude)

## Compliance Notes

This skill is designed to support fair and objective candidate evaluation:

- Uses only factual evidence from resumes
- Does not make hiring recommendations
- Excludes consideration of protected characteristics
- Provides transparent, auditable scoring methodology

**Note**: This tool is designed to assist in initial screening only. All hiring decisions should follow your organization's complete evaluation process and comply with applicable employment laws.

## Skill Structure

```
candidate-fitness/
├── SKILL.md                          # Main workflow instructions
├── scripts/
│   └── candidate_fit.py              # Fitness score calculation
└── references/
    └── output_template.md            # Report format example
```

## Customization

To modify the scoring algorithm, edit `scripts/candidate_fit.py`:

```python
def calculate_candidate_score(total_requirements: int, 
                              satisfied_requirements: int, 
                              is_referral: bool) -> float:
    base_score = (satisfied_requirements / total_requirements) * 100
    if is_referral:
        base_score += 10
    return min(round(base_score, 1), 100.0)
```

## License

This skill is provided as-is for use in candidate evaluation processes. Users are responsible for ensuring compliance with all applicable employment laws and regulations in their jurisdiction.

## Contributing

To suggest improvements or report issues:
1. Test the modification with sample resumes and job descriptions
2. Ensure compliance requirements remain intact
3. Document any changes to scoring methodology

## Version History

- **v0.1 Alpha** - Initial release with core assessment functionality. Several bugs.

---

**Built for Claude** | A skill to streamline candidate screening while maintaining objectivity and compliance
