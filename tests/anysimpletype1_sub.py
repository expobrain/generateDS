#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 2.7.13 (default, May  2 2017, 14:07:15)  [GCC 6.3.0 20170406]
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--silence', '')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-o', 'tests/anysimpletype2_sup.py')
#   ('-s', 'tests/anysimpletype2_sub.py')
#   ('--super', 'anysimpletype2_sup')
#
# Command line arguments:
#   tests/anysimpletype.xsd
#
# Command line:
#   generateDS.py --no-dates --no-versions --silence --member-specs="list" -f -o "tests/anysimpletype2_sup.py" -s "tests/anysimpletype2_sub.py" --super="anysimpletype2_sup" tests/anysimpletype.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys
from lxml import etree as etree_

import anysimpletype2_sup as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class test1elementSub(supermod.test1element):
    def __init__(self, test1attribute=None, test1member=None):
        super(test1elementSub, self).__init__(test1attribute, test1member, )
supermod.test1element.subclass = test1elementSub
# end class test1elementSub


class cimAnySimpleTypeSub(supermod.cimAnySimpleType):
    def __init__(self, valueOf_=None):
        super(cimAnySimpleTypeSub, self).__init__(valueOf_, )
supermod.cimAnySimpleType.subclass = cimAnySimpleTypeSub
# end class cimAnySimpleTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'test1element'
        rootClass = supermod.test1element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='',
##             pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'test1element'
        rootClass = supermod.test1element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(content)
##         sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'test1element'
        rootClass = supermod.test1element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'test1element'
        rootClass = supermod.test1element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('#from anysimpletype2_sup import *\n\n')
##         sys.stdout.write('import anysimpletype2_sup as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
