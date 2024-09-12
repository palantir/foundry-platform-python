# ScheduleRunResult

The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[ScheduleRunSubmitted](ScheduleRunSubmitted.md) | submitted
[ScheduleRunIgnored](ScheduleRunIgnored.md) | ignored
[ScheduleRunError](ScheduleRunError.md) | error


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
