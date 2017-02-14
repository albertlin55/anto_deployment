#!/usr/bin/python2.7

import argparse
import os
import sys
import subprocess
import json

def deploy_main(path):

    proc = subprocess.Popen(['fuel2', 'node', 'list', '-f', 'json'], stdout=subprocess.PIPE)

    if proc.returncode != 0:
        print 'command fuel2 not found \n'
        sys.exit(1)

    nodeinfo = proc.communicate()

    nodeinfo_json = json.loads(nodeinfo[0])

    print "ggyy \n"

# class FooAction(argparse.Action):
#      def __init__(self, option_strings, dest, nargs=None, **kwargs):
#          print 'gg \n'
#          super(FooAction, self).__init__(option_strings, dest, **kwargs)
#
#      def __call__(self, parser, namespace, values, option_string=None):
         #deploy_main()


def load_env_cfg_main():
    pass


class Deployment(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        #print 'gg \n'
        super(Deployment, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        #deploy_main()
        return 1

    def pr(self, yy):
        print self.dest

#class gy1:


# class FooAction(argparse.Action):
#     def __init__(self, option_strings, dest, nargs=None, **kwargs):
#         if nargs is not None:
#             raise ValueError("nargs not allowed")
#         super(FooAction, self).__init__(option_strings, dest, **kwargs)
#
#     def __call__(self, parser, namespace, values, option_string=None):
#         print '%r %r %r' % (namespace, values, option_string)
#             setattr(namespace, self.dest, values)

#x = Deployment("tt", dest = "hh")

#x.pr("ss\n")
parser = argparse.ArgumentParser(description='Process some integers.')

#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')

#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

#parser.add_argument("gg", action=FooAction)

parser.add_argument("--deployment", action="store_true", help='Deploy New Openstack environment.', default='True')

parser.add_argument("--dir", help='select directory to which store fuel configure files.', default='./')

#parser.add_argument("--node", help='select directory to which store fuel configure files.')
#
#parser.add_argument('-integ', '--gui')
#parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()

if not os.path.isdir(args.dir):
    print "The path don't exist."
    sys.exit()
#    print os.path.isdir(args.dir)

if args.deployment:
    deploy_main(args.dir)
    print args.deployment

print args.dir

##print args.accumulate(args.integers)



