# pip3 antlr4_python3_runtime
# git clone https://github.com/deeso/antlr_vb

import antlr4
from antlr_vb.vb6.VisualBasic6Parser import VisualBasic6Parser
from antlr_vb.vb6.VisualBasic6Parser import VisualBasic6Parser
from antlr_vb.vb6.VisualBasic6Lexer import VisualBasic6Lexer
from antlr_vb.vb6.VisualBasic6Listener import VisualBasic6Listener
filename = "../obfuscated_code"
data = open(filename).read()


lexer = VisualBasic6Lexer(data)
stream = antlr4.CommonTokenStream(lexer)
parser = VisualBasic6Parser(stream)
tree = parser.expression()


from antlr_vb.vba.vbaParser import vbaParser
from antlr_vb.vba.vbaParser import vbaParser
from antlr_vb.vba.vbaLexer import vbaLexer
from antlr_vb.vba.vbaListener import vbaListener

lines = '\n'.join(data.split(':'))).strip()
lexer = vbaLexer(antlr4.InputStream(data))
stream = antlr4.CommonTokenStream(lexer)
parser = vbaParser(stream)
