import re
statusdat = "/Users/User/Documents/python/status.dat"
new_hostname = ""
count =  0
print "{"
print '\t"data":['
with open(statusdat,'r') as fin:
#with open('status.dat','r') as fin:
    for line in fin:
        line = line.replace ('\n','')      
        
        if "host_name" in line:
            hostname = line.split('host_name=')[1]
            #print hostname
            if hostname != new_hostname:
                new_hostname = hostname
                #not print the first round
                if count != 0:
                    print "\t\t}"
                print "\t\t{"
                print '\t\t\t"hostname":','"',new_hostname,'"'
            count = int(count) + int(1)
        if "service_description" in line:
            servicedescription = line.split('service_description=')[1]
            print '\t\t\t,"service"','"',servicedescription,'"'
    

print "\t\t}"
print "\t]"
print '}'
