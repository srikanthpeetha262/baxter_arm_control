
Before operating the baxter, edit the following lines in "baxter.sh" file

 -> go to terminal 
 	$ cd ~/bax-myo_ws
 	$ gedit baxter.sh
 
 -> Enter the below values in the file
 	(line 22, approx) -> baxter_hostname="bax.srb.louisville.edu"
 	(line 26, approx) -> your ip ="xxx.xxx.xxx.xxx" (check the ip of your PC and enter it here)
 			---> SAVE & CLOSE the file
 			

NOTE:	1. The host name of baxter was set to "bax.srb.louisville.edu". However on the baxter 	
	   screen if you look up the host name it shows 011604P0019. Ignore it.
	2. The ip address of your PC/Laptop might change after restart. So double check it.

''' for setup '''
$ cd ~/bax-myo_ws/src/baxter_arm_control
$ catkin_make

$ cd ~/bax-myo_ws
$ source /opt/ros/indigo/setup.bash
$ catkin_make
_______________________________________________________________________________________
		'''	moving the baxter's arms  '''
____________________________________________________________________________________________

# ~~~~~ If NOTHING WAS CHANGED from the previous time, start from here
#go back to the original baxter workspace
$ cd ~/bax-myo_ws
$ source ./devel/setup.bash
$ . baxter.sh

# This will take you the baxter's console or something
''' inside the baxter's console, you have to source the workspace you created, move_ind '''
$ source ~/bax-myo_ws/src/baxter_arm_control/devel/setup.bash
# (enable Baxter)
$ rosrun baxter_tools enable_robot.py -e

$ rosrun move_arms inverseKin.py -l left # to move the left arm
$ rosrun move_arms inverseKin.py -l right # to move the right arm






____________________________________________________________________________________________
		'''	~~~~~~~ REFERENCES ~~~~~  '''
____________________________________________________________________________________________

Baxter Arm Controls -> http://sdk.rethinkrobotics.com/wiki/Arm_Control_Modes
Git code -> https://gist.github.com/rethink-imcmahon/237e6be4d29d812577be

http://sdk.rethinkrobotics.com/wiki/Collaborative_Manipulation

Baxter IK -> http://sdk.rethinkrobotics.com/wiki/IK_Service_Example
















