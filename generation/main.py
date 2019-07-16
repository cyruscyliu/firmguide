import os

from board import Board
from render import Template

ARM926 = 'arm926'
TEMPLATE_DIR = 'template'

if __name__ == '__main__':
    b = Board(board_name='wrt350n_v2', soc_name='mv88f5181L', cpu_type=ARM926)
    context = b.get_context()
    context['upper'] = lambda x: x.upper()
    templates = os.listdir(TEMPLATE_DIR)
    BOARD_DIR = context['board_name']
    if not os.path.exists(BOARD_DIR):
        os.mkdir(BOARD_DIR)
    for template in templates:
        target = template.replace('_', '.')
        print('generating {} ...'.format(target))
        with open(os.path.join(BOARD_DIR, target), 'w') as f_target:
            with open(os.path.join(TEMPLATE_DIR, template), 'r') as f_template:
                for line in f_template:
                    text_update = Template(line).render(context)
                    f_target.writelines(text_update)
                    f_target.flush()
    print('done!')
