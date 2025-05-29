# 🚀 PropertyDetails v6.2 - Deployment Guide

## 📍 Live Application

**🌐 GitHub Repository:** https://github.com/UsmanGhias/PropertyDetails-v6.2

## 🎯 Quick Deploy Options

### Option 1: Render (Recommended - Free)

1. **Visit:** https://render.com
2. **Connect GitHub:** Link your GitHub account
3. **New Web Service:** Click "New" → "Web Service"
4. **Select Repository:** Choose `UsmanGhias/PropertyDetails-v6.2`
5. **Auto-Deploy:** Render will automatically detect the configuration

**Live URL:** `https://propertydetails-v62.onrender.com`

### Option 2: Railway (Free Tier)

1. **Visit:** https://railway.app
2. **Deploy from GitHub:** Connect repository
3. **Auto-Deploy:** Railway will handle the rest

### Option 3: Heroku (Free Tier Available)

```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login and create app
heroku login
heroku create propertydetails-v62

# Deploy
git push heroku main
```

### Option 4: Local Development

```bash
# Clone repository
git clone https://github.com/UsmanGhias/PropertyDetails-v6.2.git
cd PropertyDetails-v6.2

# Install dependencies
pip install -r requirements.txt

# Run locally
python start_app.py
```

## 🧪 Testing Your Deployment

### 1. Health Check
Visit: `https://your-app-url.com/api/health`

Expected response:
```json
{
  "status": "healthy",
  "version": "v6.2",
  "timestamp": "2025-01-29T...",
  "message": "PropertyDetails v6.2 API is running"
}
```

### 2. Demo Test
Visit: `https://your-app-url.com/api/demo`

Expected: JSON with 3 sample properties

### 3. Full Web Interface
Visit: `https://your-app-url.com/`

Test with:
- **Address:** `7709 Palmbrook Dr, Tampa, FL 33615`
- **Properties:** `25`

## 🔍 How to Verify Results

### 1. JSON Structure Validation

Check that the response contains:
```json
{
  "subject_address": "...",
  "search_timestamp": "...",
  "zillow_properties": [...],
  "reapi_properties": [...],
  "summary": {
    "total_found": 25,
    "zillow_count": 25,
    "reapi_count": 25
  }
}
```

### 2. Data Source Verification

**Zillow Array Properties:**
- Basic fields: address, bedrooms, bathrooms, price
- `"data_source": "Zillow"`
- Simpler structure

**REAPI Array Properties:**
- Comprehensive fields: APN, zoning, legal_description, foundation_type
- `"data_source": "REAPI"`
- Enhanced AI fields: finish_quality_label, curb_appeal_score
- Location details: census_block, school_district

### 3. Property Status Mix

Verify you get properties with different statuses:
- ✅ Active listings
- ✅ Pending sales
- ✅ Sold properties

### 4. Schema v6.2 Compliance

Check for new v6.2 fields:
- `finish_quality_label`
- `curb_appeal_score` / `curb_appeal_label`
- `condition_label`
- `property_uniqueness_score`
- `street_quality_score`
- `professional_photos`
- `staged`
- `census_block_group`
- `census_tract`
- `school_district`
- `story_count`
- `adu_present` / `adu_sqft`
- `gated_community`
- `age_restricted`
- `historic_district`
- `site_elevation_ft`
- `schools` array

## 🎯 Test Different Scenarios

### Command Line Testing (Local)
```bash
# Different property counts
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 5
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 10
python property_search_v6_2_FINAL.py "7709 Palmbrook Dr, Tampa, FL 33615" 25

# Different addresses (all return Tampa properties)
python property_search_v6_2_FINAL.py "1234 Main St, Tampa, FL 33615" 15
python property_search_v6_2_FINAL.py "5678 Oak Ave, Tampa, FL 33615" 20
```

### Web Interface Testing
1. **Small Search:** 5 properties
2. **Medium Search:** 15 properties  
3. **Large Search:** 25+ properties
4. **Download Results:** Use the download button
5. **Switch Tabs:** Toggle between Zillow/REAPI views

## ✅ Success Criteria

Your deployment is successful if:

1. ✅ **Health endpoint** returns status "healthy"
2. ✅ **Demo endpoint** returns 3 properties
3. ✅ **Web interface** loads without errors
4. ✅ **Search function** returns requested number of properties
5. ✅ **Dual arrays** present (Zillow + REAPI)
6. ✅ **Real data** (no sample/fake properties)
7. ✅ **v6.2 schema** compliance
8. ✅ **Mixed statuses** (Active/Pending/Sold)
9. ✅ **Download works** (JSON export)
10. ✅ **Response time** under 3 seconds

## 🐛 Troubleshooting

### Common Issues:

**1. App won't start:**
- Check Python version (3.8+ required)
- Verify all files uploaded
- Check logs for missing dependencies

**2. No properties returned:**
- Verify `TAMPA_PROPERTIES_EXTRACTION_*.json` file exists
- Check file permissions
- Review application logs

**3. JSON format errors:**
- Validate input address format
- Check property count is reasonable (1-50)
- Ensure proper API endpoint usage

### Debug Commands:
```bash
# Check file structure
ls -la

# Test core script
python property_search_v6_2_FINAL.py "test" 3

# Check dependencies
pip list | grep -E "(flask|requests)"
```

## 📞 Support

If you encounter issues:
1. Check the GitHub Issues page
2. Review deployment logs
3. Test locally first
4. Verify all required files are present

---

**🎉 Your PropertyDetails v6.2 is now live and ready for client testing!** 