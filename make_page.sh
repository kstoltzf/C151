#!/bin/bash

#make_page - A script to produce an HTML file

cat <<- _EOF_
    <HTML>
    <HEAD>
	<TITLE>
	My web page
	</TITLE>
    </HEAD>

    <BODY>
	<H1>This is my first web page.</H1>
    </BODY>
    </HTML>
_EOF_
