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
import time

import pytest

PORT = 8123


@pytest.fixture(scope="session", autouse=True)
def fastapi_server():
    # Start the server
    process = subprocess.Popen(
        ["uvicorn", "tests.server:app", "--host", "127.0.0.1", "--port", str(PORT)]
    )
    time.sleep(2)  # Wait a moment for the server to start

    yield

    # Teardown: Stop the server
    process.terminate()
