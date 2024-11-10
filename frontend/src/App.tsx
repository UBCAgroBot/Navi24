import { KeyboardEventHandler, useEffect, useRef, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Button from './Button'
import ROSLIB from 'roslib';

// let API_ENDPOINT = "http://0.0.0.0:5000/"
// let API_ENDPOINT = "http://10.43.26.25:5000/"

function App() {

  let [speed, _setSpeed] = useState(0);
  let [direction, _setDirection] = useState(0);
  let [speedMagnitude, setSpeedMagnitude] = useState(1);

  let [connectionStatus, setConnectionStatus] = useState(false);

  const rosRef = useRef<null | ROSLIB.Ros>(null);

  useEffect(() => {
    if (rosRef.current === null) {
      rosRef.current = new ROSLIB.Ros({
        url: 'ws://localhost:9090'
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

    if (rosRef.current !== null) {
      var cmd_motor = new ROSLIB.Topic({
        ros: rosRef.current,
        name: 'motor_instruction',
        messageType: 'interfaces/msg/Motor'
      });

      var motor_msg = new ROSLIB.Message({ direction: direction, mode: 1, speed: speed });
      cmd_motor.publish(motor_msg);

      console.log("Sent packet: ", speed, " ", direction);
    }
  }, [speed, direction]);


  // let sendToRobot = () => {
  //   fetch(API_ENDPOINT + "control"
  //     , {
  //       method: 'POST',
  //       body: JSON.stringify({
  //         speed: speed * speedMagnitude,
  //         direction: direction,
  //         mode: 0,
  //       }),
  //       headers: {
  //         'Content-type': 'application/json; charset=UTF-8',
  //       },
  //     }
  //   )
  //     .then(response => response.json())
  //     .then(data => console.log(data));
  // }

  let setSpeed = (speed: number) => {
    _setSpeed(speed * speedMagnitude);
  }

  let setDirection = (dir: number) => {
    _setDirection(dir);
  }

  let keyPress = (event: any) => {
    switch (event.key) {
      case "w":
        setSpeed(127);
        break;

      case "s":
        setSpeed(-128);
        break;

      case "a":
        setDirection(-30);
        break;

      case "d":
        setDirection(30);
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
      <p className="font-bold">Connection status: <span className={connectionStatus ? "text-green-600" : "text-red-600"}>
        {connectionStatus ? "Connected" : "Disconnected"}
      </span></p>
      <p>Speed: {speed}, Direction: {direction}, Speed mag: {speedMagnitude}</p>

      <div className="flex flex-col">
        <Button onPress={() => { setSpeed(127) }}
          onRelease={() => { setSpeed(0) }}>^</Button>

        <Button onPress={() => { setSpeed(-128) }}
          onRelease={() => { setSpeed(0) }}>V</Button>
      </div>

      <p>

        Direction: <button className="bg-red-100 m-1 p-2" onClick={() => { setDirection(0) }}>Reset to straight</button>
        <input type="range" className="w-full" min={-30} max={30} step={1} onChange={(event) => { setDirection(Number(event.target.value)) }} value={direction} />

        Speed:
        <input type="range" className="w-full" min={0} max={1} step={0.1} onChange={(event) => { setSpeedMagnitude(Number(event.target.value)) }} value={speedMagnitude} />
      </p>
    </div>
  )
}

export default App
