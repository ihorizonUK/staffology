from typing import Any, Dict, List, Optional, Union

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    page_num: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tenants/{id}/email".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pageNum"] = page_num

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
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
    *,
    client: Client,
    page_num: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[Item]]:
    """List Emails

     Returns a list of all emails sent for this Tenant.

    Args:
        id (str):
        page_num (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page_num=page_num,
        page_size=page_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    page_num: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[Item]]:
    """List Emails

     Returns a list of all emails sent for this Tenant.

    Args:
        id (str):
        page_num (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    return sync_detailed(
        id=id,
        client=client,
        page_num=page_num,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    page_num: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[Item]]:
    """List Emails

     Returns a list of all emails sent for this Tenant.

    Args:
        id (str):
        page_num (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page_num=page_num,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    page_num: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[Item]]:
    """List Emails

     Returns a list of all emails sent for this Tenant.

    Args:
        id (str):
        page_num (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page_num=page_num,
            page_size=page_size,
        )
    ).parsed
