# EcoGuard Dashboard

Professional, world-class sustainability dashboard for real-time monitoring of carbon footprint and energy consumption metrics.

## Features

### 📊 Overview Tab
- **Daily Emissions Trend** - Line chart showing CO₂ emissions over time
- **Energy Consumption** - Bar chart of kWh usage
- **Emissions by Source** - Doughnut chart breakdown (CI/CD, Deployments, Cloud, Other)
- **Carbon Intensity by Region** - Horizontal bar chart comparing regions

### 📈 Metrics Tab
- **Daily Average** - Current day's CO₂ emissions
- **Weekly Total** - Week's aggregated metrics
- **Monthly Total** - Month's aggregated metrics
- **CO₂ per Build** - SCI score metric
- **Weekly Comparison** - Multi-dataset bar chart
- **Monthly Trend** - Long-term trend analysis

### 🎯 Goals Tab
- **Sustainability Goals** - Track progress toward targets
- **Progress Bars** - Visual representation of goal completion
- **Status Indicators** - On Track, At Risk, Achieved
- **Deadline Tracking** - Countdown to goal deadlines

### ⚠️ Issues Tab
- **High Priority Issues** - Critical sustainability problems
- **Recent Issues** - Latest detected issues
- **Severity Levels** - High, Medium, Low indicators
- **Estimated Savings** - Potential energy/CO₂ reduction

### 💡 Recommendations Tab
- **Optimization Recommendations** - Actionable improvement suggestions
- **Estimated Savings** - Quantified impact of each recommendation
- **Priority Ranking** - Sorted by impact score

## Design Features

### Color Scheme
- **Primary Green** (#10b981) - Success, positive metrics
- **Secondary Blue** (#3b82f6) - Information, secondary data
- **Warning Orange** (#f59e0b) - Caution, medium severity
- **Danger Red** (#ef4444) - Critical, high severity
- **Dark Gray** (#1f2937) - Text, primary content
- **Light Gray** (#f9fafb) - Background

### Typography
- **Font Family** - System fonts (Apple, Segoe, Roboto)
- **Responsive** - Scales from mobile to 4K displays
- **Accessibility** - WCAG compliant contrast ratios

### Components
- **Header** - Gradient background with key metrics
- **Cards** - Elevated design with hover effects
- **Charts** - Interactive Chart.js visualizations
- **Progress Bars** - Smooth animations
- **Badges** - Status indicators
- **Responsive Grid** - Auto-layout for different screen sizes

## Data Sources

Dashboard pulls data from:
- `dashboards/data/daily-metrics.json` - Daily metrics
- `dashboards/data/weekly-metrics.json` - Weekly aggregates
- `dashboards/data/monthly-metrics.json` - Monthly aggregates
- `dashboards/data/sustainability-goals.json` - Goal definitions

## Installation

1. Copy `index.html` and `dashboard.js` to your web server
2. Ensure data JSON files are accessible at `../data/`
3. Open `index.html` in a modern web browser

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **Load Time** - < 2 seconds
- **Chart Rendering** - < 500ms
- **Responsive** - 60 FPS animations
- **Mobile Optimized** - Touch-friendly interface

## Customization

### Colors
Edit CSS variables in `index.html`:
```css
:root {
    --primary: #10b981;
    --secondary: #3b82f6;
    /* ... */
}
```

### Data Refresh
Modify the data loading interval in `dashboard.js`:
```javascript
setInterval(loadDashboardData, 300000); // 5 minutes
```

### Charts
Customize chart options in `initializeCharts()` function

## Future Enhancements

- Real-time WebSocket updates
- Export to PDF/CSV
- Custom date range selection
- Comparison mode (vs baseline)
- Predictive analytics
- Team collaboration features
- Mobile app version

## License

MIT License - See LICENSE file
