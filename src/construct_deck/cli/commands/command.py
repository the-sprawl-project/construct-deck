from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Any

class CommandType(IntEnum):
    """
    The command type of this SQL query.
    """
    SENTINEL = -1
    PING = 0
    CREATE = 1
    READ = 2
    UPDATE = 3
    DELETE = 4


class Command(ABC):

    # Must be overridden by all inheritors of this class
    @classmethod
    @abstractmethod
    def command_type(cls) -> CommandType:
        return CommandType.SENTINEL
    
    # Basic syntax help, must be overridden as well
    @classmethod
    @abstractmethod
    def help_syntax(cls) -> str:
        return "Override Me"

    # Build the protobuf object
    @abstractmethod
    def make_proto(self) ->Any:
        pass

    # Generate request payload for this command, and is dependent on the
    # object.
    @abstractmethod
    def generate_req_payload(self) -> Any:
        pass

    # Parse response for this command. Expects a byte array as input, parses
    # the response for downstream use
    @classmethod
    @abstractmethod
    def parse_response(cls, payload: bytes):
        pass
