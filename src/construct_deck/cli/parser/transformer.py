from lark import Transformer
from lark.lexer import Token

class ConstructTransformer(Transformer):

    def _strip(self, token):
        if isinstance(token, Token):
            val = token.value
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            return val
        return str(token)

    # each rule type and token type requires a parse
    def ping__CNAME(self, args):
        return self._strip(args)
    
    def ping__ESCAPED_STRING(self, args):
        return self._strip(args)

    def ping_stmt(self, args):
        msg = args[0]
        return ("PING", msg)