import os
import analyses.pymake.parser as parser
from analyses.pymake.parserdata import SetVariable


def obj_definition_filter(path_to_makefile, configs):
    """
    Parse obj-$(CONFIG_XXX) += xxx.o in the given makefile.
    """
    with open(path_to_makefile) as f:
        lines = f.readlines()
    stmts = parser.parsestring(''.join(lines), path_to_makefile)
    results = []
    for stmt in stmts:
        if not isinstance(stmt, SetVariable):
            continue
        if stmt.vnameexp.is_static_string:
            continue
        for v_f in stmt.vnameexp.variable_references():
            config = v_f.vname.s

            if config in configs:
                results.append(stmt)
    return results
