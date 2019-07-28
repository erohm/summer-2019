# Sets the path of the executable
#!/bin/bash

#Anytime you execute this shell script, it does whatever commands are inside of it in the directory you executed it in.

 #Automatically logs into lngs server, enters password, executes commands. Will need to be edited for different username and password

 #Creates an output root file called "test.root" in lngs 

sshpass -p "givemecuoredata0" ssh -o StrictHostKeyChecking=no adams@cuore-login.lngs.infn.it 'cd /afs/lngs.infn.it/user/cuore/adams/; source .bashrc; source /nfs/cuore/geant4/sbin/setup-g4.9.6.p03-lngs; qshields -N100 -p mu+,1000 -o rmuons_100_evts.root -U'
#; g4cuore -n1000 -r100 -i rmuons_1k_evts.root -o rmuons_1k_evts_g4cuore.root'

# Now back in local, copy file from lngs to local. This will prompt you to enter a password, and going back and forth between local/lngs more than once is slower, so those will need to be debugged
scp -p 45122 adams@cuore-login.lngs.infn.it:/afs/lngs.infn.it/user/cuore/adams/muons_100_evts.root .


#To transfer a file called "filename.file" in the present directory from local to cuore cluster, do the following: 

#rsync ./filename.file adams@cuore-login.lngs.infn.it:/afs/lngs.infn.it/user/cuore/adams/


