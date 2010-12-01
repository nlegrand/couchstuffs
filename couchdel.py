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

import sys, httplib, getopt, ConfigParser, os, json

opts, args = getopt.getopt(sys.argv[1:], 'h:p:s:c:')

def usage():
    print "couchdelete -c <config> -s <config section> -h <host> -p <port> /<base>[/<ressource>]?rev=<rev>"

host           = ""
port           = ""
config_file    = ""
config_section = ""


for o, a in opts:
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

rev_connexion = httplib.HTTPConnection(host, port)
rev_connexion.request("GET", args[0])
rev_response = rev_connexion.getresponse()
rev_response_output = rev_response.read()
if rev_response.status != 200:
    sys.stderr.write(str(rev_response.status) + " "
                     + rev_response.reason + "\n")
    sys.stdout.write(rev_response_output)
    sys.exit(1)
try:
    doc = json.loads(rev_response_output)
except ValueError:
    sys.stderr.write("http://" + host + ":" + "port" + args[0]
                     + " answer doesn't seem to be JSON\n")
    sys.exit(1)
    

#check if doc is a ressource or a database
if '_rev' in doc:
    url_arg = "?rev=" + doc['_rev']
elif 'db_name' in doc:
    url_arg = ""
else:
    sys.stderr.write("cannot get _rev from ressource:"
                     + host + ":" + port + "/" + args[0] + "\n")
    sys.exit(1)

connexion = httplib.HTTPConnection(host, port)

connexion.request("DELETE", args[0] + url_arg)
response = connexion.getresponse()
sys.stderr.write(str(response.status) + " "
                 + response.reason + "\n")
sys.stdout.write(response.read())
