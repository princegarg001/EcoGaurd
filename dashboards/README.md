# EcoGuard Dashboard

This directory contains dashboard visualization code and data.

## Structure

- `src/` - Dashboard source code (HTML, CSS, JavaScript)
- `data/` - Metrics data files (JSON)
- `config.json` - Dashboard configuration
- `package.json` - Dependencies

## Building the Dashboard

```bash
cd dashboards
npm install
npm run build
```

Output is generated in `public/` for deployment.

## Data Files

The Dashboard Data Agent updates these files daily:

- `data/daily-metrics.json` - Daily CO₂ and energy metrics
- `data/weekly-totals.json` - Weekly aggregated data
- `data/monthly-totals.json` - Monthly aggregated data
- `data/compliance-issues.json` - Sustainability issues

## Customization

Edit `config.json` to customize:

- Chart types and colors
- Sustainability goals
- Metric thresholds
- Display options

See `docs/DASHBOARD.md` for detailed guide.
