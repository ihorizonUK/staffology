from typing import Any, Dict, Optional, Union, cast

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.apply_year_end_employer_json_body import ApplyYearEndEmployerJsonBody
from ...models.year_end import YearEnd
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: ApplyYearEndEmployerJsonBody,
) -> Dict[str, Any]:
    url = "{}/employers/{id}/YearEnd".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, YearEnd]]:
    if response.status_code == 200:
        response_200 = YearEnd.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Any, YearEnd]]:
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
    json_body: ApplyYearEndEmployerJsonBody,
) -> Response[Union[Any, YearEnd]]:
    """Make Year End Changes

     Apply the changes for the year end and start the next tax year for the employer.

    Args:
        id (str):
        json_body (ApplyYearEndEmployerJsonBody):

    Returns:
        Response[Union[Any, YearEnd]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: ApplyYearEndEmployerJsonBody,
) -> Optional[Union[Any, YearEnd]]:
    """Make Year End Changes

     Apply the changes for the year end and start the next tax year for the employer.

    Args:
        id (str):
        json_body (ApplyYearEndEmployerJsonBody):

    Returns:
        Response[Union[Any, YearEnd]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: ApplyYearEndEmployerJsonBody,
) -> Response[Union[Any, YearEnd]]:
    """Make Year End Changes

     Apply the changes for the year end and start the next tax year for the employer.

    Args:
        id (str):
        json_body (ApplyYearEndEmployerJsonBody):

    Returns:
        Response[Union[Any, YearEnd]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: ApplyYearEndEmployerJsonBody,
) -> Optional[Union[Any, YearEnd]]:
    """Make Year End Changes

     Apply the changes for the year end and start the next tax year for the employer.

    Args:
        id (str):
        json_body (ApplyYearEndEmployerJsonBody):

    Returns:
        Response[Union[Any, YearEnd]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
