INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin
COMMANDS=couchget couchdel couchput couchcopy couchfromdir \
couchtodir couchgetid couchgrep strtojson jsontostr

.SUFFIXES: .py

all:
	@echo type make install

.py:
	${INSTALL} $< ${DESTDIR}/$@

install: ${COMMANDS}

deinstall:
	rm ${COMMANDS:%=${DESTDIR}/%}
