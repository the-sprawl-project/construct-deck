from .command import Command, CommandType
from typing import Any, override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class PingCommand(Command):

    def __init__(self, msg):
        self._msg = msg

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.PING
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "PING <message>"
    
    def make_proto(self):
        message = self._msg
        ping_message = smpb2.PingRequest()
        ping_message.ping_message = message

        return ping_message
    
    @override
    def generate_req_payload(self):
        return self.make_proto()

    @override
    @classmethod
    def parse_response(cls, payload):
        pass