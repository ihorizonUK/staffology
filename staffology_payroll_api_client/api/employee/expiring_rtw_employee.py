from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    employer_id: str,
    *,
    client: Client,
    number_of_days: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/employees/expiring-rtw".format(
        client.base_url, employerId=employer_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["numberOfDays"] = number_of_days

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
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Item]]:
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
    number_of_days: Union[Unset, None, int] = UNSET,
) -> Response[List[Item]]:
    """Expiring RightToWork

     Returns a list of Item representing Employees that have a RightToWork with a DocumentExpiring date
    within the next numberOfDays days.

    Args:
        employer_id (str):
        number_of_days (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        number_of_days=number_of_days,
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
    number_of_days: Union[Unset, None, int] = UNSET,
) -> Optional[List[Item]]:
    """Expiring RightToWork

     Returns a list of Item representing Employees that have a RightToWork with a DocumentExpiring date
    within the next numberOfDays days.

    Args:
        employer_id (str):
        number_of_days (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    return sync_detailed(
        employer_id=employer_id,
        client=client,
        number_of_days=number_of_days,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    *,
    client: Client,
    number_of_days: Union[Unset, None, int] = UNSET,
) -> Response[List[Item]]:
    """Expiring RightToWork

     Returns a list of Item representing Employees that have a RightToWork with a DocumentExpiring date
    within the next numberOfDays days.

    Args:
        employer_id (str):
        number_of_days (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        number_of_days=number_of_days,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    *,
    client: Client,
    number_of_days: Union[Unset, None, int] = UNSET,
) -> Optional[List[Item]]:
    """Expiring RightToWork

     Returns a list of Item representing Employees that have a RightToWork with a DocumentExpiring date
    within the next numberOfDays days.

    Args:
        employer_id (str):
        number_of_days (Union[Unset, None, int]):

    Returns:
        Response[List[Item]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            number_of_days=number_of_days,
        )
    ).parsed
