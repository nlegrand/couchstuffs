INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchattach ${DESTDIR}
	${INSTALL} couchget ${DESTDIR}
	${INSTALL} couchdel ${DESTDIR}
	${INSTALL} couchput ${DESTDIR}
	${INSTALL} couchcopy ${DESTDIR}
	${INSTALL} couchexport ${DESTDIR}
	${INSTALL} couchimport ${DESTDIR}
	${INSTALL} couchaddimage ${DESTDIR}
	${INSTALL} couchgetid ${DESTDIR}
	${INSTALL} strtojson ${DESTDIR}
	${INSTALL} jsontostr ${DESTDIR}

deinstall:
	rm ${DESTDIR}/couchattach
	rm ${DESTDIR}/couchget
	rm ${DESTDIR}/couchdel
	rm ${DESTDIR}/couchput
	rm ${DESTDIR}/coucopy
	rm ${DESTDIR}/couchexport
	rm ${DESTDIR}/couchimport
	rm ${DESTDIR}/couchaddimage
	rm ${DESTDIR}/couchgetid
	rm ${DESTDIR}/strtojson
	rm ${DESTDIR}/jsontostr