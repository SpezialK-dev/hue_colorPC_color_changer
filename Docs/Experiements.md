# Tested things :

## Nmap scan
the open ports on a normal philips hue bridge are 
| Port | State | Service |
| ---- | ---- | ---- | 
| 80/tcp |open | http | 
| 443/tcp |open | https |
| 8080/tcp |open | http-proxy |

## Server usage :
known software :
nginx : wit h the option to hide the version from the header
runns on the linux kernel ergo its just a headless linux install. Most likely https://openwrt.org/ as it is mentiont in the open source section from which they are using software from. As it states Version 204.4 is used. This is a outdated version of what should be used. As I checked my hue bridge is on the newest Firmware version and I cannot update and big parts of the system appear to be around 2 years old and not updated.
ssh Server Dropbear SSH, aswell as https://github.com/rxi/log.c for logging I dont know in which projekt it is used but this might be vulnrable to something similar to Log4J. 


# Possible Attack vectors

## Server :

Depending on the ngnix Version used on the bridge there might be exploits that could be used to get code execution on the bridge -> and root permission 

this is also running Web-based Enterprise Managment CIM serverOpenPegasus WBEM httpd_http-titel

## ZigBee Protocoll 

The master key this protocoll is leaked hence we might be able to flash our own firmware on this getting us root priviliges. -> this would be sub optimal since it would be could be noticable. 
