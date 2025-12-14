# A-Cost-Effective-Open-Source-Framework-for-Urban-Rooftop-Solar-Potential

## Project Overview

This repository hosts an open-source and cost-effective framework designed for assessing urban rooftop solar photovoltaic (PV) potential at a city scale. It leverages publicly available geospatial data, such as Digital Surface Models (DSM), building footprints, and aerial imagery, in conjunction with established solar simulation models (like PVLib) to perform comprehensive solar potential assessment, economic feasibility analysis, and result visualization within a local computing environment.

The framework's workflow is structured across several sequential Jupyter Notebooks:

1.  **01_Data_Processing.ipynb**: Handles the cleaning, clipping, and preparation of raw geospatial data, including aligning building footprints and the DSM to the study area boundary.
2.  **02_Solar_Analysis.ipynb**: The core analysis script. It integrates the processed DSM and building footprints to calculate effective rooftop area, shading factor, annual energy potential (kWh/yr), economic savings, and investment payback period.
3.  **03_Model_Validation.ipynb**: Validates the locally computed results against an external benchmark (e.g., Google Solar API) using random sampling and statistical metrics to ensure model accuracy and confidence.
4.  **04_Visualization.ipynb & 05_Fig_*.ipynb**: Scripts dedicated to generating high-quality static and interactive maps, statistical charts, and figures that visualize solar potential distribution, economic viability, and shading impacts.

## Directory Structure
. ├── 01_Data_Processing.ipynb ├── 02_Solar_Analysis.ipynb ├── 03_Model_Validation.ipynb ├── 04_Visualization.ipynb ├── 05_Fig_Interactive_Website.ipynb ├── config.py ├── requirements.txt ├── .gitignore ├── inputs/ │ ├── boundaries/ # Study area boundary GeoJSON file │ ├── raw_data/ # Raw DSM, Building Footprints (e.g., Parquet, Shapefile) │ └── processed/ # Processed and clipped data └── outputs/ ├── final_results/ # Final calculated results GeoJSON file ├── intermediates/ # Intermediate files like shading rasters └── figures/ # Charts, maps, and figures (PDF/PNG/HTML)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/YourUsername/A-Cost-Effective-Open-Source-Framework-for-Urban-Rooftop-Solar-Potential.git](https://github.com/YourUsername/A-Cost-Effective-Open-Source-Framework-for-Urban-Rooftop-Solar-Potential.git)
cd A-Cost-Effective-Open-Source-Framework-for-Urban-Rooftop-Solar-Potential
