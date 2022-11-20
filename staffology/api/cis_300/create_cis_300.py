from typing import Any, Dict, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.cis_300 import Cis300
from ...models.tax_year import TaxYear
from ...types import Response


def _get_kwargs(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
    json_body: Cis300,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/rti/cis300/{taxYear}".format(
        client.base_url, employerId=employer_id, taxYear=tax_year
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Cis300]:
    if response.status_code == 201:
        response_201 = Cis300.from_dict(response.json())

        return response_201
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Cis300]:
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
    json_body: Cis300,
) -> Response[Cis300]:
    """Create Cis300

     A Cis300 is automatically created for each Tax Month that you pay a Subcontractor.
    You would only manually create one if you are intending to submit a nil return.

    Args:
        employer_id (str):
        tax_year (TaxYear):
        json_body (Cis300):

    Returns:
        Response[Cis300]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
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
    *,
    client: Client,
    json_body: Cis300,
) -> Optional[Cis300]:
    """Create Cis300

     A Cis300 is automatically created for each Tax Month that you pay a Subcontractor.
    You would only manually create one if you are intending to submit a nil return.

    Args:
        employer_id (str):
        tax_year (TaxYear):
        json_body (Cis300):

    Returns:
        Response[Cis300]
    """

    return sync_detailed(
        employer_id=employer_id,
        tax_year=tax_year,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
    json_body: Cis300,
) -> Response[Cis300]:
    """Create Cis300

     A Cis300 is automatically created for each Tax Month that you pay a Subcontractor.
    You would only manually create one if you are intending to submit a nil return.

    Args:
        employer_id (str):
        tax_year (TaxYear):
        json_body (Cis300):

    Returns:
        Response[Cis300]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        tax_year=tax_year,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: str,
    tax_year: TaxYear,
    *,
    client: Client,
    json_body: Cis300,
) -> Optional[Cis300]:
    """Create Cis300

     A Cis300 is automatically created for each Tax Month that you pay a Subcontractor.
    You would only manually create one if you are intending to submit a nil return.

    Args:
        employer_id (str):
        tax_year (TaxYear):
        json_body (Cis300):

    Returns:
        Response[Cis300]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            tax_year=tax_year,
            client=client,
            json_body=json_body,
        )
    ).parsed
