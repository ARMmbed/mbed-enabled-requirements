"""
Copyright (c) 2020 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Checks whether URLs in docs are valid or not
# Usage:
# python resources\check-urls.py

import requests
import re
import glob, os

def check_url_exists(url_name):
    request = requests.get(url_name)
    if request.status_code == 200:
        return True # exist
    else:
        return False

def test_url(file_name):
    try:
        file_desc = open(file_name, 'r')
    except IOError as error:
        print("I/O error({0}): {1}".format(error.errno, error.strerror))
        return
    
    data = file_desc.read()
    file_desc.close()
    
    # Search any URL that starts with http
    list_url = re.findall(r'\((https?://[^\s]+)\)', data)
        
    error_check = 0 # by detault, there are no errors
    for i in list_url:
        valid_url = check_url_exists(i)
        if valid_url == False:
            error_check = error_check + 1
            print(" + ", i, "- Not found")
        else:
            print(" + ", i, "- OK")
        
    return error_check

def main():
    
    # Search all .md files in current folder
    os.chdir("./")  
    list_files = glob.glob("*.md")
    
    # Test URLs in all files
    for file in list_files:
        print("\n=== File: %s ===\n" % file)
        
        check_errors = test_url(file)
        
        if check_errors == 0:
            print("\nNo Errors\n") 
        else:
            print("\n", check_errors, "Errors\n") 
           
if __name__ == "__main__":
    main()