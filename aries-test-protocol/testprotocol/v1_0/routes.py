"""Test Message"""

from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, request_schema, response_schema

from marshmallow import fields, Schema

from aries_cloudagent.connections.models.connection_record import ConnectionRecord
from aries_cloudagent.messaging.valid import UUIDFour
from aries_cloudagent.storage.error import StorageNotFoundError

from .messages.testmessage import Testmessage


class SendMessageSchema(Schema):
    """Request schema for sending a message."""

    content = fields.Str(description="Message content", example="What UP!")


class ConnIdMatchInfoSchema(Schema):
    """Path parameters and validators for request taking connection id."""

    conn_id = fields.Str(
        description="Connection identifier", required=True, example=UUIDFour.EXAMPLE
    )


@docs(tags=["testmessage"], summary="Sending test message")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(SendMessageSchema())
async def connections_send_message(request: web.BaseRequest):
    """
    Request handler to send test message

    Args:
        request:aiohttp request object
    """
    context = request.app["request_context"]
    connection_id = request.match_info["conn_id"]
    outbound_handler = request.app["outbound_message_router"]
    params = await request.json()

    try:
        connection = await ConnectionRecord.retrieve_by_id(context, connection_id)
    except StorageNotFoundError:
        raise web.HTTPNotFound()

    if connection.is_ready:
        msg = Testmessage(content=params["content"])
        await outbound_handler(msg, connection_id=connection_id)

    return web.json_response({})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [web.post("/connections/{conn_id}/Test-message", connections_send_message)]
    )
