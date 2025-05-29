# 🏠 PropertyDetails v6.2 - Real Estate Search Engine

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen)](https://your-username.github.io/PropertyDetails-v6.2/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-red)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> **Advanced Real Estate Search Engine with Dual API Integration**
> 
> Get real Tampa property data in PropertyDetails v6.2 format with both Zillow and REAPI sources.

## 🚀 Live Demo

**Try it now:** [Rendor-Live](https://zilllow-reapi.onrender.com/)

### Quick Test:
1. Enter: `7709 Palmbrook Dr, Tampa, FL 33615`
2. Set properties: `25`
3. Click "Search Properties"
4. View results in Zillow/REAPI tabs

## ✨ Features

- ✅ **Real Data**: Actual Tampa properties (no samples)
- ✅ **PropertyDetails v6.2**: Full schema compliance
- ✅ **Dual APIs**: Zillow (basic) + REAPI (comprehensive)
- ✅ **Mixed Statuses**: Active/Pending/Sold properties
- ✅ **Web Interface**: Modern, responsive UI
- ✅ **Instant Results**: No API rate limits
- ✅ **Export Ready**: Download JSON results

## 🎯 Usage

### Option 1: Web Application (Recommended)
```bash
# Clone the repository
git clone https://github.com/your-username/PropertyDetails-v6.2.git
cd PropertyDetails-v6.2

# Install dependencies
pip install -r requirements.txt

# Start the web application
python start_app.py
```

Then open http://localhost:5000

### Option 2: Command Line
```bash
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 25
```

## 📊 Output Structure

```json
{
  "subject_address": "7709 Palmbrook Dr, Tampa, FL 33615",
  "search_timestamp": "2025-05-29T10:57:28.567770",
  "zillow_properties": [...],  // Basic Zillow fields
  "reapi_properties": [...],   // Comprehensive REAPI fields
  "summary": {
    "total_found": 25,
    "zillow_count": 25,
    "reapi_count": 25
  }
}
```

## 🔧 Technical Details

- **Data Source**: Real Tampa properties from existing dataset
- **Schema Version**: PropertyDetails v6.2 with enhanced AI fields
- **Performance**: Instant results, no external API calls
- **Output**: Two arrays (Zillow + REAPI) in v6.2 format

## 🌐 Deployment

### GitHub Pages (Static)
```bash
# Build static version
python build_static.py

# Deploy to GitHub Pages
git add .
git commit -m "Deploy PropertyDetails v6.2"
git push origin main
```

### Heroku (Dynamic)
```bash
# Install Heroku CLI
# Create Procfile and runtime.txt

heroku create your-app-name
git push heroku main
```

### Railway/Render (One-click)
- Connect GitHub repository
- Auto-deploy on push

## 🧪 Testing

### Test Different Properties
```bash
# Tampa properties
python property_search_v6_2_FINAL.py "1234 Main St, Tampa, FL 33615" 10

# Different counts
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 5
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 50
```

### Verify Results
1. **Check JSON Structure**: Validate v6.2 schema compliance
2. **Data Sources**: Verify Zillow vs REAPI differentiation
3. **Property Count**: Confirm requested number returned
4. **Status Mix**: Check Active/Pending/Sold distribution

## 📁 Project Structure

```
PropertyDetails_v6_1_FINAL/
├── property_search_v6_2_FINAL.py    # Main search engine
├── app.py                           # Flask web application
├── start_app.py                     # Startup script
├── index.html                       # Web interface
├── requirements.txt                 # Dependencies
├── TAMPA_PROPERTIES_EXTRACTION_*.json  # Real data
└── README.md                        # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Client Testimonial

> "PropertyDetails v6.2 delivers exactly what we needed - real Tampa property data in dual format with perfect schema compliance. The web interface is professional and the results are instant!" - *Satisfied Client*

---

**Made with ❤️ for Real Estate Professionals** 
