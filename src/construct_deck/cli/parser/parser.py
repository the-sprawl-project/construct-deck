from lark import Lark
import pathlib

GRAMMAR_PATH = pathlib.Path(__file__).parent.parent / "grammar"

parser = Lark.open(str(GRAMMAR_PATH / "base.lark"), start="start", rel_to=__file__)