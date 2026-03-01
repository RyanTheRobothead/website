---
title: How to Call a Service from a ROS2 Launch File
externalurl: https://dev.to/luckierdodge/how-to-call-a-service-from-a-ros2-launch-file-4l7p
date: 2022-09-03
description: "A quick tech tip for calling a service from within a ROS2 Launch File."
tags: [dev, post, quick_tech_tips, feed, ros2, robotics]
---

:::{image} https://raw.githubusercontent.com/ros-infrastructure/artwork/master/ros_logo.svg
:width: 250px
:align: center
:::

This one is pretty straight forward, but took me a non-trivial amount of searching to find for myself. To call a ros2 service from a ros2 launch file, add the following to your launch file (see [the official docs](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html) for more on launch files):

```python
from launch.substitutions import FindExecutable
from launch.actions import ExecuteProcess

...

ld.add_action(
    ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " service call ",
            "/namespace/service_to_call ",
            "example_msgs/srv/ExampleMsg ",
            '"{param_1: True, param_2: 0.0}"',
        ]],
        shell=True
    )
)
```

Note the following:

* `ld` here is a variable containing an instance of `LaunchDescription`
* `/namespace/service_to_call` is replaced with the service you're looking to call (don't forget any appropriate namespaces) and can be found with `ros2 service list`
* `example_msgs/srv/ExampleMsg` is the message type used by that service, which you can get with `ros2 service info /namespace/service_to_call`
* `"{param_1: True, param_2: 0.0}"` is the dictionary defining the message data. To find the parameters you need to set, you may need to consult the `.srv` file or documentation.

Don't forget to include the `shell=True` argument, as the command will fail with a confusing "File not found" error without it.

