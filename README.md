# Source-Based AI Recommendation Explanations

## Overview

This project examines how the information source disclosed in an AI-generated
recommendation explanation influences users' perceptions of the recommendation
and their willingness to rely on it.

AI recommendation systems may explain recommendations using different types of
information, such as a user's previous behavior, other consumers' reviews, or
product attributes. These sources may produce different psychological responses:
behavioral information may increase perceived relevance while also raising privacy
concerns, review information may increase perceived source credibility, and
product-feature information may strengthen perceived fit.

The project develops a controlled online experiment to investigate these effects.

## Research Question

How does the information source disclosed in an AI-generated recommendation
explanation influence consumers' perceived relevance, source credibility,
privacy concern, trust, and willingness to rely on the recommendation?

## Experimental Design

The study uses a five-condition between-subjects experimental design.

Participants imagine shopping online for wireless headphones. An AI shopping
assistant recommends the same fictional product, the AeroSound X5 Wireless
Headphones, across all conditions.

The primary manipulation is the information source disclosed in the explanation.

| Condition | Explanation Source |
| --- | --- |
| Control | No specific information source is disclosed |
| Behavior-Based | Previous browsing and shopping activity |
| Review-Based | Patterns in other consumers' reviews |
| Product-Feature-Based | Product features and specifications |
| Mixed-Source | Behavior, reviews, and product features combined |

Product, recommendation target, product attributes, tone, and presentation are
held as constant as possible across conditions.

## Conceptual Model

The project examines several psychological mechanisms linking explanation source
to reliance:

```text
Explanation Source
        |
        v
+---------------------------+
| Perceived Relevance       |
| Source Credibility        |
| Privacy Concern           |
+---------------------------+
        |
        v
       Trust
        |
        v
     Reliance
```

Behavior-based explanations are expected to increase perceived relevance but may
also increase privacy concern.

Review-based explanations are expected to increase perceived source credibility.

Product-feature-based explanations are expected to increase perceived relevance.

The mixed-source condition is treated as exploratory in the initial study.

## Measures

The current measurement plan includes:

- Perceived Relevance
- Perceived Source Credibility
- Situational Privacy Concern
- Trust in the AI Recommendation
- Reliance Intention
- Behavioral Reliance
- Manipulation Checks

Most psychological constructs are measured using multi-item 7-point Likert scales.

Behavioral reliance is measured separately using a binary decision between
accepting the AI-recommended product and continuing to search.

## Planned Analysis

The planned analysis proceeds from measurement validation to hypothesis testing.

1. Data-quality checks
2. Scale construction and internal-consistency assessment
3. Manipulation checks
4. One-way ANOVA and planned contrasts for experimental condition effects
5. Multiple linear regression for psychological predictors of trust
6. Linear regression for trust and reliance intention
7. Logistic regression for behavioral reliance
8. Mediation/path analysis for indirect effects
9. Exploratory comparisons involving the mixed-source condition

Indirect effects will be evaluated using bootstrap confidence intervals.

Associations among measured psychological variables will not automatically be
interpreted as causal effects.

## Current Status

### Completed

- Research question and conceptual model
- Five-condition experimental design
- Matched stimuli
- Manipulation checks
- Hypotheses
- Measurement plan
- Experiment specification
- Analysis plan

### In Progress

- Qualtrics implementation
- Pilot preparation
- Experimental interface and portfolio documentation

## Research Transparency

This repository currently documents an experimental design and analysis plan.

No empirical participant findings are claimed at this stage.

Any simulated or synthetic data used to validate the future analysis pipeline
will be explicitly labeled as simulated and will not be presented as evidence
about real consumer behavior.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── experiment_spec.pdf
│   ├── stimuli.pdf
│   ├── manipulation_checks.pdf
│   ├── hypotheses.pdf
│   ├── measurement.pdf
│   └── analysis_plan.pdf
├── assets/
│   ├── conceptual_model.png
│   └── experiment_flow.png
├── qualtrics/
│   └── survey_flow.md
└── analysis/
    └── future analysis scripts
```

## Project Stage

Experimental design complete. Qualtrics implementation and pilot preparation
are currently in progress.
