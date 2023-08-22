# Web stack debugging #4

This was the fifth in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.

## Tasks :page_with_curl:

* **0. Sky is the limit, let's bring that limit higher**
  * [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp): This script first increases the limit of open files for the Nginx server by modifying a configuration file using sed. After that, it restarts the Nginx service to apply the changes. The use of the path and require parameters helps ensure the correct order of execution and the availability of the necessary commands. This script is part of server configuration management and automation, making it easy to manage system changes across multiple servers in a consistent manner.

* **1. User limit**
  * [1-user_limit.pp](./1-user_limit.pp): This script is designed to increase the limits for the maximum number of open files allowed for the "holberton" user. It modifies the relevant lines in the /etc/security/limits.conf file, applies the changes using sysctl -p, and ensures that the changes are applied in the correct order. The script focuses on system configuration management, enabling consistent and automated management of user limits across different systems. test
