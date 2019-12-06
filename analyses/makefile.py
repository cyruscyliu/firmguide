import pymake.pymake.parser as parser
from pymake.pymake.parserdata import SetVariable


def definition_filter(target, path_to_makefile, configs):
    with open(path_to_makefile) as f:
        lines = f.readlines()
    stmts = parser.parsestring(''.join(lines), path_to_makefile)
    results = []
    for stmt in stmts:
        if not isinstance(stmt, SetVariable):
            continue
        if stmt.vnameexp.is_static_string:
            continue
        if stmt.vnameexp[0][0] != target:
            continue
        for v_f in stmt.vnameexp.variable_references():
            config = v_f.vname.s

            if config in configs:
                results.append(stmt)
    return results


def obj_definition_filter(path_to_makefile, configs):
    """
    Parse obj-$(CONFIG_XXX) += xxx.o in the given makefile.
    """
    return definition_filter('obj-', path_to_makefile, configs)


def machine_definition_filter(path_to_makefile, configs):
    """
    Parse machine-$(CONFIG_XXX) += xxx.o in the given makefile.
    """
    return definition_filter('machine-', path_to_makefile, configs)
