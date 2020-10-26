# data-science-template
Starter template for data science projects. Inspired to [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science).

### Directory structure
------------

The directory structure of the new project looks like this:

```
├── Makefile           <- Makefile with commands like `make data` or `make train`.
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting.
│
├── Pipfile            <- Requirements file generated by pipenv for reproducing the analysis environment.
├── Pipfile.lock       <- Lock file that comes with Pipfile for full reproducibility.
│
├── .env               <- Environment variables.
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module.
│   │
│   ├── data           <- Scripts to download or generate data.
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling.
│   │   ├── __init__.py
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions.
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   ├── visualization  <- Scripts to create exploratory and results oriented visualizations.
│   │   ├── __init__.py
│   │   └── visualize.py
│   │
│   └── utils          <- Utility functions for the project.
│       └── __init__.py
│
└── tests              <- Scripts to test the source code.
```
