# Source-Based AI Recommendation Explanations

## Overview

This project examines how the **information source disclosed in an AI-generated recommendation explanation** shapes users' perceptions of the recommendation and their willingness to rely on it.

AI recommendation systems may justify recommendations using different kinds of information, including a user's previous behavior, other consumers' reviews, product attributes, or combinations of these sources. These explanation sources may produce different psychological responses. For example, behavioral information may increase perceived relevance while also raising privacy concerns, whereas review-based information may increase perceived source credibility.

The project develops a controlled five-condition experiment to investigate these mechanisms.

> **Project status:** Research design complete; pilot implementation pending.  
> **Human-participant data have not yet been collected.**

---

## Research Question

**How does the information source disclosed in an AI-generated recommendation explanation influence users' perceived relevance, source credibility, privacy concern, trust, and willingness to rely on the recommendation?**

---

## Experimental Design

The study uses a **five-condition between-subjects experimental design**.

Participants imagine shopping online for wireless headphones. An AI shopping assistant recommends the same fictional product, the **AeroSound X5 Wireless Headphones**, across all conditions.

The primary manipulation is the information source disclosed in the explanation.

| Condition | Explanation Source |
| --- | --- |
| Control | No specific information source disclosed |
| Behavior-Based | Previous browsing and shopping activity |
| Review-Based | Patterns in other consumers' reviews |
| Product-Feature-Based | Product features and stated preferences |
| Mixed-Source | Behavior, reviews, and product features combined |

Product, recommendation target, product attributes, tone, and presentation are held as constant as possible across conditions.

---

## Conceptual Model

The project examines several psychological mechanisms linking explanation source to reliance:

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

The proposed mechanisms include:

- **Behavior-based explanations** may increase perceived relevance while also increasing situational privacy concern.
- **Review-based explanations** may increase perceived source credibility.
- **Product-feature-based explanations** may increase perceived relevance without relying heavily on behavioral data.
- **Mixed-source explanations** combine multiple information sources and are treated as exploratory rather than assumed to be superior.

---

## Measures

The current measurement framework includes:

- Perceived Relevance
- Perceived Source Credibility
- Situational Privacy Concern
- Trust in the AI Recommendation
- Reliance Intention
- Behavioral Reliance
- Manipulation Checks

Most psychological constructs are measured using multi-item 7-point Likert scales.

Behavioral reliance is measured separately through a binary decision between accepting the AI-recommended product and continuing to search.

---

## Planned Analysis

The planned analysis includes:

1. Data-quality checks
2. Scale construction and internal-consistency assessment
3. Manipulation checks
4. One-way ANOVA
5. Theoretically specified planned contrasts
6. Multiple linear regression
7. Linear regression for reliance intention
8. Logistic regression for behavioral reliance
9. Mediation/path analysis
10. Bootstrap confidence intervals for indirect effects
11. Exploratory comparisons involving the mixed-source condition

The analysis distinguishes experimentally manipulated condition effects from associations among measured psychological constructs.

---

## Power Analysis

An a priori power analysis was developed for the five-condition experiment.

The current design-stage assumptions are:

- **α = .05**
- **Power = .80**
- **Five experimental groups**
- **Cohen's f = .20**

Under these assumptions, the minimum balanced analyzable sample is approximately:

**N = 305**

The current recruitment target for a future main study is:

**N = 360**, or approximately 72 participants per condition.

This effect-size assumption is used for study planning and is not an empirical estimate from the present project.

*To reproduce: pip install -r pip install -r analysis/requirements.txt && python analysis/power_analysis.py*

---

## Pilot Plan

The planned pilot consists of two stages.

### Stage 1 — Internal Functionality Testing

A small number of testers will evaluate:

- experiment flow;
- random assignment;
- stimulus presentation;
- instructions;
- response recording; and
- general usability.

### Stage 2 — Manipulation and Measurement Pilot

A small independent pilot will evaluate:

- whether participants distinguish the five source conditions;
- whether the manipulation functions as intended;
- preliminary scale performance;
- potential construct overlap;
- behavioral-response variation; and
- overall study feasibility.

Pilot results are intended for **design refinement**, not substantive hypothesis testing.

---

## Research Transparency

This repository currently documents a **planned experimental study**.

No human-participant data have been collected, and no empirical claims about consumer behavior are made at this stage.

Any simulated or synthetic data used in future development of the analysis pipeline will be explicitly labeled as simulated and will not be presented as evidence about real participants.

Human-participant recruitment and data collection will proceed only after applicable institutional research-ethics requirements have been addressed.

---

## Project Documentation

Detailed project materials are available in [`docs/`](docs/).

| File | Description |
| --- | --- |
| [`01_Stimuli_v2.pdf`](docs/01_Stimuli_v2.pdf) | Matched experimental stimuli for the five conditions |
| [`02_Manipulation_Checks_v1.pdf`](docs/02_Manipulation_Checks_v1.pdf) | Manipulation-check design |
| [`03_Hypotheses_v1.pdf`](docs/03_Hypotheses_v1.pdf) | Hypotheses and exploratory research question |
| [`04_Measurement_v1.pdf`](docs/04_Measurement_v1.pdf) | Measurement framework |
| [`05_Experiment_Spec_v1.pdf`](docs/05_Experiment_Spec_v1.pdf) | Full experiment specification |
| [`06_Analysis_Plan_v1.pdf`](docs/06_Analysis_Plan_v1.pdf) | Planned statistical analysis |
| [`07_Power_Analysis_v1.pdf`](docs/07_Power_Analysis_v1.pdf) | A priori power analysis and sensitivity analysis |
| [`08_Experiment_Flow_v1.pdf`](docs/08_Experiment_Flow_v1.pdf) | Platform-independent experiment flow |
| [`09_Pilot_Protocol_v1.pdf`](docs/09_Pilot_Protocol_v1.pdf) | Pilot-testing and study-refinement protocol |
| [`10_Research_Project_Summary_v1.pdf`](docs/10_Research_Project_Summary_v1.pdf) | Application-facing summary of the research project |

---

## Current Project Stage

### Completed

- Research question and conceptual model
- Five-condition experimental design
- Matched stimuli
- Manipulation checks
- Hypotheses
- Measurement framework
- Experiment specification
- Analysis plan
- A priori power analysis
- Experiment flow
- Pilot protocol
- Research project summary

### Next Steps

- Implement the experiment on an appropriate survey or experimental platform
- Conduct internal functionality testing
- Develop and validate a reproducible analysis pipeline using simulated data
- Conduct pilot testing when appropriate
- Refine the study before preregistration and formal data collection

---

## Broader Research Motivation

This project is part of a broader research interest in how the **provenance and verifiability of AI-generated information** shape human trust, judgment, and reliance.

The broader goal is not simply to identify explanation designs that increase trust, but to understand when explanations support **better-calibrated and more informed reliance on AI-generated recommendations**.
