# Application server

This was the application deployment project for our AirBnB clone. In this
project, I configured Nginx on the web servers provided me by ALX
to serve a WSGI Flask app running through Gunicorn. Additionally, I set up an
Upstart script to keep the application running on server reboots.

## Tasks :page_with_curl:

* **0. Set up development with Python**
  * In this task, I configured the file `web_flask/0-hello_route.py` from my
  [AirBnB_clone_v2](https://github.com/aysuarex/AirBnB_clone_v2) to serve content
  on the route `/airbnb-onepage/`, running on port `5000`.

* **1. Set up production with Gunicorn**
  * This task involved setting up a production environment, installing and configuring
  Gunicorn to serve the same file from task 0.

* **2. Serve a page with Nginx**
  * [2-app_server-nginx_config](./2-app_server-nginx_config): Nginx configuration file
  proxying requests on the route `/airbnb-onepage/` to the Gunicorn app running on
  port `5000`.



   ```markdown
       # Flask App Deployment with Nginx
       
       This guide explains how to deploy a Flask web application using Nginx as a reverse proxy server. This setup will enable your Flask app to be accessible via a specific route and port, and Nginx will handle the communication between the internet and your app.
       
       ## Step 3: Create Nginx Configuration
       
       1. Navigate to your server's terminal.
       
       2. Create a new Nginx configuration file using the following command:
       
          ```bash
          sudo nano /etc/nginx/sites-available/2-app_server-nginx_config
     ```

     Add the following Nginx configuration to the file. Replace `your_domain_or_ip` with your actual domain name or IP address:

   ```nginx
   # Configures Nginx to serve the route /airbnb-onepage/ from AirBnB_clone_v2.

    server {
            # Listen on port 80
            listen 80;
        
            # Use IP of server as domain name
            server_name YOUR_IP_ADDRESS;  # Replace with your actual domain or IP address
    
            # Customize HTTP response header
            add_header  X-Served-By 213221-web-01;
    
            # Serve /airbnb-onepage/ route from AirBnB_clone_v2
            location /airbnb-onepage/ {
                    proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
                    # proxy_set_header Host $host;
                    # proxy_set_header X-Real-IP $remote_addr;
                    # proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
            # 404 error page
            error_page 404 /404.html;
            location /404 {
                    root /var/www/html;
                    internal;
            }
    }
   ```

   Press `Ctrl + O` to save the file and `Ctrl + X` to exit.

     ## Enable the Nginx Configuration
     
     1. Create a symbolic link to enable the Nginx site configuration:
     
        ```bash
        sudo ln -s /etc/nginx/sites-available/2-app_server-nginx_config /etc/nginx/sites-enabled/
        ```
     
     ## Test and Restart Nginx
     
     1. Test the Nginx configuration for syntax errors:
     
        ```bash
        sudo nginx -t
        ```
     
     2. If the test is successful, restart Nginx:
     
        ```bash
        sudo systemctl restart nginx
        ```
     
     ## Access Your App
     
        Your Flask app is now accessible at `http://your_domain_or_ip/airbnb-onepage/`.
        
        ## Testing Locally (Optional)
        
        To test the deployment locally, you might need to modify your computer's hosts file to point the domain to your server's IP address.
        
        - On most systems, the hosts file is located at `/etc/hosts`.
        
        **Note**: Ensure your server's firewall allows traffic on port 80 and consider using SSL certificates for security.
        
        
        Remember to replace `your_domain_or_ip` with your actual domain name or IP address.

* **3. Add a route with query parameters**
  * [3-app_server-nginx_config](./3-app_server-nginx_config): Nginx configuration file
  proxying requests on the route `/airbnb-dynamic/number_odd_or_even/<int: num>` to the
  Gunicorn app running on port `5000`.

* **4. Let's do this for your API**
  * In this task, I configured the API from my [AirBnB_clone_v3](https://github.com/Tijani1402/AirBnB_clone_v31) to run on Gunicorn.
  * [4-app_server-nginx_config](./4-app_server-nginx_config): Nginx configuration file
  that proxies requests on the AirBnB API to the corresponding Gunicorn app.

* **5. Serve your AirBnB clone**
  * In this task, I configured the complete AirBnB app from [AirBnB_clone_v4](https://github.com/aysuarex/AirBnB_clone_v4) to run on Gunicorn and be served through Nginx.
  * [5-app_server-nginx_config](./5-app_server-nginx_config): Nginx configuration file
  configured to serve the static assets from `web_dynamic/static/` on the Gunicorn AirBnB
  app.

* **6. Deploy it**
  * [gunicorn.conf](./gunicorn.conf): Configuration file for an Upstart script that starts a
  Gunicorn process bounded to port 5003 that serves the content from task 5.
  * The Gunicorn process spawns three worker processes and logs errors to `/tmp/airbnb-error.log`,
  access to `/tmp/airbnb-access.log`.

* **7. No service interruption**
  * [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime): Bash script that gracefully
  reloads Gunicorn.
