from .command import Command, CommandType
from typing import override
import construct_deck.construct_protocol.socket_messages_pb2 as smpb2

class DeleteCommand(Command):

    def __init__(self, key):
        self._key = key

    @override
    @classmethod
    def command_type(cls) -> CommandType:
        return CommandType.DELETE
    
    @override
    @classmethod
    def help_syntax(cls) -> str:
        return "DELETE PAIR <key>"
    
    @override
    def make_proto(self):
        key = self._key
        drop_message = smpb2.DeleteKVPairReq()
        drop_message.key = key

        return drop_message
    
    @override
    def generate_req_payload(self):
        return self.make_proto()
    
    @override
    @classmethod
    def parse_response(cls, payload):
        pass
