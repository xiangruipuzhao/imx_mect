#!/bin/sh

read query

. ./load.cgi

eval `echo "$query" | sed 'y/+/ /; s/=/="/g; s/&/";/g; s/$/"/' | tr '[:lower:]' '[:upper:]'`

date -s $YEAR$MONTH$DAY$HOURS$MINUTES.$SECONDS
if [ $? == 0 ]
then
	/sbin/hwclock -w
	if [ $? == 0 ]
	then
		TABLE="<table style=\"border:solid 2px #335970;\" bgcolor=#f1fbff cellspacing=10 cellpadding=4 align=center >"
		MSG="Date and time settings updated."
	else
		TABLE="<table style=\"border:solid 2px #FF0000;\" bgcolor=#fffbff cellspacing=10 cellpadding=4 align=center >"
		MSG="Problem to save Date and time settings.$YEAR$MONTH$DAY$HOURS$MINUTES.$SECONDS."
	fi
else
	TABLE="<table style=\"border:solid 2px #FF0000;\" bgcolor=#fffbff cellspacing=10 cellpadding=4 align=center >"
	MSG="Problem to update Date and time settings.$YEAR$MONTH$DAY$HOURS$MINUTES.$SECONDS."
fi

cat <<EOF
Content-Type: text/html

<html>
<head>
<title>DATE AND TIME</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div id="container">
<div id="header">
<table width="100%">
<tr align="right">
<td>
EOF
. ./info.cgi
cat <<EOF
</td>
</tr>
<tr>
<td>
<h1>REMOTE UPDATER</h1>
</td>
</tr>
</table>
</div>
<center>
<div id="content">
EOF
echo "$TABLE"
cat <<EOF
<tbody>
<tr>
<td>
EOF
echo "$MSG"
cat <<EOF
</td>
</tr>
</tbody>
</table>
</div>                                                                                
EOF
echo "<input class=bottoni type=\"button\" value=\"Home\" onclick=\"window.location.href='$HOME_PAGE'\">"
echo "<input class=bottoni type=\"button\" value=\"Back\" onclick=\"window.location.href='date_time.cgi'\">"
cat <<EOF
</center>
</div>                                                                                
EOF
echo "         <div id=\"footer\"><h2>$COMPANY_NAME</h2></div>"
cat <<EOF
</body>
</html>
EOF