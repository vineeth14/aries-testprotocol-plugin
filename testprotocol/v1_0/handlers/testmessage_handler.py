"""Test message handler"""

from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)

from ..messages.testmessage import Testmessage


class TestmessageHandler(BaseHandler):
    """Handler class for Test message"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        self._logger.info("TestmessageHandler is called")
        assert isinstance(context.message, Testmessage)

        self.logger.info("Received testmessage: %s", context.message.content)

        body = context.message.content
        meta = {"content": body}

        # For Workshop: mark invitations as copyable
        if context.message.content and context.message.content.startswith(
            ("http:", "https:")
        ):
            meta["copy_invite"] = True

        await responder.send_webhook(
            "testmessages",
            {
                "connection_id": context.connection_record.connection_id,
                "message_id": context.message._id,
                "content": body,
                "state": "received",
            },
        )
        reply = None
        if body:
            if context.settings.get("debug.auto_respond_messages"):
                if "received your message" not in body:
                    reply = f"{context.default_label} received your message"
            elif body.startswith("Reply with: "):
                reply = body[12:]

        if reply:
            reply_msg = Testmessage(message=reply)
            reply_msg.assign_thread_from(context.message)
            reply_msg.assign_trace_from(context.message)
            if "l10n" in context.message._decorators:
                reply_msg._decorators["l10n"] = context.message._decorators["l10n"]
            await responder.send_reply(reply_msg)
