from foundry._core.utils import remove_prefixes


def test_remove_prefixes():
    assert remove_prefixes("http://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("https://example.com", ["https://", "http://"]) == "example.com"
    assert remove_prefixes("example.com", ["https://", "http://"]) == "example.com"
