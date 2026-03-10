# CreateSubscriberRequest

CreateSubscriberRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**subscriber_id** | SubscriberId | Yes |  |
**read_position** | Optional[ReadPosition] | No | Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
