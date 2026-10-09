# Heck Reaction Yield Prediction Using Machine Learning

## Overview

This project investigates machine learning methods for predicting chemical reaction yields in Heck cross-coupling reactions.

The objective is to compare different molecular and reaction representations and evaluate how well models generalize to reactions with unfamiliar chemical structures.

## Project Objectives

- Develop a reproducible workflow for reaction yield prediction.
- Compare Morgan fingerprints, DRFP, and RXNFP representations.
- Evaluate classical machine learning models using consistent data splits.
- Investigate the effect of increasingly challenging generalization splits.
- Analyze model performance using regression metrics and prediction plots.

## Methods

### Molecular and Reaction Representations

- **Morgan fingerprints:** Circular molecular fingerprints generated using RDKit.
- **DRFP:** Difference reaction fingerprint representation.
- **RXNFP:** Learned reaction representations.

### Model Evaluation

The project investigates model performance across different data-splitting strategies, including random splits and more demanding generalization splits.

Performance is summarized using regression metrics and visualizations. Comparisons should use consistent evaluation conditions wherever possible.

## Repository Structure

```text
heck-yield-ml/
├── src/
│   ├── features.py
│   ├── splits.py
│   └── evaluate.py
├── results/
│   ├── final_r2_table.csv
│   ├── multiseed_all_splits.csv
│   ├── multiseed_ref.csv
│   ├── multiseed_ref_drfp.csv
│   └── multiseed_ref_hgb.csv
├── figures/
│   ├── feature_importance_ref.png
│   ├── parity_reference.png
│   └── r2_by_split_errorbars.png
├── .gitignore
├── LICENSE
└── README.md
```

*This structure describes the intended organization; files should be moved and source code added before considering the repository complete.*

## Results

The repository includes model evaluation tables and figures comparing selected model configurations and data-splitting strategies.

See the [`results/`](results/) and [`figures/`](figures/) directories for the reported outputs.

Interpretation should consider the exact model configurations, split definitions, and evaluation metrics used to produce each result.

## Dataset Bias and Limitations

Reaction datasets can contain uneven representation of chemical structures, reaction conditions, and yield ranges. Reported performance may therefore depend on the composition of the dataset and the evaluation split.

Random splits can place chemically similar reactions in both training and test sets, potentially overstating performance on genuinely unfamiliar reactions. More demanding generalization splits can provide additional insight, although their difficulty depends on how the split is defined.

Invalid or incomplete molecular representations may also affect feature generation. Data-cleaning decisions and excluded records should be documented, and preprocessing should avoid using test-set outcomes to inform model development.

Predicted yields are estimates, not guarantees of experimental outcomes. Results from this project should be interpreted within the limitations of the available dataset and modeling methodology.

## Reproducibility and Data Handling

The repository is intended to contain source code, documentation, aggregate results, and figures rather than raw or licensed reaction datasets.

Raw datasets, local feature matrices, serialized data files, and notebooks are excluded through `.gitignore`. Users must obtain any required datasets through authorized sources and comply with the relevant licensing terms.

The source code and documentation will be expanded as the workflow is finalized.

