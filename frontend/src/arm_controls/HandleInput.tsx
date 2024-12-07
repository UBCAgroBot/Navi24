import { useEffect, useState } from "react";

interface HandleInputProps {
	speed: number;
	direction: number;
	setSpeed: React.Dispatch<React.SetStateAction<number>>;
	setDirection: React.Dispatch<React.SetStateAction<number>>;
	setWPressed: React.Dispatch<React.SetStateAction<boolean>>;
	setAPressed: React.Dispatch<React.SetStateAction<boolean>>;
	setSPressed: React.Dispatch<React.SetStateAction<boolean>>;
	setDPressed: React.Dispatch<React.SetStateAction<boolean>>;
}

function HandleInput({
	speed,
	direction,
	setSpeed,
	setDirection,
	setWPressed,
	setAPressed,
	setSPressed,
	setDPressed,
}: HandleInputProps) {
	const [targetSpeed, setTargetSpeed] = useState(speed);
	const [targetDirection, setTargetDirection] = useState(direction);

	const speed_accelerate_smoothing_factor = 0.3;
	const speed_return_smoothing_factor = 1;
	const direction_accelerate_smoothing_factor = 0.1;
	const direction_return_smoothing_factor = 0.1;

	useEffect(() => {
		const smoothUpdate = () => {
			setSpeed((currentSpeed) => {
				if (currentSpeed === targetSpeed) { return currentSpeed; }

				const diff = targetSpeed - currentSpeed;

				let speed_smoothing_factor = undefined;
				// Going up away from zero
				if (diff > 0 && currentSpeed >= 0) {
					speed_smoothing_factor = speed_accelerate_smoothing_factor;	
				}
				// Going down toward zero
				if (diff < 0 && currentSpeed > 0) {
					speed_smoothing_factor = speed_return_smoothing_factor;	
				}

				// Going up toward zero
				if (diff > 0 && currentSpeed < 0) {
					speed_smoothing_factor = speed_return_smoothing_factor;	
				}
				// Going down away from zero
				if (diff < 0 && currentSpeed <= 0) {
					speed_smoothing_factor = speed_accelerate_smoothing_factor;
				}

				if (!speed_smoothing_factor) {
					alert("Bug in deciding a speed smoothing factor")
					speed_smoothing_factor = 1
				}

				const step = Math.cbrt(Math.abs(diff)) * Math.sign(diff) * speed_smoothing_factor; // Cubic smoothing step
				const nextSpeed = currentSpeed + step;

				return Math.abs(diff) < 0.5 ? targetSpeed : nextSpeed; // Stop when close enough
			});

			setDirection((currentDirection) => {
				if (currentDirection === targetDirection) { return currentDirection; }

				const diff = targetDirection - currentDirection;
				
				
				let direction_smoothing_factor = undefined;
				// Going up away from zero
				if (diff > 0 && currentDirection >= 0) {
					direction_smoothing_factor = direction_accelerate_smoothing_factor;	
				}
				// Going down toward zero
				if (diff < 0 && currentDirection > 0) {
					direction_smoothing_factor = direction_return_smoothing_factor;	
				}

				// Going up toward zero
				if (diff > 0 && currentDirection < 0) {
					direction_smoothing_factor = direction_return_smoothing_factor;	
				}
				// Going down away from zero
				if (diff < 0 && currentDirection <= 0) {
					direction_smoothing_factor = direction_accelerate_smoothing_factor;
				}

				if (!direction_smoothing_factor) {
					alert("Bug in deciding a speed smoothing factor")
					direction_smoothing_factor = 1
				}

				const step = Math.cbrt(Math.abs(diff)) * Math.sign(diff) * direction_smoothing_factor; // Cubic smoothing step
				const nextDirection = currentDirection + step;

				return Math.abs(diff) < 0.5 ? targetDirection : nextDirection; // Stop when close enough
			});
		};

		const interval = setInterval(smoothUpdate, 16); // Approx 60 FPS
		return () => clearInterval(interval);
	}, [targetSpeed, targetDirection]);

	useEffect(() => {
		function handleKeyDown(event: KeyboardEvent) {
			const key = event.key;

			if (key !== "w" && key !== "a" && key !== "s" && key !== "d") {
				return;
			}

			switch (key) {
				case "w":
					setTargetSpeed(127);
					setWPressed(true);
					break;

				case "a":
					setTargetDirection(-180);
					setAPressed(true);
					break;

				case "s":
					setTargetSpeed(-127);
					setSPressed(true);
					break;

				case "d":
					setTargetDirection(180);
					setDPressed(true);
					break;
			}
		}

		function handleKeyUp(event: KeyboardEvent) {
			const key = event.key;

			if (key !== "w" && key !== "a" && key !== "s" && key !== "d") {
				return;
			}

			switch (key) {
				case "w":
					setTargetSpeed(0);
					setWPressed(false);
					break;

				case "a":
					setTargetDirection(0);
					setAPressed(false);
					break;

				case "s":
					setTargetSpeed(0);
					setSPressed(false);
					break;

				case "d":
					setTargetDirection(0);
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
