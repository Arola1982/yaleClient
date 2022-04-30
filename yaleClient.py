import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument(
  '--username',
  help="Yale Username"
)
parser.add_argument(
  '--password',
  help="Yale Password"
)
parser.add_argument(
  '--device-status',
  help="Get Device Status"
)
parser.add_argument(
  '--panel-mode',
  help="Set Alarm panel, arm,disarm,home"
)

parser.add_argument(
  '--filter',
  help="Filter json field"
)

args = parser.parse_args()

yale = {
    "host": "https://mob.yalehomesystem.co.uk",
    "base_path": "/yapi", 
    "auth_token": "VnVWWDZYVjlXSUNzVHJhcUVpdVNCUHBwZ3ZPakxUeXNsRU1LUHBjdTpkd3RPbE15WEtENUJ5ZW1GWHV0am55eGhrc0U3V0ZFY2p0dFcyOXRaSWNuWHlSWHFsWVBEZ1BSZE1xczF4R3VwVTlxa1o4UE5ubGlQanY5Z2hBZFFtMHpsM0h4V3dlS0ZBcGZzakpMcW1GMm1HR1lXRlpad01MRkw3MGR0bmNndQ==",
    "token": "/o/token/",
    "device_status": "/api/panel/device_status/",
    "panel_status": "/api/panel/mode/"
}

def get_token():
  headers = {
      "Authorization": "Basic " + yale['auth_token']
  }

  payload = {
      "grant_type": "password",
      "username": args.username,
      "password": args.password
  }
  response = requests.post(yale['host'] + yale['base_path'] + yale['token'], headers=headers, data=payload).json()
  return response['access_token']

def get_device_status():
  headers = {
      "Authorization": "Bearer " + get_token()
  }

  response = json.dumps(requests.get(yale['host'] + yale['base_path'] + yale['device_status'], headers=headers).json())
  device_list = json.loads(response)['data']

  num_devices = len(device_list)

  for index in range(0, num_devices):
    if device_list[index]['name'] == args.device_status and args.filter is None:
      return json.dumps(device_list[index], indent=2)
    elif device_list[index]['name'] == args.device_status and args.filter is not None:
      return json.dumps(device_list[index][args.filter], indent=2)
    if args.device_status == 'all':
      return json.dumps(device_list, indent=2)



def set_panel_mode():
  headers = {
      "Authorization": "Bearer " + get_token()
  }

  payload = {
      "area": "1",
      "mode": args.panel_mode,
  }

  response = requests.post(yale['host'] + yale['base_path'] + yale['panel_status'], headers=headers, data=payload)
  return response.text

if args.device_status:
  print (get_device_status())

if args.panel_mode:
  set_panel_mode()
