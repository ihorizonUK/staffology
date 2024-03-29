from typing import Any, Dict, List, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.item import Item
from ...models.tax_year import TaxYear
from ...types import Response


def _get_kwargs(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/rti/eps/{taxYear}".format(
        client.base_url, employerId=employer_id, taxYear=tax_year
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
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
) -> Response[List[Item]]:
    """List EPS

     Returns all Employment Payment Summaries for the given tax year.
    If the 'Linked EPS' is enabled by the employer, Employment Payment Summaries
    for employer as well as for any linked employers with 'Linked EPS' enabled
    and with the same PAYE scheme are returned.

    Args:
        employer_id (str):
        tax_year (TaxYear):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
) -> Optional[List[Item]]:
    """List EPS

     Returns all Employment Payment Summaries for the given tax year.
    If the 'Linked EPS' is enabled by the employer, Employment Payment Summaries
    for employer as well as for any linked employers with 'Linked EPS' enabled
    and with the same PAYE scheme are returned.

    Args:
        employer_id (str):
        tax_year (TaxYear):

    Returns:
        Response[List[Item]]
    """

    return sync_detailed(
        employer_id=employer_id,
        tax_year=tax_year,
        client=client,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
) -> Response[List[Item]]:
    """List EPS

     Returns all Employment Payment Summaries for the given tax year.
    If the 'Linked EPS' is enabled by the employer, Employment Payment Summaries
    for employer as well as for any linked employers with 'Linked EPS' enabled
    and with the same PAYE scheme are returned.

    Args:
        employer_id (str):
        tax_year (TaxYear):

    Returns:
        Response[List[Item]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
) -> Optional[List[Item]]:
    """List EPS

     Returns all Employment Payment Summaries for the given tax year.
    If the 'Linked EPS' is enabled by the employer, Employment Payment Summaries
    for employer as well as for any linked employers with 'Linked EPS' enabled
    and with the same PAYE scheme are returned.

    Args:
        employer_id (str):
        tax_year (TaxYear):

    Returns:
        Response[List[Item]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            tax_year=tax_year,
            client=client,
        )
    ).parsed
