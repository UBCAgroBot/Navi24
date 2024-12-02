import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ClassicControls from './ClassicControls'
import ArmControls from './arm_controls/ArmControls'

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<ClassicControls />} />
				<Route path="arm-controls" element={<ArmControls />} />
			</Routes>
		</BrowserRouter>
	)
}

export default App