import pytest
from foundry import ConfidentialClientAuth
from foundry._errors.not_authenticated import NotAuthenticated


def test_fails_no_escopes():
    with pytest.raises(ValueError) as info:
        ConfidentialClientAuth(
            client_id="123",
            client_secret="abc",
            hostname="hey.com",
            scopes=[],
        )

    assert (
        str(info.value) == "You have not provided any scopes. At least one scope must be provided."
    )


def test_can_pass_config():
    config = ConfidentialClientAuth(
        client_id="123",
        client_secret="abc",
        hostname="hey.com",
        scopes=["hello"],
    )

    assert config._hostname == "hey.com"
    assert config._client_id == "123"
    assert config._client_secret == "abc"

    with pytest.raises(NotAuthenticated) as info:
        config.get_token()

    assert str(info.value) == "Client has not been authenticated."
