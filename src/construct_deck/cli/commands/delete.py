from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class DeleteCommand(Command):

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.DELETE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "DELETE PAIR <key>"
    
    @override
    @classmethod
    def generate_req_payload(cls, **kwargs):
        # Expect a key to drop
        key = kwargs.get("key", None)
        if key is None:
            raise Exception("Syntax Error: DELETE expects a key")
        
        drop_message = smpb2.DeleteKVPairReq()
        drop_message.key = key

        return drop_message
    
    @override
    @classmethod
    def parse_response(cls, payload):
        pass
