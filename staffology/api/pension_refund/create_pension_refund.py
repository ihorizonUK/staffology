from typing import Any, Dict

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...models.pension_refund import PensionRefund
from ...types import Response


def _get_kwargs(
    employer_id: str,
    employee_id: str,
    *,
    client: Client,
    json_body: PensionRefund,

) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/employees/{employeeId}/pensionrefund".format(
        client.base_url,employerId=employer_id,employeeId=employee_id)

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




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    employer_id: str,
    employee_id: str,
    *,
    client: Client,
    json_body: PensionRefund,

) -> Response[Any]:
    """Create Pension Refund

     Creates a Pension Refund for the Employee

    Args:
        employer_id (str):
        employee_id (str):
        json_body (PensionRefund): Used to represent a Pension Refund

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        employer_id=employer_id,
employee_id=employee_id,
client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    employer_id: str,
    employee_id: str,
    *,
    client: Client,
    json_body: PensionRefund,

) -> Response[Any]:
    """Create Pension Refund

     Creates a Pension Refund for the Employee

    Args:
        employer_id (str):
        employee_id (str):
        json_body (PensionRefund): Used to represent a Pension Refund

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        employer_id=employer_id,
employee_id=employee_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)


