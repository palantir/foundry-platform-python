import timeit

import pytest


def test_import_v1_client_performance():
    import_time = timeit.timeit(
        stmt="import foundry.v1", setup="import sys; sys.modules.pop('foundry.v1', None);", number=1
    )

    assert import_time < 0.25


def test_client_v1_initialization_performance():
    init_time = timeit.timeit(
        stmt="foundry.v1.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost')",
        setup="import sys; sys.modules.pop('foundry.v1', None);import foundry; import foundry.v1",
        number=1,
    )

    assert init_time < 0.25


def test_datasets_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v1.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').datasets",
        setup="import sys; sys.modules.pop('foundry.v1', None);import foundry; import foundry.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_datasets_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v1.datasets.models",
        setup="import sys; sys.modules.pop('foundry.v1.datasets.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_ontologies_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v1.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').ontologies",
        setup="import sys; sys.modules.pop('foundry.v1', None);import foundry; import foundry.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_ontologies_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v1.ontologies.models",
        setup="import sys; sys.modules.pop('foundry.v1.ontologies.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_import_v2_client_performance():
    import_time = timeit.timeit(
        stmt="import foundry.v2", setup="import sys; sys.modules.pop('foundry.v2', None);", number=1
    )

    assert import_time < 0.25


def test_client_v2_initialization_performance():
    init_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost')",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_time < 0.25


def test_admin_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').admin",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_admin_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.admin.models",
        setup="import sys; sys.modules.pop('foundry.v2.admin.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_aip_agents_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').aip_agents",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_aip_agents_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.aip_agents.models",
        setup="import sys; sys.modules.pop('foundry.v2.aip_agents.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_connectivity_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').connectivity",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_connectivity_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.connectivity.models",
        setup="import sys; sys.modules.pop('foundry.v2.connectivity.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_datasets_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').datasets",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_datasets_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.datasets.models",
        setup="import sys; sys.modules.pop('foundry.v2.datasets.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_filesystem_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').filesystem",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_filesystem_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.filesystem.models",
        setup="import sys; sys.modules.pop('foundry.v2.filesystem.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_functions_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').functions",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_functions_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.functions.models",
        setup="import sys; sys.modules.pop('foundry.v2.functions.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_media_sets_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').media_sets",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_media_sets_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.media_sets.models",
        setup="import sys; sys.modules.pop('foundry.v2.media_sets.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_ontologies_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').ontologies",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_ontologies_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.ontologies.models",
        setup="import sys; sys.modules.pop('foundry.v2.ontologies.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_orchestration_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').orchestration",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_orchestration_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.orchestration.models",
        setup="import sys; sys.modules.pop('foundry.v2.orchestration.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_sql_queries_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').sql_queries",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_sql_queries_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.sql_queries.models",
        setup="import sys; sys.modules.pop('foundry.v2.sql_queries.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_streams_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').streams",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_streams_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.streams.models",
        setup="import sys; sys.modules.pop('foundry.v2.streams.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_third_party_applications_v2_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="foundry.v2.FoundryClient(foundry.UserTokenAuth(token='token'), hostname='localhost').third_party_applications",
        setup="import sys; sys.modules.pop('foundry.v2', None);import foundry; import foundry.v2",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_third_party_applications_v2_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import foundry.v2.third_party_applications.models",
        setup="import sys; sys.modules.pop('foundry.v2.third_party_applications.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5
