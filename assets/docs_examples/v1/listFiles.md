### Read the contents of a file from a dataset (by exploration / listing)

```python
import foundry

foundry_client = foundry.FoundryV1Client(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

result = foundry_client.datasets.Dataset.File.list(dataset_rid="...")

if result.data:
    file_path = result.data[0].path

    print(foundry_client.datasets.Dataset.File.read(
        dataset_rid="...", file_path=file_path
    ))
```

```
b'Hello!'
```
