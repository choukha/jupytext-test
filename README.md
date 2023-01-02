# Jupytext Test
In this repo, we test the Jupytext library to convert ipynb notebooks to .py files and vice versa.
[![Code Quality Checks](https://github.com/choukha/jupytext-test/actions/workflows/code-quality.yaml/badge.svg)](https://github.com/choukha/jupytext-test/actions/workflows/code-quality.yaml)


To get started with this repo :

1. First clone the repository, example such as
```
git clone git@github.com:your-user/your-repo-name.git
```
2. Make sure that you've [poetry](https://python-poetry.org/) installed.
Also change the following setting in `poetry`
```
poetry config virtualenvs.in-project true
```
Open the repo in IDE (e.g. VS code) and run the following command in the terminal/commandline after navigating to the repo folder, this installs the dependencies defined in the `pyproject.toml` file.
```
poetry install
```

3. Also install pre-commit hooks
```
pre-commit install
```

Note : Before committing to github, Always run below command, to check that pre-commit checks are passed.
```
poetry run pre-commit run --all-files
``` 

4. Add new libraries as needed
```
poetry add pandas numpy
```
or if only required for development
```
poetry add pytest --group dev
```

## To convert formatted .py files into .ipynb notebook
After applying pre-commit hooks, to have formatted and corrected notebooks corresponding to .py files.
Run the below commands before running pre-commit hook again.

Now convert IPYNB --> PY files
```
jupytext --from notebooks///ipynb --to notebooks_py///py:nomarker --pre-commit
```
Also add the new files
```
git add .
```

Run the pre-commit checks on create PY files
```
pre-commit run --all-files
``` 
Again, Add the modified files if any
```
git add .
```
Check the PY files, after formatting and other checks. If these files look fine, then re-create the Notebooks.
Finally convert formatted PY files --> IPYNB
```
jupytext --from notebooks_py///py:nomarker --to notebooks///ipynb --pre-commit
```

