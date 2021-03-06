import gramfuzz
from gramfuzz.fields import *
import fuzz

class YRef(Ref):
    cat = "config_def"
class YDef(Def):
    cat = "config_def"

max_repeat = 2

Def("anyxml", And(YRef("optsep"), YRef("module-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("anyxml-stmt")), "}", cat="anyxml")
YDef("optsep", Or(Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat), ""))
YDef("WSP", Or(YRef("SP"), YRef("HTAB")))
YDef("SP", " ")
YDef("HTAB", "\t")
YDef("line-break", Or(YRef("CRLF"), YRef("LF")))
YDef("CRLF", And(YRef("CR"), YRef("LF")))
YDef("CR", "")
YDef("LF", "\n")
YDef("module-keyword", "module")
YDef("sep", Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat))
YDef("identifier-arg-str", YRef("identifier-arg"))
YDef("identifier-arg", YRef("identifier"))
YDef("identifier", And(Or(YRef("ALPHA"), "_"), Or(Join(Or(YRef("ALPHA"), YRef("DIGIT"), "_", "-", "."), sep="", max=max_repeat), "")))
YDef("ALPHA", String(charset=String.charset_alpha))
YDef("DIGIT", String(charset="0123456789"))
YDef("stmtsep", Or(Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat), ""))
YDef("anyxml-stmt", And(YRef("anydata-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("anydata-keyword", "anydata")
YDef("when-stmt", And(YRef("when-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("when-keyword", "when")
YDef("string", YRef("yang-string"))
YDef("yang-string", Or(Join(YRef("yang-char"), sep="", max=max_repeat), ""))
YDef("yang-char", String(max=1))
YDef("description-stmt", And(YRef("description-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("description-keyword", "description")
YDef("stmtend", And(YRef("optsep"), Or(";", And("{", YRef("stmtsep"), "}")), YRef("stmtsep")))
YDef("reference-stmt", And(YRef("reference-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("reference-keyword", "reference")
YDef("if-feature-stmt", And(YRef("if-feature-keyword"), YRef("sep"), YRef("if-feature-expr-str"), YRef("stmtend")))
YDef("if-feature-keyword", "if-feature")
YDef("if-feature-expr-str", YRef("if-feature-expr"))
YDef("if-feature-expr", And(YRef("if-feature-term"), Or(And(YRef("sep"), YRef("or-keyword"), YRef("sep"), YRef("if-feature-expr")), "")))
YDef("if-feature-term", And(YRef("if-feature-factor"), Or(And(YRef("sep"), YRef("and-keyword"), YRef("sep"), YRef("if-feature-term")), "")))
YDef("if-feature-factor", Or(And(YRef("not-keyword"), YRef("sep"), YRef("if-feature-factor")), And("(", YRef("optsep"), YRef("if-feature-expr"), YRef("optsep"), ")"), YRef("identifier-ref-arg")))
YDef("not-keyword", "not")
YDef("identifier-ref-arg", YRef("identifier-ref"))
YDef("identifier-ref", And(Or(And(YRef("prefix"), ":"), ""), YRef("identifier")))
YDef("prefix", YRef("identifier"))
YDef("and-keyword", "and")
YDef("or-keyword", "or")
YDef("must-stmt", And(YRef("must-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("must-keyword", "must")
YDef("error-message-stmt", And(YRef("error-message-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("error-message-keyword", "error-message")
YDef("error-app-tag-stmt", And(YRef("error-app-tag-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("error-app-tag-keyword", "error-app-tag")
YDef("config-stmt", And(YRef("config-keyword"), YRef("sep"), YRef("config-arg-str"), YRef("stmtend")))
YDef("config-keyword", "config")
YDef("config-arg-str", Or(YRef("true-keyword"), YRef("false-keyword")))
YDef("true-keyword", "true")
YDef("false-keyword", "false")
YDef("mandatory-stmt", And(YRef("mandatory-keyword"), YRef("sep"), YRef("mandatory-arg-str"), YRef("stmtend")))
YDef("mandatory-keyword", "mandatory")
YDef("mandatory-arg-str", Or(YRef("true-keyword"), YRef("false-keyword")))
YDef("status-stmt", And(YRef("status-keyword"), YRef("sep"), YRef("status-arg-str"), YRef("stmtend")))
YDef("status-keyword", "status")
YDef("status-arg-str", Or(YRef("current-keyword"), YRef("obsolete-keyword"), YRef("deprecated-keyword")))
YDef("current-keyword", "current")
YDef("obsolete-keyword", "obsolete")
YDef("deprecated-keyword", "deprecated")