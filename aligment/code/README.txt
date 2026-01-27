Step 1. Check what venv you are running on - it should be specific to this project folder:
import sys
print(sys.executable)

Step 1A. Activate virtual environment in terminal with: venv\Scripts\activate

Step 2. Install function packages in venv with: pip install -e /path/to/functions
Step 2.5. Should say successfully installed common_funcs-0.1

Step 3. Call functions using: from alignment_funcs.[function file] import [function] or from verify_funcs.[functio file] import [function]