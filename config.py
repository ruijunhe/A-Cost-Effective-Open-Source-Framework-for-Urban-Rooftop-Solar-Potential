import os

# ==============================================================================
# 0. BASE CONFIGURATION
# ==============================================================================
# Project root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Default study area name (Used for naming files and directories)
REGION_NAME = "university_city" 

# ==============================================================================
# 1. PATH CONFIGURATION
# ==============================================================================

# Input and Output Directories
INPUTS_DIR = os.path.join(BASE_DIR, "inputs")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# Research boundary file (GeoJSON/Shapefile)
BOUNDARY_PATH = os.path.join(INPUTS_DIR, "boundaries", f"{REGION_NAME}_boundary.geojson")

# Raw building footprints data (e.g., Parquet, downloaded from external source)
BUILDINGS_RAW_PATH = os.path.join(INPUTS_DIR, "raw_data", "global_buildings_raw.parquet")

# Processed building footprints file (Input for analysis)
BUILDINGS_PATH = os.path.join(INPUTS_DIR, "processed", f"{REGION_NAME}_buildings.geojson")

# Digital Surface Model (DSM) - Clipped TIF file
DSM_PATH = os.path.join(INPUTS_DIR, "processed", f"{REGION_NAME}_dsm.tif")

# Intermediate Shading analysis file (Generated in 02_Solar_Analysis)
SHADE_TIF_PATH = os.path.join(OUTPUTS_DIR, "intermediates", f"{REGION_NAME}_shading_factor.tif")

# Final results file (GeoJSON)
FINAL_GEOJSON = os.path.join(OUTPUTS_DIR, "final_results", "rooftop_solar_potential_optimized.geojson")

# ==============================================================================
# 2. SOLAR AND ECONOMIC PARAMETERS
# ==============================================================================

# Solar System Parameters
SYSTEM_SIZE_Wp_PER_M2 = 150   # System capacity per square meter of effective roof area (Wp/m²)
SYSTEM_EFFICIENCY = 0.85     # System performance ratio (PR)
SHADING_THRESHOLD = 0.4      # Minimum acceptable shading factor for inclusion in analysis

# Economic Parameters (Adjust based on local conditions)
COST_PER_Wp = 2.50           # Total installed system cost (USD/Wp)
ELECTRICITY_PRICE = 0.18     # Current average electricity price (USD/kWh)
SYSTEM_LIFETIME_YEARS = 25   # System design lifespan (years)
INTEREST_RATE = 0.05         # Discount rate or opportunity cost (for NPV analysis)