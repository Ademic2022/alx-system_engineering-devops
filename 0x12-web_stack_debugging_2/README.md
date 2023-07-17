# Project Title: Web stack debugging #2

## Task 0: Run Software as Another User

The user `root` is a "superuser" on Linux with the ability to do anything on the system. However, running tasks as the root user can be dangerous as it grants unrestricted access, making it prone to accidental mistakes.

To mitigate this risk, it is advisable to run specific tasks as privileged users (i.e., users with elevated permissions) instead of directly using the root user. In this task, we'll create a Bash script that allows us to run a command under a specified user.

### Requirements:
- Write a Bash script that accepts one argument (the username).
- The script should run the `whoami` command under the user passed as an argument.
- Test the script with different users.

Example:
```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
 * Usage: `./0-iamsomeonelese <user>`
## Task 1: Run Nginx as Nginx

Running web servers, like Nginx, as the root user is not recommended due to security risks. It's better to run them under a less privileged user, such as `nginx`. In this task, we'll configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.

### Requirements:
- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- You cannot use `apt-get remove`.
- Write a Bash script to configure the container to meet the above requirements.

After debugging:
```bash
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

## Task 2: 7 Lines or Less

Using the solution from Task 1, make the script short and concise.

### Requirements:
- Your Bash script must be 7 lines or less.
- There must be a new line at the end of the file.
- You must respect Bash script requirements.
- You cannot use `;`, `&&`, `wget`, or execute the previous answer file.

---
*Please note that the exact implementation of the Bash scripts is not provided here, and you should create your own scripts based on the tasks' 
