INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchget.py ${DESTDIR}/couchget
	${INSTALL} couchdel.py ${DESTDIR}/couchdel
	${INSTALL} couchput.py ${DESTDIR}/couchput
	${INSTALL} couchcopy.py ${DESTDIR}/couchcopy
	${INSTALL} couchfromdir.py ${DESTDIR}/couchfromdir
	${INSTALL} couchtodir.py ${DESTDIR}/couchtodir
	${INSTALL} couchgetid.py ${DESTDIR}/couchgetid
	${INSTALL} strtojson.py ${DESTDIR}/strtojson
	${INSTALL} jsontostr.py ${DESTDIR}/jsontostr

deinstall:
	rm ${DESTDIR}/couchget
	rm ${DESTDIR}/couchdel
	rm ${DESTDIR}/couchput
	rm ${DESTDIR}/couchcopy
	rm ${DESTDIR}/couchfromdir
	rm ${DESTDIR}/couchtodir
	rm ${DESTDIR}/couchgetid
	rm ${DESTDIR}/strtojson
	rm ${DESTDIR}/jsontostr