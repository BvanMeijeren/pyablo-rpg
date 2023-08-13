import os
import subprocess

def execute_python_file(file_path):
   """Function for running other files as subprocess"""
   try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         print_slow("Execution successful.")
         print_slow("Output:")
         print_slow(completed_process.stdout)
      else:
         print_slow(f"Error: Failed to execute '{file_path}'.")
         print_slow("Error output:")
         print_slow(completed_process.stderr)
   except FileNotFoundError:
      print_slow(f"Error: The file '{file_path}' does not exist.")