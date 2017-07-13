#!usr/bin/env python


loadbalancer_dic = {

  'ip_addr': '10.32.10.5',
  'username': 'nsroot',
  'password': 'nsroot',
  'vendor':  'citrix',
  'model': 'vpx-1005',
  }

print()

for k, v in loadbalancer_dic.items():
     
       print(k, v)



loadbalancer_dic['password'] = 'nsadmin'
loadbalancer_dic['secret'] = 'enable secret'

device_type = loadbalancer_dic.get('device_type', 'vpx_citrix')
print("\nDefault device type: {}\n".format(device_type))

