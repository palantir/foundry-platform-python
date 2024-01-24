#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import subprocess

gitversion = subprocess.check_output("git describe --tags --abbrev=0".split()).decode().strip()

print(f"Setting version to {gitversion}...")

path = "foundry/_versions.py"

with open(path, "r") as f:
    content = f.read()

content = content.replace('__version__ = "0.0.0"', f'__version__ = "{gitversion}"')

with open(path, "w") as f:
    f.write(content)

print("Done!")
