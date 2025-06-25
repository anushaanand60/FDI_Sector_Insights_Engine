```markdown
# 🇮🇳 FDI Sector Insights: 2000–2025

A modular data pipeline to clean, transform, and query India's sector-wise FDI equity inflows using Python and SQLite.

## Tech Stack
- Python (pandas, sqlite3, logging)
- Google Colab (notebook interface)
- SQLite (local database)
- DB Browser for SQLite (SQL querying)
- Pytest (unit testing)

## Project Structure
```

FDI\_Sector\_Insights\_Engine/
├── data\_maker.py         # Cleans and reshapes Excel data
├── data\_feeder.py        # Loads cleaned data into SQLite
├── run\_pipeline.py       # Orchestrates full pipeline
├── fdi\_insights.ipynb    # Optional notebook for analysis/visuals
├── tests/
│   └── test\_data\_maker.py  # Unit test for cleaning logic
├── fdi\_sector.db         # SQLite database (output)
├── requirements.txt      # Project dependencies
└── README.md             # Project overview

````

## How to Run (Colab/CLI)
```bash
python run_pipeline.py --input "Sectoral FDI Equity Data (25 years).xlsx" --db "fdi_sector.db"
````
Or use `fdi_insights.ipynb` in Colab for interactive exploration.

## Sample Query

```sql
SELECT sector, SUM(inflow_mn_usd) AS total_inflow
FROM fdi_sector
GROUP BY sector
ORDER BY total_inflow DESC;
```

## Tests

Run tests using `pytest`:

```bash
pytest tests/
```

## Future Scope

* Streamlit dashboard for visual insights
* PostgreSQL migration for handling larger database (once we add state-wise and country-wise data from DPIIT website)
* CLI automation and sector-level filters
