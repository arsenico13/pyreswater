#!/usr/bin/python

'''

Author 	: Nasir Khan (r0ot h3x49)
Github 	: https://github.com/r0oth3x49
License : MIT
Edited by 	: arsenico13


Copyright (c) 2018-2019 Nasir Khan (r0ot h3x49)
Copyright (c) 2019 Giacomo Monari (arsenico13)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

'''

from .colors import *


def banner():
    banner = '''
%s%s   Python Watermark (and Resize) Tool
              %s%sVersion : %s%s0.5
              %s%sAuthor  : %s%sarsenico13
              %s%sGithub  : %s%shttps://github.com/arsenico13

''' % (fy, sb, fy, sd, fg, sd, fy, sd, fg, sd, fy, sd, fg, sd)
    return banner
