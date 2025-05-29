#!/usr/bin/env python3
"""
PropertyDetails v6.2 - Startup Script
Checks dependencies and starts the web application
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all required files and dependencies exist"""
    print("🔍 Checking requirements...")
    
    # Check required files
    required_files = [
        'property_search_v6_2_FINAL.py',
        'TAMPA_PROPERTIES_EXTRACTION_20250528_182304.json',
        'index.html',
        'app.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    
    # Check Python dependencies
    try:
        import flask
        import requests
        print("✅ Python dependencies satisfied")
    except ImportError as e:
        print(f"❌ Missing Python dependency: {e}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    return True

def start_application():
    """Start the Flask web application"""
    print("\n🚀 Starting PropertyDetails v6.2 Web Application")
    print("=" * 60)
    print("📍 Web Interface: http://localhost:5000")
    print("🔍 API Endpoint: http://localhost:5000/api/search")
    print("📊 Health Check: http://localhost:5000/api/health")
    print("=" * 60)
    print("\n💡 Usage:")
    print("1. Open http://localhost:5000 in your browser")
    print("2. Enter a property address (e.g., '7709 Palmbrook Dr, Tampa, FL 33615')")
    print("3. Click 'Search Properties' to get real results")
    print("4. View results in Zillow/REAPI tabs or download JSON")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Start the Flask app
    try:
        from app import app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🏠 PropertyDetails v6.2 - Real Estate Search Engine")
    print("=" * 60)
    
    if not check_requirements():
        print("\n❌ Requirements check failed. Please fix the issues above.")
        sys.exit(1)
    
    start_application()

if __name__ == "__main__":
    main() 