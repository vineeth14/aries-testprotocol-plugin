"""Test Message"""

from ..message_types import PROTOCOL_PACKAGE, TEST_MESSAGE
from marshmallow import fields

from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.testmessage_handler.TestmessageHandler"


class Testmessage(AgentMessage):
    class meta:
        handler_class = HANDLER_CLASS
        message_type = TEST_MESSAGE
        schema_class = "TestmessageSchema"

    def __init__(
        self, *, content: str = None, localization: str = None, **kwargs,
    ):

        super().__init__(**kwargs)
        if localization:
            self._decorators["l10n"] = localization
        self.content = content


class TestmessageSchema(AgentMessageSchema):

    """ Schema for the test message"""

    class meta:
        model_class = Testmessage

    content = fields.Str(
        required=False,
        description="This is an example of a string field in your message",
        example="this is an example",
        allow_none=False,
    )
