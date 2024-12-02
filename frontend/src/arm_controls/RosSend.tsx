import ROSLIB from 'roslib';

function sendRosMsg(
	rosRef:React.MutableRefObject<ROSLIB.Ros | null>, 
	direction: number, 
	speed: number, 
	endpoint: string,
	connectionStatus:boolean,
	setConnectionStatus:React.Dispatch<React.SetStateAction<boolean>>
) {
	if (rosRef.current === null) {
		rosRef.current = new ROSLIB.Ros({
			url: endpoint
		});
		rosRef.current.on('connection', function () {
			console.log('Connected to websocket server.');
			setConnectionStatus(true);
		});

		rosRef.current.on('error', function (error) {
			console.log('Error connecting to websocket server: ', error);
			setConnectionStatus(false);
		});

		rosRef.current.on('close', function () {
			console.log('Connection to websocket server closed.');

			rosRef.current = null;
		})
	}

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