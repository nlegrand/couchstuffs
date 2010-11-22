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

import sys, fileinput, json, httplib, re, getopt, ConfigParser, os

opts, args = getopt.getopt(sys.argv[1:], 'h:p:s:c:')

host           = ""
port           = ""
config_file    = ""
config_section = ""

for o, a in opts:
    sys.stderr.write(o + a + "\n")
    if o == '-h':
        host = a
    if o == '-p':
        port = a
    if o == '-c':
        config_file = a
    if o == '-s':
        config_section = a

config = ConfigParser.ConfigParser()
if not config_section:
    config_section = 'default'
if not config_file:
    config_file = "~/.couchstuffs"
config.read([os.path.expanduser(config_file)])

if not host:
    host = config.get(config_section, 'host')
if not port:
    port = config.get(config_section, 'port')

connexion = httplib.HTTPConnection(host + ":" + port)

if re.search("^/[a-zA-Z0-9\-_\.]+$", args[0]):
    connexion.request("PUT",args[0])
else:
    json_data = sys.stdin.read()
    connexion.request("PUT",args[0],
                 json_data, {"Content-type": "application/json"}) 

http_response    = connexion.getresponse()
couchdb_response = http_response.read()

if os.path.exists('_rev') and http_response.reason == "Created": #bump version
    f = open('_rev','w')
    resp = json.loads(couchdb_response)
    f.write(json.dumps(resp["rev"]))

sys.stderr.write(str(http_response.status) + " "
                 + http_response.reason + "\n")
sys.stdout.write(couchdb_response)
