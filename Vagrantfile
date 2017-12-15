# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "esss/devenv-7"

  # If you installed jupyter notebook and want to access it from outside the VM,
  # uncomment the following line:
  # config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.network "private_network", ip: "192.168.10.11"
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "ansible", "/home/vagrant/ansible", owner:"vagrant"
  config.vm.synced_folder "scripts", "/home/vagrant/scripts", owner:"vagrant"
  # For example:
  # On OSX:
  # config.vm.synced_folder "/Users/benjaminbertrand/data", "/data", owner:"benjaminbertrand"
  # On Windows:
  # config.vm.synced_folder "C:/Users/bzupanc/Shared", "/data", owner:"blazzupanc"
  # You can pass mount options if you don't want the folder to be writable by everyone:
  # config.vm.synced_folder "C:/Users/bzupanc/Shared", "/data", owner:"blazzupanc", mount_options:[“fmask=022”,”dmask=022”]

  # Customize the amount of memory and CPUs on the VM
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
    # change the network card hardware for better performance
    vb.customize ["modifyvm", :id, "--nictype1", "virtio" ]
    vb.customize ["modifyvm", :id, "--nictype2", "virtio" ]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    # Set the name seen in Virtualbox GUI
    vb.name = "dm-sinq-amor"
  end
end
