INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchattach ${DESTDIR}
	${INSTALL} couchget ${DESTDIR}
	${INSTALL} couchdel ${DESTDIR}
	${INSTALL} couchput ${DESTDIR}
	${INSTALL} couchjsonize ${DESTDIR}
	${INSTALL} couchdejsonize ${DESTDIR}
	${INSTALL} couchaddimage ${DESTDIR}

clean:
	rm ${DESTDIR}/couchattach
	rm ${DESTDIR}/couchget
	rm ${DESTDIR}/couchdel
	rm ${DESTDIR}/couchput
	rm ${DESTDIR}/couchjsonize
	rm ${DESTDIR}/couchdejsonize
	rm ${DESTDIR}/couchaddimage