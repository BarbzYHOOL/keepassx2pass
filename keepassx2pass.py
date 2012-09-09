#! /usr/bin/env python

from xml.etree import ElementTree
from sys import argv

def import_entry(element, path=''):
    print element
    print element.find('title').text

def import_group(element):
    print element
    print element.find('title').text
    for g in element.findall('group'):
        import_group(g)
    for e in element.findall('entry'):
        import_entry(e)


if __name__ == '__main__':
    with open(argv[1]) as f:
        doc = ElementTree.XML(f.read())
        for g in doc.findall('group'):
            import_group(g)
