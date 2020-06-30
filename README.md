# Aries-testprotocol-plugin

This repository is a python implementation of a Hyperledger Aries protocol as a plugin.

Hyperledger Aries is an open-source reference architecture that is used for developing self-sovereign identity agents. These aries agents send asynchronous messages using a protocol called DIDComm. The benefits we see when using aries agent’s DIDComm channels for communication is the ability to define flexible and domain-specific trust architectures in the form of trusted credential issuers and verifiable credentials. 

The asynchronous messages sent by aries agents have a type that defines the structure of the message.The message type informs the agent on how to decipher the content and what content is to be expected as part of a given message.Thus each message type has its own handler to carry out agent specific responses according to the message type.

This plugin allows for easy testing of message types for future development. The plugin allows for a Hyperledger Aries protocol to be included in [aries-cloudagent-python](https://github.com/hyperledger/aries-cloudagent-python) as a plugin.

To run the plugin clone the repo and run `./manage up`. This will implement the test-protocol as a plugin with 2 aca-py agents.

You can navigate to the swagger API for the two agents at:

http://localhost:8021/api/doc

http://localhost:8051/api/doc

Simply create a peer to peer connection between the two agents using the swagger interface.Then invoke the protocolexample protocol using the swagger interface to send a protocolexample message from one agent to the other.
