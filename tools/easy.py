import os
import yaml


def p_wrapper(string, indent):
    # return '<p>' + ' ' * indent + string + '</p>\n'
    return ' ' * indent + string + '\n'


def main():
    paused_analyses = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'pause.yaml')))
    f = open(os.path.join(os.getcwd(), 'tools', 'pause'), 'w')
    for k, v in paused_analyses.items():
        f.write(p_wrapper(k, 0))
        for kk, vv in v.items():
            f.write(p_wrapper(kk, 0))
            vv = vv.strip()
            for vvv in vv.split('\n'):
                f.write(p_wrapper(vvv, 4))
        f.write(p_wrapper('----------------------------------------------------------------', 0))


if __name__ == '__main__':
    main()
