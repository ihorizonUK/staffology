from typing import Any, Dict, List, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.item import Item
from ...types import Response


def _get_kwargs(
    id: str,
    year: int,
    month: int,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/tenants/{id}/bills/{year}/{month}".format(
        client.base_url,id=id,year=year,month=month)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[List[Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    year: int,
    month: int,
    *,
    client: Client,

) -> Response[List[Item]]:
    """Get Bills

     Returns a list of UsageBill for Users of this Tenant, for the Year and Month supplied

    Args:
        id (str):
        year (int):
        month (int):

    Returns:
        Response[List[Item]]
    """


    kwargs = _get_kwargs(
        id=id,
year=year,
month=month,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    id: str,
    year: int,
    month: int,
    *,
    client: Client,

) -> Optional[List[Item]]:
    """Get Bills

     Returns a list of UsageBill for Users of this Tenant, for the Year and Month supplied

    Args:
        id (str):
        year (int):
        month (int):

    Returns:
        Response[List[Item]]
    """


    return sync_detailed(
        id=id,
year=year,
month=month,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    year: int,
    month: int,
    *,
    client: Client,

) -> Response[List[Item]]:
    """Get Bills

     Returns a list of UsageBill for Users of this Tenant, for the Year and Month supplied

    Args:
        id (str):
        year (int):
        month (int):

    Returns:
        Response[List[Item]]
    """


    kwargs = _get_kwargs(
        id=id,
year=year,
month=month,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    id: str,
    year: int,
    month: int,
    *,
    client: Client,

) -> Optional[List[Item]]:
    """Get Bills

     Returns a list of UsageBill for Users of this Tenant, for the Year and Month supplied

    Args:
        id (str):
        year (int):
        month (int):

    Returns:
        Response[List[Item]]
    """


    return (await asyncio_detailed(
        id=id,
year=year,
month=month,
client=client,

    )).parsed

