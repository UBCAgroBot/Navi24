// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MOTOR__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__MOTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/motor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Motor_direction
{
public:
  explicit Init_Motor_direction(::interfaces::msg::Motor & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Motor direction(::interfaces::msg::Motor::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Motor msg_;
};

class Init_Motor_mode
{
public:
  explicit Init_Motor_mode(::interfaces::msg::Motor & msg)
  : msg_(msg)
  {}
  Init_Motor_direction mode(::interfaces::msg::Motor::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_Motor_direction(msg_);
  }

private:
  ::interfaces::msg::Motor msg_;
};

class Init_Motor_speed
{
public:
  Init_Motor_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Motor_mode speed(::interfaces::msg::Motor::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_Motor_mode(msg_);
  }

private:
  ::interfaces::msg::Motor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Motor>()
{
  return interfaces::msg::builder::Init_Motor_speed();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__MOTOR__BUILDER_HPP_
