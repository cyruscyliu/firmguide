#!/usr/bin/python

import json
import argparse


def preprocessor(path_to_assembly_file):
    """
    remove comments and blank lines
    """
    with open(path_to_assembly_file) as f:
        lines = f.readlines()

    lines_preprocessed = []
    for line in lines:
        line = line.strip()
        if line.startswith('#'):  # whole line comment
            continue
        if not len(line):  # block lines
            continue
        line, _, comments = line.partition('@')  # partial line comment
        split_lines = line.split(';')
        for split_line in split_lines:
            split_line = split_line.strip()
            lines_preprocessed.append(split_line)

    return lines_preprocessed


def parse(lines_preprocessed):
    """
    parser all macros
    the syntax should be
        .macro name, conditions
        .endm
    """
    target_json = {}

    macro_stack = []
    global_stack = []
    type_stack = []
    section = None

    for line in lines_preprocessed:
        line = line.strip()
        if line.startswith('.macro'):
            # .macro macname
            # .macro macname p1,p2
            # .macro macname,p1,p2
            # .macro macname p1 p2
            macro_name = None
            macro_conditions = []
            for i in line[7:].split():
                for j in i.split(','):
                    if not len(j):
                        continue
                    if macro_name is None:
                        macro_name = j
                    else:
                        macro_conditions.append(j)
            macro_stack.append(macro_name)
            target_json[macro_name] = {
                'type': 'macro', 'section': section,
                'name': macro_name, 'arguments': macro_conditions, 'body': [],
            }
        elif line.startswith('.endm'):
            macro_stack.pop(-1)
        elif len(macro_stack):  # in macro body
            macro_name = macro_stack[-1]
            target_json[macro_name]['body'].append(line)
        elif line.startswith('.globl'):
            if len(type_stack):
                type_stack.pop(-1)
            if len(global_stack):
                global_stack.pop(-1)
            global_name = line.split()[1]
            global_stack.append(global_name)
            target_json[global_name] = {
                'type': 'global', 'section': section,
                'name': global_name, 'arguments': None, 'body': []
            }
        elif line.startswith('.type'):
            if len(type_stack):
                type_stack.pop(-1)
            if len(global_stack):
                global_stack.pop(-1)
            # .type xxx, #object
            # .type xxx, %function
            t = line.split('#')
            if len(t) != 2:
                type_ = line.split('%')[1]
            else:
                type_ = line.split('#')[1]
            name = line.split()[1].split(',')[0]
            type_stack.append(name)
            target_json[name] = {
                'type': type_, 'section': section,
                'name': name, 'arguments': None, 'body': []
            }
        elif line.startswith('.section'):
            section_info = line[8:].split(',')
            section_name = section_info[0].strip()
            if len(section_info) > 1:
                section_attribute = [i.strip() for i in section_info[1:]]
            else:
                section_attribute = None
            section = {'name': section_name, 'attirbute': section_attribute}
        elif line.startswith('.size'):
            # skip .size in type body
            pass
        elif len(global_stack):  # in global body
            global_name = global_stack[-1]
            target_json[global_name]['body'].append(line)
        elif len(type_stack):  # in type body
            name = type_stack[-1]
            if line.startswith(name):
                # skip the label in type body
                continue
            target_json[name]['body'].append(line)
        else:
            pass

    return target_json


def asm2json(path_to_assembly_file_preprocessed):
    lines = preprocessor(path_to_assembly_file_preprocessed)
    return parse(lines)

test_json = asm2json('test.i')
with open('test.json', 'w') as f:
    json.dump(test_json, f)

