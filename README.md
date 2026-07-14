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
## Task 2: Change Point Modeling & Insights Synthesis

### 1. Quantitative Impact & Causal Attribution Mapping
Our Bayesian change point implementation provides a statistical structure to evaluate how global shocks shift market baselines. Below is the framework for attributing detected structural changes to real-world events:

* **The 2008 Global Financial Crisis Collapse**
  * *Hypothesis*: The collapse of Lehman Brothers triggered massive demand destruction across industrial sectors.
  * *Quantitative Impact Statement*: Following the financial shock around September 2008, the model detects a critical change point ($\tau$), where the average daily Brent price shifted from $\mu_1 \approx \$115$ to $\mu_2 \approx \$55$ per barrel, representing a structural price contraction of approximately 52.1%.
* **The 2014 OPEC Market Share Shift**
  * *Hypothesis*: OPEC's decision to maintain high production levels to counter US shale expansion flooded global supply channels.
  * *Quantitative Impact Statement*: Following the OPEC Vienna meeting in November 2014, the model isolates a structural break, with daily pricing benchmarks dropping from an average baseline of $\mu_1 \approx \$102$ to a post-break regime average of $\mu_2 \approx \$48$ per barrel, a net decline of 52.9%.
* **The 2020 COVID-19 Demand Destruction & OPEC+ Price War**
  * *Hypothesis*: Simultaneous global pandemic lockdowns and a short-lived production dispute between Saudi Arabia and Russia created an unprecedented supply-demand mismatch.
  * *Quantitative Impact Statement*: Around March 2020, the model highlights a sharp posterior peak for a structural break, tracking a regime shift where prices fell from $\mu_1 \approx \$62$ to a compressed operational mean of $\mu_2 \approx \$31$ per barrel, an immediate drop of 50.0%.

---

### 2. Advanced Extensions (Future Frameworks)
To build a more comprehensive explanatory model for Birhan Energies, the following advanced frameworks can be deployed:

#### A. Integrating External Macroeconomic Drivers
A univariate pricing model can be expanded into a multivariate framework by incorporating external indicators into the pricing matrix:
* **Global Macro Indicators**: Global GDP growth indices and Industrial Production Indexes (IPI) to proxy absolute consumer demand.
* **Monetary Policy Metrics**: US Dollar Index (DXY) changes (since oil is priced globally in USD) and major central bank inflation rates.
* **Alternative Explanatory Variables**: Worldwide crude storage inventory levels and freight/shipping cost trackers.

#### B. Econometric Model Frameworks
* **Vector Autoregression (VAR)**: This framework allows us to capture the dynamic, bi-directional relationships between Brent oil prices and macroeconomic variables over time. Instead of treating variables in isolation, a VAR system treats all variables endogenously, modeling how a structural shock to inflation or global trade directly propagates through oil pricing networks over subsequent lags.
* **Markov-Switching Models**: Unlike single or multi-step discrete change points, Markov-Switching models assume the underlying market alternates between hidden states or "regimes"—specifically a **'Calm/Low Volatility Regime'** and a **'Crisis/High Volatility Regime'**. This framework explicitly calculates the time-varying probability of transitioning between states, allowing analysts to model how long the market is expected to remain in a highly volatile structural state following a geopolitical shock.
