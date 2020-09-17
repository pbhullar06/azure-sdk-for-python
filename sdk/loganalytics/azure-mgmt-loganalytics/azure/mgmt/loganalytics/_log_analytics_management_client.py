# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import LogAnalyticsManagementClientConfiguration
from .operations import DataExportsOperations
from .operations import DataSourcesOperations
from .operations import IntelligencePacksOperations
from .operations import LinkedServicesOperations
from .operations import LinkedStorageAccountsOperations
from .operations import ManagementGroupsOperations
from .operations import Operations
from .operations import OperationStatusesOperations
from .operations import SharedKeysOperations
from .operations import UsagesOperations
from .operations import WorkspacesOperations
from .operations import DeletedWorkspacesOperations
from .operations import ClustersOperations
from .operations import StorageInsightConfigsOperations
from .operations import SavedSearchesOperations
from .operations import AvailableServiceTiersOperations
from .operations import GatewaysOperations
from .operations import SchemaOperations
from .operations import WorkspacePurgeOperations
from .operations import TablesOperations
from . import models


class LogAnalyticsManagementClient(SDKClient):
    """The Log Analytics Client.

    :ivar config: Configuration for client.
    :vartype config: LogAnalyticsManagementClientConfiguration

    :ivar data_exports: DataExports operations
    :vartype data_exports: azure.mgmt.loganalytics.operations.DataExportsOperations
    :ivar data_sources: DataSources operations
    :vartype data_sources: azure.mgmt.loganalytics.operations.DataSourcesOperations
    :ivar intelligence_packs: IntelligencePacks operations
    :vartype intelligence_packs: azure.mgmt.loganalytics.operations.IntelligencePacksOperations
    :ivar linked_services: LinkedServices operations
    :vartype linked_services: azure.mgmt.loganalytics.operations.LinkedServicesOperations
    :ivar linked_storage_accounts: LinkedStorageAccounts operations
    :vartype linked_storage_accounts: azure.mgmt.loganalytics.operations.LinkedStorageAccountsOperations
    :ivar management_groups: ManagementGroups operations
    :vartype management_groups: azure.mgmt.loganalytics.operations.ManagementGroupsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.loganalytics.operations.Operations
    :ivar operation_statuses: OperationStatuses operations
    :vartype operation_statuses: azure.mgmt.loganalytics.operations.OperationStatusesOperations
    :ivar shared_keys: SharedKeys operations
    :vartype shared_keys: azure.mgmt.loganalytics.operations.SharedKeysOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.loganalytics.operations.UsagesOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.loganalytics.operations.WorkspacesOperations
    :ivar deleted_workspaces: DeletedWorkspaces operations
    :vartype deleted_workspaces: azure.mgmt.loganalytics.operations.DeletedWorkspacesOperations
    :ivar clusters: Clusters operations
    :vartype clusters: azure.mgmt.loganalytics.operations.ClustersOperations
    :ivar storage_insight_configs: StorageInsightConfigs operations
    :vartype storage_insight_configs: azure.mgmt.loganalytics.operations.StorageInsightConfigsOperations
    :ivar saved_searches: SavedSearches operations
    :vartype saved_searches: azure.mgmt.loganalytics.operations.SavedSearchesOperations
    :ivar available_service_tiers: AvailableServiceTiers operations
    :vartype available_service_tiers: azure.mgmt.loganalytics.operations.AvailableServiceTiersOperations
    :ivar gateways: Gateways operations
    :vartype gateways: azure.mgmt.loganalytics.operations.GatewaysOperations
    :ivar schema: Schema operations
    :vartype schema: azure.mgmt.loganalytics.operations.SchemaOperations
    :ivar workspace_purge: WorkspacePurge operations
    :vartype workspace_purge: azure.mgmt.loganalytics.operations.WorkspacePurgeOperations
    :ivar tables: Tables operations
    :vartype tables: azure.mgmt.loganalytics.operations.TablesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = LogAnalyticsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(LogAnalyticsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-08-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.data_exports = DataExportsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_sources = DataSourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.intelligence_packs = IntelligencePacksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_storage_accounts = LinkedStorageAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.management_groups = ManagementGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation_statuses = OperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.shared_keys = SharedKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deleted_workspaces = DeletedWorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.clusters = ClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_insight_configs = StorageInsightConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.saved_searches = SavedSearchesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.available_service_tiers = AvailableServiceTiersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.gateways = GatewaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.schema = SchemaOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_purge = WorkspacePurgeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tables = TablesOperations(
            self._client, self.config, self._serialize, self._deserialize)
