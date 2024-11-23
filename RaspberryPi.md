### Connect through SSH:

`ssh agrobot@agrobot.local`

Password is same as `agrobotappliedai@gmail.com` google password.  

Open devcontainer:

devcontainer exec --workspace-folder . bash

### Connecting to outside internet:

The TP Link is setup to connect to UBC Visitor. Connect to the TP Link on your laptop and agree to UBC Visitor's terms and it will allows all devices on the TP Link to connect

### Access the PI's DevContainer
Connect to the raspberry pi:

First connect to the TP-Link router

Then,
```
ssh agrobot@agrobot.local
```


Open the dev container:
```
cd Navi24
dc_up # devcontainer up --workspace-folder .
dc_in # devcontainer exec --workspace-folder . bash
```
If stuff doesn't work, run the `rpi_install.sh` script.