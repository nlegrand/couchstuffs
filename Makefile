INSTALL=install -c -o root -g bin -m 555
DESTDIR=/usr/local/bin

all:
	@echo type make install

install:
	${INSTALL} couchattach ${DESTDIR}
	${INSTALL} couchget ${DESTDIR}
	${INSTALL} couchdel ${DESTDIR}
	${INSTALL} couchput ${DESTDIR}

clean:
	rm ${DESTDIR}/couchattach
	rm ${DESTDIR}/couchget
	rm ${DESTDIR}/couchdel
	rm ${DESTDIR}/couchput