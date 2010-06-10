INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchattach ${DESTDIR}
	${INSTALL} couchget ${DESTDIR}
	${INSTALL} couchdel ${DESTDIR}
	${INSTALL} couchput ${DESTDIR}
	${INSTALL} jsonize ${DESTDIR}
	${INSTALL} dejsonize ${DESTDIR}

clean:
	rm ${DESTDIR}/couchattach
	rm ${DESTDIR}/couchget
	rm ${DESTDIR}/couchdel
	rm ${DESTDIR}/couchput
	rm ${DESTDIR}/jsonize
	rm ${DESTDIR}/dejsonize