from __future__ import print_function

import re
import json

def load_data():
    with open('./template.html') as fp:
        template = fp.read()
    with open('./data.json') as fp:
        data = json.load(fp)
    return template, data


START_TOKEN = '<* '
END_TOKEN = ' *>'


def scan_until_start_token(txt, cursor):
    return txt.find(START_TOKEN, cursor)

def scan_until_end_token(txt, cursor):
    return txt.find(END_TOKEN, cursor)

def get(s, *data):
    fields = s.split('.')
    for datum in data:
        try:
            for field in fields:
                datum = datum[field]
            return datum
        except:
            pass

def get_each_var(txt):
    # something like 'EACH students student'
    # or 'EACH student.nicknames nickname'
    match = re.search('EACH (.*) (.*)', txt)
    variable_name, replacement = match.groups()
    return variable_name, replacement

def apply_template(template, data, cursor=0, context=None):
    context = context or {}
    output = []

    while True:
        i = scan_until_start_token(template, cursor)
        plain = template[cursor:i]
        output.append(plain)

        cursor = i

        eof = cursor == -1 or cursor >= len(template)-1
        if eof:
            return output, cursor

        j = scan_until_end_token(template, cursor)

        esc_block = template[i+len(START_TOKEN):j]  # "page.title" or "EACH students student" or "ENDEACH"

        cursor = j+len(END_TOKEN)  # cursor is at the end of the esc_block

        is_endeach_block = 'ENDEACH' in esc_block
        if is_endeach_block:
            return output, cursor

        # if each_block, find the end esc_block and apply_template to the sub section
        is_each_block = 'EACH' in esc_block
        if is_each_block:
            # students, student
            # student.nicknames nickname
            var, replacement = get_each_var(esc_block)
            iter_of_each_data = get(var, context, data)
            for item in iter_of_each_data:
                each_context = context.copy()
                #              student    = student-record
                each_context[replacement] = item
                each_output, endeach_cursor = apply_template(template, data, cursor, context=each_context)
                output.extend(each_output)

            cursor = endeach_cursor
            continue

        # its a substitution block, replace with the value
        var_name = esc_block.strip()
        output.append(get(var_name, context, data))
        continue

def run():
    template, data = load_data()
    output, _ = apply_template(template, data)
    print(''.join(output))

if __name__ == '__main__':
    run()

