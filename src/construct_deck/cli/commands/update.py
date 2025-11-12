from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class UpdateCommand(Command):

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.CREATE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "UPDATE PAIR <key> to VALUE <value>"
    
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
        
        update_message = smpb2.UpdateKVPairReq()
        update_pair = smpb2.KeyValuePair()

        update_pair.key = key
        update_pair.value = value
        update_message.pair.CopyFrom(update_pair)

        return update_message
