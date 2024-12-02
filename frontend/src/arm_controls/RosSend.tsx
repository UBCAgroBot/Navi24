import ROSLIB from 'roslib';

function sendRosMsg(
	rosRef:React.MutableRefObject<ROSLIB.Ros | null>, 
	direction: number, 
	speed: number, 
	connectionStatus:boolean,
) {

	if (rosRef.current !== null && connectionStatus) {
		var cmd_motor = new ROSLIB.Topic({
			ros: rosRef.current,
			name: 'motor_instruction',
			messageType: 'interfaces/msg/Motor'
		});

		var motor_msg = new ROSLIB.Message({ mode: 0, direction: Math.round(direction), speed: Math.round(speed) });
		cmd_motor.publish(motor_msg);

		console.log("Sent packet: ", motor_msg);
	}
}


export { sendRosMsg };