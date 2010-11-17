#!/usr/bin/env python

# Copyright (c) 2010 Nicolas P. M. Legrand <nlegrand@ethelred.fr>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os, sys, json, base64, re

json_data = sys.stdin.read()
doc = json.loads(json_data)
dir = re.sub("/",".", doc['_id'])

if not os.path.exists(dir):
   os.mkdir(dir)

for key in doc:
    if key == 'views':
        for view in doc[key]:
            view_dir = os.path.join(dir, key, view)
            if not os.path.exists(view_dir):
                os.makedirs(view_dir)
            for js in doc[key][view]:
                js_file = os.path.join(view_dir, js + '.js')
                f = open(js_file, 'w')
                f.write(eval(json.dumps(doc[key][view][js]
                                        , indent=4)))
    elif key == 'shows' or key == 'lists' or key == 'commonjs':
        show_or_list_dir = os.path.join(dir, key)
        if not os.path.exists(show_or_list_dir):
            os.makedirs(show_or_list_dir)
        for js in doc[key]:
            js_file = os.path.join(dir,key, js + '.js')
            f = open(js_file,'w')
            f.write(eval(json.dumps(doc[key][js]
                                    , indent=4)))
    elif re.search("^template_",key):
       file_name = "exports_" + key
       f = open(os.path.join(dir, file_name), 'w')
       f.write(json.loads(re.sub('^exports.str = | ;$', '', eval(json.dumps(doc[key])))).encode('UTF-8'))
       f.close()
    elif key != '_attachments' and not re.search("^template_",key):
        value = eval(json.dumps(doc[key]))
        if type(value) is str:
           if re.search('^"exports.str = ', value):
              value = re.sub('^"exports.str = | ;$', '', json.loads(doc[key]), 2)
              key = "lol_exports_" + key
           else:
              value = json.dumps(doc[key], indent=4)
        else:
           value = json.dumps(doc[key], indent=4)
        f = open(os.path.join(dir, key), 'w')
        f.write(value)
        f.close()
    else:
        attachments_dir = os.path.join(dir, "_attachments")
        if not os.path.exists(attachments_dir):
            os.mkdir(attachments_dir)
        for attachment in doc[key]:
            if not "stub" in doc[key][attachment]:
                attachment_file = os.path.join(dir, "_attachments/", attachment)
                f = open(attachment_file, 'wb')
                data = base64.b64decode(doc[key][attachment]['data'])
                f.write(data)
