from foundry._core.auth_utils import Auth
from foundry._namespaces.namespaces import Datasets
from foundry._namespaces.namespaces import Ontologies
from foundry.api_client import ApiClient
from foundry._errors.environment_not_configured import EnvironmentNotConfigured


class FoundryClient:
    """
    The Foundry API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    """

    def __init__(self, auth: Auth, hostname: str):
        api_client = ApiClient(auth=auth, hostname=hostname)
        self.datasets = Datasets(api_client=api_client)
        self.ontologies = Ontologies(api_client=api_client)
