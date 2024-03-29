from typing import Any, Dict, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.usage_bill import UsageBill
from ...types import Response


def _get_kwargs(
    id: str,
    year: int,
    month: int,
    bill_id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/tenants/{id}/bills/{year}/{month}/{billId}".format(
        client.base_url,id=id,year=year,month=month,billId=bill_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UsageBill]:
    if response.status_code == 200:
        response_200 = UsageBill.from_dict(response.json())



        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[UsageBill]:
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
    bill_id: str,
    *,
    client: Client,

) -> Response[UsageBill]:
    """Get Bill

     Returns details of a UsageBill for a User of this Tenant

    Args:
        id (str):
        year (int):
        month (int):
        bill_id (str):

    Returns:
        Response[UsageBill]
    """


    kwargs = _get_kwargs(
        id=id,
year=year,
month=month,
bill_id=bill_id,
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
    bill_id: str,
    *,
    client: Client,

) -> Optional[UsageBill]:
    """Get Bill

     Returns details of a UsageBill for a User of this Tenant

    Args:
        id (str):
        year (int):
        month (int):
        bill_id (str):

    Returns:
        Response[UsageBill]
    """


    return sync_detailed(
        id=id,
year=year,
month=month,
bill_id=bill_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    year: int,
    month: int,
    bill_id: str,
    *,
    client: Client,

) -> Response[UsageBill]:
    """Get Bill

     Returns details of a UsageBill for a User of this Tenant

    Args:
        id (str):
        year (int):
        month (int):
        bill_id (str):

    Returns:
        Response[UsageBill]
    """


    kwargs = _get_kwargs(
        id=id,
year=year,
month=month,
bill_id=bill_id,
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
    bill_id: str,
    *,
    client: Client,

) -> Optional[UsageBill]:
    """Get Bill

     Returns details of a UsageBill for a User of this Tenant

    Args:
        id (str):
        year (int):
        month (int):
        bill_id (str):

    Returns:
        Response[UsageBill]
    """


    return (await asyncio_detailed(
        id=id,
year=year,
month=month,
bill_id=bill_id,
client=client,

    )).parsed

