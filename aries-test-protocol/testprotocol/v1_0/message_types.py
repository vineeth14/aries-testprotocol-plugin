PROTOCOL_URI = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/testprotocol/1.0"

TEST_MESSAGE = f"{PROTOCOL_URI}/testprotocol"


NEW_PROTOCOL_URI = "https://didcomm.org/testprotocol/1.0"

NEW_TEST_MESSAGE = f"{NEW_PROTOCOL_URI}/testprotocol"


PROTOCOL_PACKAGE = "acapy_testprotocol.testprotocol.v1_0"

MESSAGE_TYPES = {
    TEST_MESSAGE: f"{PROTOCOL_PACKAGE}.messages.testprotocol.testprotocol",
    NEW_TEST_MESSAGE: f"{PROTOCOL_PACKAGE}.messages.testprotocol.testprotocol",
}
