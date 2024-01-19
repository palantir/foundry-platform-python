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

import os
import re


def test_no_remaining_references():
    try:
        # If this works, it means we are in the generator repository
        from scripts.util import DOCS_PATH
    except ModuleNotFoundError:
        # Otherwise, the docs are just located in the docs folder
        # This happens when we are running the tests in the generated SDK
        DOCS_PATH = "docs"

    # Recursively search for .md files in the DOCS_PATH
    for root, _, files in os.walk(DOCS_PATH):
        for file in files:
            if not file.endswith(".md"):
                continue

            with open(os.path.join(root, file), "r") as f:
                docs = f.read()
                assert re.match(r"[A-Z_]+\([a-z_]+\)", docs) is None
