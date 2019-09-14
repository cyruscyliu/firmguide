#!/usr/bin/env python

import sys
import binwalk

for module in binwalk.scan(*sys.argv[1:], signature=True, quit=False, extract=False):
    print('%s Results:' % module.name)
    # for result in module.results:
    #     if result.file.path in module.extractor.output:
    #         if module.extractor.output[result.file.path].extracted.has_key(result.offset):
    #             pass
