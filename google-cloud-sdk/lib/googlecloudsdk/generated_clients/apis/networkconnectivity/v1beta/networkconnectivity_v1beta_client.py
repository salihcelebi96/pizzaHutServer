"""Generated client library for networkconnectivity version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.networkconnectivity.v1beta import networkconnectivity_v1beta_messages as messages


class NetworkconnectivityV1beta(base_api.BaseApiClient):
  """Generated client library for service networkconnectivity version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://networkconnectivity.googleapis.com/'
  MTLS_BASE_URL = 'https://networkconnectivity.mtls.googleapis.com/'

  _PACKAGE = 'networkconnectivity'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'NetworkconnectivityV1beta'
  _URL_VERSION = 'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new networkconnectivity handle."""
    url = url or self.BASE_URL
    super(NetworkconnectivityV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_customHardwareLinkAttachments = self.ProjectsLocationsCustomHardwareLinkAttachmentsService(self)
    self.projects_locations_global_hubs_groups = self.ProjectsLocationsGlobalHubsGroupsService(self)
    self.projects_locations_global_hubs = self.ProjectsLocationsGlobalHubsService(self)
    self.projects_locations_global = self.ProjectsLocationsGlobalService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_regionalEndpoints = self.ProjectsLocationsRegionalEndpointsService(self)
    self.projects_locations_spokes = self.ProjectsLocationsSpokesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsCustomHardwareLinkAttachmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_customHardwareLinkAttachments resource."""

    _NAME = 'projects_locations_customHardwareLinkAttachments'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsCustomHardwareLinkAttachmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new CustomHardwareLinkAttachment in a given project and location.

      Args:
        request: (NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/customHardwareLinkAttachments',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.customHardwareLinkAttachments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['customHardwareLinkAttachmentId', 'requestId'],
        relative_path='v1beta/{+parent}/customHardwareLinkAttachments',
        request_field='googleCloudNetworkconnectivityV1betaCustomHardwareLinkAttachment',
        request_type_name='NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single CustomHardwareLinkAttachment.

      Args:
        request: (NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/customHardwareLinkAttachments/{customHardwareLinkAttachmentsId}',
        http_method='DELETE',
        method_id='networkconnectivity.projects.locations.customHardwareLinkAttachments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single CustomHardwareLinkAttachment.

      Args:
        request: (NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudNetworkconnectivityV1betaCustomHardwareLinkAttachment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/customHardwareLinkAttachments/{customHardwareLinkAttachmentsId}',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.customHardwareLinkAttachments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsGetRequest',
        response_type_name='GoogleCloudNetworkconnectivityV1betaCustomHardwareLinkAttachment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists CustomHardwareLinkAttachments in a given project and location.

      Args:
        request: (NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudNetworkconnectivityV1betaListCustomHardwareLinkAttachmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/customHardwareLinkAttachments',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.customHardwareLinkAttachments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/customHardwareLinkAttachments',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsListRequest',
        response_type_name='GoogleCloudNetworkconnectivityV1betaListCustomHardwareLinkAttachmentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single CustomHardwareLinkAttachment.

      Args:
        request: (NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/customHardwareLinkAttachments/{customHardwareLinkAttachmentsId}',
        http_method='PATCH',
        method_id='networkconnectivity.projects.locations.customHardwareLinkAttachments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1beta/{+name}',
        request_field='googleCloudNetworkconnectivityV1betaCustomHardwareLinkAttachment',
        request_type_name='NetworkconnectivityProjectsLocationsCustomHardwareLinkAttachmentsPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsGlobalHubsGroupsService(base_api.BaseApiService):
    """Service class for the projects_locations_global_hubs_groups resource."""

    _NAME = 'projects_locations_global_hubs_groups'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsGlobalHubsGroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsGroupsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}/groups/{groupsId}:getIamPolicy',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.global.hubs.groups.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsGroupsGetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsGroupsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}/groups/{groupsId}:setIamPolicy',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.global.hubs.groups.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:setIamPolicy',
        request_field='googleIamV1SetIamPolicyRequest',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsGroupsSetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsGroupsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}/groups/{groupsId}:testIamPermissions',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.global.hubs.groups.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:testIamPermissions',
        request_field='googleIamV1TestIamPermissionsRequest',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsGroupsTestIamPermissionsRequest',
        response_type_name='GoogleIamV1TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGlobalHubsService(base_api.BaseApiService):
    """Service class for the projects_locations_global_hubs resource."""

    _NAME = 'projects_locations_global_hubs'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsGlobalHubsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}:getIamPolicy',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.global.hubs.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsGetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}:setIamPolicy',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.global.hubs.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:setIamPolicy',
        request_field='googleIamV1SetIamPolicyRequest',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsSetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (NetworkconnectivityProjectsLocationsGlobalHubsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/global/hubs/{hubsId}:testIamPermissions',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.global.hubs.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:testIamPermissions',
        request_field='googleIamV1TestIamPermissionsRequest',
        request_type_name='NetworkconnectivityProjectsLocationsGlobalHubsTestIamPermissionsRequest',
        response_type_name='GoogleIamV1TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGlobalService(base_api.BaseApiService):
    """Service class for the projects_locations_global resource."""

    _NAME = 'projects_locations_global'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsGlobalService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (NetworkconnectivityProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:cancel',
        request_field='googleLongrunningCancelOperationRequest',
        request_type_name='NetworkconnectivityProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (NetworkconnectivityProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='networkconnectivity.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (NetworkconnectivityProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (NetworkconnectivityProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+name}/operations',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsOperationsListRequest',
        response_type_name='GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegionalEndpointsService(base_api.BaseApiService):
    """Service class for the projects_locations_regionalEndpoints resource."""

    _NAME = 'projects_locations_regionalEndpoints'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsRegionalEndpointsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new RegionalEndpoint in a given project and location.

      Args:
        request: (NetworkconnectivityProjectsLocationsRegionalEndpointsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/regionalEndpoints',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.regionalEndpoints.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['regionalEndpointId', 'requestId'],
        relative_path='v1beta/{+parent}/regionalEndpoints',
        request_field='googleCloudNetworkconnectivityV1betaRegionalEndpoint',
        request_type_name='NetworkconnectivityProjectsLocationsRegionalEndpointsCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single RegionalEndpoint.

      Args:
        request: (NetworkconnectivityProjectsLocationsRegionalEndpointsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/regionalEndpoints/{regionalEndpointsId}',
        http_method='DELETE',
        method_id='networkconnectivity.projects.locations.regionalEndpoints.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsRegionalEndpointsDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single RegionalEndpoint.

      Args:
        request: (NetworkconnectivityProjectsLocationsRegionalEndpointsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudNetworkconnectivityV1betaRegionalEndpoint) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/regionalEndpoints/{regionalEndpointsId}',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.regionalEndpoints.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsRegionalEndpointsGetRequest',
        response_type_name='GoogleCloudNetworkconnectivityV1betaRegionalEndpoint',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists RegionalEndpoints in a given project and location.

      Args:
        request: (NetworkconnectivityProjectsLocationsRegionalEndpointsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudNetworkconnectivityV1betaListRegionalEndpointsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/regionalEndpoints',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.regionalEndpoints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/regionalEndpoints',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsRegionalEndpointsListRequest',
        response_type_name='GoogleCloudNetworkconnectivityV1betaListRegionalEndpointsResponse',
        supports_download=False,
    )

  class ProjectsLocationsSpokesService(base_api.BaseApiService):
    """Service class for the projects_locations_spokes resource."""

    _NAME = 'projects_locations_spokes'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsSpokesService, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (NetworkconnectivityProjectsLocationsSpokesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/spokes/{spokesId}:getIamPolicy',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.spokes.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsSpokesGetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (NetworkconnectivityProjectsLocationsSpokesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/spokes/{spokesId}:setIamPolicy',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.spokes.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:setIamPolicy',
        request_field='googleIamV1SetIamPolicyRequest',
        request_type_name='NetworkconnectivityProjectsLocationsSpokesSetIamPolicyRequest',
        response_type_name='GoogleIamV1Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (NetworkconnectivityProjectsLocationsSpokesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/spokes/{spokesId}:testIamPermissions',
        http_method='POST',
        method_id='networkconnectivity.projects.locations.spokes.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta/{+resource}:testIamPermissions',
        request_field='googleIamV1TestIamPermissionsRequest',
        request_type_name='NetworkconnectivityProjectsLocationsSpokesTestIamPermissionsRequest',
        response_type_name='GoogleIamV1TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (NetworkconnectivityProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudLocationLocation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsGetRequest',
        response_type_name='GoogleCloudLocationLocation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (NetworkconnectivityProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudLocationListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations',
        http_method='GET',
        method_id='networkconnectivity.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+name}/locations',
        request_field='',
        request_type_name='NetworkconnectivityProjectsLocationsListRequest',
        response_type_name='GoogleCloudLocationListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(NetworkconnectivityV1beta.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
