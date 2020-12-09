# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class Oauth2PermissionGrantOAuth2PermissionGrantOperations(object):
    """Oauth2PermissionGrantOAuth2PermissionGrantOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_o_auth2_permission_grant(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Enum105"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum106"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfOAuth2PermissionGrant"]
        """Get entities from oauth2PermissionGrants.

        Get entities from oauth2PermissionGrants.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_sign_ins.models.Enum105]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum106]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfOAuth2PermissionGrant or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_sign_ins.models.CollectionOfOAuth2PermissionGrant]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfOAuth2PermissionGrant"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_o_auth2_permission_grant.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfOAuth2PermissionGrant', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_o_auth2_permission_grant.metadata = {'url': '/oauth2PermissionGrants'}  # type: ignore

    def create_o_auth2_permission_grant(
        self,
        id=None,  # type: Optional[str]
        client_id=None,  # type: Optional[str]
        consent_type=None,  # type: Optional[str]
        principal_id=None,  # type: Optional[str]
        resource_id=None,  # type: Optional[str]
        scope=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOAuth2PermissionGrant"
        """Add new entity to oauth2PermissionGrants.

        Add new entity to oauth2PermissionGrants.

        :param id: Read-only.
        :type id: str
        :param client_id: The id of the client service principal for the application which is
         authorized to act on behalf of a signed-in user when accessing an API. Required. Supports
         $filter (eq only).
        :type client_id: str
        :param consent_type: Indicates if authorization is granted for the client application to
         impersonate all users or only a specific user. AllPrincipals indicates authorization to
         impersonate all users. Principal indicates authorization to impersonate a specific user.
         Consent on behalf of all users can be granted by an administrator. Non-admin users may be
         authorized to consent on behalf of themselves in some cases, for some delegated permissions.
         Required. Supports $filter (eq only).
        :type consent_type: str
        :param principal_id: The id of the user on behalf of whom the client is authorized to access
         the resource, when consentType is Principal. If consentType is AllPrincipals this value is
         null. Required when consentType is Principal.
        :type principal_id: str
        :param resource_id: The id of the resource service principal to which access is authorized.
         This identifies the API which the client is authorized to attempt to call on behalf of a
         signed-in user.
        :type resource_id: str
        :param scope: A space-separated list of the claim values for delegated permissions which should
         be included in access tokens for the resource application (the API). For example, openid
         User.Read GroupMember.Read.All. Each claim value should match the value field of one of the
         delegated permissions defined by the API, listed in the publishedPermissionScopes property of
         the resource service principal.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOAuth2PermissionGrant, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphOAuth2PermissionGrant
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOAuth2PermissionGrant"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOAuth2PermissionGrant(id=id, client_id=client_id, consent_type=consent_type, principal_id=principal_id, resource_id=resource_id, scope=scope)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_o_auth2_permission_grant.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOAuth2PermissionGrant')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOAuth2PermissionGrant', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_o_auth2_permission_grant.metadata = {'url': '/oauth2PermissionGrants'}  # type: ignore

    def get_o_auth2_permission_grant(
        self,
        o_auth2_permission_grant_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum107"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOAuth2PermissionGrant"
        """Get entity from oauth2PermissionGrants by key.

        Get entity from oauth2PermissionGrants by key.

        :param o_auth2_permission_grant_id: key: id of oAuth2PermissionGrant.
        :type o_auth2_permission_grant_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_sign_ins.models.Enum107]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOAuth2PermissionGrant, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphOAuth2PermissionGrant
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOAuth2PermissionGrant"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_o_auth2_permission_grant.metadata['url']  # type: ignore
        path_format_arguments = {
            'oAuth2PermissionGrant-id': self._serialize.url("o_auth2_permission_grant_id", o_auth2_permission_grant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOAuth2PermissionGrant', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_o_auth2_permission_grant.metadata = {'url': '/oauth2PermissionGrants/{oAuth2PermissionGrant-id}'}  # type: ignore

    def update_o_auth2_permission_grant(
        self,
        o_auth2_permission_grant_id,  # type: str
        id=None,  # type: Optional[str]
        client_id=None,  # type: Optional[str]
        consent_type=None,  # type: Optional[str]
        principal_id=None,  # type: Optional[str]
        resource_id=None,  # type: Optional[str]
        scope=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update entity in oauth2PermissionGrants.

        Update entity in oauth2PermissionGrants.

        :param o_auth2_permission_grant_id: key: id of oAuth2PermissionGrant.
        :type o_auth2_permission_grant_id: str
        :param id: Read-only.
        :type id: str
        :param client_id: The id of the client service principal for the application which is
         authorized to act on behalf of a signed-in user when accessing an API. Required. Supports
         $filter (eq only).
        :type client_id: str
        :param consent_type: Indicates if authorization is granted for the client application to
         impersonate all users or only a specific user. AllPrincipals indicates authorization to
         impersonate all users. Principal indicates authorization to impersonate a specific user.
         Consent on behalf of all users can be granted by an administrator. Non-admin users may be
         authorized to consent on behalf of themselves in some cases, for some delegated permissions.
         Required. Supports $filter (eq only).
        :type consent_type: str
        :param principal_id: The id of the user on behalf of whom the client is authorized to access
         the resource, when consentType is Principal. If consentType is AllPrincipals this value is
         null. Required when consentType is Principal.
        :type principal_id: str
        :param resource_id: The id of the resource service principal to which access is authorized.
         This identifies the API which the client is authorized to attempt to call on behalf of a
         signed-in user.
        :type resource_id: str
        :param scope: A space-separated list of the claim values for delegated permissions which should
         be included in access tokens for the resource application (the API). For example, openid
         User.Read GroupMember.Read.All. Each claim value should match the value field of one of the
         delegated permissions defined by the API, listed in the publishedPermissionScopes property of
         the resource service principal.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOAuth2PermissionGrant(id=id, client_id=client_id, consent_type=consent_type, principal_id=principal_id, resource_id=resource_id, scope=scope)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_o_auth2_permission_grant.metadata['url']  # type: ignore
        path_format_arguments = {
            'oAuth2PermissionGrant-id': self._serialize.url("o_auth2_permission_grant_id", o_auth2_permission_grant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOAuth2PermissionGrant')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_o_auth2_permission_grant.metadata = {'url': '/oauth2PermissionGrants/{oAuth2PermissionGrant-id}'}  # type: ignore

    def delete_o_auth2_permission_grant(
        self,
        o_auth2_permission_grant_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete entity from oauth2PermissionGrants.

        Delete entity from oauth2PermissionGrants.

        :param o_auth2_permission_grant_id: key: id of oAuth2PermissionGrant.
        :type o_auth2_permission_grant_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_o_auth2_permission_grant.metadata['url']  # type: ignore
        path_format_arguments = {
            'oAuth2PermissionGrant-id': self._serialize.url("o_auth2_permission_grant_id", o_auth2_permission_grant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_o_auth2_permission_grant.metadata = {'url': '/oauth2PermissionGrants/{oAuth2PermissionGrant-id}'}  # type: ignore
