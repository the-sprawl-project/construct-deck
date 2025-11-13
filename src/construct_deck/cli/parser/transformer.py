from lark import Transformer, Token

class ConstructTransformer(Transformer):
    def message(self, args):
        # message → a single Token, either ESCAPED_STRING or CNAME
        token = args[0]
        if isinstance(token, Token):
            value = token.value
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            return value
        return str(token)

    def ping_stmt(self, args):
        msg = args[0]
        # Strip quotes for escaped strings
        if msg.startswith('"') and msg.endswith('"'):
            msg = msg[1:-1]
        
        return ("PING", msg)