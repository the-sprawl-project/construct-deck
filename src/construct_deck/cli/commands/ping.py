from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class PingCommand(Command):

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.PING
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "PING <message>"
    
    @override
    @classmethod
    def generate_req_payload(cls, **kwargs):
        # Expect a message
        message = kwargs.get("message", None)
        if message is None:
            raise Exception("Syntax error: PING expects a message")
        ping_message = smpb2.PingRequest()
        ping_message.ping_message = message
        
        return ping_message
        
    @override
    @classmethod
    def parse_response(cls, payload):
        pass