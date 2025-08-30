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


from typing import TYPE_CHECKING
from typing import Any
from typing import Optional

if TYPE_CHECKING:
    import duckdb  # type: ignore
    import pandas as pd  # type: ignore
    import polars as pl  # type: ignore
    import pyarrow as pa  # type: ignore


def _error_msg(package_required: str, convert_to: str, extra_dependency: str):
    return (
        f"{package_required} is required to convert to {convert_to}. If you are using pip, "
        f"you can install it with 'pip install foundry_sdk[{extra_dependency}]'."
    )


class TableResponse(bytes):
    """A generic class for deserializing an Arrow Table into various formats."""

    _arrow_table: Optional["pa.Table"]

    def __new__(cls, arrow_bytes: bytes):
        instance = super().__new__(cls, arrow_bytes)
        instance._arrow_table = None
        return instance

    def to_pandas(self) -> "pd.DataFrame":
        """Convert the bytes into a Pandas DataFrame."""
        try:
            return self._get_arrow_table("pandas").to_pandas()
        except ImportError:
            raise ImportError(_error_msg("pandas", "a Pandas DataFrame", "pandas"))

    def to_polars(self) -> "pl.DataFrame":
        """Convert the bytes into a Polars DataFrame."""
        try:
            import polars as pl

            return pl.DataFrame(self._get_arrow_table("polars"))
        except ImportError:
            raise ImportError(_error_msg("polars", "a Polars DataFrame", "polars"))

    def to_pyarrow(self) -> "pa.Table":
        """Convert the bytes into an Arrow Table."""
        return self._get_arrow_table("pyarrow")

    def to_duckdb(self) -> "duckdb.DuckDBPyRelation":
        """Convert the bytes into a DuckDB relation."""
        try:
            import duckdb

            return duckdb.from_arrow(self._get_arrow_table("duckdb"))
        except ImportError:
            raise ImportError(_error_msg("duckdb", "a DuckDB relation", "duckdb"))

    def _get_arrow_table(self, extra_dependency: str) -> "pa.Table":
        try:
            import pyarrow as pa
        except ImportError:
            raise ImportError(_error_msg("pyarrow", "an Arrow Table", extra_dependency))

        if self._arrow_table is None:
            self._arrow_table = pa.ipc.open_stream(self).read_all()

        return self._arrow_table
