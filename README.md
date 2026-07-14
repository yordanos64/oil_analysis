# Brent Crude Oil Price Analysis: Change Point & Statistical Modeling

This repository contains the analysis framework for Birhan Energies to detect historical change points in Brent crude oil prices (1987-2022) and map them to global political, regulatory, and economic drivers.

## 1. Data Analysis Workflow
Our workflow is organized into seven sequential stages:
1. **Environment Setup & Scaffolding**: Standardize project structures and isolate dependencies.
2. **Data Acquisition & Engineering**: Clean historical daily records and normalize dates.
3. **Exploratory Data Analysis (EDA)**: Map volatility trends, check stationarity (ADF tests), and analyze log returns.
4. **Bayesian Change Point Modeling**: Deploy MCMC sampling routines via PyMC to pinpoint structural mean/variance breaks.
5. **Convergence Verification**: Evaluate trace plots and verify that $\hat{R}$ metrics align near 1.0.
6. **Causal Mapping & Attribution**: Validate statistical breaks against our researched historical event timeline.
7. **Strategic Synthesis**: Translate modeling parameter variations into risk briefs for energy stakeholders.

## 2. Modeling Assumptions & Limitations
When interpreting this time series analysis, the following structural limitations apply:
* **The Correlation vs. Causation Divide**: Identifying a structural change point matching a specific calendar window proves statistical association, not structural causation. The price shift could be a lagging reaction, an anticipatory adjustment, or an interaction with unmeasured underlying financial factors.
* **Information Bottleneck**: The baseline model relies entirely on univariate daily pricing histories. It deliberately excludes compounding macro parameters such as international shipping freight tracking, real-time US dollar valuations, and global storage capacities.
* **Structural Break Simplification**: Standard uniform prior configurations are designed to locate single or discrete multi-step breaks, which may obscure long-duration structural transitions or multi-layered rolling events.
# Stage all modified and new files
git add .

# Create your foundation checkpoint commit
git commit -m "docs: finalize project scaffolding, workflow design, and historical event dataset for task 1"
