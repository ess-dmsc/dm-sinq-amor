# dm-sinq-amor
Development machine for SINQ AMOR. Following taks can be handled in an automated way:
- Create a new virtual machine with a static IP address
- Install software, processes and services required to run SINQ AMOR simulation including IOC's, Kafka, Forwarder, FileWriter and NICOS
- Start/Stop the services

## Setting up the Virtual machine
Following is modified from: https://confluence.esss.lu.se/display/DE/Development+Machine+Installation
- Install vagrant and VirtualBox
- Ensure vagrant-vbguest plugin is installed by running
```
$ vagrant plugin install vagrant-vbguest
```

- Create the machine
```
vagrant up
```

- Use following setup options when machine GUI pops up: Custom > EEE local

- Login to machine using:
```
vagrant ssh
```

## Installing software related to SINQ AMOR experiment control
Note that following commands are to be run inside the VM (directory `ansible`)
```
cd ~/ansible
```

- First, update ansible such that the version being used in > 2.4. This can be easily done using `pip`
```
sudo pip install ansible
```

- Prepare for the installation using the playbook prepare.yml
```
/usr/bin/ansible-playbook -i hosts prepare.yml
```

- Install everything using one command (may take a lot of time). Other option is to run every playbook in the `ansible/installer` directory
```
/usr/bin/ansible-playbook -i hosts install.yml
```

## Managing services
- Start all the services (also creates the required topics)
```
/usr/bin/ansible-playbook -i hosts start.yml
```

- Stop all the services (also creates the required topics)
```
/usr/bin/ansible-playbook -i hosts stop.yml
```

## Sample Forwarder command script
A sample Python script to send a command for the Forwarder to start an EPICS PV is included. Note that following commands are to be run inside the VM (directory `scripts`)
```
cd ~/scripts
```

- Run the script to start forwarding
```
./send-forwarder-cmd.py
```

- Change the PV values to get updates
```
caput SQ:AMOR:DIMETIX:LASER ON
caput SQ:AMOR:DIMETIX:SimVal <newvalue>
```

- Read the PV values directly
```
caget SQ:AMOR:DIMETIX:DIST
```
