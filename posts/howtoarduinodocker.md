---
title: How to Communicate with an Arduino from Docker
date: 2021-03-14
externalurl: "https://dev.to/luckierdodge/how-to-communicate-with-an-arduino-from-docker-3fo7"
description: "A quick tech tip for communicating with Arduino-based microcontrollers from applications running in Docker containers."
tags: [dev, post, quick_tech_tips, feed]
---

:::{image} https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ei52k2optp8x8dp8cz75.png
:width: 80%
:align: center
:::

Something I learned this weekend. Let's say you have an Arduino, and you want to communicate with it via serial from a Linux device, like a Jetson Nano. But not from that device's host operating system. No, that'd be too easy.

Instead, you want to talk with this Arduino from an application running in an unprivileged Docker container. How would you do that?

## How To Bring an Arduino inside Docker

It turns out it's actually quite simple! When connected to a Linux device via a USB cable, most Arduino's show up as a device in the form `/dev/ttyAMCx` where x is replaced with an integer counter, starting from 0. So the first Arduino you connect is `/dev/ttyAMC0`, the second is `/dev/ttyAMC1` and so on.

To access that from Docker, all you need is the docker `--device` flag. Include it in the docker run command as `docker run <other options> --device="/dev/ttyACM0" <more options, image name, etc>` and you're all set. You can access the Arduino in the container at `/dev/ttyACMx` just like you would on the host, say with the `pyserial` package in Python.

## Words of Warning

Couple quick notes:

1. You need to have the device connected before you launch your docker container with that flag. Otherwise, you'll get an error.
1. You may run into issues if the device is disconnected and reconnected while the container is running.
1. Serial over wires (for instance, with jumper cables connecting pins on the arduino to GPIO on a Jetson or Raspberry Pi) rather than via the USB port will probably have a different device file handle, but will function the same way (pass the device file handle into the container with `--devices`.
