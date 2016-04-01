#!/bin/sh

# Network configuration

. ./load.cgi

[ -f "$NETCONF" ] && . "$NETCONF"

eval `echo "$NAMESERVER01" | sed 's/
eval `echo "$NAMESERVER02" | sed 's/
eval `echo "$IPADDR0" | sed 's/
eval `echo "$NETMASK0" | sed 's/
eval `echo "$GATEWAY0" | sed 's/

#initialize unset value
[ -n "$DN11" ] || DN11=1
[ -n "$DN12" ] || DN12=0
[ -n "$DN13" ] || DN13=0
[ -n "$DN14" ] || DN14=0
[ -n "$DN21" ] || DN21=1
[ -n "$DN22" ] || DN22=0
[ -n "$DN23" ] || DN23=0
[ -n "$DN24" ] || DN24=0

cat <<EOF
Content-Type: text/html

<html>
<head>
<title>$TARGET_NAME LAN MANAGEMENT</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div id="container">
<center>
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
			<h1>$TARGET_NAME LAN MANAGEMENT</h1>
</td>
</tr>
</table>
		</div>
        <div id="content">
            <div id="form"> 
                <form action="lan_setup.cgi" method="POST">
                    <fieldset>
                        <legend>Network Configuration</legend>
                        <table>
                        <tbody>
                        <tr>
	                        <td>
    	                    <label>Static: </label>
        	                </td>
                        </tr>
                        <tr>
EOF
$WWW_DIR/select $IP1 $IP2 $IP3 $IP4 $NM1 $NM2 $NM3 $NM4 $GW1 $GW2 $GW3 $GW4 $DN11 $DN12 $DN13 $DN14 $DN21 $DN22 $DN23 $DN24 < $WWW_DIR/select-template.html > /tmp/select.html
cat /tmp/select.html
rm -f /tmp/select.html
cat <<EOF
                        </tr>
                        </tbody>
                        </table>
					<input class=bottoni type="submit" value="Apply">
                    </fieldset>
                 </form>
			</div> <!-- end div form -->
EOF
echo "      <input class=bottoni type=\"button\" value=\"Home\" onclick=\"window.location.href='$HOME_PAGE'\">"
cat <<EOF
		</div> <!-- end div content -->
</center>
EOF
echo "         <div id=\"footer\"><h2>$COMPANY_NAME</h2></div>"
cat <<EOF
	</div> <!-- end div container -->
</body>
</html>
EOF