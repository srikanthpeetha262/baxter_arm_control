
Before operating the baxter, edit the following lines in "baxter.sh" file

 -> go to terminal and to your core workspace, here 'bax-myo_ws'.
 	$ cd ~/bax-myo_ws
 	$ gedit baxter.sh
 
 -> Enter the below values in the file
 	(line 22, approx) -> baxter_hostname="bax.srb.louisville.edu"
 	(line 26, approx) -> your ip ="xxx.xxx.xxx.xxx" (check the ip of your PC and enter it here)
 			---> SAVE & CLOSE the file


NOTE:	1. The host name of baxter was set to "bax.srb.louisville.edu". However on the baxter 	
	   screen if you look up the host name it shows 011604P0019. Ignore it.
	2. The ip address of your PC/Laptop might change after restart. So double check it.


 -> $ cd ~/bax-myo_ws
    $ source /opt/ros/indigo/setup.bash
    $ catkin_make (run it during the baxter setup)
    $ . baxter.sh
    $ ping bax.srb.louisville.edu (You should be able to ping baxter now)
    
    $ rosrun baxter_tools enable_robot.py -e (enable Baxter)
    $ rosrun baxter_tools enable_robot.py -d (disable Baxter)


____________________________________________________________________________________________
                 Control the position of baxter's arms from Terminal

source:
https://groups.google.com/a/rethinkrobotics.com/forum/#!topic/brr-users/MOoHAnM0YnY


-> you can control it by publishing the messages to the topics
-> after running the above steps, enable the baxter robot
-> the publish command should be in the below format
   --> rostopicpub [topic] [msg_type] ['mode', 'command', 'names']

--> For commanding the left arm of baxter 

	$rostopic pub /robot/limb/left/joint_command baxter_core_msgs/JointCommand "{mode: 1, command: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], names: ['left_w0', 'left_w1', 'left_w2', 'left_e0', 'left_e1', 'left_s0', 'left_s1']}" -r 100
	
	
--> And so the command for the right arm of baxter will be

	$rostopic pub /robot/limb/right/joint_command baxter_core_msgs/JointCommand "{mode: 1, command: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], names: ['right_w0', 'right_w1', 'right_w2', 'right_e0', 'right_e1', 'right_s0', 'right_s1']}" -r 100


Untuck the Baxter's arms
	$ rosrun baxter_tools tuck_arms.py -u
	
Tuck Baxter's arms
	$ rosrun baxter_tools tuck_arms.py -t
	


	
	
____________________________________________________________________________________________
'''	creating a workspace 'move_ind' to move baxter's arms indepedently '''
____________________________________________________________________________________________

'# ~~~~~~~~~~~~  For first time building  ~~~~~~~~~~~~

$ cd ~/bax-myo_ws/src  
# instead you can also do this..... $cd ~/baxter_ws
$ mkdir -p baxter_arm_control/src
$ cd baxter_arm_control
$ catkin_make

# create a package to move baxters left arm
#$ catkin_create_pkg moveBaxLeft std_msgs roscpp rospy baxter_core_msgs
# here "baxter_core_msgs" is the message_type required to move baxter's arms.
# So I made it as dependency of the package

$ catkin_create_pkg move_arms std_msgs roscpp rospy baxter_core_msgs

now go to the "move_arms" package folder and create a cpp file "mv_left_arm"


# now go to the 'move_bax_left' folder and edit the package.xml file. 
# The package.xml file would look like tis after editing

'''
<?xml version="1.0"?>
<package>
  <name>move_arms</name>
  <version>0.1.0</version>
  <description>The move_arms package</description>

  <maintainer email="srikanth.peetha@louisville.edu">andromeda-2-1-2</maintainer>

  buildtool_depend>catkin</buildtool_depend>
  
  <build_depend>baxter_core_msgs</build_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  
  <run_depend>baxter_core_msgs</run_depend>
  <run_depend>roscpp</run_depend>
  <run_depend>rospy</run_depend>
  <run_depend>std_msgs</run_depend>


  <!-- The export tag contains other, unspecified, tags -->
  <export>
    <!-- Other tools can request additional information be placed here -->

  </export>
</package>
'''

-> you now have the package.xml file ready

#now go to the "src" folder and create a cpp file "left_arm.cpp" and write the code.
-> now you have the code to move the left arm, mv_left_arm.cpp

go to the CMakeLists.txt file in the "move_arms/src" folder and add the below lines


~~~~~~~~~~~~~~~~~ These lines were added ~~~~~~~~~~~~~~~~~~~

#add_executable(pkg_name src/left_arm.cpp)
add_executable(mv_left_arm  src/mv_left_arm.cpp)

#target_link_libraries(test_node ${catkin_LIBRARIES})
target_link_libraries(mv_left_arm ${catkin_LIBRARIES})

#add_dependencies(test_node <package_name>_generate_messages_cpp) 
add_dependencies(mv_left_arm mv_left_arm_generate_messages_cpp) 
~~~~~~~~~~~~~~~~~ These lines were added ~~~~~~~~~~~~~~~~~~~


-> you now have the CMakeLists.txt file ready

# go back to the workspace folder and run cmake

$ cd ~/bax-myo_ws/src/baxter_arm_control
$ catkin_make


# the catkin_make should run without any errors


____________________________________________________________________________________________
		'''	moving the baxter's arms  '''
____________________________________________________________________________________________

#if you MADE CHANGES to files from the previous time you ran it start from here.
$ cd ~/bax-myo_ws/src/baxter_arm_control
$ catkin_make

$ cd ~/bax-myo_ws
$ source /opt/ros/indigo/setup.bash
$ catkin_make

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

#Independent movement with positions
$ rosrun move_arms mv_left_arm # for C++ code file
$ rosrun move_arms mv_left.py # for python code file

____________________________________________________________________________________________
		'''	moves with Inverse Kinematics  '''
____________________________________________________________________________________________

Reference: Baxter IK -> http://sdk.rethinkrobotics.com/wiki/IK_Service_Example

#go back to the original baxter workspace
$ cd ~/bax-myo_ws
$ source ./devel/setup.bash
$ . baxter.sh

# This will take you the baxter's console or something
''' inside the baxter's console, you have to source the workspace you created, move_ind '''
$ source ~/bax-myo_ws/src/baxter_arm_control/devel/setup.bash
# (enable Baxter)
$ rosrun baxter_tools enable_robot.py -e

$ rosrun move_arms inverseKin.py -l <left/right>







____________________________________________________________________________________________
		'''	~~~~~~~ REFERENCES ~~~~~  '''
____________________________________________________________________________________________

Baxter Arm Controls -> http://sdk.rethinkrobotics.com/wiki/Arm_Control_Modes
Git code -> https://gist.github.com/rethink-imcmahon/237e6be4d29d812577be

http://sdk.rethinkrobotics.com/wiki/Collaborative_Manipulation

Baxter IK -> http://sdk.rethinkrobotics.com/wiki/IK_Service_Example
















