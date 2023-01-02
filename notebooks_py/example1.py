# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: nomarker
#       format_version: '1.0'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # Test Notebook for Jupytext

# # Import the Libraries

import os

import pandas as pd

# # Example code

os.listdir()

d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)

df
