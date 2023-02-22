import sys
import os
import dotenv
from pyzabbix import ZabbixAPI, ZabbixAPIException, ZabbixAPIObject, ZabbixAPIMethod

if len(sys.argv) <= 1:
    print(
        "Por favor informe o nome do grupo que deseja obter o ID"
        )
    exit(1)

g_name = sys.argv[1]

# Login API do Zabbix 
dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.getenv("api_token")

#Insira a URL do seu Zabbix Server
#Crie um arquivo .env na pasta deste script e insira o token API do zabbix:
#     EXEMPLO api_token=<seu_token>
z = ZabbixAPI("http://192.168.0.44")
z.login(api_token=TOKEN)

group = z.hostgroup.get(filter={'name': g_name}, selectTriggers='extend')
group_id = group[0]['groupid']
#print(group[0]['groupid'])

p = z.problem.get(groupids=group_id, selectHosts='extend')
event_ids = [event['eventid'] for event in p]

for event_id in event_ids:
    eventupdate = z.event.acknowledge(
        eventids=[event_id],
        action=1,
        message="Problema fechado por se tratar de um falso alerta."
    )


    
 