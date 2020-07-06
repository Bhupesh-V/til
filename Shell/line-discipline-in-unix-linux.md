# Line Discipline in Unix/Linux Machines

Line discipline handles things like <kbd>backspace</kbd> and also generates various signals for special characters like <kbd>Ctrl + C/Z</kbd> etc.

`stty -a` will display all these settings.
To know more do `man ssty`.

## Demo

Other than <kbd>Ctrl+c</kbd> and <kbd>Ctrl+z</kbd> which you already know about. Here are some other tricks.

Fire up your terminal. And start typing....

<table>
	<tr>
		<th>
			<td>Keyboard Shortcut</td>
			<td>Description</td>
		</th>
	</tr>
	<tr>
	<td><kbd>Ctrl + ?</kbd></td>
		<td>Delete the last input character, Basically Backspace (See what I am talking about, ^? can be used in terminals which may not support the backspace key</td>
	</tr>
	<tr>
		<td><kbd>Ctrl + q</kbd></td>
		<td>Erase line, works like carriage return <code>/r</code></td>
	</tr>
	<tr>
		<td><kbd>Ctrl + a</kbd></td>
		<td>Moves cursor to beginning of line</td>
	</tr>
	<tr>
		<td><kbd>Ctrl + e</kbd></td>
		<td>Moves cursor to end of line</td>
	</tr>
	<tr>
		<td><kbd>Ctrl + w</kbd></td>
		<td>Delete the last input "word"</td>
	</tr>
	<tr>
		<td><kbd>Ctrl+k</kbd></td>
		<td>Erase line to the end, from current cursor position</td>
	</tr>
	<tr>
		<td><kbd>Ctrl + y</kbd></td>
		<td>Paste the last erased text</td>
	</tr>
</table>

Apart from these line input specific kwyboard shortcuts. We also have

#### Multiline Input

Use / for continuing the multiline input.

```bash
bhupesh@dev: hello my name\
is\
bhupesh\
check\
> my boi\
> hoooo\
> 
```

A better version

```bash
#!/bin/bash

echo -e "Enter Commit Message (Ctrl+d to stop) : "
commit_message=$(</dev/stdin)

echo -e "\n\n$commit_message"
```

Make it executable and run.

```bash
Enter Commit Message (Ctrl+d to stop) : 
- fixed bug #454
- Increase reponse time
- style fixes


- fixed bug #454
- Increase reponse time
- style fixes

```

All of this is controlled by the `tty` driver

## Resources

- [The TTY demystified](https://www.linusakesson.net/programming/tty/index.php)
