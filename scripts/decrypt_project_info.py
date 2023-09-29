#!/usr/bin/env python

# Copyright 2023 Google
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import plistlib
import json

# Check if the PLIST file path was provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python read_plist.py <path_to_googleService-info.plist>")
    sys.exit(1)

plist_file_path = sys.argv[1]

# Read the PLIST file
try:
    with open(plist_file_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    # Extract the 'project_id' field only for confidentiality
    project_id = plist_data.get('PROJECT_ID')

    if project_id:
        with open('Firestore/Example/App/project_info.json', 'w') as json_file:
            json.dump({'project_id': project_id}, json_file)
    else:
        print("PROJECT_ID key not found in the plist file.")
except FileNotFoundError:
    print(f"File not found: {plist_file_path}")
except Exception:
    print("An error occurred.")
