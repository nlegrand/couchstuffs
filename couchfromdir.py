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

import sys, json, os, httplib, pprint, urllib, re, mimetypes, base64

file_list = os.listdir(".")

try:
    file_list.index("_id")
except ValueError:
    sys.stderr.write("No '_id' file, this doesn't look like a couchtodir directory\n")
    sys.exit(1)

json_data = {}

for file in file_list:
    if file == 'views':
        json_data[file] = {}
        for view in os.listdir(file):
            if re.search('~$', view):
                continue
            json_data[file][view] = {}
            f = open(os.path.join(file, view, 'map.js'),'r')
            map = re.sub('"', '\"',f.read())
            f.close()
            json_data[file][view] = { 'map' : map}
            if os.path.isfile(os.path.join(file, view, 'reduce.js')):
                f = open(os.path.join(file, view, '/reduce.js','r'))
                reduce = re.sub('"', '\"',f.read())
                f.close()
                json_data['views'][view]['reduce'] = reduce
    elif file == 'shows' or file == 'lists' or file == 'commonjs':
        json_data[file] = {}
        for js in os.listdir(file):
            if re.search("~$", js):
                continue
            f = open(os.path.join(file, js),'r')
            fdata = f.read()
            f.close()
            json_data[file][re.sub('\.js$', '', js)] = fdata
    elif re.search('^exports_', file) and not re.search("~$", file):
        f = open(file, 'r')
        json_data[re.sub('^exports_','', file)] = "exports.str = " + json.dumps(f.read()) + " ;"
    elif not re.search("^\.|~$", file) and file != '_attachments':
        try:
            json_data[file] = json.loads(open(file, "r").read())
        except ValueError:
            sys.stderr.write("file " + file + " doesn't look like a JSON file\n")
            sys.exit(1)
    elif file == '_attachments':
        json_data['_attachments'] = {}
        for attachment in os.listdir('_attachments'):
            if re.search('~$', attachment):
                continue
            mime = mimetypes.guess_type('_attachments' + attachment)[0]
            if not mime:
                sys.stderr.write("Can't guess _attachments/" + attachment + "mime-type")
                continue
            b = open('_attachments/' + attachment, 'rb')
            content = base64.b64encode(b.read())
            json_data['_attachments'][attachment] = {
                "content_type" : mime,
                "data" : content
                }
        

print json.dumps(json_data)


