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

from typing import Any

PropertyValue = Any
"""
Represents the value of a property in the following format.

| Type            | JSON encoding                                               | Example                                                                                            |
|---------------- |-------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Array           | array                                                       | `["alpha", "bravo", "charlie"]`                                                                    |
| Attachment      | JSON encoded `AttachmentProperty` object                    | `{"rid":"ri.blobster.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"}`                       |
| Boolean         | boolean                                                     | `true`                                                                                             |
| Byte            | number                                                      | `31`                                                                                               |
| CipherText      | string                                                      | `"CIPHER::ri.bellaso.main.cipher-channel.e414ab9e-b606-499a-a0e1-844fa296ba7e::unzjs3VifsTxuIpf1fH1CJ7OaPBr2bzMMdozPaZJtCii8vVG60yXIEmzoOJaEl9mfFFe::CIPHER"`                                                                                                                                                                                        |        
| Date            | ISO 8601 extended local date string                         | `"2021-05-01"`                                                                                     |
| Decimal         | string                                                      | `"2.718281828"`                                                                                    |
| Double          | number                                                      | `3.14159265`                                                                                       |
| Float           | number                                                      | `3.14159265`                                                                                       |
| GeoPoint        | geojson                                                     | `{"type":"Point","coordinates":[102.0,0.5]}`                                                       |
| GeoShape        | geojson                                                     | `{"type":"LineString","coordinates":[[102.0,0.0],[103.0,1.0],[104.0,0.0],[105.0,1.0]]}`            |
| Integer         | number                                                      | `238940`                                                                                           |
| Long            | string                                                      | `"58319870951433"`                                                                                 |
| MediaReference  | JSON encoded `MediaReference` object                        | `{"mimeType":"application/pdf","reference":{"type":"mediaSetViewItem","mediaSetViewItem":{"mediaSetRid":"ri.mio.main.media-set.4153d42f-ca4b-4e42-8ca5-8e6aa7edb642","mediaSetViewRid":"ri.mio.main.view.82a798ad-d637-4595-acc6-987bcf16629b","mediaItemRid":"ri.mio.main.media-item.001ec98b-1620-4814-9e17-8e9c4e536225"}}}`                       |
| Short           | number                                                      | `8739`                                                                                             |
| String          | string                                                      | `"Call me Ishmael"`                                                                                |
| Struct          | JSON object of struct field API name -> value               | {"firstName": "Alex", "lastName": "Karp"}                                                          |
| Timestamp       | ISO 8601 extended offset date-time string in UTC zone       | `"2021-01-04T05:00:00Z"`                                                                           |
| Timeseries      | JSON encoded `TimeseriesProperty` object or seriesId string | `{"seriesId": "wellPressureSeriesId", "syncRid": ri.time-series-catalog.main.sync.04f5ac1f-91bf-44f9-a51f-4f34e06e42df"}` or `{"templateRid": "ri.codex-emu.main.template.367cac64-e53b-4653-b111-f61856a63df9", "templateVersion": "0.0.0"}` or `"wellPressureSeriesId"`|                                                                           |

Note that for backwards compatibility, the Boolean, Byte, Double, Float, Integer, and Short types can also be encoded as JSON strings.
"""
