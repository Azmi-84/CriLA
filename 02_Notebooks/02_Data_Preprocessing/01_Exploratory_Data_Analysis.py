import marimo

__generated_with = "0.23.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import mlflow
    import numpy as np
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt

    return mlflow, mo, pd


@app.cell
def _(mlflow):
    # Set up MLflow tracking
    mlflow.set_experiment("eda_of_user_behaviour_analysis")
    mlflow.start_run(run_name="explanatory_data_analysis")
    return


@app.cell
def _(mlflow, pd):
    dataset = pd.read_csv("data/raw/instagram_usage_lifestyle.csv")

    # Log dataset metadata
    mlflow.log_param("dataset_path", "data/raw/instagram_usage_lifestyle.csv")
    mlflow.log_param("dataset_shape", dataset.shape)
    mlflow.log_param("features_names", list(dataset.columns))

    dataset
    return (dataset,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Ydata Profiling**
    """)
    return


@app.cell
def _():
    from ydata_profiling import ProfileReport

    return (ProfileReport,)


@app.cell
def _(ProfileReport, dataset, mlflow):
    profile = ProfileReport(
        df=dataset,
        title="User Behaviour Analysis on Social Media (Instagram).",
        explorative=True,  # In-depth analysis not just a summary for EDA
        minimal=False,  # Generate comprehensive and in-depth analysis not just summary
        progress_bar=True,  # Show progress while generating the report
        correlations={
            "pearson": {"calculate": True},
            "kendall": {"calculate": True},
            "spearman": {"calculate": True},
        },
        memory_deep=True,
    )

    # Log profiling parameters
    mlflow.log_param("minimal", False)
    mlflow.log_param("explorative", True)
    mlflow.log_param("memory_deep", True)
    mlflow.log_param("correlations", ["pearson", "kendall", "spearman"])
    return (profile,)


@app.cell
def _(mlflow, profile):
    output_path = "src/eda/user_behaviour_analysis.html"
    profile.to_file(output_path)

    # Log the HTML report as an artifact
    mlflow.log_artifact(output_path)
    return


@app.cell
def _(mlflow):
    mlflow.end_run()
    return


if __name__ == "__main__":
    app.run()
