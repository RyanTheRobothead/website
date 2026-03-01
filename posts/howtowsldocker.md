---
title: How to Install and Use Docker in WSL2
externalurl: https://dev.to/luckierdodge/how-to-install-and-use-docker-in-wsl2-217l
date: 2022-03-06
description: "A quick tech tip for installing and using Docker in WSL2."
tags: [dev, post, quick_tech_tips, feed]
---

:::{image} https://res.cloudinary.com/practicaldev/image/fetch/s--1feip6b4--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qb7uf53w3fnv7t0pzfsw.jpg
:width: 80%
:align: center
:::

_Edit: It's come to my attention that, since I figured out this workaround back when WSL2 and thus Docker's WSL2 backend were new, Docker Desktop for Windows has added support for using Docker from within your WSL2 distro. This obviates the need to install Docker within a WSL2 distro in most cases. But if you find yourself in a position where you can't or don't want to use the Docker Desktop support, read on._

Say you want to run a Linux environment on a Windows machine, and in that environment one of the things you want to do is make use of docker containers. Here's the quick and dirty way to get that set up:

## Install WSL

Nowadays, this should be as simple as `Win+X`, selecting `<Command Prompt/Powershell/Windows Terminal> (Admin)`, and running `wsl --install`.

If that doesn't work, or you want to fiddle/customize/use a non-default distro, check out [Microsoft's guide here](https://docs.microsoft.com/en-us/windows/wsl/install). Make sure you install a WSL2 distro.

For the rest of this, I'm assuming you've installed the default Ubuntu Distro, steps might be slightly different for other distros.

## Verify and Setup WSL

Make sure that the distro you just installed is a WSL2 distro, as you can't run docker in WSL1.

```
# Set the default version to 2
wsl --set-default-version 2
# Check that the distro you installed is version 2
wsl -l -v
# Upgrade a v1 distro to v2
wsl --set-version <distro-name> 2
```

If you're having trouble upgrading the distro, see [here for help](https://docs.microsoft.com/en-us/windows/wsl/install#ways-to-run-multiple-linux-distributions-with-wsl).

Now, open the "Ubuntu" application that you just got installed, and set your username and password. Do package updates, install whatever tools and packages you want, and just generally make yourself at home.

## Install Docker

Follow [these setup instructions](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) (if you chose to install a distro other than Ubuntu, find the appropriate install guide on the left of that page).

Stop before running `sudo docker run hello-world`.

## Configuring Docker on WSL2

### Using Docker Without Invoking Root

Don't want to have to run docker commands with `sudo` all the time? [Follow this guide to add yourself to the docker group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

### Starting the Docker Daemon

One hiccup with docker in WSL2 is that it doesn't automatically start the Docker service. The simple but annoying solution is to run `sudo service docker start` whenever you want to use Docker.

If you don't want to have to remember and invoke that command every time, you can add the following to your "~/.profile", or your shell configuration file like "~/.bashrc":

```
if [ -n "`service docker status | grep not`" ]; then
    sudo /usr/sbin/service docker start
fi
```

Now this has the annoying side effect of making you have to type out your sudo password whenever you start WSL2 for the first time.

To fix this, you can run `sudo visudo -f /etc/sudoers.d/passwordless_docker_start`, add the following to the file (replacing `username` with your Linux username), save and close. ([See here to learn more about the intricacies and nuances of sudoer files](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file))

```
username        ALL = (root) NOPASSWD: /usr/sbin/service docker start
```

Now, the docker service automatically starts in WSL2 without requiring authentication, and you can use it more or less exactly like you would use Docker on a regular Linux install.

Cover Photo by [Tom Fisk](https://www.pexels.com/@tomfisk?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/aerial-view-photography-of-container-van-lot-1427107/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels).