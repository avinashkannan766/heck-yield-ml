# Heck Reaction Yield Prediction Using Machine Learning

## Overview

This project investigates machine learning methods for predicting experimental yields in Heck coupling reactions. It compares different molecular and reaction representations and evaluates how well models generalize to reactions with unfamiliar chemical structures.

The project focuses on reproducible evaluation, representation comparison, and understanding the limitations of yield prediction models.

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

### Data Splitting

The project investigates model performance across different data-splitting strategies, including random splits and more demanding generalization splits.

Random splits provide a baseline evaluation. Grouped or other generalization-oriented splits can help investigate whether model performance decreases when related reaction combinations are less likely to appear in both training and test sets.

The interpretation of each split depends on its precise implementation and the chemical information used to define groups.

### Model Evaluation

Model performance is evaluated using regression metrics, including:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Coefficient of Determination (R²)

Prediction plots and comparisons across data splits are used to examine model performance and generalization.

Comparisons should use consistent evaluation conditions wherever possible.

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

## Results

The repository includes model evaluation tables and figures comparing selected model configurations and data-splitting strategies.

- **Results:** [View the results directory](results/)
- **Figures:** [View the figures directory](figures/)

Interpretation should consider the exact model configurations, split definitions, and evaluation metrics used to produce each result. Reported performance should not be assumed to represent performance on every type of unseen chemical reaction.

## Dataset Bias and Limitations

Reaction datasets can contain uneven representation of chemical structures, reaction conditions, and yield ranges. Reported performance may therefore depend on the composition of the dataset and the evaluation split.

Random splits can place chemically similar reactions in both training and test sets, potentially overstating performance on genuinely unfamiliar reactions. More demanding generalization splits can provide additional insight, although their difficulty depends on how each split is defined.

Invalid or incomplete molecular representations may also affect feature generation. Data-cleaning decisions and excluded records should be documented, and preprocessing should avoid using test-set outcomes to inform model development.

Predicted yields are estimates, not guarantees of experimental outcomes. Results from this project should be interpreted within the limitations of the available dataset and modeling methodology.

## Reproducibility and Data Handling

The repository is intended to contain source code, documentation, aggregate results, and figures rather than raw or licensed reaction datasets.

Raw datasets, local feature matrices, serialized data files, and notebooks are excluded through `.gitignore`. Users must obtain any required datasets through authorized sources and comply with the relevant licensing terms.

The repository includes reusable utilities for Morgan fingerprint generation, reproducible train/test splitting, and regression evaluation. Further development will focus on integrating these components into a fully reproducible training and benchmarking workflow.

## Future Work

- Integrate feature generation, data splitting, model training, and evaluation into a reproducible workflow.
- Expand comparisons across molecular and reaction representations.
- Evaluate additional machine learning models under consistent conditions.
- Investigate more rigorous generalization splits.
- Improve documentation of data preprocessing, excluded records, and experimental settings.

## License

See the `LICENSE` file for the licensing terms that apply to this repository.