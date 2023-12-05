from typing import Any, Dict, Optional, Union, cast

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.contract_job_response import ContractJobResponse
from ...types import Response


def _get_kwargs(
    employer_id: str,
    job_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/jobs/{jobId}".format(client.base_url, employerId=employer_id, jobId=job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ContractJobResponse]]:
    if response.status_code == 200:
        response_200 = ContractJobResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ContractJobResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ContractJobResponse]]:
    """Get Job

     Returns a job

    Args:
        employer_id (str):
        job_id (str):

    Returns:
        Response[Union[Any, ContractJobResponse]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: str,
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ContractJobResponse]]:
    """Get Job

     Returns a job

    Args:
        employer_id (str):
        job_id (str):

    Returns:
        Response[Union[Any, ContractJobResponse]]
    """

    return sync_detailed(
        employer_id=employer_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ContractJobResponse]]:
    """Get Job

     Returns a job

    Args:
        employer_id (str):
        job_id (str):

    Returns:
        Response[Union[Any, ContractJobResponse]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ContractJobResponse]]:
    """Get Job

     Returns a job

    Args:
        employer_id (str):
        job_id (str):

    Returns:
        Response[Union[Any, ContractJobResponse]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
