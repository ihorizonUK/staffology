from typing import Any, Dict, Optional, Union

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.cis_300_report_response import Cis300ReportResponse
from ...models.tax_year import TaxYear
from ...types import UNSET, Response, Unset


def _get_kwargs(
    employer_id: str,
    tax_year: TaxYear,
    id: str,
    *,
    client: Client,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/reports/{taxYear}/cis300/{id}".format(
        client.base_url, employerId=employer_id, taxYear=tax_year, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(accept, Unset):
        headers["accept"] = accept

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Cis300ReportResponse]:
    if response.status_code == 200:
        response_200 = Cis300ReportResponse.from_dict(response.json())

        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Cis300ReportResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    tax_year: TaxYear,
    id: str,
    *,
    client: Client,
    accept: Union[Unset, str] = UNSET,
) -> Response[Cis300ReportResponse]:
    """CIS300

     Returns a CIS300 as a CSV or human-readable report

    Args:
        employer_id (str):
        tax_year (TaxYear):
        id (str):
        accept (Union[Unset, str]):

    Returns:
        Response[Cis300ReportResponse]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        id=id,
        client=client,
        accept=accept,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: str,
    tax_year: TaxYear,
    id: str,
    *,
    client: Client,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Cis300ReportResponse]:
    """CIS300

     Returns a CIS300 as a CSV or human-readable report

    Args:
        employer_id (str):
        tax_year (TaxYear):
        id (str):
        accept (Union[Unset, str]):

    Returns:
        Response[Cis300ReportResponse]
    """

    return sync_detailed(
        employer_id=employer_id,
        tax_year=tax_year,
        id=id,
        client=client,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    tax_year: TaxYear,
    id: str,
    *,
    client: Client,
    accept: Union[Unset, str] = UNSET,
) -> Response[Cis300ReportResponse]:
    """CIS300

     Returns a CIS300 as a CSV or human-readable report

    Args:
        employer_id (str):
        tax_year (TaxYear):
        id (str):
        accept (Union[Unset, str]):

    Returns:
        Response[Cis300ReportResponse]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        id=id,
        client=client,
        accept=accept,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    tax_year: TaxYear,
    id: str,
    *,
    client: Client,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Cis300ReportResponse]:
    """CIS300

     Returns a CIS300 as a CSV or human-readable report

    Args:
        employer_id (str):
        tax_year (TaxYear):
        id (str):
        accept (Union[Unset, str]):

    Returns:
        Response[Cis300ReportResponse]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            tax_year=tax_year,
            id=id,
            client=client,
            accept=accept,
        )
    ).parsed
