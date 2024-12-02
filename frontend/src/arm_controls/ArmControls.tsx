import { useState, useRef, useEffect } from 'react'
import { sendRosMsg } from './RosSend';
import HandleInput from './HandleInput';
import ROSLIB from 'roslib';

function ArmControls() {
	const rosRef = useRef<null | ROSLIB.Ros>(null);

	const [apiEndpoint, setApiEndpoint] = useState<string>("ws://localhost:9090");
	const [connectionStatus, setConnectionStatus] = useState<boolean>(false);
	const [gamepadConnected, setGamepadConnected] = useState<boolean>(false);

	const [speed, setSpeed] = useState<number>(0);
	const [direction, setDirection] = useState<number>(0);

	const [wPressed, setWPressed] = useState<boolean>(false);
	const [aPressed, setAPressed] = useState<boolean>(false);
	const [sPressed, setSPressed] = useState<boolean>(false);
	const [dPressed, setDPressed] = useState<boolean>(false);

	useEffect(() => {
		sendRosMsg(
			rosRef,
			direction,
			speed,
			apiEndpoint,
			connectionStatus,
			setConnectionStatus,
		);
	}, [speed, direction])

	return (
		<main className="flex flex-col h-screen">
			<HandleInput 
				speed={speed} 
				direction={direction} 
				setSpeed={setSpeed} 
				setDirection={setDirection} 
				setWPressed={setWPressed}
				setAPressed={setAPressed}
				setSPressed={setSPressed}
				setDPressed={setDPressed}
				/>
			<div className="flex flex-grow">
				<div className="w-[40%] flex flex-col">
					<div className="flex flex-col relative items-center justify-center h-[50%]">
						<p className="text-[96px]">{speed}</p>
						{/* Direction gauge */}
						<div className="bottom-0 absolute h-[25px] w-[400px] bg-[#D9D9D9]"></div>
					</div>
					<div className="h-[50%] flex items-center justify-center">
						<div className="grid grid-rows-2 grid-cols-3 gap-4 text-[32px]">
							<div></div>
							{ wPressed ? 
								<div className="w-[100px] h-[100px] bg-[#8C8C8C] rounded-full flex items-center justify-center">W</div>
								:
								<div className="w-[100px] h-[100px] bg-[#D9D9D9] rounded-full flex items-center justify-center">W</div>
							}
							<div></div>
							{aPressed ?
								<div className="w-[100px] h-[100px] bg-[#8C8C8C] rounded-full flex items-center justify-center">A</div>
								:
								<div className="w-[100px] h-[100px] bg-[#D9D9D9] rounded-full flex items-center justify-center">A</div>
							}
							{sPressed ?
								<div className="w-[100px] h-[100px] bg-[#8C8C8C] rounded-full flex items-center justify-center">S</div>
								:
								<div className="w-[100px] h-[100px] bg-[#D9D9D9] rounded-full flex items-center justify-center">S</div>
							}
							{dPressed ?
								<div className="w-[100px] h-[100px] bg-[#8C8C8C] rounded-full flex items-center justify-center">D</div>
								:
								<div className="w-[100px] h-[100px] bg-[#D9D9D9] rounded-full flex items-center justify-center">D</div>
							}
						</div>
					</div>
				</div>
				<div className="w-[60%] flex flex-col items-center justify-center text-[24px]">
				</div>
			</div>
			<div className="bg-[#1A1A1D] flex items-center !h-[80px] w-full px-24 text-[#D9D9D9] font-light">
				<div className="border border-[#D9D9D9] h-[42px] flex items-center justify-center px-8 rounded-[8px] mx-4"><p>Stop</p></div>
				<div className="border border-[#D9D9D9] h-[42px] flex items-center justify-center px-8 rounded-[8px] mx-4"><p>Auto Pilot</p></div>
				<div className="border border-[#D9D9D9] h-[42px] flex items-center justify-center px-8 rounded-[8px] mx-4"><p>ws://localhost:9090</p></div>
				<div className="border border-[#D9D9D9] h-[42px] flex items-center justify-center px-8 rounded-[8px] mx-4">
					<p>Agrobot Connection:
							{connectionStatus ?
								<span className="text-green-600"> Connected</span>
								:
								<span className="text-red-600"> Disconnected</span>
							}
					</p>
				</div>
				<div className="border border-[#D9D9D9] h-[42px] flex items-center justify-center px-8 rounded-[8px] mx-4">
					{gamepadConnected ?
						<p className="text-green-600">Connected to Controller</p>
						:
						<p className="">No Controller</p>
					}
				</div>
			</div>

		</main>
	)
}

export default ArmControls