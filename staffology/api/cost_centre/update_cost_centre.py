from typing import Any, Dict, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.cost_centre import CostCentre
from ...types import Response


def _get_kwargs(
    employer_id: str,
    code: str,
    *,
    client: Client,
    json_body: CostCentre,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/costcentres/{code}".format(client.base_url, employerId=employer_id, code=code)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CostCentre]:
    if response.status_code == 200:
        response_200 = CostCentre.from_dict(response.json())

        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[CostCentre]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    code: str,
    *,
    client: Client,
    json_body: CostCentre,
) -> Response[CostCentre]:
    """Update Cost Centre (deprecated)

     Updates a Cost Centre for the Employer.
    Use the other Update endpoint that supports non-alphanumeric characters for a cost centre code

    Args:
        employer_id (str):
        code (str):
        json_body (CostCentre):

    Returns:
        Response[CostCentre]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        code=code,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: str,
    code: str,
    *,
    client: Client,
    json_body: CostCentre,
) -> Optional[CostCentre]:
    """Update Cost Centre (deprecated)

     Updates a Cost Centre for the Employer.
    Use the other Update endpoint that supports non-alphanumeric characters for a cost centre code

    Args:
        employer_id (str):
        code (str):
        json_body (CostCentre):

    Returns:
        Response[CostCentre]
    """

    return sync_detailed(
        employer_id=employer_id,
        code=code,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    code: str,
    *,
    client: Client,
    json_body: CostCentre,
) -> Response[CostCentre]:
    """Update Cost Centre (deprecated)

     Updates a Cost Centre for the Employer.
    Use the other Update endpoint that supports non-alphanumeric characters for a cost centre code

    Args:
        employer_id (str):
        code (str):
        json_body (CostCentre):

    Returns:
        Response[CostCentre]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        code=code,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    code: str,
    *,
    client: Client,
    json_body: CostCentre,
) -> Optional[CostCentre]:
    """Update Cost Centre (deprecated)

     Updates a Cost Centre for the Employer.
    Use the other Update endpoint that supports non-alphanumeric characters for a cost centre code

    Args:
        employer_id (str):
        code (str):
        json_body (CostCentre):

    Returns:
        Response[CostCentre]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            code=code,
            client=client,
            json_body=json_body,
        )
    ).parsed
