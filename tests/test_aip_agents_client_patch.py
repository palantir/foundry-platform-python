import pytest
from foundry_sdk.v2.aip_agents._client import AipAgentsClient
from foundry_sdk.v2.client import FoundryClient
from foundry_sdk._core import HostnameSupplier, Auth


class DummyAuth(Auth):
    def execute(self, *args, **kwargs):
        pass

    def execute_with_token(self, *args, **kwargs):
        pass

    def get_token(self, *args, **kwargs):
        return "dummy"

    def run_with_token(self, *args, **kwargs):
        pass


class DummyHostnameSupplier(HostnameSupplier):
    def get_hostname(self):
        return "https://example.com"

    def get_endpoint(self, endpoint_type):
        return "https://example.com"

    def is_user_supplied(self):
        return True


def test_aip_agents_client_patch():
    auth = DummyAuth()
    hostname = "https://example.palantirfoundry.com"
    config = None

    # Test direct AipAgentsClient instantiation
    client = AipAgentsClient(auth=auth, hostname=hostname, config=config)

    # Verify we can access .Agent multiple times without descriptor errors
    assert hasattr(client, "Agent")
    agent_1 = client.Agent
    agent_2 = client.Agent
    assert agent_1 is agent_2

    # Test via FoundryClient to perfectly mirror user behavior
    foundry_client = FoundryClient(auth=auth, hostname=hostname)

    # Ensure client.aip_agents.Agent returns True for hasattr
    assert hasattr(foundry_client.aip_agents, "Agent")

    # Access multiple times to verify no errors
    foundry_agent_1 = foundry_client.aip_agents.Agent
    foundry_agent_2 = foundry_client.aip_agents.Agent
    assert foundry_agent_1 is foundry_agent_2
