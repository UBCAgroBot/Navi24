import { useEffect } from "react";

function HandleInput({
	speed,
	direction,
	setSpeed,
	setDirection,
	setWPressed,
	setAPressed,
	setSPressed,
	setDPressed
}) {
	useEffect(() => {

		function handleKeyDown(event) {
			const key = event.key;
	
			if (key !== "w" &&
				key !== "a" &&
				key !== "s" &&
				key !== "d") {
					return;
			}
	
			switch (key) {
				case 'w':
					setSpeed(127)
					setWPressed(true);
					break;
	
				case 'a':
					setDirection(-180);
					setAPressed(true);
					break;
	
				case 's':
					setSpeed(-127);
					setSPressed(true);
					break;
	
				case 'd':
					setDirection(180);
					setDPressed(true);
					break;
			}
		}
	
		function handleKeyUp(event) {
			const key = event.key;
	
			if (key !== "w" &&
				key !== "a" &&
				key !== "s" &&
				key !== "d") {
					return;
			}
	
			switch (key) {
				case 'w':
					setSpeed(0);
					setWPressed(false);
					break;
	
				case 'a':
					setDirection(0);
					setAPressed(false);
					break;
	
				case 's':
					setSpeed(0);
					setSPressed(false);
					break;
	
				case 'd':
					setDirection(0);
					setDPressed(false);
					break;
			}
	
		}

		window.addEventListener("keydown", handleKeyDown);
		window.addEventListener("keyup", handleKeyUp);

		return () => {
			window.removeEventListener("keydown", handleKeyDown);
			window.removeEventListener("keyup", handleKeyUp);
		};
	}, []);

	return null;
}

export default HandleInput;