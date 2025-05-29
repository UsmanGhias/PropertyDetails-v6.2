#!/usr/bin/env python3
"""
PropertyDetails v6.2 Web Application
Flask server for the property search interface
"""

from flask import Flask, render_template_string, request, jsonify
import subprocess
import json
import os
import sys
from datetime import datetime

app = Flask(__name__)

# Read the HTML template
def get_html_template():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/')
def index():
    """Serve the main HTML interface"""
    return get_html_template()

@app.route('/api/search', methods=['POST'])
def search_properties():
    """API endpoint to search properties"""
    try:
        data = request.get_json()
        address = data.get('address', '')
        max_properties = data.get('max_properties', 25)
        
        if not address:
            return jsonify({'error': 'Address is required'}), 400
        
        # Run the property search script
        cmd = [sys.executable, 'property_search_v6_2_FINAL.py', address, str(max_properties)]
        
        print(f"🔍 Running command: {' '.join(cmd)}")
        
        # Execute the script
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
        
        if result.returncode != 0:
            print(f"❌ Script failed with error: {result.stderr}")
            return jsonify({'error': f'Script execution failed: {result.stderr}'}), 500
        
        # Find the generated JSON file
        output_lines = result.stdout.split('\n')
        json_filename = None
        
        for line in output_lines:
            if 'Saved to:' in line:
                json_filename = line.split('Saved to:')[1].strip()
                break
        
        if not json_filename or not os.path.exists(json_filename):
            print(f"❌ Output file not found: {json_filename}")
            return jsonify({'error': 'Output file not found'}), 500
        
        # Read the results
        with open(json_filename, 'r') as f:
            results = json.load(f)
        
        print(f"✅ Successfully loaded {results['summary']['total_found']} properties")
        
        return jsonify(results)
        
    except Exception as e:
        print(f"❌ Error in search_properties: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': 'v6.2',
        'timestamp': datetime.now().isoformat(),
        'message': 'PropertyDetails v6.2 API is running'
    })

@app.route('/api/demo')
def demo_endpoint():
    """Demo endpoint for quick testing"""
    try:
        # Run a quick demo search
        cmd = [sys.executable, 'property_search_v6_2_FINAL.py', '7709 Palmbrook Dr, Tampa, FL 33615', '3']
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
        
        if result.returncode == 0:
            # Find the output file
            output_lines = result.stdout.split('\n')
            for line in output_lines:
                if 'Saved to:' in line:
                    json_filename = line.split('Saved to:')[1].strip()
                    if os.path.exists(json_filename):
                        with open(json_filename, 'r') as f:
                            results = json.load(f)
                        return jsonify({
                            'status': 'success',
                            'demo_results': results,
                            'message': 'Demo search completed successfully'
                        })
        
        return jsonify({'status': 'error', 'message': 'Demo search failed'})
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    print("🚀 Starting PropertyDetails v6.2 Web Application")
    
    # Get port from environment variable (for deployment platforms)
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"📍 Server will be available at: http://{host}:{port}")
    print("🔍 API endpoints:")
    print(f"  - Main: http://{host}:{port}/")
    print(f"  - Search: http://{host}:{port}/api/search")
    print(f"  - Health: http://{host}:{port}/api/health")
    print(f"  - Demo: http://{host}:{port}/api/demo")
    
    # Check if required files exist
    required_files = ['property_search_v6_2_FINAL.py', 'TAMPA_PROPERTIES_EXTRACTION_20250528_182304.json']
    for file in required_files:
        if not os.path.exists(file):
            print(f"⚠️  Warning: Required file not found: {file}")
    
    # Run the app
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host=host, port=port) 