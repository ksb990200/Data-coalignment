# Data-coalignment


This repository contains Python code developed for the data co-alignment process of the Solar Acoustic Halos project using HMI Continuum data from the Solar Dynamics Observatory (SDO) telescope. The project aims to analyze time-series images of the Sun's surface to study acoustic halos, which are phenomena caused by solar oscillations propagating through the Sun's interior and resulting in localized intensity variations on the solar surface.

## Code Overview
- **Filename:** `solar_data_alignment.py`

1. **Data Collection:**
   - Continuum and Dopplergram data are collected from specified paths.
   
2. **Map Sequence Creation:**
   - Submaps are created from collected data using the SunPy library, defining specific coordinates of interest.
   - Map sequences are generated for both Continuum and Dopplergram data.
   
3. **Data Co-alignment:**
   - The `sunkit_image.coalignment` library is utilized to perform data co-alignment based on matching templates.
   - Co-aligned data is stored in separate arrays for Continuum and Dopplergram data.

4. **Data Visualization:**
   - Animations are generated to visualize the co-aligned data using matplotlib.
   - Separate animations are created for Continuum and Dopplergram data.

5. **Data Cube Generation:**
   - Data cubes are generated for further analysis, taking into account the alignment of data.




## Usage

1. Make sure you have the required libraries installed. You can install them using the following command:
   
   ```bash
   pip install sunpy sunkit-image pfsspy astropy


## Contributing

Contributions to this repository are welcome! If you have improvements, bug fixes, or additional features to suggest, feel free to open an issue or submit a pull request. Please follow the existing code style and conventions.


Feel free to explore, adapt, and experiment with these code snippets to further your understanding of solar physics and data visualization!
For questions or further information, please contact Karthik at ksb990200@gmail.com.


