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


from foundry.v2.streams.errors._cannot_create_streaming_dataset_in_user_folder import (
    CannotCreateStreamingDatasetInUserFolder,
)  # NOQA
from foundry.v2.streams.errors._cannot_write_to_trashed_stream import (
    CannotWriteToTrashedStream,
)  # NOQA
from foundry.v2.streams.errors._create_stream_permission_denied import (
    CreateStreamPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._create_streaming_dataset_permission_denied import (
    CreateStreamingDatasetPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._failed_to_process_binary_record import (
    FailedToProcessBinaryRecord,
)  # NOQA
from foundry.v2.streams.errors._invalid_stream_no_schema import InvalidStreamNoSchema
from foundry.v2.streams.errors._invalid_stream_type import InvalidStreamType
from foundry.v2.streams.errors._publish_binary_record_to_stream_permission_denied import (
    PublishBinaryRecordToStreamPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._publish_record_to_stream_permission_denied import (
    PublishRecordToStreamPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._publish_records_to_stream_permission_denied import (
    PublishRecordsToStreamPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._record_does_not_match_stream_schema import (
    RecordDoesNotMatchStreamSchema,
)  # NOQA
from foundry.v2.streams.errors._record_too_large import RecordTooLarge
from foundry.v2.streams.errors._reset_stream_permission_denied import (
    ResetStreamPermissionDenied,
)  # NOQA
from foundry.v2.streams.errors._stream_not_found import StreamNotFound
from foundry.v2.streams.errors._view_not_found import ViewNotFound

__all__ = [
    "CannotCreateStreamingDatasetInUserFolder",
    "CannotWriteToTrashedStream",
    "CreateStreamPermissionDenied",
    "CreateStreamingDatasetPermissionDenied",
    "FailedToProcessBinaryRecord",
    "InvalidStreamNoSchema",
    "InvalidStreamType",
    "PublishBinaryRecordToStreamPermissionDenied",
    "PublishRecordToStreamPermissionDenied",
    "PublishRecordsToStreamPermissionDenied",
    "RecordDoesNotMatchStreamSchema",
    "RecordTooLarge",
    "ResetStreamPermissionDenied",
    "StreamNotFound",
    "ViewNotFound",
]
