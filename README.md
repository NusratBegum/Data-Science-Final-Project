# Bangkok Air Pollution Analysis
**Data Science Essentials - Final Project - Group 3**

![Bangkok Air Pollution](bangkok_air_pollution_title_slide.png)

## Authors
- **Student ID: 6736748** (Liam)
- **Student ID: 6638009** (Nusrat)

## Project Overview
This project investigates the impact of meteorological conditions on PM2.5 levels in Bangkok, Thailand. Through comprehensive data collection and statistical analysis, we aim to identify high-risk air quality scenarios and inform policy and mitigation strategies for better public health outcomes.

### Problem Statement
Investigate the impact of meteorological conditions (low wind speed, high humidity, and rainfall) on PM2.5 levels in Bangkok to identify high-risk air quality scenarios and inform policy and mitigation strategies.

## Hypotheses
1. **Hypothesis 1**: PM2.5 levels are significantly higher (>100 µg/m³) on days with low wind speed (<64 km/h) and high humidity (>70%) compared to other days.
2. **Hypothesis 2**: There is a significant difference in PM2.5 levels on rainy days in Bangkok compared to non-rainy days.

## Data Sources
- **AQI Data**: Air Quality Index from [AQICN API](https://aqicn.org/api/)
- **WAQI Data**: World Air Quality Index historical data
- **Open-Meteo Weather Data**: Meteorological data including wind speed, humidity, and precipitation

## Stakeholders
- **Pollution Control Department (PCD)**: Evidence-based insights for air quality alerts and emission controls
- **Bangkok Metropolitan Administration (BMA)**: Data for urban planning and public health measures
- **Thai Meteorological Department**: Weather-pollution interaction insights for enhanced forecasting

## Project Structure
```
.
├── README.md                              # Project documentation (this file)
├── main.ipynb                             # Main Jupyter notebook with complete analysis
├── fetch_airdata.py                       # Script to fetch air quality data from AQICN API
├── read_airdata.py                        # Script to read and display collected data
├── air_data.csv                           # Collected air quality data
├── bangkok_air_pollution_title_slide.png  # Title image
└── SECURITY.md                            # Security documentation
```

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Libraries
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

The main dependencies include:
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization
- `scipy` - Scientific computing and statistical tests
- `scikit-learn` - Machine learning library
- `requests` - HTTP library for API calls

### API Key Setup
To collect air quality data, you need an API key from AQICN:
1. Register at [AQICN Data Platform](https://aqicn.org/data-platform/register/)
2. Set the API key as an environment variable:
   ```bash
   export AQICN_API_KEY="your_api_key_here"
   ```

## Usage

### 1. Data Collection
Fetch air quality data from the AQICN API:
```bash
python fetch_airdata.py
```
This script collects AQI and PM2.5 data for Bangkok, Beijing, and Los Angeles, and saves it to `air_data.csv`.

### 2. Read Collected Data
View the collected data:
```bash
python read_airdata.py
```

### 3. Run Analysis
Open and run the Jupyter notebook to see the complete analysis:
```bash
jupyter notebook main.ipynb
```

## Methodology

### Data Collection and Preparation
- Daily automated data collection using the AQICN API
- Integration of weather data from Open-Meteo
- Data cleaning and handling of missing values
- Feature engineering for hypothesis testing

### Analysis Techniques
1. **Descriptive Statistics**: Summary statistics and data distribution analysis
2. **Data Visualization**: Time series plots, correlation heatmaps, and distribution plots
3. **Statistical Testing**: 
   - One-tailed t-test for Hypothesis 1
   - Mann-Whitney U test for Hypothesis 2
4. **Machine Learning**: Linear regression models with cross-validation

## Key Findings

### Hypothesis 1 Results
Testing whether PM2.5 levels are significantly higher on days with low wind speed and high humidity:
- Statistical significance achieved (p-value < 0.05)
- PM2.5 levels exceeding 100 µg/m³ observed under specified conditions

### Hypothesis 2 Results
Testing the difference in PM2.5 levels between rainy and non-rainy days:
- Significant difference identified using Mann-Whitney U test
- Actionable insights for air quality management

## Success Metrics
- **Statistical Significance**: p-value < 0.05 for both hypothesis tests
- **Practical Significance**: PM2.5 exceeding health thresholds (100 µg/m³)
- **Model Performance**: R² scores and cross-validation metrics for predictive models

## Recommendations
Based on our analysis, we provide evidence-based recommendations for:
- Air quality alert systems during high-risk weather conditions
- Traffic management strategies during poor air quality episodes
- Public health advisories for vulnerable populations

## Contributing
This is an academic project for the Data Science Essentials course. For questions or collaboration, please contact the authors through their student IDs.

## License
This project is for educational purposes as part of the Data Science Essentials course at Mahidol University.

## Acknowledgments
- **Instructor**: Data Science Essentials course faculty
- **Data Providers**: AQICN, World Air Quality Index Project, Open-Meteo
- **Institution**: Mahidol University ICT
