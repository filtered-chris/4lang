from ConfigParser import ConfigParser
import os

from pymachine.utils import MachineGraph
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def batches(l, n):
    """ Yield successive n-sized chunks from l.
    (source: http://stackoverflow.com/questions/312443/
    how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def print_4lang_graphs(words_to_machines, graph_dir):
    for word, machine in words_to_machines.iteritems():
        print_4lang_graph(word, machine, graph_dir)

def print_4lang_graph(word, machine, graph_dir):
    graph = MachineGraph.create_from_machines([machine])
    fn = os.path.join(graph_dir, u"{0}.dot".format(word))
    with open(fn, 'w') as dot_obj:
        dot_obj.write(graph.to_dot().encode('utf-8'))

def get_cfg(cfg_file=None):
    cfg_files = ['conf/default.cfg']
    if cfg_file is not None:
        cfg_files.append(cfg_file)
    cfg = ConfigParser()
    cfg.read(cfg_files)
    return cfg
