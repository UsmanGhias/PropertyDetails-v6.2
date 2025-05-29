#!/usr/bin/env python3
"""
🏠 Zillow PropertyDetails v6.0 Live Fetcher - CLIENT APPROVED
Real-Time Zillow API Integration with Client-Approved Structure

This module provides Zillow data extraction and mapping to PropertyDetails v6.0 schema.
Delivers the EXACT JSON structure that the client has approved and expects for Zillow data.
Uses AS-IS fields only as specified by client - no translation fields.

Author: Zillow Analysis Team
Version: v6.0 Client Approved
Date: May 2025
"""

import requests
import json
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

class ZillowLiveFetcherV60:
    """Zillow Live Fetcher for PropertyDetails v6.0 Schema - Client Approved Structure"""
    
    def __init__(self):
        """Initialize the Zillow fetcher with client-approved configuration"""
        self.api_key = "2cae43d3a4msh71904354378dd90p179e60jsn9c5b773f7d2c"
        self.base_url = "https://zillow-com1.p.rapidapi.com"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
        }
        
        # Property type mapping (AS-IS fields only as per client)
        self.property_type_mapping = {
            "SINGLE_FAMILY": "SFR",
            "TOWNHOUSE": "Townhome", 
            "CONDO": "Condo",
            "APARTMENT": "MFR",
            "MULTI_FAMILY": "MFR",
            "MANUFACTURED": "Manufactured",
            "MOBILE_HOME": "MobileHome",
            "LOT": "Land",
            "LAND": "Land"
        }
        
        # Heating type mapping (AS-IS fields only)
        self.heating_type_mapping = {
            "Forced air": "ForcedAirUnit",
            "Heat pump": "HeatPump", 
            "Radiant": "Radiant",
            "Baseboard": "Baseboard",
            "Other": "Other",
            "None": "None"
        }
        
        print("✅ Zillow Live Fetcher v6.0 initialized - Client Approved Structure (AS-IS fields)")
        
    def fetch_property_data(self, zpid: str) -> Optional[Dict[str, Any]]:
        """
        Fetch property data from Zillow API
        
        Args:
            zpid: Zillow Property ID
            
        Returns:
            Raw Zillow API response data or None if failed
        """
        print(f"🔍 Fetching Zillow data for ZPID: {zpid}")
        
        try:
            url = f"{self.base_url}/property"
            params = {"zpid": zpid}
            
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Successfully fetched Zillow data for ZPID {zpid}")
                return data
            else:
                print(f"❌ API request failed with status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error fetching Zillow data: {str(e)}")
            return None
    
    def fetch_property_photos(self, zpid: str) -> Optional[Dict[str, Any]]:
        """
        Fetch property photos from Zillow API
        
        Args:
            zpid: Zillow Property ID
            
        Returns:
            Photos data or None if failed
        """
        try:
            url = f"{self.base_url}/photos"
            params = {"zpid": zpid}
            
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
            if response.status_code == 200:
                photos_data = response.json()
                print(f"✅ Successfully fetched {len(photos_data.get('images', []))} photos")
                return photos_data
            else:
                print(f"⚠️ Photos request failed with status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"⚠️ Error fetching photos: {str(e)}")
            return None
    
    def get_image_dimensions_simple(self, image_url: str) -> Tuple[int, int]:
        """
        Get image dimensions with simple fallback
        
        Args:
            image_url: URL of the image
            
        Returns:
            Tuple of (width, height), defaults based on URL patterns
        """
        try:
            # Use reasonable defaults based on Zillow image patterns
            if "uncropped_scaled_within_1536_1024" in image_url:
                return 1536, 1024
            elif "uncropped_scaled_within_1344_1008" in image_url:
                return 1344, 1008
            elif "uncropped_scaled_within_1024_768" in image_url:
                return 1024, 768
            elif "uncropped_scaled_within_960_720" in image_url:
                return 960, 720
            else:
                return 1024, 768  # Standard default
                
        except Exception:
            return 1024, 768  # Safe default
    
    def classify_photo_basic(self, index: int, total_photos: int) -> str:
        """
        Basic photo classification (no AI as per client - classification not applied yet)
        
        Args:
            index: Photo index (0-based)
            total_photos: Total number of photos
            
        Returns:
            Classification type - using "unassigned" as client specified no classification yet
        """
        # Client specified: "we didn't applied the Classification yet"
        return "unassigned"
    
    def convert_to_client_approved_structure(self, zillow_data: Dict[str, Any], zpid: str) -> Optional[Dict[str, Any]]:
        """
        Convert Zillow data to client-approved PropertyDetails v6.0 structure
        Uses AS-IS fields only as specified by client
        
        Args:
            zillow_data: Raw Zillow API response
            zpid: Zillow Property ID
            
        Returns:
            PropertyDetails in client-approved v6.0 format
        """
        if not zillow_data or "property" not in zillow_data:
            return None
        
        prop = zillow_data["property"]
        photos_data = zillow_data.get("photos", {})
        
        # Extract basic property info (AS-IS fields)
        address = prop.get("address", {})
        details = prop.get("propertyDetails", {})
        
        # Build address components
        street = address.get("streetAddress", "")
        city = address.get("city", "")
        state = address.get("state", "")
        zipcode = address.get("zipcode", "")
        address_full = f"{street}, {city}, {state} {zipcode}".strip(", ")
        
        # Process photos (client approved - no captions, proper width/height, no classification yet)
        processed_photos = []
        photo_urls = photos_data.get("images", []) if isinstance(photos_data, dict) else []
        
        if photo_urls:
            print(f"Processing {len(photo_urls)} photos (no classification applied yet)...")
            for i, photo_url in enumerate(photo_urls):
                if isinstance(photo_url, str):
                    # Get image dimensions
                    width, height = self.get_image_dimensions_simple(photo_url)
                    
                    # Basic classification (unassigned as per client)
                    classification = self.classify_photo_basic(i, len(photo_urls))
                    
                    # Client approved structure: NO CAPTION FIELD
                    photo_obj = {
                        "sources": [{
                            "url": photo_url,
                            "width": width,
                            "height": height,
                            "classification_type": classification
                        }]
                    }
                    processed_photos.append(photo_obj)
        
        # Process price history (AS-IS from Zillow)
        mls_history = []
        price_history = prop.get("priceHistory", [])
        if price_history:
            for entry in price_history:
                if entry.get("price") and entry.get("date"):
                    mls_entry = {
                        "price": entry["price"],
                        "date": entry["date"],
                        "event": entry.get("event", "Unknown"),
                        "source": "Zillow"
                    }
                    mls_history.append(mls_entry)
        
        # Map heating type (AS-IS fields only)
        heating_type = details.get("heating", {}).get("type")
        mapped_heating = None
        if heating_type:
            mapped_heating = self.heating_type_mapping.get(heating_type, "Other")
        
        # Map property type (AS-IS fields only)
        property_type = details.get("homeType", "").upper()
        mapped_property_type = self.property_type_mapping.get(property_type, "Other")
        
        # Build identification section (client approved structure with AS-IS fields)
        identification = {
            "address_full": address_full,
            "street": street or None,
            "city": city or None,
            "state": state or None,
            "postal_code": zipcode or None,
            "property_type": mapped_property_type,
            "year_built": details.get("yearBuilt"),
            "living_sqft": details.get("livingArea"),
            "lot_sqft": details.get("lotSize"),
            "bedrooms": details.get("bedrooms"),
            "bathrooms_full": details.get("bathrooms"),
            "bathrooms_half": None,  # Not available in AS-IS Zillow fields
            "heating_type": mapped_heating,
            "exterior_materials": [],  # Not available in AS-IS Zillow fields
            "interior_materials": []   # Not available in AS-IS Zillow fields
        }
        
        # Build location section (AS-IS fields)
        location = {
            "lat": prop.get("latitude"),
            "lon": prop.get("longitude"),
            "county_fips": None,      # Not available in AS-IS Zillow fields
            "subdivision": None,      # Not available in AS-IS Zillow fields
            "neighborhood": None      # Not available in AS-IS Zillow fields
        }
        
        # Build AI fields section (empty as per client - no AI applied yet)
        ai_fields = {
            "architectural_styles": [],
            "finish_quality_score": None,
            "condition_score": None,
            "road_relations": []
        }
        
        # Build price history section (AS-IS fields)
        price_history_section = {
            "property_market_status": "Active",  # Default for listed properties
            "list_price": prop.get("price"),
            "last_sale_price": None,  # Not consistently available in AS-IS fields
            "mls_history": mls_history,
            "sale_history": []        # Not available in AS-IS Zillow fields
        }
        
        # Build complete PropertyDetails structure (client approved)
        property_details = {
            "PropertyDetails": {
                "identification": identification,
                "location": location,
                "ai_fields": ai_fields,
                "price_history": price_history_section,
                "photos": processed_photos,
                "meta_data": {
                    "data_source": "Zillow",
                    "source_property_id": str(zpid),
                    "fetch_timestamp": datetime.now().isoformat(),
                    "api_version": "v6.0_CLIENT_APPROVED_AS_IS"
                }
            }
        }
        
        return property_details
    
    def generate_client_approved_sample(self, zpid: str) -> Dict[str, Any]:
        """
        Generate a client-approved Zillow sample
        
        Args:
            zpid: Zillow Property ID
            
        Returns:
            Complete PropertyDetails in client-approved format
        """
        print(f"🏠 Generating Client-Approved Zillow Sample")
        print(f"📍 ZPID: {zpid}")
        print("=" * 60)
        print("⚠️ Using AS-IS fields only (no translation fields)")
        print("⚠️ No photo classification applied yet")
        
        # Fetch Zillow data
        zillow_data = self.fetch_property_data(zpid)
        
        if not zillow_data:
            print("❌ Failed to fetch Zillow data")
            return {}
        
        # Fetch photos
        photos_data = self.fetch_property_photos(zpid)
        if photos_data:
            zillow_data["photos"] = photos_data
        
        # Convert to client-approved structure
        property_details = self.convert_to_client_approved_structure(zillow_data, zpid)
        
        if not property_details:
            print("❌ Failed to convert Zillow data")
            return {}
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"CLIENT_APPROVED_ZILLOW_v60_{zpid}_{timestamp}.json"
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(property_details, f, indent=2)
        
        print(f"✅ SUCCESS! Client-approved Zillow JSON saved to: {filename}")
        
        # Print summary
        identification = property_details["PropertyDetails"]["identification"]
        print("\n📊 PROPERTY SUMMARY (AS-IS FIELDS):")
        print(f"Address: {identification['address_full']}")
        print(f"Property Type: {identification['property_type']}")
        print(f"Bedrooms: {identification['bedrooms']}")
        print(f"Bathrooms: {identification['bathrooms_full']}")
        print(f"Year Built: {identification['year_built']}")
        print(f"Living Area: {identification['living_sqft']} sqft")
        print(f"List Price: ${property_details['PropertyDetails']['price_history']['list_price']:,}" if property_details['PropertyDetails']['price_history']['list_price'] else "List Price: Not available")
        print(f"Photos: {len(property_details['PropertyDetails']['photos'])} (no classification applied)")
        print(f"MLS History: {len(property_details['PropertyDetails']['price_history']['mls_history'])} entries")
        
        return property_details

def main():
    """Main function to generate client-approved Zillow sample"""
    if len(sys.argv) != 2:
        print("Usage: python zillow_live_fetcher_v6_0.py <ZPID>")
        print("Example: python zillow_live_fetcher_v6_0.py 32345614")
        sys.exit(1)
    
    zpid = sys.argv[1]
    
    fetcher = ZillowLiveFetcherV60()
    result = fetcher.generate_client_approved_sample(zpid)
    
    if result:
        print("\n🎯 Client-approved Zillow sample generated successfully!")
        print("📄 This matches the client's expectations for AS-IS Zillow fields")
        print("📄 No translation fields or advanced features included")
    else:
        print("\n❌ Failed to generate client-approved sample")

if __name__ == "__main__":
    main() 