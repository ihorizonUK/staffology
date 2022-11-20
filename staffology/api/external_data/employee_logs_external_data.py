from typing import Any, Dict, List, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.external_data_provider_id import ExternalDataProviderId
from ...models.log_entry import LogEntry
from ...types import Response


def _get_kwargs(
    employer_id: str,
    id: ExternalDataProviderId,
    employee_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/external-data/{id}/employees/{employeeId}/logs".format(
        client.base_url, employerId=employer_id, id=id, employeeId=employee_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[LogEntry]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LogEntry.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[List[LogEntry]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    id: ExternalDataProviderId,
    employee_id: str,
    *,
    client: Client,
) -> Response[List[LogEntry]]:
    """Get Employee Logs

     Return a list of changes made locally to this employee based on changes in the external data
    provider

    Args:
        employer_id (str):
        id (ExternalDataProviderId):
        employee_id (str):

    Returns:
        Response[List[LogEntry]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        id=id,
        employee_id=employee_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: str,
    id: ExternalDataProviderId,
    employee_id: str,
    *,
    client: Client,
) -> Optional[List[LogEntry]]:
    """Get Employee Logs

     Return a list of changes made locally to this employee based on changes in the external data
    provider

    Args:
        employer_id (str):
        id (ExternalDataProviderId):
        employee_id (str):

    Returns:
        Response[List[LogEntry]]
    """

    return sync_detailed(
        employer_id=employer_id,
        id=id,
        employee_id=employee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    id: ExternalDataProviderId,
    employee_id: str,
    *,
    client: Client,
) -> Response[List[LogEntry]]:
    """Get Employee Logs

     Return a list of changes made locally to this employee based on changes in the external data
    provider

    Args:
        employer_id (str):
        id (ExternalDataProviderId):
        employee_id (str):

    Returns:
        Response[List[LogEntry]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        id=id,
        employee_id=employee_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    id: ExternalDataProviderId,
    employee_id: str,
    *,
    client: Client,
) -> Optional[List[LogEntry]]:
    """Get Employee Logs

     Return a list of changes made locally to this employee based on changes in the external data
    provider

    Args:
        employer_id (str):
        id (ExternalDataProviderId):
        employee_id (str):

    Returns:
        Response[List[LogEntry]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            id=id,
            employee_id=employee_id,
            client=client,
        )
    ).parsed
