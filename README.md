Extraction of statistics for the Galaxy Training Material
================

# Usage

## Requirements

- [conda](https://conda.io/miniconda.html)
- Create the conda environment:

    ```
    $ conda env create -f environment.yaml
    ```

## Extraction of the GitHub statistics

- Launch the conda environment

    ```
    $ source activate galaxy-training-material-stats
    ```

- Generate a Personal access tokens on GitHub (in Setting)
- Launch Jupyter

    ```
    $ jupyter notebook
    ```

- Open [http://localhost:8888](http://localhost:8888)
- Open:
    - [`src/extract_repo_content_stats.ipynb` Notebook](http://localhost:8888/notebooks/src/extract_repo_content_stats.ipynb) to extract the details about the current resources in the Galaxy Training Material and some statistics
    - [`src/extract_github_info.ipynb` Notebook](http://localhost:8888/notebooks/src/extract_github_info.ipynb) to extract statistics and contributors picture from the GitHub repository
    - [`src/analyze_feedback.ipynb` Notebook](http://localhost:8888/notebooks/src/analyze_feedback.ipynb) to analyze the Google drive feedback (exported as tsv) that are embeded at the end of tutorials
