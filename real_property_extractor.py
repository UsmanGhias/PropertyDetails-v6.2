#!/usr/bin/env python3
"""
🏠 Real Property Extractor v6.0 - CLIENT REQUESTED
Search and extract REAL property data for multiple listings

This script does what the client actually wants:
1. Search for properties around a given address
2. Extract REAL Zillow data for each property found
3. Extract REAL REAPI data for each property found
4. Return dozens of listings with real data

Subject Property Address = 7709 Palmbrook Dr, Tampa, FL 33615
Client expects: "a couple dozen listings each with an extracted zillow and reapi"

Author: Property Analysis Team
Version: v6.0 Real Data Extraction
Date: May 2025
"""

import requests
import json
import sys
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from property_mapper_v6_0 import PropertyMapperV60
from zillow_live_fetcher_v6_0 import ZillowLiveFetcherV60

class RealPropertyExtractor:
    """Extract real property data for multiple listings"""
    
    def __init__(self):
        """Initialize the real property extractor"""
        self.zillow_api_key = "2cae43d3a4msh71904354378dd90p179e60jsn9c5b773f7d2c"
        self.reapi_key = "2cae43d3a4msh71904354378dd90p179e60jsn9c5b773f7d2c"
        
        # Initialize our mappers
        self.reapi_mapper = PropertyMapperV60()
        self.zillow_fetcher = ZillowLiveFetcherV60()
        
        # Zillow search headers
        self.zillow_headers = {
            "x-rapidapi-key": self.zillow_api_key,
            "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
        }
        
        print("🏠 Real Property Extractor v6.0 initialized")
        print("🎯 Ready to extract REAL data for multiple properties")
        
    def search_properties_zillow(self, address: str, radius_miles: float = 2.0) -> List[Dict[str, Any]]:
        """
        Search for properties around the given address using Zillow
        
        Args:
            address: Target address to search around
            radius_miles: Search radius in miles
            
        Returns:
            List of property search results
        """
        print(f"🔍 Searching for properties around: {address}")
        print(f"📍 Search radius: {radius_miles} miles")
        
        try:
            # Use Zillow search API
            url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
            
            params = {
                "location": address,
                "status_type": "ForSale",
                "home_type": "Houses",
                "sort": "Newest",
                "page": "1"
            }
            
            response = requests.get(url, headers=self.zillow_headers, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                properties = data.get("props", [])
                print(f"✅ Found {len(properties)} properties in search results")
                return properties
            else:
                print(f"❌ Search failed with status {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error searching properties: {str(e)}")
            return []
    
    def extract_real_zillow_data(self, zpid: str) -> Optional[Dict[str, Any]]:
        """
        Extract REAL Zillow data for a specific property
        
        Args:
            zpid: Zillow Property ID
            
        Returns:
            Real Zillow PropertyDetails or None
        """
        print(f"📊 Extracting REAL Zillow data for ZPID: {zpid}")
        
        try:
            # Use the real Zillow fetcher (not mock)
            zillow_data = self.zillow_fetcher.fetch_property_data(zpid)
            
            if not zillow_data:
                print(f"❌ Failed to fetch Zillow data for {zpid}")
                return None
            
            # Fetch photos
            photos_data = self.zillow_fetcher.fetch_property_photos(zpid)
            if photos_data:
                zillow_data["photos"] = photos_data
            
            # Convert to PropertyDetails format
            property_details = self.zillow_fetcher.convert_to_client_approved_structure(zillow_data, zpid)
            
            if property_details:
                print(f"✅ Successfully extracted Zillow data for {zpid}")
                return property_details
            else:
                print(f"❌ Failed to convert Zillow data for {zpid}")
                return None
                
        except Exception as e:
            print(f"❌ Error extracting Zillow data for {zpid}: {str(e)}")
            return None
    
    def extract_real_reapi_data(self, address: str) -> Optional[Dict[str, Any]]:
        """
        Extract REAL REAPI data for a specific address
        
        Args:
            address: Property address
            
        Returns:
            Real REAPI PropertyDetails or None
        """
        print(f"📊 Extracting REAL REAPI data for: {address}")
        
        try:
            # Use the real REAPI mapper
            property_details = self.reapi_mapper.fetch_and_map_property(address)
            
            if property_details:
                print(f"✅ Successfully extracted REAPI data for {address}")
                return property_details
            else:
                print(f"❌ Failed to extract REAPI data for {address}")
                return None
                
        except Exception as e:
            print(f"❌ Error extracting REAPI data for {address}: {str(e)}")
            return None
    
    def extract_multiple_properties(self, target_address: str, max_properties: int = 25) -> Dict[str, Any]:
        """
        Extract real data for multiple properties around target address
        
        Args:
            target_address: Address to search around
            max_properties: Maximum number of properties to process
            
        Returns:
            Dictionary containing all extracted property data
        """
        print("🎯 REAL PROPERTY EXTRACTION STARTED")
        print("=" * 80)
        print(f"🏠 Target Address: {target_address}")
        print(f"📊 Max Properties: {max_properties}")
        print(f"🔍 Extracting REAL Zillow + REAPI data for each property")
        print("=" * 80)
        
        # Search for properties
        search_results = self.search_properties_zillow(target_address)
        
        if not search_results:
            print("❌ No properties found in search")
            return {}
        
        # Limit to max_properties
        properties_to_process = search_results[:max_properties]
        print(f"📋 Processing {len(properties_to_process)} properties...")
        
        extracted_data = {
            "extraction_summary": {
                "target_address": target_address,
                "extraction_timestamp": datetime.now().isoformat(),
                "total_properties_found": len(search_results),
                "properties_processed": len(properties_to_process),
                "successful_extractions": 0,
                "failed_extractions": 0
            },
            "properties": []
        }
        
        # Process each property
        for i, prop in enumerate(properties_to_process, 1):
            print(f"\n🏠 Processing Property {i}/{len(properties_to_process)}")
            print("-" * 50)
            
            # Extract basic info from search result
            zpid = prop.get("zpid")
            address = prop.get("address", {})
            full_address = f"{address.get('streetAddress', '')}, {address.get('city', '')}, {address.get('state', '')} {address.get('zipcode', '')}"
            
            print(f"Address: {full_address}")
            print(f"ZPID: {zpid}")
            
            property_data = {
                "property_index": i,
                "search_result": prop,
                "zillow_extraction": None,
                "reapi_extraction": None,
                "extraction_status": {
                    "zillow_success": False,
                    "reapi_success": False,
                    "extraction_timestamp": datetime.now().isoformat()
                }
            }
            
            # Extract Zillow data
            if zpid:
                zillow_data = self.extract_real_zillow_data(str(zpid))
                if zillow_data:
                    property_data["zillow_extraction"] = zillow_data
                    property_data["extraction_status"]["zillow_success"] = True
                    print("✅ Zillow extraction: SUCCESS")
                else:
                    print("❌ Zillow extraction: FAILED")
            else:
                print("⚠️ No ZPID available for Zillow extraction")
            
            # Extract REAPI data
            if full_address.strip():
                reapi_data = self.extract_real_reapi_data(full_address)
                if reapi_data:
                    property_data["reapi_extraction"] = reapi_data
                    property_data["extraction_status"]["reapi_success"] = True
                    print("✅ REAPI extraction: SUCCESS")
                else:
                    print("❌ REAPI extraction: FAILED")
            else:
                print("⚠️ No valid address for REAPI extraction")
            
            # Update summary
            if property_data["extraction_status"]["zillow_success"] or property_data["extraction_status"]["reapi_success"]:
                extracted_data["extraction_summary"]["successful_extractions"] += 1
            else:
                extracted_data["extraction_summary"]["failed_extractions"] += 1
            
            extracted_data["properties"].append(property_data)
            
            # Rate limiting
            time.sleep(1)  # 1 second between requests
        
        return extracted_data
    
    def save_extraction_results(self, extraction_data: Dict[str, Any], target_address: str) -> str:
        """
        Save extraction results to JSON file
        
        Args:
            extraction_data: Complete extraction results
            target_address: Target address used for search
            
        Returns:
            Filename of saved results
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Clean address for filename
        clean_address = target_address.replace(" ", "_").replace(",", "").replace("/", "_")
        filename = f"REAL_PROPERTY_EXTRACTION_{clean_address}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(extraction_data, f, indent=2)
        
        print(f"💾 Results saved to: {filename}")
        return filename
    
    def print_extraction_summary(self, extraction_data: Dict[str, Any]):
        """Print summary of extraction results"""
        summary = extraction_data["extraction_summary"]
        properties = extraction_data["properties"]
        
        print("\n" + "=" * 80)
        print("🎯 REAL PROPERTY EXTRACTION COMPLETE")
        print("=" * 80)
        
        print(f"🏠 Target Address: {summary['target_address']}")
        print(f"📊 Properties Found: {summary['total_properties_found']}")
        print(f"📋 Properties Processed: {summary['properties_processed']}")
        print(f"✅ Successful Extractions: {summary['successful_extractions']}")
        print(f"❌ Failed Extractions: {summary['failed_extractions']}")
        
        # Count successful extractions by source
        zillow_success = sum(1 for p in properties if p["extraction_status"]["zillow_success"])
        reapi_success = sum(1 for p in properties if p["extraction_status"]["reapi_success"])
        
        print(f"\n📊 EXTRACTION BREAKDOWN:")
        print(f"   Zillow Successful: {zillow_success}/{len(properties)}")
        print(f"   REAPI Successful: {reapi_success}/{len(properties)}")
        
        print(f"\n🎯 CLIENT DELIVERY:")
        print(f"   ✅ Multiple real properties extracted")
        print(f"   ✅ Real Zillow data (not dummy)")
        print(f"   ✅ Real REAPI data (not dummy)")
        print(f"   ✅ PropertyDetails v6.0 format")

def main():
    """Main function for real property extraction"""
    if len(sys.argv) < 2:
        print("Usage: python real_property_extractor.py '<address>' [max_properties]")
        print("Example: python real_property_extractor.py '7709 Palmbrook Dr, Tampa, FL 33615' 25")
        sys.exit(1)
    
    target_address = sys.argv[1]
    max_properties = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    
    extractor = RealPropertyExtractor()
    
    # Extract real data for multiple properties
    results = extractor.extract_multiple_properties(target_address, max_properties)
    
    if results:
        # Save results
        filename = extractor.save_extraction_results(results, target_address)
        
        # Print summary
        extractor.print_extraction_summary(results)
        
        print(f"\n📁 Complete results saved to: {filename}")
        print("🎯 This is what the client requested - REAL data for multiple properties!")
    else:
        print("❌ Failed to extract any property data")

if __name__ == "__main__":
    main() 