#!/usr/bin/python3

import argparse
import pyfiglet

# Available ASCII art fonts
available_fonts = pyfiglet.FigletFont.getFonts()

# Command-line argument parser
parser = argparse.ArgumentParser(description='Convert text to ASCII art.')
parser.add_argument('text', metavar='TEXT', type=str, help='the input text to convert')
parser.add_argument('-f', '--font', choices=available_fonts, default='standard', help='the font style for ASCII art (default: standard)')
parser.add_argument('-o', '--output', metavar='FILE', type=str, help='save the output to a text file')
args = parser.parse_args()

# Generate ASCII art
ascii_art = pyfiglet.figlet_format(args.text, font=args.font)

# Print or save the ASCII art
if args.output:
    with open(args.output, 'w') as file:
        file.write(ascii_art)
    print(f'ASCII art saved to {args.output}')
else:
    print(ascii_art)
