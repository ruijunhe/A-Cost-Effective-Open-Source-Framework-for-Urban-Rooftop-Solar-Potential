# A Cost-Effective Open-Source Framework for Urban Rooftop Solar Potential

## Introduction

This project presents a **cost-effective and fully open-source framework** designed to rapidly assess the solar photovoltaic (PV) potential of urban rooftops. By integrating high-resolution geospatial data (DSM/DTM) with advanced shading analysis and a robust economic model, the framework accurately quantifies annual energy generation, installation costs, and **payback periods** for every building within a study area.

The goal is to provide a comprehensive, replicable, and low-barrier tool for urban planners, policymakers, and researchers to guide strategic, city-scale PV deployment.

## Key Results & Visualizations

![Fig_Rooftop_Solar_Potential_page-0001](https://github.com/user-attachments/assets/8f3481af-dce2-4abe-af84-5e2fca5f9fb8)
![Fig_Economic_Payback_Period_page-0001](https://github.com/user-attachments/assets/3e39915c-b505-403f-9054-f0b68f5208c8)
![Fig_Shading_Analysis_page-0001](https://github.com/user-attachments/assets/caf38c8c-bbd6-4733-804e-fdd244f72d78)

## Framework Workflow

The framework is structured as a five-step process, clearly defined by the numbered Jupyter Notebooks in the `notebooks/` directory:

| Step | Notebook | Description |
| :--- | :--- | :--- |
| **Step 1** | `01_Data_Processing.ipynb` | **Data Pre-processing:** Cleans, clips, and reprojects raw input data (e.g., building footprints, DSM, boundary files) to ensure consistency for analysis. |
| **Step 2** | `02_Solar_Analysis.ipynb` | **Core Analysis & Economics:** Calculates roof geometry (slope/aspect), applies advanced **shading analysis** (based on DSM), and integrates an economic model to determine potential generation, system capacity, and **Payback Period**. |
| **Step 3** | `03_Model_Validation.ipynb` | **Model Validation:** Compares the local model's results (e.g., energy density) against external, high-confidence data sources (like the Google Solar API) to demonstrate accuracy and quantify error metrics (e.g., R² and RMSE). |
| **Step 4** | `04_Visualization.ipynb` | **Static Visualization:** Generates publication-ready static maps and charts for solar potential, economic metrics, and shading analysis. |
| **Step 5** | `05_Fig_*.ipynb` | **Advanced Visuals & Interactive Map:** Focuses on detailed statistical breakdowns (by zoning or building type) and creates an interactive **Folium/HTML web map** for easy sharing and exploration of the final results. |

## Getting Started

### 1. Environment Setup

This project is built with Python. Start by creating a virtual environment and installing the dependencies listed in `requirements.txt`.

```bash
# It is recommended to use a virtual environment
conda activate geoai

# Install all required libraries
pip install -r requirements.txt
```

### 2. Data Requirements

The framework requires the following core geospatial data for your study area. Please place your files into the corresponding subfolders within the **`inputs/`** directory.

| Data Type | Description | Suggested Format |
| :--- | :--- | :--- |
| **DSM/DTM** | Digital Surface/Terrain Model (essential for height, pitch, and shading analysis) | GeoTIFF (`.tif`) |
| **Buildings** | Building footprints (vector polygons) | GeoJSON, Shapefile, or Parquet |
| **Boundary** | The outer boundary of the study area | GeoJSON |
| **Zoning** | Zoning map/building classification data (used in `05_Fig_Solar_Potential_By_Zoning.ipynb`) | GeoJSON/Shapefile |

### 3. Configuration

All critical project parameters, file paths, and economic model assumptions are centrally managed in **`config/parameters.py`**.

Before running the analysis, you **must** modify this file to align with your study area:

* **Update File Paths:** Adjust variables like `DSM_PATH`, `BUILDING_SRC_PATH`, and `BOUNDARY_PATH` to accurately point to your input data locations.
* **Adjust Economic Model Parameters:** Review and modify economic assumptions (e.g., `PV_COST_PER_W` for system cost, `PPA_RATE` for local electricity price, and `LIFECYCLE_YEARS`) to reflect the target city's market.

### 4. Running the Analysis

The entire analysis is executed sequentially through the Jupyter Notebooks located in the **`notebooks/`** folder. Follow the numbered steps precisely:

1.  **Start:** Run `01_Data_Processing.ipynb` to prepare the input files.
2.  **Core Model:** Execute `02_Solar_Analysis.ipynb` to perform the geometric, shading, and economic calculations (this notebook calls functions from `src/analysis_utils.py`).
3.  **Validation & Visuals:** Complete the process by running `03_Model_Validation.ipynb`, `04_Visualization.ipynb`, and the `05_Fig_*.ipynb` notebooks.

Final processed data (`rooftop_solar_potential_optimized.geojson`) and all output images will be saved to the **`outputs/`** folder.


### Contribution and License

This project is released under the **MIT License**. We welcome contributions, suggestions, and bug reports via Issues or Pull Requests.

* If you encounter a bug, please open an Issue.
* If you wish to contribute code (e.g., a new solar model or analysis method), please submit a Pull Request.

Please refer to the `LICENSE` file for full details on usage and distribution permissions.
