// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MOTOR__STRUCT_H_
#define INTERFACES__MSG__DETAIL__MOTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Motor in the package interfaces.
typedef struct interfaces__msg__Motor
{
  int8_t speed;
  uint8_t mode;
  int8_t direction;
} interfaces__msg__Motor;

// Struct for a sequence of interfaces__msg__Motor.
typedef struct interfaces__msg__Motor__Sequence
{
  interfaces__msg__Motor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Motor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__MOTOR__STRUCT_H_
