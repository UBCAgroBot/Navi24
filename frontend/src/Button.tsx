import { ReactNode } from 'react'

function Button(props: {
  onPress: () => void,
  onRelease: () => void,
  children: ReactNode
}) {
  return (
    <button className="p-20 m-5 bg-green-100 text-xl"
      onMouseDown={props.onPress}
      onMouseUp={props.onRelease}
      onTouchStart={props.onPress}
      onTouchEnd={props.onRelease}>
      {props.children}
    </button>
  )
}

export default Button
