from typing import Any, Dict, Optional

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.pension import Pension
from ...types import Response


def _get_kwargs(
    employer_id: str,
    employee_id: str,
    id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/employees/{employeeId}/pension/{id}".format(
        client.base_url,employerId=employer_id,employeeId=employee_id,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Pension]:
    if response.status_code == 200:
        response_200 = Pension.from_dict(response.json())



        return response_200
    return raise_staffology_exception(response)


def _build_response(*, response: httpx.Response) -> Response[Pension]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: str,
    employee_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Pension]:
    """Get Pension

     Returns a Pension for an Employee

    Args:
        employer_id (str):
        employee_id (str):
        id (str):

    Returns:
        Response[Pension]
    """


    kwargs = _get_kwargs(
        employer_id=employer_id,
employee_id=employee_id,
id=id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    employer_id: str,
    employee_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Pension]:
    """Get Pension

     Returns a Pension for an Employee

    Args:
        employer_id (str):
        employee_id (str):
        id (str):

    Returns:
        Response[Pension]
    """


    return sync_detailed(
        employer_id=employer_id,
employee_id=employee_id,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    employer_id: str,
    employee_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Pension]:
    """Get Pension

     Returns a Pension for an Employee

    Args:
        employer_id (str):
        employee_id (str):
        id (str):

    Returns:
        Response[Pension]
    """


    kwargs = _get_kwargs(
        employer_id=employer_id,
employee_id=employee_id,
id=id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    employer_id: str,
    employee_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Pension]:
    """Get Pension

     Returns a Pension for an Employee

    Args:
        employer_id (str):
        employee_id (str):
        id (str):

    Returns:
        Response[Pension]
    """


    return (await asyncio_detailed(
        employer_id=employer_id,
employee_id=employee_id,
id=id,
client=client,

    )).parsed

