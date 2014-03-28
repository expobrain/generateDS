#!/usr/bin/env python

#
# Generated  by generateDS.py.
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--silence', '')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-o', 'tests/anywildcard2_sup.py')
#   ('-s', 'tests/anywildcard2_sub.py')
#   ('--super', 'anywildcard2_sup')
#
# Command line arguments:
#   tests/anywildcard.xsd
#

import sys

import anywildcard2_sup as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class PlantType_singleSub(supermod.PlantType_single):
    def __init__(self, name=None, anytypeobjs_=None, description=None):
        super(PlantType_singleSub, self).__init__(name, anytypeobjs_, description, )
supermod.PlantType_single.subclass = PlantType_singleSub
# end class PlantType_singleSub


class PlantType_multipleSub(supermod.PlantType_multiple):
    def __init__(self, name=None, anytypeobjs_=None, description=None):
        super(PlantType_multipleSub, self).__init__(name, anytypeobjs_, description, )
supermod.PlantType_multiple.subclass = PlantType_multipleSub
# end class PlantType_multipleSub


class DescriptionTypeSub(supermod.DescriptionType):
    def __init__(self, name=None, size=None):
        super(DescriptionTypeSub, self).__init__(name, size, )
supermod.DescriptionType.subclass = DescriptionTypeSub
# end class DescriptionTypeSub


class CatalogTypeSub(supermod.CatalogType):
    def __init__(self, name=None, catagory=None):
        super(CatalogTypeSub, self).__init__(name, catagory, )
supermod.CatalogType.subclass = CatalogTypeSub
# end class CatalogTypeSub


class PlantType_single_nochildSub(supermod.PlantType_single_nochild):
    def __init__(self, anytypeobjs_=None):
        super(PlantType_single_nochildSub, self).__init__(anytypeobjs_, )
supermod.PlantType_single_nochild.subclass = PlantType_single_nochildSub
# end class PlantType_single_nochildSub


class PlantType_multiple_nochildSub(supermod.PlantType_multiple_nochild):
    def __init__(self, anytypeobjs_=None):
        super(PlantType_multiple_nochildSub, self).__init__(anytypeobjs_, )
supermod.PlantType_multiple_nochild.subclass = PlantType_multiple_nochildSub
# end class PlantType_multiple_nochildSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PlantType_single'
        rootClass = supermod.PlantType_single
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
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PlantType_single'
        rootClass = supermod.PlantType_single
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
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PlantType_single'
        rootClass = supermod.PlantType_single
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
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PlantType_single'
        rootClass = supermod.PlantType_single
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('#from anywildcard2_sup import *\n\n')
##         sys.stdout.write('import anywildcard2_sup as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
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
