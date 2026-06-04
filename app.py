import os 
from flask import Flask
import psutil
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    hostname = socket.gethostname()

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""

<!DOCTYPE html>

<html>
<head>
    <title>Linux Monitoring Dashboard</title>

```
<meta http-equiv="refresh" content="5">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

</head>

<body class="bg-dark text-light">

<div class="container mt-5">

```
<h1 class="text-center mb-5">
    Linux Monitoring Dashboard
</h1>
<div class="text-center mb-4">
        <img src="/static/cr7.png"
             class="img-fluid rounded shadow"
             width="500"
             alt="Cristiano Ronaldo">
    </div>
<div class="text-center mb-4">
        <img src="/static/cr7.png"
             class="img-fluid rounded shadow"
             width="500"
             alt="Cristiano Ronaldo">
    </div>

<div class="row">

    <div class="col-md-4">
        <div class="card bg-primary text-white mb-3">
            <div class="card-body">
                <h5>CPU Usage</h5>
                <h2>{cpu}%</h2>

                <div class="progress">
                    <div class="progress-bar"
                         role="progressbar"
                         style="width: {cpu}%">
                        {cpu}%
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card bg-success text-white mb-3">
            <div class="card-body">
                <h5>RAM Usage</h5>
                <h2>{ram}%</h2>

                <div class="progress">
                    <div class="progress-bar bg-light text-dark"
                         role="progressbar"
                         style="width: {ram}%">
                        {ram}%
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card bg-warning text-dark mb-3">
            <div class="card-body">
                <h5>Disk Usage</h5>
                <h2>{disk}%</h2>

                <div class="progress">
                    <div class="progress-bar bg-dark"
                         role="progressbar"
                         style="width: {disk}%">
                        {disk}%
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

<div class="card bg-secondary">
    <div class="card-body">

        <h4>System Information</h4>

        <p><b>Hostname:</b> {hostname}</p>

        <p><b>Current Time:</b> {current_time}</p>

    </div>
</div>
```

</div>

</body>
</html>
"""


    return html

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
