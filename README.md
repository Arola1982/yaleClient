# yaleClient.py

### Description

&nbsp;

A client written in Python3 with the ability to query your Yale alarm system to get information about your devices. As well as being able to set your alarm state. Home (Part Arm) / ARM / Disarm

&nbsp;

### Requirements

- Python3

&nbsp;

### Help

&nbsp;

```
usage: client.py [-h] [--username USERNAME] [--password PASSWORD] [--device-status DEVICE_STATUS] [--panel-mode PANEL_MODE] [--filter FILTER]

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   Yale Username
  --password PASSWORD   Yale Password
  --device-status DEVICE_STATUS
                        Get Device Status
  --panel-mode PANEL_MODE
                        Set Alarm panel, arm,disarm,home
  --filter FILTER       Filter json field
  ```

&nbsp;

### Examples

&nbsp;

#### Retrieve data for all devices and all information
&nbsp;

Request:

```python3 client.py --username USERNAME --password PASSWORD --device-status all```


Response (Truncated):

&nbsp;


```
[
  {
    "area": "1",
    "no": "1",
    "rf": null,
    "address": "RF:0265a030",
    "type": "device_type.pir",
    "name": "Kitchen"
  },
  {
    "name": "Garage",
    "status_open": [],
    "trigger_by_zone": []
  }
]
```

#### Retrieve data for a single device

&nbsp;

Request:

```python3 client.py --username USERNAME --password PASSWORD --device-status 'Front Door'```

Response (Truncated):

&nbsp;

```
{
  "area": "1",
  "no": "3",
  "rf": null,
  "address": "RF:0179bb10",
  "type": "device_type.door_contact",
  "name": "Front Door",
  "status1": "device_status.dc_open",
  "status2": null,
  "status_switch": null,
  "status_power": null,
  "ipcam_trigger_by_zone2": null,
  "ipcam_trigger_by_zone3": null,
  "status_temp_format": "C",
  "type_no": "4",
  "device_group": "000",
  "status_fault": [],
  "status_open": [
    "device_status.dc_open"
  ],
  "trigger_by_zone": []
}
```

&nbsp;

### Retrieve a single piece of data for a single device

&nbsp;

Request:

```python3 client.py --username USERNAME --password PASSWORD --device-status 'Front Door' --filter status_open```

Response:

&nbsp;

```
[
  "device_status.dc_close"
]
```

&nbsp;

### Set your alarm state

&nbsp;

`python3 client.py --username USERNAME --password PASSWORD --panel-mode STATUS`

Status's:

```
arm - Fully Armed
home - Part Armed
disarm - Disarmed
```
