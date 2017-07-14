Extraction of statistics for the Galaxy Training Material
================

# Usage

## Requirements

- [conda]()
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
    
- Extract statistics and contributors picture from the GitHub repository

    ```
    $ snakemake --snakefile src/extract_github_info.py
    ```

- Extract statistics about the GTN events on the Galaxy Hub

    ```
    $ snakemake --snakefile src/extract_hub_info.py
    ```