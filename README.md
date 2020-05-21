# nagios2json

Convert to JSON the information of status.dat from nagios. Change the variable "statusdat" inside of script.

Ex:
```json

{
        "data":[
                {
                        "hostname": " shire-router "
                }
                {
                        "hostname": " bilbo "
                }
                {
                        "hostname": " samwise "
                }
                {
                        "hostname": " frodo "
                }
                {
                        "hostname": " shire-router "
                        ,"service" " Interface Status: Cisco Border Router "
                        ,"service" " Ping Upstream Router1 1.2.3.4 Satanic "
                        ,"service" " Ping Upstream Router2 4.3.2.1 SauronNetworks "
                        ,"service" " Ping: Reachable "
                }
                {
                        "hostname": " bilbo "
                        ,"service" " reachable "
                }
                {
                        "hostname": " samwise "
                        ,"service" " Free Space: / "
                        ,"service" " Free Space: /home/ "
                        ,"service" " Free Space: /var/lib/vservers "
                        ,"service" " Load Average "
                        ,"service" " Raid State "
                        ,"service" " Reachable "
                        ,"service" " Service: debian security patches "
                        ,"service" " Service: ntpd "
                        ,"service" " Service: ssh "
                        ,"service" " Swap Free Non Production "
                }
                {
                        "hostname": " frodo "
                        ,"service" " Free Space: / "
                        ,"service" " Free Space: /home/ "
                        ,"service" " Free Space: /var/dumps/ "
                        ,"service" " Free Space: /var/lib/postgresql/ "
                        ,"service" " Free Space: /var/log/ "
                        ,"service" " Integrit "
                        ,"service" " Load Average "
                        ,"service" " Raid State "
                        ,"service" " Reachable "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend Replication "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Service: debian security patches "
                        ,"service" " Service: klogd "
                        ,"service" " Service: ntpd "
                        ,"service" " Service: postgres "
                        ,"service" " Service: puppetd "
                        ,"service" " Service: rsync "
                        ,"service" " Service: ssh "
                        ,"service" " Service: syslogd "
                        ,"service" " Swap Free "
                        ,"service" " Timezone Data "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                        ,"service" " Production: Apache "
                        ,"service" " Production: Backend State "
                        ,"service" " Production: Environment Availability "
                        ,"service" " Production: HTTP on port 80 "
                        ,"service" " Production: Logtail "
                        ,"service" " Production: Scheduled Jobs "
                        ,"service" " Production: Spread Listener "
                        ,"service" " Production: Supervisor "
                }
        ]
}
```
