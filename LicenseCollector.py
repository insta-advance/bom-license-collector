#!/usr/bin/env python3

# BOM License Collector generates a file that contains all license texts
# of a BOM xml file. The script is designed to work with CycloneDX BOM files.
#
# MIT License
#
# Copyright (c) 2019 Intopalo Digital


import argparse
from xml.dom.minidom import parse

def main():
    """
    Creates a file containing license texts from a given bom file
    """
    parser = argparse.ArgumentParser(description='License Text Collector for BOM files')
    parser.add_argument('-i', action="store", dest="input_file", default="bom.xml")
    parser.add_argument('-o', action="store", dest="output_file", default="license_texts.txt")
    args = parser.parse_args()

    try:
        license_text_separator = '\n' + '-'*110 + '\n'
        all_license_text = ''

        with open(args.input_file, 'r') as bom_file:
            for license_elements in parse(bom_file).getElementsByTagName('license'):
                for license_text_elements in license_elements.getElementsByTagName('text'):
                    all_license_text += license_text_elements.firstChild.data + license_text_separator

        with open(args.output_file, 'w') as out_file:
            out_file.write(all_license_text)
            print("License texts in a file \"" + args.output_file + "\"")

    except Exception as e:
        print(e)

main()
