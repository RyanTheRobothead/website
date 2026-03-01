---
title: Extending an Old-school Programmable Keyboard with AutoHotKey
date: 2021-02-23
externalurl: "https://dev.to/luckierdodge/extending-an-old-school-programmable-keyboard-with-autohotkey-31fb-temp-slug-3842210?preview=afe4ec4a7ab6763b3713f9f19654cbe4b93fb10d89eee861c2c396998cdc8873ff3a6731808f09d8768b34fb92b4986af38d71bf4f53607a6964b1ee"
description: "In this adventure, I explore the possibilities presented by an old-school programmable keyboard from the 90s, unearthed at a thrift store, and how it can still be useful and productive in the 2020's."
tags: [Adventures_in_Tech, post, feed]
---

:::{image} /assets/images/mck142pro/box.jpg
:width: 80%
:align: center
:::

## So it Begins...

Our tale begins in December of 2020 with a message from my friend, roommate, and a notorious thrifter/dumpster diver extraordinaire, Jorge (name changed to protect the innocent) asking if I was interested in an old mechanical keyboard from the thrift store, still in the original packaging.
The message came with a picture of the front of the box, from which little information could be gleaned except the words "TWENTY-FOUR PROGRAMMABLE KEYS".
Like any good computer nerd, I said "Absolutely!".
So he picked up two, one for himself and one for me, for a crisp $3 USD each.

When he returned with his loot, I quickly set to figuring out what, exactly, we had on our hands.
These were brand-new in the box keyboards, and the box said _MCK-142 Pro_...and not much else.
Not even a manufacturer.
But a name's as good a place to start as any, and I turned to the internet and my search engine of choice to look for clues.

And that's where I found [http://www.mck142.com/](http://www.mck142.com/), a lovely little time capsule/memorial devoted to this keyboard specifically.
I encourage you to click through and appreciate this website for a moment (it doesn't take too long to read in its entirety, and it's such a lovingly crafted little webpage).

## Getting to Know the MCK-142 Pro

For those of you who didn't click through, I'll give you a quick rundown of this keyboard's features

* Satisfyingly Clicky Mechanical Switches
* Two sets of Function Keys: the standard top row and a "Left-handed" column on the left side of the main keyboard
* 8-directional arrow keys (that's right, this thing can move the cursor diagonally with a single keypress)
* Coiled PS2 cable
* A Fast Repeat Key. According to the manual, this bumps the keyboard from a default of 10 Characters Per Second (CPS) when a key is held, to a crisp 20 CPS with the Fast Repeat Key.
* 24 Programmable Keys
* 8K (as in, Kilobytes) of Onboard CMOS SRAM Memory, maintained by a set of 4(!) AA batteries (not included, thankfully. Otherwise they'd be a corroded mess by now)
* A floppy disk with software for programming the aformentioned Programmable Keys

Some of this functionality has been rendered obsolete by the passage of time, of course.
The "Fast Repeat" key, which would allow the user to more quickly enter the same key when holding it down, is superseded by the host operating system's settings on key repeats and associated delays these days.
The floppy disk with included software for programming may still be usable on some IBM PC's from the 90s, but I wasn't about to try and find out.

Notably, it does not feature a Windows Key, because it wasn't really intended for use with Windows NT-based computers, but [PowerToys'](https://github.com/microsoft/PowerToys) key remapping utility solves that (in my case, I remapped the Caps Lock key, a key which I ONLY press accidentally).

The keyboard itself very much reminds me of the old Gateway family PC we had when I was growing up, with the same solid square body, weighty heft, and lightly textured beige ABS with gray accents.
I've never had too much nostalgia for that era of computing (I mostly remember that PC for being slow, noisy, and prone to crashes), but it's well-built, if nothing else.

:::{image} /assets/images/mck142pro/keyboard.jpg
:width: 80%
:::

## Programming the Programmable Keyboard

Now, I had to figure out how to program this beauty.
At first, I was concerned that, without the software working (aka, without an IBM PC or some sort of emulator), I'd be unable to actually program the keyboard.
Not the end of the world, but disappointing to relinquish such unique functionality.

Thankfully, a detailed reading of the manual revealed that this was not the case!
In addition to the 24 Programmable Keys, the keyboard has a "Select" key and two LEDs: "Menu" and "Prog".
As it turns out, that key could be used to program each of the 24 keys, with the following steps (taken word for word out of the manual):

1. Press the SELECT Key twice within a second, the PROG LED indicator in YELLOW will turn on.
1. Press one PF Key, e.g. any one of PF1 to PF24, to start data entry.
1. Type strings or commands you want to save in any one of PF keys by using keyboard typewriter keys. The keystrokes of every PF key is limited within 320 keystrokes.
1. Press the SELECT Key once to save the data to the chosen PF Key, the PROG LED indicator in YELLOW will flash once.
1. Repeat the action from 2. to 4. for defining others or redefining any PF keys.
1. Press the SELECT Key one more time to complete data entry, the PROG LED indicator in YELLOW will turn off.

So, for instance, if I wanted to map the `PF1` key to something like `Ctrl+Shift+V`, I could do that by:

> Pressing `SELECT` twice, pressing `PF1`, typing `Ctrl+Shift+V`, pressing the `SELECT` key, and then pressing the `SELECT` key again to exit.

Now, the manual did forget to mention something: how to actually use the `PF` keys.
After programming one of the keys, I found that pressing it didn't actually do anything.
Perplexing.

With the quest teetering on the edge of disaster, I set out to find a solution.
After some experimentation, I discovered that I needed to press the `SELECT` key once to activate the `PF` keys. When I did that, the Menu LED lit up green and the `PF` keys would work.
Without it, no dice.
Moreover, this needed to be done anytime the computer was restarted or the keyboard was disconnected.
Easy enough, but strangely, not mentioned anywhere in the manual.
I can't help but think the software might automatically handle that functionality, but without it the keys have to be manually toggled.

## Extending with AutoHotKey

Now at this point, I can program the keys to do essentially anything I can do on my keyboard (with 320 keystrokes, at least).
This includes both entering hotkeys and typing text (or a mix of both), which is neat, but I wanted to push it further.
After all, I could already use hotkeys by...pressing the hotkey.

Naturally, the first thing I did once I got programming working was program it to type [The Tragedy of Darth Plagueis the Wise](https://knowyourmeme.com/memes/the-tragedy-of-darth-plagueis-the-wise) at the press of a button.
There are rules, after all.

But how to make this actually useful?
The use cases suggested by the keyboard were things like passwords, email signatures, and other text you have to repeat often.
But I've found that most of these scenarios have been solved by password managers, built-in email signatures, and other software approaches.
Plus programming passwords or other sensitive information into a keyboard really sets my security spider-senses atingling.

What I really wanted to do with this keyboard, was configure it such that I could essentially trigger an arbitrary action on my computer with each button.
And I wanted to be able to easily change what each `PF` key would do (typing out the whole Tragedy of Darth Plagueis takes awhile, after all).

### Enter AutoHotKey

To do that, I turned to [AutoHotKey](https://www.autohotkey.com/), the self-proclaimed "ultimate automation scripting language for Windows".
It's a powerful tool, capable of a great many things, but for our purposes, it provides us with a way to create custom hot keys that can trigger a wide range of things: run one or more programs, manage which windows are open and active, type text, make decisions based on whats happening on the computer, and more.
Moreover, these hotkeys and outcomes are laid out in a script, which can be quickly modified and restarted to change the effect of a given hotkey.

One wrinkle quickly presents itself, however.
AutoHotKey works by intercepting values from the keyboard.
For instance, if I type `Ctrl+Shift+J`, and I have an AutoHotKey script with that hotkey programmed as a trigger, the corresponding actions will be run when `Ctrl+Shift+J` is detected.
But the `PF` keys aren't really keys, at least, not from the Operating System's perspective.
When a `PF` key is pressed, the only keys the computer sees are whatever strokes the key was programmed to type.
So I can't have an AutoHotKey script listen for the `PF` keys directly, I have to have it listen for a special hot key which I program into each `PF` key.

Since I don't want the AutoHotKey hooks to trigger when I press something other than a `PF` key, these can't be hotkeys I need to use regularly.
And I don't want the AutoHotKey functionality to mask actual functionality, either.

So I set out to find a set of 24 hotkeys not used anywhere else on my computer.
And I almost succeeded.
The closest I got was with the pattern `Ctrl+Alt+Shift+Fx`, where `Fx` corresponds to `PFx`, i.e. `PF1:F1`, `PF2:F2`, etc.
Now, you'll quickly realize there's a problem here: I have 24 programmable keys, but only 12 function keys.
Not to fear, as it turns out AutoHotKey can differentiate between left and right modifier keys! So I set the first 12 `PF` keys to use the left control key, and the last 12 to use the right control key.

Unfortunately, exactly one of these shortcuts (the `F7` combo, I think) is actually already mapped to some obscure function of Nvidia's GeForce Experience software.
But since I had never used that functionality or key combo before in my life, I decided that was okay.
This specific pattern of hotkeys may not work for everyone, but it worked for my purposes.

Notably, this approach confers another advantage: even without this particular keyboard, I can still use my AutoHotKey setup, because they just correspond to (awkward, inconvenient) hotkeys.
The Programmable keyboard provides a simple, clean interface from which I can trigger whatever functionality I want with the press of a single button now.

### The AutoHotKey Script

So what does the script look like, and what am I actually doing with it?
[Here's a Gist](https://gist.github.com/LuckierDodge/2ed678e035306d7f3cd935a40b3b0028) of the full version, but I'll break it down below.

We start with some opening configuration, which are pretty much the defaults for a new AutoHotKey script:

```
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
```

Then, we add 24 of the following, slightly modified to match each `PF` key:

```
; PF1
<^!+F1::
Run, wt
return
```

The first line is a comment identifying the programmable key I'm creating a hotkey for (AutoHotKey uses semicolons for its comment character).
The second is declaring the hotkey, broken up as follows:

* `<` indicates that we want the "left" version of the next modifier key
* `^` corresponds to the control key in AutoHotKey parlance.
* `!` corresponds to the alt key
* `+` corresponds to the shift key
* `F1` corresponds to the first function key
* `::` indicates the end of our hotkey, with everything after it corresponding to what should happen after the hotkey is detected.

This brings us to the third line `Run, wt` which, as the name implies, runs a program.
In this case, its running the `wt` shortcut, which opens the Windows Terminal, but you could replace that with any shortcut name or path to an application.
Basically, it works the same as the Windows Run dialog accessed with `Win+r`.

But we're not limited to running just a single command. Consider,

```
; PF2
<^!+F2::
Run, outlook
Run, "C:\Users\Ryan Lewis\AppData\Local\Microsoft\Teams\Update.exe" --processStart "Teams.exe"
Run, "C:\Users\Ryan Lewis\AppData\Local\slack\slack.exe"
Run, "C:\Users\Ryan Lewis\AppData\Local\Discord\Update.exe" --processStart Discord.exe
return
```

which opens all of my various communications applications. I just switch to an empty virtual desktop, press `PF2`, and it opens Outlook, Teams, Slack, and Discord. With [PowerToys'](https://github.com/microsoft/PowerToys) Fancy Zones, it even nicely positions them in the same grid pattern every time.

Last but not least, my proudest creation so far:

```
; PF3
<^!+F3::
WinHTTP := ComObjCreate("WinHTTP.WinHttpRequest.5.1")
WinHTTP.Open("GET", "https://wttr.in/12345?nFATQ")
WinHttp.Send()
response := WinHTTP.ResponseText
Gui, New,, Weather Report
Gui, Color, 111111
Gui, Font, s14 cWhite, Cascadia Mono
Gui, Add, Text,, % response
Gui, Show
return
```

Which sends an HTTP request to the wonderful [wttr.in](https://wttr.in) weather API, and displays the results in a helpful dialog.
I won't bore you with the details of how it works, but I think it's a simple example of some of the powerful potential here: anything I can hook up to an API endpoint, I can run with the press of a button.

:::{image} /assets/images/mck142pro/weather-dialog.png
:width: 80%
:::

## Denouement

To summarize, I took an old programmable mechanical keyboard, combined it with the power of AutoHotKey, and found a needlessly complicated way to create a budget [Stream Deck](https://www.elgato.com/en/gaming/stream-deck).
Compared to the $150 price tag for one of those, $3 and some elbow grease doesn't seem half bad.
And, more importantly, it was pretty fun to figure out!

I'm not done with this project just yet: I hope to find some more useful shortcuts to map, as well as integrating into my homelab/self hosting.
Once I get Home Assistant setup, for instance, it would be fun to hook up buttons to some automations.
Of course, I'll update the Gist as I go.

Got any suggestions, questions, or thoughts? What would you map these buttons to? Let me know! Otherwise, support open source projects, and be nice to each other out there!
