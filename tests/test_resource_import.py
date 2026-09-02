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


def test_datasets_v1_branch_import():
    from foundry_sdk.v1.datasets.branch import BranchClient

    assert BranchClient is not None


def test_datasets_v1_dataset_import():
    from foundry_sdk.v1.datasets.dataset import DatasetClient

    assert DatasetClient is not None


def test_datasets_v1_file_import():
    from foundry_sdk.v1.datasets.file import FileClient

    assert FileClient is not None


def test_datasets_v1_transaction_import():
    from foundry_sdk.v1.datasets.transaction import TransactionClient

    assert TransactionClient is not None


def test_ontologies_v1_action_import():
    from foundry_sdk.v1.ontologies.action import ActionClient

    assert ActionClient is not None


def test_ontologies_v1_action_type_import():
    from foundry_sdk.v1.ontologies.action_type import ActionTypeClient

    assert ActionTypeClient is not None


def test_ontologies_v1_attachment_import():
    from foundry_sdk.v1.ontologies.attachment import AttachmentClient

    assert AttachmentClient is not None


def test_ontologies_v1_object_type_import():
    from foundry_sdk.v1.ontologies.object_type import ObjectTypeClient

    assert ObjectTypeClient is not None


def test_ontologies_v1_ontology_import():
    from foundry_sdk.v1.ontologies.ontology import OntologyClient

    assert OntologyClient is not None


def test_ontologies_v1_ontology_object_import():
    from foundry_sdk.v1.ontologies.ontology_object import OntologyObjectClient

    assert OntologyObjectClient is not None


def test_ontologies_v1_query_import():
    from foundry_sdk.v1.ontologies.query import QueryClient

    assert QueryClient is not None


def test_ontologies_v1_query_type_import():
    from foundry_sdk.v1.ontologies.query_type import QueryTypeClient

    assert QueryTypeClient is not None


def test_admin_v2_authentication_provider_import():
    from foundry_sdk.v2.admin.authentication_provider import (
        AuthenticationProviderClient,
    )

    assert AuthenticationProviderClient is not None


def test_admin_v2_cbac_banner_import():
    from foundry_sdk.v2.admin.cbac_banner import CbacBannerClient

    assert CbacBannerClient is not None


def test_admin_v2_cbac_marking_restrictions_import():
    from foundry_sdk.v2.admin.cbac_marking_restrictions import (
        CbacMarkingRestrictionsClient,
    )

    assert CbacMarkingRestrictionsClient is not None


def test_admin_v2_enrollment_import():
    from foundry_sdk.v2.admin.enrollment import EnrollmentClient

    assert EnrollmentClient is not None


def test_admin_v2_enrollment_role_assignment_import():
    from foundry_sdk.v2.admin.enrollment_role_assignment import (
        EnrollmentRoleAssignmentClient,
    )

    assert EnrollmentRoleAssignmentClient is not None


def test_admin_v2_group_import():
    from foundry_sdk.v2.admin.group import GroupClient

    assert GroupClient is not None


def test_admin_v2_group_member_import():
    from foundry_sdk.v2.admin.group_member import GroupMemberClient

    assert GroupMemberClient is not None


def test_admin_v2_group_membership_import():
    from foundry_sdk.v2.admin.group_membership import GroupMembershipClient

    assert GroupMembershipClient is not None


def test_admin_v2_group_membership_expiration_policy_import():
    from foundry_sdk.v2.admin.group_membership_expiration_policy import (
        GroupMembershipExpirationPolicyClient,
    )

    assert GroupMembershipExpirationPolicyClient is not None


def test_admin_v2_group_provider_info_import():
    from foundry_sdk.v2.admin.group_provider_info import GroupProviderInfoClient

    assert GroupProviderInfoClient is not None


def test_admin_v2_host_import():
    from foundry_sdk.v2.admin.host import HostClient

    assert HostClient is not None


def test_admin_v2_marking_import():
    from foundry_sdk.v2.admin.marking import MarkingClient

    assert MarkingClient is not None


def test_admin_v2_marking_category_import():
    from foundry_sdk.v2.admin.marking_category import MarkingCategoryClient

    assert MarkingCategoryClient is not None


def test_admin_v2_marking_category_permissions_import():
    from foundry_sdk.v2.admin.marking_category_permissions import (
        MarkingCategoryPermissionsClient,
    )

    assert MarkingCategoryPermissionsClient is not None


def test_admin_v2_marking_member_import():
    from foundry_sdk.v2.admin.marking_member import MarkingMemberClient

    assert MarkingMemberClient is not None


def test_admin_v2_marking_role_assignment_import():
    from foundry_sdk.v2.admin.marking_role_assignment import MarkingRoleAssignmentClient

    assert MarkingRoleAssignmentClient is not None


def test_admin_v2_organization_import():
    from foundry_sdk.v2.admin.organization import OrganizationClient

    assert OrganizationClient is not None


def test_admin_v2_organization_guest_member_import():
    from foundry_sdk.v2.admin.organization_guest_member import (
        OrganizationGuestMemberClient,
    )

    assert OrganizationGuestMemberClient is not None


def test_admin_v2_organization_role_assignment_import():
    from foundry_sdk.v2.admin.organization_role_assignment import (
        OrganizationRoleAssignmentClient,
    )

    assert OrganizationRoleAssignmentClient is not None


def test_admin_v2_role_import():
    from foundry_sdk.v2.admin.role import RoleClient

    assert RoleClient is not None


def test_admin_v2_user_import():
    from foundry_sdk.v2.admin.user import UserClient

    assert UserClient is not None


def test_admin_v2_user_provider_info_import():
    from foundry_sdk.v2.admin.user_provider_info import UserProviderInfoClient

    assert UserProviderInfoClient is not None


def test_aip_agents_v2_agent_import():
    from foundry_sdk.v2.aip_agents.agent import AgentClient

    assert AgentClient is not None


def test_aip_agents_v2_agent_version_import():
    from foundry_sdk.v2.aip_agents.agent_version import AgentVersionClient

    assert AgentVersionClient is not None


def test_aip_agents_v2_content_import():
    from foundry_sdk.v2.aip_agents.content import ContentClient

    assert ContentClient is not None


def test_aip_agents_v2_session_import():
    from foundry_sdk.v2.aip_agents.session import SessionClient

    assert SessionClient is not None


def test_aip_agents_v2_session_trace_import():
    from foundry_sdk.v2.aip_agents.session_trace import SessionTraceClient

    assert SessionTraceClient is not None


def test_audit_v2_log_file_import():
    from foundry_sdk.v2.audit.log_file import LogFileClient

    assert LogFileClient is not None


def test_audit_v2_organization_import():
    from foundry_sdk.v2.audit.organization import OrganizationClient

    assert OrganizationClient is not None


def test_checkpoints_v2_record_import():
    from foundry_sdk.v2.checkpoints.record import RecordClient

    assert RecordClient is not None


def test_connectivity_v2_connection_import():
    from foundry_sdk.v2.connectivity.connection import ConnectionClient

    assert ConnectionClient is not None


def test_connectivity_v2_file_import_import():
    from foundry_sdk.v2.connectivity.file_import import FileImportClient

    assert FileImportClient is not None


def test_connectivity_v2_table_import_import():
    from foundry_sdk.v2.connectivity.table_import import TableImportClient

    assert TableImportClient is not None


def test_connectivity_v2_virtual_table_import():
    from foundry_sdk.v2.connectivity.virtual_table import VirtualTableClient

    assert VirtualTableClient is not None


def test_data_health_v2_check_import():
    from foundry_sdk.v2.data_health.check import CheckClient

    assert CheckClient is not None


def test_data_health_v2_check_report_import():
    from foundry_sdk.v2.data_health.check_report import CheckReportClient

    assert CheckReportClient is not None


def test_datasets_v2_branch_import():
    from foundry_sdk.v2.datasets.branch import BranchClient

    assert BranchClient is not None


def test_datasets_v2_dataset_import():
    from foundry_sdk.v2.datasets.dataset import DatasetClient

    assert DatasetClient is not None


def test_datasets_v2_file_import():
    from foundry_sdk.v2.datasets.file import FileClient

    assert FileClient is not None


def test_datasets_v2_transaction_import():
    from foundry_sdk.v2.datasets.transaction import TransactionClient

    assert TransactionClient is not None


def test_datasets_v2_view_import():
    from foundry_sdk.v2.datasets.view import ViewClient

    assert ViewClient is not None


def test_filesystem_v2_folder_import():
    from foundry_sdk.v2.filesystem.folder import FolderClient

    assert FolderClient is not None


def test_filesystem_v2_project_import():
    from foundry_sdk.v2.filesystem.project import ProjectClient

    assert ProjectClient is not None


def test_filesystem_v2_project_resource_reference_import():
    from foundry_sdk.v2.filesystem.project_resource_reference import (
        ProjectResourceReferenceClient,
    )

    assert ProjectResourceReferenceClient is not None


def test_filesystem_v2_resource_import():
    from foundry_sdk.v2.filesystem.resource import ResourceClient

    assert ResourceClient is not None


def test_filesystem_v2_resource_role_import():
    from foundry_sdk.v2.filesystem.resource_role import ResourceRoleClient

    assert ResourceRoleClient is not None


def test_filesystem_v2_resource_tag_import():
    from foundry_sdk.v2.filesystem.resource_tag import ResourceTagClient

    assert ResourceTagClient is not None


def test_filesystem_v2_space_import():
    from foundry_sdk.v2.filesystem.space import SpaceClient

    assert SpaceClient is not None


def test_functions_v2_execution_import():
    from foundry_sdk.v2.functions.execution import ExecutionClient

    assert ExecutionClient is not None


def test_functions_v2_query_import():
    from foundry_sdk.v2.functions.query import QueryClient

    assert QueryClient is not None


def test_functions_v2_value_type_import():
    from foundry_sdk.v2.functions.value_type import ValueTypeClient

    assert ValueTypeClient is not None


def test_functions_v2_version_id_import():
    from foundry_sdk.v2.functions.version_id import VersionIdClient

    assert VersionIdClient is not None


def test_language_models_v2_anthropic_model_import():
    from foundry_sdk.v2.language_models.anthropic_model import AnthropicModelClient

    assert AnthropicModelClient is not None


def test_language_models_v2_open_ai_model_import():
    from foundry_sdk.v2.language_models.open_ai_model import OpenAiModelClient

    assert OpenAiModelClient is not None


def test_media_sets_v2_media_set_import():
    from foundry_sdk.v2.media_sets.media_set import MediaSetClient

    assert MediaSetClient is not None


def test_models_v2_experiment_import():
    from foundry_sdk.v2.models.experiment import ExperimentClient

    assert ExperimentClient is not None


def test_models_v2_experiment_artifact_table_import():
    from foundry_sdk.v2.models.experiment_artifact_table import (
        ExperimentArtifactTableClient,
    )

    assert ExperimentArtifactTableClient is not None


def test_models_v2_experiment_series_import():
    from foundry_sdk.v2.models.experiment_series import ExperimentSeriesClient

    assert ExperimentSeriesClient is not None


def test_models_v2_live_deployment_import():
    from foundry_sdk.v2.models.live_deployment import LiveDeploymentClient

    assert LiveDeploymentClient is not None


def test_models_v2_model_import():
    from foundry_sdk.v2.models.model import ModelClient

    assert ModelClient is not None


def test_models_v2_model_function_import():
    from foundry_sdk.v2.models.model_function import ModelFunctionClient

    assert ModelFunctionClient is not None


def test_models_v2_model_studio_import():
    from foundry_sdk.v2.models.model_studio import ModelStudioClient

    assert ModelStudioClient is not None


def test_models_v2_model_studio_config_version_import():
    from foundry_sdk.v2.models.model_studio_config_version import (
        ModelStudioConfigVersionClient,
    )

    assert ModelStudioConfigVersionClient is not None


def test_models_v2_model_studio_run_import():
    from foundry_sdk.v2.models.model_studio_run import ModelStudioRunClient

    assert ModelStudioRunClient is not None


def test_models_v2_model_studio_trainer_import():
    from foundry_sdk.v2.models.model_studio_trainer import ModelStudioTrainerClient

    assert ModelStudioTrainerClient is not None


def test_models_v2_model_version_import():
    from foundry_sdk.v2.models.model_version import ModelVersionClient

    assert ModelVersionClient is not None


def test_ontologies_v2_action_import():
    from foundry_sdk.v2.ontologies.action import ActionClient

    assert ActionClient is not None


def test_ontologies_v2_action_type_import():
    from foundry_sdk.v2.ontologies.action_type import ActionTypeClient

    assert ActionTypeClient is not None


def test_ontologies_v2_action_type_full_metadata_import():
    from foundry_sdk.v2.ontologies.action_type_full_metadata import (
        ActionTypeFullMetadataClient,
    )

    assert ActionTypeFullMetadataClient is not None


def test_ontologies_v2_attachment_import():
    from foundry_sdk.v2.ontologies.attachment import AttachmentClient

    assert AttachmentClient is not None


def test_ontologies_v2_attachment_property_import():
    from foundry_sdk.v2.ontologies.attachment_property import AttachmentPropertyClient

    assert AttachmentPropertyClient is not None


def test_ontologies_v2_cipher_text_property_import():
    from foundry_sdk.v2.ontologies.cipher_text_property import CipherTextPropertyClient

    assert CipherTextPropertyClient is not None


def test_ontologies_v2_geotemporal_series_property_import():
    from foundry_sdk.v2.ontologies.geotemporal_series_property import (
        GeotemporalSeriesPropertyClient,
    )

    assert GeotemporalSeriesPropertyClient is not None


def test_ontologies_v2_linked_object_import():
    from foundry_sdk.v2.ontologies.linked_object import LinkedObjectClient

    assert LinkedObjectClient is not None


def test_ontologies_v2_media_reference_property_import():
    from foundry_sdk.v2.ontologies.media_reference_property import (
        MediaReferencePropertyClient,
    )

    assert MediaReferencePropertyClient is not None


def test_ontologies_v2_object_type_import():
    from foundry_sdk.v2.ontologies.object_type import ObjectTypeClient

    assert ObjectTypeClient is not None


def test_ontologies_v2_ontology_import():
    from foundry_sdk.v2.ontologies.ontology import OntologyClient

    assert OntologyClient is not None


def test_ontologies_v2_ontology_interface_import():
    from foundry_sdk.v2.ontologies.ontology_interface import OntologyInterfaceClient

    assert OntologyInterfaceClient is not None


def test_ontologies_v2_ontology_object_import():
    from foundry_sdk.v2.ontologies.ontology_object import OntologyObjectClient

    assert OntologyObjectClient is not None


def test_ontologies_v2_ontology_object_set_import():
    from foundry_sdk.v2.ontologies.ontology_object_set import OntologyObjectSetClient

    assert OntologyObjectSetClient is not None


def test_ontologies_v2_ontology_scenario_import():
    from foundry_sdk.v2.ontologies.ontology_scenario import OntologyScenarioClient

    assert OntologyScenarioClient is not None


def test_ontologies_v2_ontology_transaction_import():
    from foundry_sdk.v2.ontologies.ontology_transaction import OntologyTransactionClient

    assert OntologyTransactionClient is not None


def test_ontologies_v2_ontology_value_type_import():
    from foundry_sdk.v2.ontologies.ontology_value_type import OntologyValueTypeClient

    assert OntologyValueTypeClient is not None


def test_ontologies_v2_query_import():
    from foundry_sdk.v2.ontologies.query import QueryClient

    assert QueryClient is not None


def test_ontologies_v2_query_type_import():
    from foundry_sdk.v2.ontologies.query_type import QueryTypeClient

    assert QueryTypeClient is not None


def test_ontologies_v2_time_series_property_v2_import():
    from foundry_sdk.v2.ontologies.time_series_property_v2 import (
        TimeSeriesPropertyV2Client,
    )

    assert TimeSeriesPropertyV2Client is not None


def test_ontologies_v2_time_series_value_bank_property_import():
    from foundry_sdk.v2.ontologies.time_series_value_bank_property import (
        TimeSeriesValueBankPropertyClient,
    )

    assert TimeSeriesValueBankPropertyClient is not None


def test_orchestration_v2_build_import():
    from foundry_sdk.v2.orchestration.build import BuildClient

    assert BuildClient is not None


def test_orchestration_v2_job_import():
    from foundry_sdk.v2.orchestration.job import JobClient

    assert JobClient is not None


def test_orchestration_v2_schedule_import():
    from foundry_sdk.v2.orchestration.schedule import ScheduleClient

    assert ScheduleClient is not None


def test_orchestration_v2_schedule_run_import():
    from foundry_sdk.v2.orchestration.schedule_run import ScheduleRunClient

    assert ScheduleRunClient is not None


def test_orchestration_v2_schedule_version_import():
    from foundry_sdk.v2.orchestration.schedule_version import ScheduleVersionClient

    assert ScheduleVersionClient is not None


def test_sql_queries_v2_sql_query_import():
    from foundry_sdk.v2.sql_queries.sql_query import SqlQueryClient

    assert SqlQueryClient is not None


def test_streams_v2_dataset_import():
    from foundry_sdk.v2.streams.dataset import DatasetClient

    assert DatasetClient is not None


def test_streams_v2_stream_import():
    from foundry_sdk.v2.streams.stream import StreamClient

    assert StreamClient is not None


def test_streams_v2_subscriber_import():
    from foundry_sdk.v2.streams.subscriber import SubscriberClient

    assert SubscriberClient is not None


def test_third_party_applications_v2_third_party_application_import():
    from foundry_sdk.v2.third_party_applications.third_party_application import (
        ThirdPartyApplicationClient,
    )

    assert ThirdPartyApplicationClient is not None


def test_third_party_applications_v2_version_import():
    from foundry_sdk.v2.third_party_applications.version import VersionClient

    assert VersionClient is not None


def test_third_party_applications_v2_website_import():
    from foundry_sdk.v2.third_party_applications.website import WebsiteClient

    assert WebsiteClient is not None


def test_widgets_v2_dev_mode_settings_import():
    from foundry_sdk.v2.widgets.dev_mode_settings import DevModeSettingsClient

    assert DevModeSettingsClient is not None


def test_widgets_v2_dev_mode_settings_v2_import():
    from foundry_sdk.v2.widgets.dev_mode_settings_v2 import DevModeSettingsV2Client

    assert DevModeSettingsV2Client is not None


def test_widgets_v2_release_import():
    from foundry_sdk.v2.widgets.release import ReleaseClient

    assert ReleaseClient is not None


def test_widgets_v2_repository_import():
    from foundry_sdk.v2.widgets.repository import RepositoryClient

    assert RepositoryClient is not None


def test_widgets_v2_widget_set_import():
    from foundry_sdk.v2.widgets.widget_set import WidgetSetClient

    assert WidgetSetClient is not None


def test_endpoints_v3_endpoint_set_import():
    from foundry_sdk.v3.endpoints.endpoint_set import EndpointSetClient

    assert EndpointSetClient is not None


def test_endpoints_v3_endpoint_set_endpoint_import():
    from foundry_sdk.v3.endpoints.endpoint_set_endpoint import EndpointSetEndpointClient

    assert EndpointSetEndpointClient is not None


def test_endpoints_v3_endpoint_set_version_import():
    from foundry_sdk.v3.endpoints.endpoint_set_version import EndpointSetVersionClient

    assert EndpointSetVersionClient is not None


def test_orchestrator_v3_process_execution_import():
    from foundry_sdk.v3.orchestrator.process_execution import ProcessExecutionClient

    assert ProcessExecutionClient is not None


def test_orchestrator_v3_process_execution_signal_import():
    from foundry_sdk.v3.orchestrator.process_execution_signal import (
        ProcessExecutionSignalClient,
    )

    assert ProcessExecutionSignalClient is not None
