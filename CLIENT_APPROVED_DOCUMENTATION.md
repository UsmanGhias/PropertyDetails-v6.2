# 🏠 Client-Approved PropertyDetails v6.0 Samples

## Overview

This package contains the exact JSON structures that the client has approved and expects from our 3 developed pipelines:

1. **Initial property search** ✅
2. **REAPI data extraction and enrichment** ✅  
3. **Zillow data extraction and enrichment** ✅

## REAPI Pipeline

**File**: `CLIENT_APPROVED_REAPI_v60_*.json`

**Features**:
- Comprehensive property details (85+ fields)
- Full address and location data
- Building specifications and features
- Price history and market data
- Property characteristics (pool, deck, fireplace, etc.)
- HOA information
- Census and flood zone data

**Sample Structure**:
```json
{
  "PropertyDetails": {
    "identification": {
      "apn": "U25281709I000001000140",
      "address_full": "7709 Palmbrook Dr, Tampa, FL 33615",
      "property_type": "SFR",
      "year_built": 1977,
      "living_sqft": 2200,
      "bedrooms": 4,
      "bathrooms_full": 2,
      "pool": true,
      "fireplace": true
    },
    "location": {
      "lat": 28.015482,
      "lon": -82.565594,
      "subdivision": "Twelve Oaks Village Unit No 2"
    },
    "price_history": {
      "list_price": 250000,
      "sale_history": [...]
    }
  }
}
```

## Zillow Pipeline

**File**: `CLIENT_APPROVED_ZILLOW_v60_*.json`

**Features**:
- AS-IS fields only (no translation fields)
- Basic property information (~15 fields)
- Photos with dimensions (no classification applied yet)
- MLS history from Zillow
- Address and location data

**Important Notes**:
- Uses AS-IS fields only as specified by client
- No photo classification applied yet
- No translation fields or advanced features
- Limited field coverage compared to REAPI

**Sample Structure**:
```json
{
  "PropertyDetails": {
    "identification": {
      "address_full": "123 Main St, City, ST 12345",
      "property_type": "SFR",
      "year_built": 2005,
      "living_sqft": 2150,
      "bedrooms": 4,
      "bathrooms_full": 3,
      "heating_type": "ForcedAirUnit"
    },
    "photos": [
      {
        "sources": [{
          "url": "https://...",
          "width": 1024,
          "height": 768,
          "classification_type": "unassigned"
        }]
      }
    ]
  }
}
```

## Key Differences

| Feature | REAPI | Zillow |
|---------|-------|--------|
| Field Coverage | 85+ fields | ~15 fields |
| Property Details | Comprehensive | Basic |
| Photos | Not available | Available (unclassified) |
| Price History | Full sale history | MLS history only |
| Features | Pool, deck, fireplace, etc. | Limited |
| Translation Fields | Yes | No (AS-IS only) |
| Classification | Not applied yet | Not applied yet |

## Client Expectations

The client has approved these exact structures and expects:

1. **REAPI**: Comprehensive property data with all available fields
2. **Zillow**: AS-IS fields only, no advanced processing
3. **No AI Classification**: Photo classification not applied yet
4. **Consistent Schema**: Both use PropertyDetails v6.0 format

## Usage

```bash
# Generate both samples
python generate_client_approved_samples.py

# Generate specific samples
python property_mapper_v6_0.py
python zillow_live_fetcher_v6_0.py 32345614
```

---
Generated: 2025-05-28 17:58:52
