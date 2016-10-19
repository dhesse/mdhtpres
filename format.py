#!/usr/bin/env python

from fragments import wrap

import argparse
import re

def tagify(**args):
    return "<{tag}>\n{text}\n</{tag}>".format(**args)

def sub_headings(mdstring):
    def mk_heading(match):
        tag_name = "h"  + str(len(match.group(1)))
        return tagify(tag=tag_name,
                      text=match.group(2).strip())
    return re.sub(r"^(#+)(.+)", mk_heading, mdstring)

PARSERS = [sub_headings]

def parse_slide(slidetext, parsers=PARSERS):
    if parsers:
        return parse_slide(parsers[0](slidetext),
                           parsers[1:])
    return tagify(tag="div class=slide",
                  text=slidetext)

def parse_md(markdown_string, callback, sep):
    slide_gen = (callback(slide)
                 for slide in markdown_string.split(sep))
    return "\n".join(slide_gen)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="File to parse.")
    parser.add_argument("--sep", default="---",
                        help="Separator between slides.")
    args = parser.parse_args()
    sep = "\n{0}\n\n".format(args.sep)
    with open(args.input_file, "r") as input_file:
        print wrap(parse_md(input_file.read(), parse_slide, sep))
