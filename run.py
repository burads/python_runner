import os
work_dir = os.getenv("PYTHON_WORKDIR")
req_file = os.getenv("PYTHON_REQUIREMENTS_FILE")
file = os.getenv("PYTHON_FILE")
if req_file:
    full_path = os.path.join(work_dir, req_file)
    if os.path.exists(full_path):
        os.system("pip install --no-cache-dir -r " + full_path)
full_path = os.path.join(work_dir, file)
os.system("python "+full_path)
