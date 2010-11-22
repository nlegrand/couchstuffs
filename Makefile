INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchget ${DESTDIR}
	${INSTALL} couchdel ${DESTDIR}
	${INSTALL} couchput ${DESTDIR}
	${INSTALL} couchcopy ${DESTDIR}
	${INSTALL} couchfromdir ${DESTDIR}
	${INSTALL} couchtodir ${DESTDIR}
	${INSTALL} couchgetid ${DESTDIR}
	${INSTALL} strtojson ${DESTDIR}
	${INSTALL} jsontostr ${DESTDIR}

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