#!/bin/sh

. ./load.cgi

cat <<EOF
Content-Type: text/html

<html>
<head>
<title>$TARGET_NAME PASSWORD MANAGEMENT</title>
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
<h1>$TARGET_NAME PASSWORD MANAGEMENT</h1>
</td>
</tr>
</table>
</div>
<div id="content">
<center>
<div id="form">

<form name="myform" enctype="multipart/form-data" action="changepwd.cgi" method="POST">
<table>
<tr>
<td>
Enter Old Password :
</td>
<td>
<input type="password" size="25" name="PWDOLD">
</td>
</tr>
<tr>
<td>
Enter New Password :
</td>
<td>
<input type="password" size="25" name="PWDNEW">
</td>
</tr>
<tr>
<td>
</td>
<td>
<input class=bottoni type="submit" value="Change">
</td>
</tr>
</table>
</div> <!-- end div form -->
<BR>
<form>
EOF
echo "      <input class=bottoni type=\"button\" value=\"Home\" onclick=\"window.location.href='$HOME_PAGE'\">"
cat <<EOF
 <input class=bottoni type="button" value="Back" onclick="window.location.href='menu.cgi'">
</form>
</center>
</div> <!-- end div content -->
EOF
echo "         <div id=\"footer\"><h2>$COMPANY_NAME</h2></div>"
cat <<EOF
</div> <!-- end div container -->
</body>
</html>
EOF
exit 0
