import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.hmrc_liability import HmrcLiability
from ...models.tax_year import TaxYear
from ...types import Response


def _get_kwargs(
    employer_id: str,
    tax_year: TaxYear,
    period_ending: datetime.datetime,
    *,
    client: Client,
    json_body: HmrcLiability,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/hmrcpayment/{taxYear}/{periodEnding}".format(
        client.base_url,
        employerId=employer_id,
        taxYear=tax_year,
        periodEnding=period_ending,
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HmrcLiability]]:
    if response.status_code == 200:
        response_200 = HmrcLiability.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HmrcLiability]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    tax_year: TaxYear,
    period_ending: datetime.datetime,
    *,
    client: Client,
    json_body: HmrcLiability,
) -> Response[Union[Any, HmrcLiability]]:
    """Update HmrcLiability

     Updates the editable fields of a HmrcLiability (ie, Adjustment, CISDeductionsSuffered, etc)

    Args:
        employer_id (str):
        tax_year (TaxYear):
        period_ending (datetime.datetime):
        json_body (HmrcLiability):

    Returns:
        Response[Union[Any, HmrcLiability]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        period_ending=period_ending,
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
    tax_year: TaxYear,
    period_ending: datetime.datetime,
    *,
    client: Client,
    json_body: HmrcLiability,
) -> Optional[Union[Any, HmrcLiability]]:
    """Update HmrcLiability

     Updates the editable fields of a HmrcLiability (ie, Adjustment, CISDeductionsSuffered, etc)

    Args:
        employer_id (str):
        tax_year (TaxYear):
        period_ending (datetime.datetime):
        json_body (HmrcLiability):

    Returns:
        Response[Union[Any, HmrcLiability]]
    """

    return sync_detailed(
        employer_id=employer_id,
        tax_year=tax_year,
        period_ending=period_ending,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    tax_year: TaxYear,
    period_ending: datetime.datetime,
    *,
    client: Client,
    json_body: HmrcLiability,
) -> Response[Union[Any, HmrcLiability]]:
    """Update HmrcLiability

     Updates the editable fields of a HmrcLiability (ie, Adjustment, CISDeductionsSuffered, etc)

    Args:
        employer_id (str):
        tax_year (TaxYear):
        period_ending (datetime.datetime):
        json_body (HmrcLiability):

    Returns:
        Response[Union[Any, HmrcLiability]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        period_ending=period_ending,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    tax_year: TaxYear,
    period_ending: datetime.datetime,
    *,
    client: Client,
    json_body: HmrcLiability,
) -> Optional[Union[Any, HmrcLiability]]:
    """Update HmrcLiability

     Updates the editable fields of a HmrcLiability (ie, Adjustment, CISDeductionsSuffered, etc)

    Args:
        employer_id (str):
        tax_year (TaxYear):
        period_ending (datetime.datetime):
        json_body (HmrcLiability):

    Returns:
        Response[Union[Any, HmrcLiability]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            tax_year=tax_year,
            period_ending=period_ending,
            client=client,
            json_body=json_body,
        )
    ).parsed
