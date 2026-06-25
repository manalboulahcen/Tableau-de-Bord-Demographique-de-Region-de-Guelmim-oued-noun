# Dashboard Codebase Summary

## Project Overview

This workspace contains a single Streamlit application: `app.py`.
The app builds a demographic dashboard for the Guelmim-Oued Noun region in Morocco, using data from the Excel workbook `RGPH__2024.xlsx` and a regional map image `image.png`.

## Main Dependencies

- `streamlit` for the web application layout and UI components
- `pandas` for loading and manipulating Excel data
- `plotly.express` and `plotly.graph_objects` for interactive charts

## App Configuration

- `st.set_page_config(page_title="Analyse Démographique", layout="wide")`
- `excel_file` is defined as `RGPH__2024.xlsx`
- Data loading is cached using `@st.cache_data`

## Navigation and Pages

The app uses a sidebar `selectbox` to switch between the following sections:

1. `Accueil`
2. `Analyse Régionale`
3. `Population et Sexe`
4. `Structure par Âge`
5. `État Matrimonial`
6. `Fécondité et Handicap`
7. `Ménages`
8. `Province de Guelmim`
9. `Province de Sidi Ifni`
10. `Province de Tan-Tan`
11. `Province d'Assa-Zag`

## Page Details

### Accueil

- Displays a custom HTML header with regional branding
- Presents a summary text block about the Guelmim-Oued Noun region
- Renders `image.png` as a regional map
- Shows administrative organization data in a table
- Presents province cards for Guelmim, Sidi Ifni, Tan-Tan, and Assa-Zag
- Includes a project objective statement for the regional demographic research dashboard

### Analyse Régionale

- Displays four key metrics:
  - Population totale
  - Population urbaine
  - Population rurale
  - Nombre de ménages
- Loads `Population` sheet to plot total population by province
- Loads `population urbaine_rurale` sheet to plot urban vs rural population by province
- Loads `menage par province` sheet to plot households by province

### Population et Sexe

- Loads `masculin_féminin` sheet
- Displays gender ratio metrics and charts:
  - grouped bar chart of men and women by province
  - donut chart for sex distribution

### Structure par Âge

- Imports `plotly.graph_objects` for a population pyramid
- Loads `pyramide_ages_region` and `age` sheets
- Shows age distribution by sex as a horizontal bar chart (population pyramid)
- Displays a donut chart of population by broad age groups

### État Matrimonial

- Loads `État Matrimonial` and `mariage` sheets
- Displays metrics for marital status and average marriage age
- Shows a donut chart for marital status distribution across the region
- Plots grouped marital status by province and average age at first marriage

### Fécondité et Handicap

- Loads `fecondite`, `handicap_sexe`, and `handicap_province` sheets
- Displays fertility and disability metrics
- Shows:
  - fertility indicator per province
  - disability prevalence by sex
  - disability prevalence by province

### Ménages

- Loads `Ménages_Urbains` sheet
- Calculates totals for urban, rural, and total households
- Presents:
  - bar chart of households by province
  - donut chart of urban vs rural households
  - grouped bar chart comparing urban and rural households per province

### Province-Specific Pages

Each province page loads province-specific sheets and displays similar metrics and charts.

#### Province de Guelmim

- Loads:
  - `guelmim_population`
  - `guelmim_sexe`
  - `guelmim_fecondite`
  - `guelmim_handicap`
- Shows population, sex distribution, fertility, and handicap charts by commune

#### Province de Sidi Ifni

- Loads:
  - `sidi ifni_population`
  - `sidi ifni_sexe`
  - `sidi ifni_fecondite`
  - `sidi ifni_handicap`
- Shows the same set of commune-level metrics and charts

#### Province de Tan-Tan

- Loads:
  - `tantan_population`
  - `tantan_sexe`
  - `tantan_fecondite`
  - `tantan_handicap`
- Displays commune-level population, sex, fertility, and handicap charts

#### Province d'Assa-Zag

- Loads:
  - `assa zag_population`
  - `assa zag_sexe`
  - `assa sag_fecondite`
  - `assa zag_handicap`
- Displays commune-level population, sex, fertility, and handicap charts

## Data Sources and Sheets Used

The app relies heavily on the following Excel workbook sheets:

- `Population`
- `population urbaine_rurale`
- `menage par province`
- `masculin_féminin`
- `pyramide_ages_region`
- `age`
- `État Matrimonial`
- `mariage`
- `fecondite`
- `handicap_sexe`
- `handicap_province`
- `Ménages_Urbains`
- `guelmim_population`
- `guelmim_sexe`
- `guelmim_fecondite`
- `guelmim_handicap`
- `sidi ifni_population`
- `sidi ifni_sexe`
- `sidi ifni_fecondite`
- `sidi ifni_handicap`
- `tantan_population`
- `tantan_sexe`
- `tantan_fecondite`
- `tantan_handicap`
- `assa zag_population`
- `assa zag_sexe`
- `assa sag_fecondite`
- `assa zag_handicap`

## Notable Implementation Details

- The app uses HTML markup inside `st.markdown(..., unsafe_allow_html=True)` for custom styling.
- Most chart layouts use Plotly's `template="plotly_dark"` with transparent backgrounds.
- Several province pages share nearly identical structure and chart layout.
- Some metric values are hard-coded in the app instead of being calculated from the Excel data.

## Potential Improvement Opportunities

- Centralize repeated page layout logic to reduce duplication
- Derive the hard-coded metrics from data rather than using fixed text values
- Add error handling for missing or malformed Excel sheets
- Normalize province sheet names to avoid typos or inconsistent naming (`assa sag_fecondite` vs `assa zag_fecondite`)

## Workspace Files

- `app.py` - main Streamlit dashboard
- `image.png` - map image used on the home page
- `RGPH__2024.xlsx` - main data workbook referenced by the app
- `RGPH2024.xlsx`, `RGPH_2024.xlsx`, and `~$RGPH__2024.xlsx` - additional workbook files or temporary file copies
