import { KeyboardEventHandler, useEffect, useRef, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Button from './Button'
import ROSLIB from 'roslib';

let API_ENDPOINT = "ws://agrobot.local:9090"

// Calibrate deadzone as needed
const DEADZONE = (input: number) => {
  if (Math.abs(input) < 0.1) {
    return 0;
  }

  return input;
};

// On the joystick, - is upwards, so the sign is flipped
const SPEED_FUNCTION = (input: number) => {
  // Start with a basic squaring function
  let sign = input <= 0 ? 1 : -1;
  return input * input * sign;
};

const DIRECTION_FUNCTION = (input: number) => {
  // Start with a basic squaring function
  let sign = input <= 0 ? -1 : 1;
  return input * input * sign;
};

const MAX_SPEED = 127;
const MAX_DIRECTION = 127;

function App() {

  let [speed, _setSpeed] = useState(0);
  let [direction, _setDirection] = useState(0);
  let [speedMagnitude, setSpeedMagnitude] = useState(1);

  let [connectionStatus, setConnectionStatus] = useState(false);

  // Use this if you want to add little debug messages
  let [dbg, setDbg] = useState("");

  const rosRef = useRef<null | ROSLIB.Ros>(null);
  let [gamepadConnected, setGamepadConnected] = useState(false);

  // Deal with the joystick stuff
  const loopRef = useRef<null | number>(null);

  const gameLoop = () => {

    // On Chrome we have to get a new gamepad instance
    // On firefox using the one in gamepadRef works fine
    // Massive chrome L
    // const gp = gamepadRef.current;
    const [gp] = navigator.getGamepads();
    if (gp == null) {
      return;
    }

    _setSpeed(MAX_SPEED * SPEED_FUNCTION(DEADZONE(gp.axes[1])));
    _setDirection(MAX_DIRECTION * DIRECTION_FUNCTION(DEADZONE(gp.axes[2])));

    loopRef.current = requestAnimationFrame(gameLoop);
  }
  useEffect(() => {

    window.addEventListener("gamepadconnected", (e) => {
      // Gamepad connected
      setGamepadConnected(true);
      requestAnimationFrame(gameLoop);
      console.log("Gamepad connected:", e.gamepad.id);

    });

    window.addEventListener("gamepaddisconnected", (e) => {
      setGamepadConnected(false);

      console.log("Gamepad disconnected:", e.gamepad.id);
    });
  }, []);

  // Communcate with ROS
  // This code runs every time speed or direction changes
  useEffect(() => {
    if (rosRef.current === null) {
      rosRef.current = new ROSLIB.Ros({
        url: API_ENDPOINT
      });
      rosRef.current.on('connection', function() {
        console.log('Connected to websocket server.');
        setConnectionStatus(true);
      });

      rosRef.current.on('error', function(error) {
        console.log('Error connecting to websocket server: ', error);
        setConnectionStatus(false);
      });

      rosRef.current.on('close', function() {
        console.log('Connection to websocket server closed.');
        setConnectionStatus(false);

        rosRef.current = null;
      })
    }

    if (rosRef.current !== null && connectionStatus) {
      var cmd_motor = new ROSLIB.Topic({
        ros: rosRef.current,
        name: 'motor_instruction',
        messageType: 'interfaces/msg/Motor'
      });

      var motor_msg = new ROSLIB.Message({ direction: Math.round(direction), mode: 0, speed: Math.round(speed) });
      cmd_motor.publish(motor_msg);

      console.log("Sent packet: ", motor_msg);
    }
  }, [speed, direction]);

  let absStop = () => {
    if (rosRef.current !== null && connectionStatus) {
      var cmd_motor = new ROSLIB.Topic({
        ros: rosRef.current,
        name: 'motor_instruction',
        messageType: 'interfaces/msg/Motor'
      });

      var motor_msg = new ROSLIB.Message({ direction: Math.round(0), mode: 0, speed: Math.round(0) });
      cmd_motor.publish(motor_msg);

      console.log("Sent packet: ", motor_msg);
    }
  }

  let setSpeed = (speed: number) => {
    _setSpeed(speed * speedMagnitude);
  }

  let setDirection = (dir: number) => {
    _setDirection(dir);
  }

  let keyPress = (event: any) => {
    switch (event.key) {
      case "w":
        setSpeed(MAX_SPEED);
        break;

      case "s":
        setSpeed(-MAX_SPEED);
        break;

      case "a":
        setDirection(-MAX_DIRECTION);
        break;

      case "d":
        setDirection(MAX_DIRECTION);
        break;

      default:
        break;
    }
  }

  let keyRelease = (event: any) => {
    switch (event.key) {
      case "w":
        setSpeed(0);
        break;

      case "s":
        setSpeed(0);
        break;

      case "a":
        setDirection(0);
        break;

      case "d":
        setDirection(0);
        break;

      default:
        break;
    }
  }

  return (
    <div onKeyDown={(event) => { keyPress(event) }} onKeyUp={keyRelease} >
      <h1 className="text-xxxl">Manual Control</h1>
      <p className="font-bold">
        Connection status: &nbsp;
        <span className={connectionStatus ? "text-green-600" : "text-red-600"}>
          {connectionStatus ? "Connected" : "Disconnected"}
        </span> &nbsp;
        Joystick status: &nbsp;
        <span className={gamepadConnected ? "text-green-600" : "text-red-600"}>
          {gamepadConnected ? "Connected" : "Disconnected"}
        </span> &nbsp;
        {dbg}
      </p>
      <p>Speed: {speed}, Direction: {direction}, Speed mag: {speedMagnitude}</p>

      <div className="flex flex-col">
        <Button onPress={() => { setSpeed(MAX_SPEED) }}
          onRelease={() => { setSpeed(0) }}>^</Button>

        <Button onPress={() => { setSpeed(-MAX_SPEED) }}
          onRelease={() => { setSpeed(0) }}>V</Button>
      </div>

      <p>

        Direction: <button className="bg-red-100 m-1 p-2" onClick={() => { setDirection(0) }}>Reset to straight</button>
        <input type="range" className="w-full" min={-MAX_DIRECTION} max={MAX_DIRECTION} step={1} onChange={(event) => { setDirection(Number(event.target.value)) }} value={direction} />

        Speed:
        <input type="range" className="w-full" min={0} max={1} step={0.1} onChange={(event) => { setSpeedMagnitude(Number(event.target.value)) }} value={speedMagnitude} />

        <br />
<button className="bg-red-500 m-1 p-2" onClick={() => { absStop(); }}>OVERRIDE STOP</button>
      </p>
    </div>
  )
}

export default App
