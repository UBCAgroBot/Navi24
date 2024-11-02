import { KeyboardEventHandler, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Button from './Button'

// let API_ENDPOINT = "http://0.0.0.0:5000/"
let API_ENDPOINT = "http://10.43.26.25:5000/"

function App() {

  let [speed, _setSpeed] = useState(0);
  let [direction, _setDirection] = useState(0);
  let [speedMagnitude, setSpeedMagnitude] = useState(1);


  let sendToRobot = () => {
    fetch(API_ENDPOINT + "control"
      , {
        method: 'POST',
        body: JSON.stringify({
          speed: speed * speedMagnitude,
          direction: direction,
          mode: 0,
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      }
    )
      .then(response => response.json())
      .then(data => console.log(data));
  }

  let setSpeed = (speed: number) => {
    _setSpeed(speed);
    sendToRobot();
  }

  let setDirection = (dir: number) => {
    _setDirection(dir);
    sendToRobot();
  }

  let keyPress = (event: any) => {
    switch (event.key) {
      case "w":
        setSpeed(127 * speedMagnitude);
        break;

      case "s":
        setSpeed(-128 * speedMagnitude);
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
        setSpeed(0 * speedMagnitude);
        break;

      case "s":
        setSpeed(0 * speedMagnitude);
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
