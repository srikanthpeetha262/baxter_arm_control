
#include "ros/ros.h"
#include "/home/andromeda-2-1-2/bax-myo_ws/devel/include/baxter_core_msgs/JointCommand.h"
#include <new>

int main(int argc, char **argv)
//int main(int command, char **names)
{
	ros::init(argc, argv, "moveBaxLeft");
	ros::NodeHandle n;
	
	ros::Publisher moveBaxLeft_pub = n.advertise<baxter_core_msgs::JointCommand>("/robot/limb/left/joint_command", 1);
	ros::Rate loop_rate(100);

	baxter_core_msgs::JointCommand msg;
	msg.mode = baxter_core_msgs::JointCommand::POSITION_MODE;
	
	msg.names.push_back("left_s0");
	msg.names.push_back("left_e1");
	msg.names.push_back("left_s0");
	msg.names.push_back("left_s1");
	msg.names.push_back("left_w0");
	msg.names.push_back("left_w1");
	msg.names.push_back("left_w2");
	
	// Memory allocation to eliminate "segmenation fault" error
	
	msg.command.resize(msg.names.size());
	
  	for(size_t i = 0; i < msg.names.size(); i++)
		msg.command[i] = 0.0;
	
	//end of the memory allocation process
	
		
	int i = 1;
	while (ros::ok())
	//while (i = 1)
	{
		moveBaxLeft_pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
		i = 2;
	}
	
	ros::shutdown();
		
	return 0;
}	

/*

rosnode info moveBaxLeft
--------------------------------------------------------------------------------
Node [/moveBaxLeft]
Publications: 
 * /robot/limb/left/joint_command [baxter_core_msgs/JointCommand]
 * /rosout [rosgraph_msgs/Log]

Subscriptions: None

Services: 
 * /moveBaxLeft/set_logger_level
 * /moveBaxLeft/get_loggers


contacting node http://10.200.189.127:36313/ ...
Pid: 3195
Connections:
 * topic: /rosout
    * to: /rosout
    * direction: outbound
    * transport: TCPROS
 * topic: /robot/limb/left/joint_command
    * to: /realtime_loop
    * direction: outbound
    * transport: TCPROS

*/


