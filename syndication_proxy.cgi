#!/bin/sh
# syndication cgi proxy
URL="http://az-mulog.tumblr.com/"
GITHUB="https://github.com/azet"
if [ -z "${QUERY_STRING}" ]; then
	echo -e "Content-type: text/html\n\n"
	cat << EoXHTML
<p class="mulog_header">
	<strong>&#xb5;_log - syndication proxy</strong>
	<br>
	&#91; <a href="http://az-mulog.tumblr.com/" alt="tumblr">http://az-mulog.tumblr.com/</a> &#93;
</p>
EoXHTML
	exec curl -s $URL
elif [ "${QUERY_STRING}" = "github" ]; then
	exec curl -s $GITHUB
else
	echo -e "Content-type: text/plain\n\n"
        cat $0
fi
# who needs $insert_hip_scripting_language for basic stuff like this anyway.. ;)
# shave the whales!
# EOF
