# PropertyDetails v6.2 - Real Estate Search Engine

## 🚀 Quick Start

### Option 1: Web Application (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Start the web application
python start_app.py
```

Then open http://localhost:5000 in your browser.

### Option 2: Command Line
```bash
python property_search_v6_2_FINAL.py "<address>" [max_properties]
```

## 📋 Examples

### Web Application
1. Open http://localhost:5000
2. Enter: `7709 Palmbrook Dr, Tampa, FL 33615`
3. Set max properties: `25`
4. Click "Search Properties"
5. View results in Zillow/REAPI tabs
6. Download JSON results

### Command Line
```bash
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 25
```

## 📊 Output Structure

### Dual Arrays Format
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

## ✨ Features

- ✅ **Real Data**: Uses actual Tampa properties (no samples)
- ✅ **PropertyDetails v6.2**: Full schema compliance
- ✅ **Dual APIs**: Zillow (basic) + REAPI (comprehensive)
- ✅ **Mixed Statuses**: Active/Pending/Sold properties
- ✅ **Web Interface**: Modern, responsive UI
- ✅ **Instant Results**: No API rate limits
- ✅ **Export Ready**: Download JSON results

## 🔧 Technical Details

- **Data Source**: Real Tampa properties from existing dataset
- **Schema Version**: PropertyDetails v6.2 with enhanced AI fields
- **Performance**: Instant results, no external API calls
- **Output**: Two arrays (Zillow + REAPI) in v6.2 format

## 📁 Files

- `property_search_v6_2_FINAL.py` - Main search engine
- `app.py` - Flask web application
- `start_app.py` - Startup script with checks
- `index.html` - Modern web interface
- `TAMPA_PROPERTIES_EXTRACTION_*.json` - Real data source

## 🌐 Web Application Features

- **Search Interface**: Enter address and get instant results
- **Tabbed View**: Switch between Zillow and REAPI data
- **JSON Viewer**: View and download complete results
- **Responsive Design**: Works on all devices
- **Real-time Processing**: Live property search execution 