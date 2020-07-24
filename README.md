
<h1 align="center">Today I Learned</h1>
<p align="center">
  <img height="200px" src="https://repository-images.githubusercontent.com/192476462/fdd6ce80-0b94-11ea-8b50-812ee66b0599" />
  <br>
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2FBhupesh-V%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/bhupesh-V/TIL?color=purple">
  <a href="https://github.com/Bhupesh-V/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Bhupesh-V/til" target="_blank" />
  </a>
  <a href="https://bhupesh.codes/til/">
    <img alt="Website Status" src="https://img.shields.io/website?down_color=red&down_message=offline&up_color=orange&up_message=online&url=https%3A%2F%2Fbhupesh.codes%2Ftil%2F" />
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> Today I Learned.
A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.




## Categories
* [CleanCode](#cleancode) [**`3`**]
* [Go](#go) [**`7`**]
* [Miscellaneous](#miscellaneous) [**`10`**]
* [Python](#python) [**`8`**]
* [Shell](#shell) [**`8`**]
* [WebDev](#webdev) [**`4`**]

---




### CleanCode

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-naming.md">Naming Variables & Functions</a><details><summary> Read More 🔽</summary>

# Naming Variables & Functions
<!--24 Jun 2019 -->
1. The name of a variable, function, or class should answer all the big questions.
   It should tell you why it exists, what it does, and how it is used.
2. Classes & Objects should have *noun* or noun phrase names like *Student*,*Account* etc.
   A class name should not be a *verb*.
3. Methods should have verb or verb phrase names like *getCategories()*, *saveTutorial()*.

---
_PS : I have been reading [CleanCode](https://www.oreilly.com/library/view/clean-code/9780136083238/) for a while & logging what I learn here._
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/CleanCode/write-clean-comments.md">Writing Comments</a><details><summary> Read More 🔽</summary>

# Writing Comments
<!--24 Jun 2019 -->
1. The proper use of comments is to compensate for our _failure to express
   ourself in code_.
2. Inaccurate comments are far worse than no comments at all.
3. Comments do not make up for the bad code.
   i.e if you find yourself writing comments for a code that is complex to understand.
   *MAKE IT LESS COMPLEX*.
4. Short functions don't need much description. A well-chosen name for a small function
   that does one thing is usually better than a comment header.
5. For example. In this code the comments are not needed bcoz the fucntion name describes what it is doing.
   
```python
def get_category_list():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs. '''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and '.git' not in x]
    return dirs
```
   
### Summary
Until now I thought writing comments is a good practice & we should write comments wherever possible.
But know reading it is an eye opener & shocking 😱. I will try to avoid comments now.

---
_PS : I have been reading [CleanCode](https://www.oreilly.com/library/view/clean-code/9780136083238/) for a while & logging what I learn here._

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-writing-functions.md">Writing Functions</a><details><summary> Read More 🔽</summary>

# Writing Functions
<!-- 24 Jun 2019 -->
Got to learn some new points regarding functions() in CleanCode.

1. Functions should be small.
2. They should do one thing only.
   > FUNCTIONS SHOULD DO ONE THING. THEY SHOULD DO IT WELL.
     THEY SHOULD DO IT ONLY.
3. To know if a function is doing more than "one thing" see if you can extract another
   funtion from it with a name that is not merely a restatement of its implementation.
4. Function arguments should *NEVER* be greater than 3.
5. We should never ignore any part of code.The parts we ignore are where the bugs will hide.

---
_PS : I have been reading [CleanCode](https://www.oreilly.com/library/view/clean-code/9780136083238/) for a while & logging what I learn here._

</details></li>
</ul>




### Go

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/clear-terminal-screen-in-go.md">Clearing terminal screen in Go</a><details><summary> Read More 🔽</summary>

# Clearing terminal screen in Go
<!-- 5 June 2020 -->
There are two ways I like (without any external dependency)

### Using `os/exec` package

I have added some boilerplate code to make sure you see whats happening. I think this is probably the best way to do this.

```golang
package main
 
import (
    "os"
    "fmt"
    "os/exec"
    "time"
)
 
func main() {
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")

	fmt.Println("Clearing Screen in 2s...")

	// sleep for 2 seconds
	duration, _ := time.ParseDuration("2s")
	time.Sleep(duration)
    
    c := exec.Command("clear")
    c.Stdout = os.Stdout
    c.Run()
}
```

### Using ANSI Escape Sequences

Not a good way but may come in handy for some situations.

```golang

package main
 
import (
    "fmt"
    "time"
)
 
func main() {
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")

	fmt.Println("Clearing Screen in 1s...")
	dur, _ := time.ParseDuration("1s")
	time.Sleep(dur)

    fmt.Print("\033[2J")
}
```

> The sequence `\033[2J` is read as _Esc[2J_ where *"2j"* clears the screen and moves the cursor to the home position (line 0, column 0).
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/string-to-int-and-vice-versa.md">Convert `string` to `int` and vice-versa in Go</a><details><summary> Read More 🔽</summary>

# Convert `string` to `int` and vice-versa in Go
<!-- 31 May 2020 -->
There are basically 2-3 methods to convert integer to string and back to integer but the most easiest way is to use the `Itoa` and `Atoi` methods in the `strconv` package.


## Demo

```golang
package main

import (
    "fmt"
    "strconv"
)

func main() {
	// String to Int
	nice, _ := strconv.Atoi("69")
	fmt.Printf("%T", nice)

	//Integer to String
	high := strconv.Itoa(420)
	fmt.Printf("\n%T", high)
}
```

`Atoi` returns a second value (`err` ignored in this example for easier understanding)

The above code should output:
```
int
string
```
See [online](https://play.golang.org/p/moTZJ5LYEz9) demo

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/python-next-alternative-go-clousers.md">Creating Python's `next()` alternative using Go Closures</a><details><summary> Read More 🔽</summary>

# Creating Python's `next()` alternative using Go Closures
<!-- 4 June 2020 -->
If you don't know what next() in python means, the below code illustrates it.

```python

MCU_Movies = iter(["Iron Man", "Thor", "Captain America: The first Avenger"])
x = next(MCU_Movies)
print(x, end="\n")
x = next(MCU_Movies)
print(x, end="\n")
x = next(MCU_Movies)
print(x)

```

So if you had guess this would print

```bash
Iron Man
Thor
Captain America: The first Avenger
```

> The `next()` function is used to get the next item in an iterator.

Go doesn't have a next method (nor the concept of iterators actually) so we will try to achieve something similar using [Closures](https://tour.golang.org/moretypes/25).


- A closure is implemented through a anonymous(_function with no name_) function, basically closure is an instance of function.
- In Go functions are first class citizens, meaning we can do all sort of things with them, assign them to a variable, pass as an argument to another function.

Below is a naive implementation of how this could look in Go. Ping me if you have a better way to do this ;)

```golang

package main

import "fmt"

/*
nextIterator returns another function, which we define anonymously in the body of nextIterator.
The returned function closes over the variable index to form a closure.
*/
func nextIterator(array []int) func() int {
    index := -1

    return func() int{
        index++
        return array[index]
    }
}
func main() {

	// an integer array
    var prices = []int{7, 1, 5}

    // create an instance of the anonymous function. i.e, a closue
    next := nextIterator(prices)

    // call the closure
    fmt.Println(next())
    fmt.Println(next())
    fmt.Println(next())

}
```

See this demo on [Go Playground](https://play.golang.org/p/8nH6t0HfnGu).
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/measure-execution-time-in-go.md">Measure Exection time in Go</a><details><summary> Read More 🔽</summary>

# Measure Exection time in Go
<!-- 2 June 2020 -->
To know who how long your go code executes you can use the `time.Now()` and `time.Since()` methods in the `time` package.

## Demo

```golang

package main

import (
	"fmt"
	"time"
)

func main(){

	start := time.Now()
	dur, _ := time.ParseDuration("15ms")

	// A Go Anonymous function (self-executing)
	func (){
		for i := 0; i < 100; i++ {
			time.Sleep(dur)
			fmt.Println("Bhupesh is programming in Go")
		}
	}()

	elapsed := time.Since(start)

	fmt.Printf("Execution Time : %s", elapsed)
}

```

Since() returns the time elapsed since t (`start` in our demo). It is shorthand for `time.Now().Sub(t)`.

Here is the output of the above code
You can also play with the [online](https://play.golang.org/p/YgiaYf_Wetq) demo


```
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Execution Time : 750ms
```

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/reading-and-setting-environment-variables-in-go.md">Reading & Setting Environment variables in Go</a><details><summary> Read More 🔽</summary>

# Reading & Setting Environment variables in Go
<!-- 9 June 2020 -->
Use `os.Getenv()` and `os.Setenv()` for reading and setting environment variables.

## Demo

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")

	fmt.Printf("My Desktop Environment : %s.\n", os.Getenv("XDG_CURRENT_DESKTOP"))
}
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/split-strings-in-go.md">Splitting strings in Go</a><details><summary> Read More 🔽</summary>

# Splitting strings in Go
<!-- 31 May 2020 -->
Splitting strings in Go is done by using the `Split()` method.
You need to import the `strings` standard library to use this.

## Demo

```golang
package main 

import (
	"fmt"
	"strings"
)

func main(){
	var date string = "1999-03-12"
	date_array = strings.Split(date, "-")

	fmt.Println(date_array)
}
```

The `split()` return a Go Array, running this program should print the following:
```
[1999 03 12]
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Go/where-are-my-build-files-when-i-use-go-run.md">Where are my build files when I use `go run`</a><details><summary> Read More 🔽</summary>

# Where are my build files when I use `go run`
<!-- 9 June 2020 -->
By default, 'go run' runs the compiled binary directly.
The binaries are stored in a `temp` work folder, to see where they are stored use the `-work` flag.


## Demo

```bash
go run --work fizzbuzz.go
```

Sample Output

```
WORK=/tmp/go-build645222420
[1 2 Fizz]
```

When you run this go will not delete the temporary build when exiting.
The default directory may vary with your system & `GOPATH`.
</details></li>
</ul>




### Miscellaneous

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/deploy-to-heroku.md">Deploying to Heroku</a><details><summary> Read More 🔽</summary>

# Deploying to Heroku
<!--15 Oct 2019 -->
## List of steps to follow when you are deployihg a **new** repository/project (Python).

1. `heroku login`
2. `touch Procfile`
Create Procfile for deployment. For a Django Web-App the contents of Procfile would be.
```
gunicorn djangoherokuapp.wsgi --log-file -
```
3. `touch runtime.txt`
Specify your Python version here. For example
```
python-3.6.8
```
4. `heroku create herokuAPPName`
Before running this, Make sure to add `appname.herokuapp.com` in ALLOWED_HOSTS and your `requirements.txt` is updated.


## List of commands to run when you are deployihg a **cloned** repository.

1. `heroku login`
Login with your e-mail and password.
2. `heroku git:remote -a <app-name>`
Where `app-name` is the name of app on heroku.
3. `git push heroku master`
Push new changes to heroku.
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/internet-search-tricks-tips-for-developers.md">Internet search tips & tricks for developers</a><details><summary> Read More 🔽</summary>

# Internet search tips & tricks for developers
<!-- 7 June 2020 -->
All of the below mentioned tips works in both DuckDuckGo & Google (i use both :wink:), it should work fine in other search engines too.

1. **`filetype:pdf golang`**

> Use it to search for books or specific file types

2. **`inurl:docs.djangoproject.com templates`**

> Use it to look for occurence of some phrases in the URL of the website mentioned.
`inurl` [docs.djangoproject.com](docs.djangoproject.com) look for `templates` phrase.

3. **`site:github.com synatx error`**

> Limit search results to a specific site, good for looking for bug fixes.

4. **`"how to add pagination in django"`**

> Double quotes can be used for exact matches of the phrase (doesn't work sometimes).

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/kill-open-ports-linux.md">Killing Open Ports in Linux</a><details><summary> Read More 🔽</summary>

# Killing Open Ports in Linux
<!--27 Jan 27 2020 -->
I had this weird error while running Django Development Server.

```
System check identified no issues (0 silenced).
January 27, 2020 - 16:42:39
Django version 2.2.9, using settings 'codeclassroom.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Error: That port is already in use.
```

## Solution
1. Run `netstat -ntlp` to see available open ports.
```
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:42405         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:5940          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      12054/python3       
tcp6       0      0 ::1:631                 :::*                    LISTEN      -  
```

Here is a `man netstat` for what it does
> netstat  -  Print  network connections, routing tables, interface statistics,
       masquerade connections, and multicast memberships

You see the _python3_ one? Kill 😈 this process

2. Run `kill -9 12054`
Kill is used for Removing a background process or job, `-9` specifies SIGKILL (Forced termination) where `12054` is the PID

3. Run the development server again.

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/my-vim-cheatsheet.md">My vim cheatsheet</a><details><summary> Read More 🔽</summary>

# My vim cheatsheet
<!-- 14 June, 2020 -->
I have started transitioning slowly to lightweight editors, because of my low system configuration.
And what can better than `vim`, so I will start logging interesting things I learn here.

For starters I use **neovim**.
(PS: I will write this TIL through vim only :)

### How to install plugins
1. Open up the `~/.config/nvim/init.vim` file add the plugin.

My init file
```
call plug#begin()
Plug 'roxma/nvim-completion-manager'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'gilgigilgil/anderson.vim'
call plug#end()

vnoremap <C-c> "+y
map <C-v> "+p
nmap <F6> :NERDTreeToggle<CR>

colorscheme anderson

set nu
set ai
```

2. Open nvim, use `:PlugInstall` to install the new plugins.

### Some nvim specifc shortcuts

- <kbd>E</kbd> - to go back the directory after opening a file.
- </kbd>:NERDTree</kbd> - to start the Tree like menu.
- When in NERDTree use </kbd>m</kbd> for creating a file.

### Vim Commands

1. `:i` : to come in Insert/Editing Mode.
2. <kbd>Esc</kbd> : for command mode. 
3. `:V` : to enable visual mode, use <kbd>shift</kbd> and arrow keys to select text.
4. `:"+y` : for yanking(copying) text from vim to system's clipboard (tested on Ubuntu 18, might not work on other systems. Search according to your system).
5. `:nohlsearch` : for clearing search highlighting.
6. `:set nu` : to enable Line numbers(left margin).
7. `:"+p` : to paste from system's clipboard (I have added key bindings for copy/paste in my nvim config file).
8. `:u` : Undo latest changes in vim.
9. <kbd>Ctrl + ws</kbd> : Split Windows horizontally.
10. <kbd>Ctrl + wv</kbd> : Split Windows vertically.
11. <kbd>Ctrl + ww</kbd> : Switch between Windows.
12. <kbd>Ctrl + wq</kbd> : Quit Window.
13. `:earlier N` : Time travel in past N seconds.
14. `:later N` : Time tavel in future N seconds.
15. `:echo $MYVIMRC`: to view location of your default `.vimrc` file.
16. Use `==` in Visual Mode to fix line indent.
---
I will only add stuff here when I start using it or use it for the first time.


</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/record-your-desktop-using-ffmpeg-on-linux.md">Record your Desktop using `ffmpeg`</a><details><summary> Read More 🔽</summary>

# Record your Desktop using `ffmpeg`
<!--24 June 2020 -->
1. Make sure you have ffmpeg installed, by checking `ffmpeg -version`. If not install use `sudo apt-get install ffmpeg`.

2. Run the following command.
```bash
ffmpeg -video_size 1280x1024 -framerate 25 -f x11grab -i :0.0+0,0 -c:v libx264rgb -crf 0 -preset ultrafast output.mkv
```
- `-video_size` specifies the size of the recorded area. If you have a different screen size, use that instead of 1920x1080. If you want to record only an area of the screen, specify the area size here.

- `-framerate` specifies the frame rate, i. e. how many frames of video are recorded in a second. The lowest allowed framerate is 20.

- `-f x11grab` is what actually tells FFmpeg to record your screen. You shouldn't change that.

- `-i :0.0+0,0` is where you specify the x and y offset of the top left corner of the area that you want to record. For example, use :0.0+100,200 to have an x offset of 100 and an y offset of 200.

- `-c:v libx264rgb -crf 0 -preset ultrafast` are encoding options. These specify a fast and lossless recording.

> Run `xdpyinfo | grep 'dimensions:'` to know your monitor dimensions

## Resources
- [Record-Your-Desktop-Using-FFmpeg-on-Ubuntu-Linux](https://www.wikihow.com/Record-Your-Desktop-Using-FFmpeg-on-Ubuntu-Linux)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/making-releases-github-gittag.md">Releases on GitHub</a><details><summary> Read More 🔽</summary>

# Releases on GitHub
<!-- 2 Jul 2019 -->
Git tagging is generally used to release software on github.
Here are some basic git commands for tagging.

- To tag specific points of your repo. Run this when you commit something.
  ```shell
  git tag -a v1.4 -m "my version 1.4"
  ```

- To lists all the tags of your repo.
  ```bash
  git tag
  ```

- To tag specific commits.
  ```bash
  git tag -a v1.4 9fceb02
  ```

- To push tags on GitHub.
  ```bash
  git push origin v1.4
  ```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/seo-tools.md">SEO Tools</a><details><summary> Read More 🔽</summary>

# SEO Tools
<!--15 Oct 2019 -->
Here is a list of some tools to test your website for SEO and Social Media.

- [Facebook's Sharing Debugger](https://developers.facebook.com/tools/debug/sharing/).
- [Twitter Card Validator](https://cards-dev.twitter.com/validator).
- [Google's Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool/u/0/).
- [web.dev](https://web.dev/)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/semantic-versioning.md">Semantic Versioning</a><details><summary> Read More 🔽</summary>

# Semantic Versioning
<!-- 24 Jul 2019 -->
- Describes how softwares are assigned version numbers.
- We generally see 3 parts in a version number, `x.y.z` (MAJOR, MINOR, PATCH)
	1. `x` represents MAJOR part - meant for describing any major backend code changes, support of APIs etc.
	2. `y` represents MINOR part - meant for describing very small changes.
	3. `z` represents PATCH part - meant for describing bug fixes.


### Resources
- [Semantic Versioning 2.0.0](https://semver.org/)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/creating-procfile-in-heroku.md">What's a Procfile 👀</a><details><summary> Read More 🔽</summary>

# What's a Procfile 👀
<!--1 Jul 2019 -->
I recently deployed a Python application on Heroku, there I encountered a `Procfile`.
This is what I got to know :

- The Procfile is a simple text file that is named `Procfile` without a file extension. For example, `Procfile.txt` is not a valid Procfile.
- It specifies the commands that are executed by the app on startup. For e.g A Django server.
- Example: If you want to run a python script on Heroku, your *Procfile* content should be
   `worker: python script.py`

### Resources
- [The Procfile](https://devcenter.heroku.com/articles/procfile)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/write-clean-commits-template.md">Writing Cleaner Commits - Template</a><details><summary> Read More 🔽</summary>

# Writing Cleaner Commits - Template
<!--20 Nov 2019 -->
Writing cleaner commits is hard, so I use this template which makes me a pro 😅

```text
# If applied, this commit will...
# [Add/Fix/Remove/Update/Refactor/Document] [issue #id] [summary]


# Why is it necessary? (Bug fix, feature, improvements?)
-
# How does the change address the issue? 
-
# What side effects does this change have?
-

```

##### OR

```text
# If applied, this commit will...
# [Add/Fix/Remove/Update/Refactor/Document]

# Reference any issue number here
- This fixes #454
# Why is it necessary? (Bug fix, feature, improvements?)
-
# How does the change address the issue? 
-
```

## How ?
You have to configure Git to use the above template file (for example, `.gitmessage` in your home directory), then create the template file by running.

```bash
git config --global commit.template ~/.gitmessage
subl ~/.gitmessage
```

This will invoke sublime with the template (use `code` if you use VSCode) Now copy paste the above template, hit save and your are done.

Now when commiting changes instead of using `git commit -m ""`, Use `git commit` this will invoke the commit template which you already set.


### Resources

- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Git commit practices your future self will thank you for](https://victoria.dev/blog/git-commit-practices-your-future-self-will-thank-you-for/)
</details></li>
</ul>




### Python

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/cryptographically-strong-random-string.md">Cryptographically strong random string</a><details><summary> Read More 🔽</summary>

# Cryptographically strong random string

One liner

```bash
python3 -c "import secrets;print(secrets.token_urlsafe())"
```

Sample Runs

```bash
>>> import secrets
>>> secrets.token_urlsafe()
'noLCpWgg5bJbALwlqAKKWUcb4nZg0LvxIUFHyhyei-I'
>>> secrets.token_urlsafe()
'8HhV5FMm2vxfrSoO9o_v65FRy6bLbvc89POSX0fnMqk'
>>> secrets.token_urlsafe()
'bClPydJqA7_0GsDvUAqqShUH5ZucWzdErg0tZIGZU2k'
>>> secrets.token_urlsafe()
'82LSHzCKkwo5y__3NZrck27ZbDL1WiKoSYxQQki8uvA'
>>> 
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/difference-class-and-function-based-views-djnago.md">Difference b/w Class & Function Based Views in Django</a><details><summary> Read More 🔽</summary>

# Difference b/w Class & Function Based Views in Django
<!--21 jul 2020 -->
<table>
	<tr>
		<th>Function Based Views</th>
		<th>Class Based Views</th>
	</tr>
	<tr>
		<td>
		<ol>
			<li>More setup</li>
			<li>Less Abstraction</li>
			<li>Requires error checking</li>
			<li>Less modular</li>
		</ol>
		</td>
		<td>
		<ol>
			<li>Little setup</li>
			<li>More "magic" abstraction</li>
			<li>Error handling built-in (generics)</li>
			<li>Much more modular</li>
			<li>Sane and stable generic API</li>
		</ol>
		</td>
	</tr>
</table>

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/faster-python-tips-and-tricks.md">Fastest Python First: Tips and Tricks 🏃</a><details><summary> Read More 🔽</summary>

# Fastest Python First: Tips and Tricks 🏃
<!--27 Jun 2019 -->
Here are some tips that I learned to make Python Programs faster (_WIP_).

1. Always compile regular expression, if you have to match patterns a lot of times.

```python
import re

pattern = re.compile(some_regular_expression)
some_text = re.sub(pattern, '', data)

```

2. Use List comprehension for iterating over a list.

```python
import time

itemlist = [23, 45, 56, 67, 1, 100, 340, 90]
""" Normal Iteration """
start_time = time.time()
for item in itemlist:
	if item % 2 == 0:
		print(item)
end_time = time.time()

print("Without List Comprehension : " + str(end_time - start_time))

""" List Comprehension """
start_time = time.time()
[print(item) for item in itemlist if item % 2 == 0]
end_time = time.time()

print("With List Comprehension : " + str(end_time - start_time))
```

Output : 
```bash
56
100
340
90
Without List Comprehension : 0.0002067089080810547
56
100
340
90
With List Comprehension : 0.00019121170043945312
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/functional-programming-in-python.md">Functional Programming in Python 🐍</a><details><summary> Read More 🔽</summary>

# Functional Programming in Python 🐍
<!--3 Jul 2019 -->
Features like `lambda`, `map`, `filter`, `reduce` are generally used to perform functional programming related tasks in Python.
Let's take a quick look on them.

### Lambdas
- Anonymous functions
- No function name, 
- They can be passed as function arguments/objects.
- No `return` statment, evaluated exrpession is returned automatically.
- Single line function.

Example : 

```python
double = lambda x: x*x
print(double(34))

elementList = [34, 56, 78, 90, 0, 12]
doubleList = lambda elementList: [e*e for e in elementList]
print(doubleList(elementList))
```

### Map
- applies a function to all the items in an input list.
- `map(function_to_apply, list_of_inputs)`.

Example :

```python
myList = ["bhupesh", "varshney", "is", "a", "developer"]

capitalize = list(map(lambda x: x.upper(), myList))
print(capitalize)
```

### Filter
- creates a list of elements for which a function returns `True`.

Example :

```python
mylist = [23, 45, 6, 8, 10, 16]
evenList = list(filter(lambda x: x%2 == 0, mylist))
print(evenList)
```

### Reduce
- accepts a function and a sequence(list/set *etc*) and returns a single value calculated.
- Initially, the function is called with the first two items from the sequence and the result is returned.
- The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.

Example :

```python
from functools import reduce

li = [5, 8, 10, 20, 50, 100]

sum = reduce((lambda x, y: x + y), li) 
print(sum)
```

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/pep8.md">PEP8 - the fashion 💃 police of Python</a><details><summary> Read More 🔽</summary>

# PEP8 - the fashion 💃 police of Python
<!--22 Jun 2019 -->
Well basically PEP8 is a style guide which provides guidelines and best practices
for writing python code.

### How I learn?
Well bascially the official Python docs for [PEP8](https://www.python.org/dev/peps/pep-0008/) seems good but I use [pep8.org](https://pep8.org/).
It provides much more cleaner interface.

### Summary
Below is a summary which includes some go-to rules you can memorize.

1. Use 4 spaces per indentation level.
2. Spaces are preferred instead of tabs (Why ?? :disappointed_relieved:)
   Python disallows mixing of Tabs & Spaces (Syntax Errors).
   So be consistent with what you choose, I prefer tabs :wink:
3. Limit all lines to a maximum of 79 characters. Use \ to break/continue line.
4. Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names. These are misunderstood with numerals one and zero in some font styles.
5. Function Names - lowercase words separated by _ .
6. Class Names - Start each word with a capital letter. Use CamelCase E.g StudentClass

### Tools 
If use Sublime Text, you can install [Python PEP8 Autoformat](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat) - it does the job for you.
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/publishing-a-package-on-pypi.md">Publishing a Package on PyPI</a><details><summary> Read More 🔽</summary>

# Publishing a Package on PyPI
<!-- 31 Oct 2019 -->
I just published my first package on pypi 😍
I used the following steps to do it :

1. Put your python files/classes inside the folder `package-name`.Also make sure your main class file has the same name `package-name`.

2. Add the `__init__.py` file in the same folder. Use the init file like this.
```python
from coderunner.coderunner import Run
```

3. Now make a file `setup.py` inside the root of your github folder.
Add the following contents in it:
```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plagcheck",
    version="0.1",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="A Powerful Moss results scrapper",
    keywords='mosspy moss plagiarism cheat',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/PlagCheck",
    project_urls={
        "Documentation": "https://github.com/codeclassroom/PlagCheck/blob/master/docs/docs.md",
        "Source Code": "https://github.com/codeclassroom/PlagCheck",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/PlagCheck/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'mosspy',
        'beautifulsoup4',
        'lxml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

4. Now make a file `setup.cfg`. 
It is used for displaying project description on PyPi.
```txt
[metadata]
description-file = README.md
```

5. Install the followig libraries.
```bash
pip3 install setuptools wheel twine
```

6. Run the following command.
```bash
python3 setup.py sdist bdist_wheel
```

7. Finally upload it to PyPi.
```bash
twine upload dist/*
```
This will prompt for your PyPi username and password.

## Resources
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/specify-dev-dependencies-python-package-setup.md">Specify dev dependencies in setup.py</a><details><summary> Read More 🔽</summary>

# Specify dev dependencies in setup.py
<!--21 jul 2020 -->
```python
# setup.py
...

extras_require = {
    "dev": [
        "pytest>=3.7",
    ],
}
```

Test it locally

```bash
pip install -e .[dev]
```

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/writing-tests-in-python-using-unittest.md">Writing Unit Tests in Python ✅</a><details><summary> Read More 🔽</summary>

# Writing Unit Tests in Python ✅
<!--27 Jun 2019 -->
1. Simple and easy just import the Python 3 built-in library `unittest`.
2. Wrap up tests in a Class.
3. Use assert methods.

```python
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

```

### Resources
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [unittest — Unit testing framework](https://docs.python.org/3.6/library/unittest.html)
</details></li>
</ul>




### Shell

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/alternative -to-ls-linux.md">Alternative to 'ls' commnand</a><details><summary> Read More 🔽</summary>

# Alternative to 'ls' commnand
<!-- 22 July 2020 -->
the bash builtin `echo` can be used to list contents of a directory.

```bash
echo *
```

List all files that start with letter 'i'.

```bash
echo i*
```

## How

The character * serves as a "wild card" for filename expansion in globbing. By itself, it matches every filename in a given directory.

## Resource
- [globbing](https://www.tldp.org/LDP/abs/html/globbingref.html)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/colorize-output-in-terminal-bash.md">Colorize Output in Terminal</a><details><summary> Read More 🔽</summary>

# Colorize Output in Terminal
<!-- 31 Jan 2020 -->
The ANSI escape sequences help adding color to the terminal (Doesn't work on Windows I guess)

Here is the format:

`\033[<ForegroundColorCode>;<BackgroundColorCode>;<Style>mYour Text`

where

`<ForegroundColorCode>`, `<BackgroundColorCode>` & `<Style>` are integer Color Codes.
See [Resources](##Resources) for list of colors.

Example : 
```bash
echo -e "\033[92;1mHello\033[0m"
```
Hello will be bold & green in color

## Resources

- [List of ANSI color escape sequences](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
- [Bash tips: Colors and formatting (ANSI/VT100 Control sequences)](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/copy-one-file-to-multiple-files.md">Copy one file to multiple files in Bash</a><details><summary> Read More 🔽</summary>

# Copy one file to multiple files in Bash
<!--24 Dec 2019 -->
```bash
for f in file{1..10}.py; do cp main.py $f; done
```
> this will create new files file_1.py, file_2.py etc and copy contents of _main.py_ file to all of them.
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/find-files-changed-7-days-ago.md">Find files changed 7 days ago</a><details><summary> Read More 🔽</summary>

# Find files changed 7 days ago

To find last modified file
```bash
find Documents/ -mtime -1
```
where `mtime` means "Last Modification Time"

To find files Accessed (read operation)
```bash
find Documents/ -atime -7
```
where `atime` means "Last Access Time"

**-7** signifies anything changed 7 days or less.
**+7** signifies anything changed atleast 7 days ago.
**7** signifies anything changed exactly 7 days ago.

an alternative version

```bash
find Documents/ -newermt "7 days ago" -ls
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/find-all-python-virtual-environments-in-your-system.md">Finding all Python Virtual Environments in your system</a><details><summary> Read More 🔽</summary>

# Finding all Python Virtual Environments in your system
<!-- 10 June 2020 -->
So if you work with Python all day, you already know about Virtual Environments.
The only problem with me 😅 is that I end up creating a lot of them when using and making my side-projects.
We know that there is a `activate` script that can be used for this purpose.

shut up & give me answer

Ok

## Using `find`

```bash
find /home -name "*activate"
```

This will list out all activate scripts in your home directory (should work fine).
Only problem, it is slow.

**Sample Ouput**

```
/home/bhupesh/Desktop/testFind/bin/activate
/home/bhupesh/Desktop/bits/bin/activate
/home/bhupesh/Desktop/cc-new/bin/activate
/home/bhupesh/Desktop/test-audio/bin/activate
/home/bhupesh/Desktop/comp-code/bin/activate
/home/bhupesh/Desktop/req-blog/bin/activate
/home/bhupesh/Desktop/py-cli/bin/activate
/home/bhupesh/Desktop/sian-env/bin/activate
/home/bhupesh/Desktop/ques/bin/activate
/home/bhupesh/Documents/api/bin/activate
/home/bhupesh/Documents/defe-venv/bin/activate
/home/bhupesh/Documents/bot-tutorial/bin/activate
/home/bhupesh/Documents/cc/bin/activate
/home/bhupesh/Documents/test-package/bin/activate
/home/bhupesh/Documents/qt-lear/bin/activate
/home/bhupesh/Documents/csv-voil/bin/activate
/home/bhupesh/Documents/bottest/bin/activate
/home/bhupesh/Documents/new-tutorialdb/bin/activate
/home/bhupesh/Documents/cc2/bin/activate
/home/bhupesh/Documents/plag/bin/activate
find /home -name "*activate"  2.57s user 4.14s system 7% cpu 1:31.72 total
```

## Using `locate`

```bash
locate -b '\activate' | grep "/home"
```
Grep your home directory for all activate scripts.

**Sample Output**

```
/home/bhupesh/Desktop/bits/bin/activate
/home/bhupesh/Desktop/cc-new/bin/activate
/home/bhupesh/Desktop/comp-code/bin/activate
/home/bhupesh/Desktop/py-cli/bin/activate
/home/bhupesh/Desktop/ques/bin/activate
/home/bhupesh/Desktop/req-blog/bin/activate
/home/bhupesh/Desktop/sian-env/bin/activate
/home/bhupesh/Desktop/test-audio/bin/activate
/home/bhupesh/Desktop/testFind/bin/activate
/home/bhupesh/Documents/api/bin/activate
/home/bhupesh/Documents/bot-tutorial/bin/activate
/home/bhupesh/Documents/bottest/bin/activate
/home/bhupesh/Documents/cc/bin/activate
/home/bhupesh/Documents/cc2/bin/activate
/home/bhupesh/Documents/csv-voil/bin/activate
/home/bhupesh/Documents/defe-venv/bin/activate
/home/bhupesh/Documents/new-tutorialdb/bin/activate
/home/bhupesh/Documents/plag/bin/activate
/home/bhupesh/Documents/qt-lear/bin/activate
/home/bhupesh/Documents/test-package/bin/activate
locate -b '\activate'  0.45s user 0.02s system 99% cpu 0.476 total
grep --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn,.idea,.tox} "/home"  0.00s user 0.00s system 0% cpu 0.472 total
```


Now you can just do `source <path>`.
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/get-system-info.md">Get System info using Shell Commands</a><details><summary> Read More 🔽</summary>

# Get System info using Shell Commands
<!-- 19 July 2020 -->

### Memory Used/Total

```shell
free -h | awk '/^Mem:/ {print $3 "/" $2}'
```

### Show CPU temperature

```shell
sensors | awk '/^Core*/ {print $1$2, $3}'
```

### Most Memory Intensive processes

```shell
ps axch -o cmd:15,%mem --sort=-%mem | head
```

### Most CPU Intensive processes

```shell
ps axch -o cmd:15,%cpu --sort=-%cpu | head
```

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/total-memory-using-vmstat.md">Get Total System Memory using `vmstat` command</a><details><summary> Read More 🔽</summary>

# Get Total System Memory using `vmstat` command
<!-- 31 May 2020 -->
```bash
vmstat -s | grep "total memory" | grep -Eo '[0-9]{1,}'
```

This will print the total memory (your RAM) in highlighted text.

The command `vmstat -s` is usually used to print memory statistics a sample output might look like

```bash
   1882140 K total memory
    644068 K used memory
    861172 K active memory
    653200 K inactive memory
    217160 K free memory
     55140 K buffer memory
    965772 K swap cache
   2097148 K total swap
    230400 K used swap
   1866748 K free swap
    169316 non-nice user cpu ticks
      4939 nice user cpu ticks
     37944 system cpu ticks
    666678 idle cpu ticks
     53315 IO-wait cpu ticks
         0 IRQ cpu ticks
       693 softirq cpu ticks
         0 stolen cpu ticks
   2554778 pages paged in
   1429680 pages paged out
     40722 pages swapped in
    191481 pages swapped out
   3487312 interrupts
  10042547 CPU context switches
1590932382 boot time
      9975 forks
```

</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/line-discipline-in-unix-linux.md">Line Discipline in Unix/Linux Machines</a><details><summary> Read More 🔽</summary>

# Line Discipline in Unix/Linux Machines

Line discipline handles things like <kbd>backspace</kbd> and also generates various signals for special characters like <kbd>Ctrl + C/Z</kbd> etc.

`stty -a` will display all these settings.
To know more do `man ssty`.

## Demo

Other than <kbd>Ctrl</kbd>+<kbd>c</kbd> and <kbd>Ctrl</kbd>+<kbd>z</kbd> which you already know about. Here are some other tricks.

Fire up your terminal. And start typing....

<table>
	<tr>
		<th>Keyboard Shortcut</th>
		<th>Description</th>
	</tr>
	<tr>
	<td><kbd>Ctrl</kbd>+<kbd>?</kbd></td>
		<td>Delete the last input character, Basically Backspace (See what I am talking about, ^? can be used in terminals which may not support the backspace key</td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>q</kbd></td>
		<td>Erase line, works like carriage return <code>/r</code></td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>a</kbd></td>
		<td>Moves cursor to beginning of line</td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>e</kbd></td>
		<td>Moves cursor to end of line</td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>w</kbd></td>
		<td>Delete the last input "word"</td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>k</kbd></td>
		<td>Erase line to the end, from current cursor position</td>
	</tr>
	<tr>
		<td><kbd>Ctrl</kbd>+<kbd>y</kbd></td>
		<td>Paste the last erased text</td>
	</tr>
</table>

Apart from these line input specific keyboard shortcuts. We also have ...

#### Multiline Input

Use `/` for continuing the multiline input.

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

</details></li>
</ul>




### WebDev

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/WebDev/html-datalist-auto-complete.md">Auto-complete in plain HTML</a><details><summary> Read More 🔽</summary>

# Auto-complete in plain HTML
<!--21 Dec 2019 -->
You can make a type-ahead/autocomplete like thing in plain HTML
using the `<datalist></datalist>` tag.

## Usage
```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<h1>Type Ahead HTML</h1>
<input list="test" placeholder="Choose an option">
<datalist id="test">
	<option value="C++">
	<option value="Python">
	<option value="Go">
	<option value="JavaScript">
	<option value="HTML">
</datalist>
</body>
</html>
```

Now as you type `G` it will show _Go_ ;)

### Resources
- [tweet by Álvaro Trigo](https://twitter.com/IMAC2/status/1206913760696373253)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/WebDev/OpenGraph.md">I learned about Open Graph protocol</a><details><summary> Read More 🔽</summary>

# I learned about Open Graph protocol
<!-- 18 Jun 2019 -->
### What it does ?
- [Open Graph](http://ogp.me/) Makes your website into rich "graph" objects.
- Now, what I understand from it is that it provides us to add
  additional metadata to your website which makes it more **rich** on social media.
  For e.g you see the thumbnails of links in the Telegram - *courtesy of OpenGraph*

### How ?
Information is added into the `<head>` tags.
For e.g below is the metadata of one of my [blogs](https://bhupeshv.me/30-Seconds-of-C++/)

```html
<meta property="og:description" content="A collection of C++ STL features (functions/libraries) which can be learned in 30 seconds or less" />
<meta property="og:title" content="30 Seconds of C++" />
<meta property="og:url" content="/30-Seconds-of-C++/" />
<meta property="og:image" content="/images/blog5.png"/>
```

### Sidenotes
Socila Media platforms like Twitter, LinkedIn, Telegram heavily use this meta info to render links, display images etc.
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/WebDev/live-edit-html.md">Live Editing HTML</a><details><summary> Read More 🔽</summary>

# Live Editing HTML
<!-- 6 Nov 2019 -->
Yes !, you can live edit webpages by adding the following in the `<html>` tag.

```html
<!DOCTYPE html>
<html contenteditable>
<head>
	<title>Yay! Live Editing</title>
</head>
<body>
	<p>Try Editing Tis</p>
</body>
</html>
```

Setting `contenteditable="true"` will make its content editable.

So what ?
Well you can use this HTML5 feature to make a motepad right into your browser.

```html
data:text/html, <html contenteditable <head ><title>Notepad</title></head><body style="background-color:black;color: white;"></body></html>
```
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/WebDev/async-defer-html-javascript.md">`async` & `defer` Attributes</a><details><summary> Read More 🔽</summary>

# `async` & `defer` Attributes
<!-- 21 Jul 2019 -->
Usually javascript files interrupt the parsing of HTML document.
To prevent this 2 special attributes of the `<script>` elements are used.


### `async`

```js
<script async src="script.js">
```
- The async attribute is used to indicate to the browser that the script file can be executed asynchronously.
- Therefore the HTML parser does not need to pause and wait for the JS code to load, it is intead fetched in parallel.
- It is only available for externally located script files.


### `defer`

```js
<script defer src="script.js">
```
- The defer attribute tells the browser to only execute the script file once the HTML document has been fully parsed.
- The js file can be downloaded but it does not executes until the whole HTML is parsed.
</details></li>
</ul>

## Usage

See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## Author

👤 **Bhupesh Varshney**

- Web : [bhupesh.codes](https://bhupesh-v.github.io)
- Twitter : [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV : [bhupesh](https://dev.to/bhupesh)


## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>

<a href="https://www.patreon.com/bhupesh">
  <img alt="Patron Bhupesh" src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [MIT](https://github.com/Bhupesh-V/til/blob/master/LICENSE) licensed.

## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
