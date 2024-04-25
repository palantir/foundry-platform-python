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


from __future__ import annotations

from pydantic import StrictStr

ValueType = StrictStr
"""
A string indicating the type of each data value. Note that these types can be nested, for example an array of
structs.

| Type                | JSON value                                                                                                        |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| Array               | `Array<T>`, where `T` is the type of the array elements, e.g. `Array<String>`.                                    |
| Attachment          | `Attachment`                                                                                                      |
| Boolean             | `Boolean`                                                                                                         |
| Byte                | `Byte`                                                                                                            |
| Date                | `LocalDate`                                                                                                       |
| Decimal             | `Decimal`                                                                                                         |
| Double              | `Double`                                                                                                          |
| Float               | `Float`                                                                                                           |
| Integer             | `Integer`                                                                                                         |
| Long                | `Long`                                                                                                            |
| Marking             | `Marking`                                                                                                         |
| OntologyObject      | `OntologyObject<T>` where `T` is the API name of the referenced object type.                                      |
| Short               | `Short`                                                                                                           |
| String              | `String`                                                                                                          |
| Struct              | `Struct<T>` where `T` contains field name and type pairs, e.g. `Struct<{ firstName: String, lastName: string }>`  |
| Timeseries          | `TimeSeries<T>` where `T` is either `String` for an enum series or `Double` for a numeric series.                 |
| Timestamp           | `Timestamp`                                                                                                       |
"""
