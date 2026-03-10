# ReadPosition

Position to start reading from when registering a subscriber or resetting offsets.

- `earliest`: Start reading from the beginning of each partition (offset 0). Use this to
  reprocess all historical data in the stream.
- `latest`: Start reading from the current end of each partition. Use this to skip
  historical data and only process new records arriving after registration.
- `specific`: Start reading from explicit offsets for each partition. Use this for precise
  replay scenarios or to resume from a known checkpoint.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
SpecificPosition | specific
EarliestPosition | earliest
LatestPosition | latest


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
