from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class CreateCommand(Command):

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.CREATE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "CREATE PAIR <key> WITH VALUE <value>"
    
    @override
    @classmethod
    def generate_req_payload(cls, **kwargs):
        # Expect a key followed by a message
        key = kwargs.get("key", None)
        if key is None:
            raise Exception("Syntax error: CREATE expects a key")
        value = kwargs.get("value", None)
        if value is None:
            raise Exception ("Syntax Error: CREATE expects a value")
        
        create_message = smpb2.CreateKVPairReq()
        create_pair = smpb2.KeyValuePair()

        create_pair.key = key
        create_pair.value = value
        create_message.pair.CopyFrom(create_pair)

        return create_message
    
    @override
    @classmethod
    def parse_response(cls, payload):
        pass
    