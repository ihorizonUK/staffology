from typing import Any, Dict

import httpx
from staffology.propagate_exceptions import raise_staffology_exception

from ...client import Client
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: str,

) -> Dict[str, Any]:
    url = "{}/tenants/{id}/users/admins".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body


    

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
    id: str,
    *,
    client: Client,
    json_body: str,

) -> Response[Any]:
    """Add Admin User

     Adds the specified user as an admin for the Tenant

    Args:
        id (str):
        json_body (str):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: str,

) -> Response[Any]:
    """Add Admin User

     Adds the specified user as an admin for the Tenant

    Args:
        id (str):
        json_body (str):

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)


