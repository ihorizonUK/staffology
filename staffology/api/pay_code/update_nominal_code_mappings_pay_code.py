from typing import Any, Dict, List, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.nominal_code_mapping import NominalCodeMapping
from ...types import Response


def _get_kwargs(
    employer_id: str,
    *,
    client: Client,
    json_body: List[NominalCodeMapping],
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/paycodes/nominalcodes".format(
        client.base_url, employerId=employer_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[NominalCodeMapping]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NominalCodeMapping.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[List[NominalCodeMapping]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    *,
    client: Client,
    json_body: List[NominalCodeMapping],
) -> Response[List[NominalCodeMapping]]:
    """Updates Nominal Code Mappings

     Updates the list of mappings of PayCodes to NominalCodes

    Args:
        employer_id (str):
        json_body (List[NominalCodeMapping]):

    Returns:
        Response[List[NominalCodeMapping]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
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
    *,
    client: Client,
    json_body: List[NominalCodeMapping],
) -> Optional[List[NominalCodeMapping]]:
    """Updates Nominal Code Mappings

     Updates the list of mappings of PayCodes to NominalCodes

    Args:
        employer_id (str):
        json_body (List[NominalCodeMapping]):

    Returns:
        Response[List[NominalCodeMapping]]
    """

    return sync_detailed(
        employer_id=employer_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    *,
    client: Client,
    json_body: List[NominalCodeMapping],
) -> Response[List[NominalCodeMapping]]:
    """Updates Nominal Code Mappings

     Updates the list of mappings of PayCodes to NominalCodes

    Args:
        employer_id (str):
        json_body (List[NominalCodeMapping]):

    Returns:
        Response[List[NominalCodeMapping]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    *,
    client: Client,
    json_body: List[NominalCodeMapping],
) -> Optional[List[NominalCodeMapping]]:
    """Updates Nominal Code Mappings

     Updates the list of mappings of PayCodes to NominalCodes

    Args:
        employer_id (str):
        json_body (List[NominalCodeMapping]):

    Returns:
        Response[List[NominalCodeMapping]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
