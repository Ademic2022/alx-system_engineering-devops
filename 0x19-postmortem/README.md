##Postmortem

**Incident Analysis**

During the release of ALX's System Engineering & DevOps project (version 0x19) in Nigeria at around 06:00 West African Time (WAT), an outage took place on a separate Ubuntu 14.04 container running an Apache web server. Instead of the expected response of a simple Holberton WordPress site in HTML format, GET requests on the server resulted in 500 Internal Server Errors.

**Debugging Process**

Our bug debugger, Brennan, addressed the issue soon after it was identified, around 19:20 PST. Here's how the debugging process unfolded:

1. Brennan checked the running processes using "ps aux" and found that two Apache2 processes, one for root and one for www-data, were functioning properly.
2. He examined the sites-available folder in the /etc/apache2/ directory and confirmed that the web server was serving content from /var/www/html/.
3. Brennan initiated the "strace" command on the PID of the root Apache process in one terminal while performing a "curl" on the server in another. Unfortunately, the "strace" command did not yield useful information.
4. He repeated the previous step, but this time on the PID of the www-data process. This time, the "strace" output revealed an error (-1 ENOENT) indicating that an attempt was made to access the file /var/www/html/wp-includes/class-wp-locale.phpp.
5. Brennan examined the files in the /var/www/html/ directory one by one, using Vim pattern matching to identify the erroneous ".phpp" file extension. He found the issue in the wp-settings.php file (Line 137, require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );).
6. He removed the trailing "p" from the identified line.
7. A successful "curl" test on the server confirmed that the issue was resolved.
8. Brennan created a Puppet manifest to automate the correction of this error in the future.

**Summary**

In summary, the root cause of the issue was a simple typo in the WordPress app. The error occurred in the wp-settings.php file when trying to load the file "class-wp-locale.phpp." The correct file name, located in the wp-content directory of the application, should have been "class-wp-locale.php." The patch involved a straightforward fix by removing the trailing "p."

**Preventive Measures**

To prevent similar outages in the future, we recommend the following steps:

1. Thorough Testing: Ensure rigorous testing of the application before deployment to catch such errors early in the process.
2. Status Monitoring: Implement an uptime-monitoring service like UptimeRobot to provide instant alerts in the event of website outages.

Additionally, a Puppet manifest named "0-strace_is_your_friend.pp" was created in response to this error. This manifest automates the correction of any identical errors that might occur in the future by replacing "phpp" extensions in the file /var/www/html/wp-settings.php with "php."

While we strive for error-free programming, the creation of these measures ensures readiness to handle potential issues. 😉
