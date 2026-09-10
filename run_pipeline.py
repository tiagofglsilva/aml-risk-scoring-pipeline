import os
import subprocess
import sys

# Define the project root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    """Executes a script from the 'scripts' folder sequentially."""
    script_path = os.path.join(BASE_DIR, "scripts", script_name)
    print("\n" + "=" * 50)
    print(f"▶️  Running: {script_name}")
    print("=" * 50)
    
    # Run the script using the currently active Python interpreter
    result = subprocess.run([sys.executable, script_path])
    
    if result.returncode != 0:
        print(f"\n❌ Error executing {script_name}. Pipeline aborted.")
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 Starting the AML Risk Scoring Pipeline...")
    
    # Updated to match '01_setup_db.py'
    run_script("01_setup_db.py")
    run_script("02_risk_analysis.py")
    run_script("03_visualizations.py")
    
    print("\n✅ Pipeline executed successfully!")
    print("📁 Database updated at: data/aml.db")
    print("📊 Reports and visualizations generated at: reports/")