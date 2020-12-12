
[<img align="right" src="https://user-images.githubusercontent.com/34342551/88784787-12507980-d1ae-11ea-82fe-f55753340168.png" width="240px" height="51x">](https://ko-fi.com/bhupesh)

<h1 align="left">Today I Learned</h1>
<p align="center">
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2FBhupesh-V%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/bhupesh-V/TIL?color=purple">
  <a href="https://github.com/Bhupesh-V/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Bhupesh-V/til" target="_blank" />
  </a>
  <a href="https://bhupesh-v.github.io/til/">
    <img alt="Website Status" src="https://img.shields.io/website?down_color=red&down_message=offline&up_color=orange&up_message=online&url=https%3A%2F%2Fbhupesh-v.github.io%2Ftil%2F" />
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.




## Categories
* [CleanCode](#cleancode) [**`3`**]
* [Go](#go) [**`7`**]
* [Miscellaneous](#miscellaneous) [**`14`**]
* [Python](#python) [**`10`**]
* [Shell](#shell) [**`19`**]
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Naming+Variables+%26+Functions+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FCleanCode%2Fcleancode-naming.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Naming%20Variables%20%26%20Functions&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-naming.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Naming%20Variables%20%26%20Functions&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-naming.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-naming.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Writing+Comments+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FCleanCode%2Fwrite-clean-comments.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Writing%20Comments&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/write-clean-comments.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Writing%20Comments&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/write-clean-comments.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/write-clean-comments.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Writing+Functions+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FCleanCode%2Fcleancode-writing-functions.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Writing%20Functions&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-writing-functions.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Writing%20Functions&url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-writing-functions.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/CleanCode/cleancode-writing-functions.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Clearing+terminal+screen+in+Go+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fclear-terminal-screen-in-go.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Clearing%20terminal%20screen%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/clear-terminal-screen-in-go.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Clearing%20terminal%20screen%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/clear-terminal-screen-in-go.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/clear-terminal-screen-in-go.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Convert+%60string%60+to+%60int%60+and+vice-versa+in+Go+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fstring-to-int-and-vice-versa.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Convert%20%60string%60%20to%20%60int%60%20and%20vice-versa%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/string-to-int-and-vice-versa.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Convert%20%60string%60%20to%20%60int%60%20and%20vice-versa%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/string-to-int-and-vice-versa.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/string-to-int-and-vice-versa.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Creating+Python%27s+%60next%28%29%60+alternative+using+Go+Closures+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fpython-next-alternative-go-clousers.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Creating%20Python%27s%20%60next%28%29%60%20alternative%20using%20Go%20Closures&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/python-next-alternative-go-clousers.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Creating%20Python%27s%20%60next%28%29%60%20alternative%20using%20Go%20Closures&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/python-next-alternative-go-clousers.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/python-next-alternative-go-clousers.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Measure+Exection+time+in+Go+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fmeasure-execution-time-in-go.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Measure%20Exection%20time%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/measure-execution-time-in-go.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Measure%20Exection%20time%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/measure-execution-time-in-go.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/measure-execution-time-in-go.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Reading+%26+Setting+Environment+variables+in+Go+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Freading-and-setting-environment-variables-in-go.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Reading%20%26%20Setting%20Environment%20variables%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/reading-and-setting-environment-variables-in-go.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Reading%20%26%20Setting%20Environment%20variables%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/reading-and-setting-environment-variables-in-go.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/reading-and-setting-environment-variables-in-go.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Splitting+strings+in+Go+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fsplit-strings-in-go.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Splitting%20strings%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/split-strings-in-go.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Splitting%20strings%20in%20Go&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/split-strings-in-go.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/split-strings-in-go.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Where+are+my+build+files+when+I+use+%60go+run%60+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FGo%2Fwhere-are-my-build-files-when-i-use-go-run.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Where%20are%20my%20build%20files%20when%20I%20use%20%60go%20run%60&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/where-are-my-build-files-when-i-use-go-run.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Where%20are%20my%20build%20files%20when%20I%20use%20%60go%20run%60&url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/where-are-my-build-files-when-i-use-go-run.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Go/where-are-my-build-files-when-i-use-go-run.md)
</details></li>
</ul>




### Miscellaneous

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/converting-videos-to-high-quality-gif.md">Converting videos to High quality GIFs</a><details><summary> Read More 🔽</summary>

# Converting videos to High quality GIFs
<!-- Dec 6, 2020 -->

Converting videos to gifs using ffmpeg is a pain in the ass if you don't know what's happening.
GIF size getting 10x the size of original video ? Don't worry, I got you!

1. Always create a custom palette
2. Don't increase/decrease file dimensions
3. Save unnecessary frame conversion by using `-t` to convert video until timestamp.
4. Experiment with `fps` (default value is 24)

```bash
# generate a palette
ffmpeg -i video.mp4 -vf "fps=22,scale=1024:-1:flags=lanczos,palettegen" palette.png
# use the generated palette
ffmpeg -t 29 -i video.mp4 -i palette.png -filter_complex "fps=22,scale=1024:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

### Resources

- [High quality GIF from video](https://d12frosted.io/posts/2018-10-13-gifify.html)


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Converting+videos+to+High+quality+GIFs+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fconverting-videos-to-high-quality-gif.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Converting%20videos%20to%20High%20quality%20GIFs&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/converting-videos-to-high-quality-gif.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Converting%20videos%20to%20High%20quality%20GIFs&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/converting-videos-to-high-quality-gif.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/converting-videos-to-high-quality-gif.md)
</details></li>
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Deploying+to+Heroku+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fdeploy-to-heroku.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Deploying%20to%20Heroku&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/deploy-to-heroku.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Deploying%20to%20Heroku&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/deploy-to-heroku.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/deploy-to-heroku.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/docker-quick-guide.md">Docker 🐋 quick guide</a><details><summary> Read More 🔽</summary>

# Docker 🐋 quick guide
<!-- 18 Oct 2020 -->

1. Remove docker image.
   ```bash
   docker rmi <img-id>
   ```

2. Remove docker container.
   ```bash
   docker rm <container-id>
   ```
3. Build a docker image with a name.
   ```bash
   docker build -f <dockerfile-path> -t name .
   ```

4. Run a container.
   ```bash
   docker run -p 3000:3000 <container-id>
   ```

5. Stop a container.
   ```bash
   docker stop <container-id>
   ```

6. Run a container in detach mode (run in background).
   ```bash
   docker run -d <container-id>
   ```
   > For the love of God always add a `-d` while running a container. Speaking this from experience.

   If you don't run in detach mode, you won't be able to Ctrl+C (or exit), instead use Ctrl+PC (yes the P key and C key).

7. List docker volumes.
   ```bash
   docker volume ls
   ```

8. Remove docker volume.
   ```bash
   docker volume rm <volume-name>
   ```

8. Check port mapping.
   ```bash
   docker port <name>
   ```

9. Starting a docker container
   ```bash
   docker start <container>
   ```

   > The first two letters of CONTAINER_ID can be provided as an argument too.

10. Run a command inside container.
    ```bash
    docker container exec <CONTAINER> ls -la
    ```

11. Check history of an image.
    ```bash
    docker history <IMAGE>
    ```
   

## Docker Compose

1. Build and run containers.
   ```bash
   docker-compose up -d
   ```

2. Stop containers.
   ```bash
   docker-compose stop
   ```

3. Check logs/console messages.
   ```bash
   docker-compose logs <image name>
   ```

4. List all containers.
   ```bash
   docker-compose ps
   ```


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Docker+%F0%9F%90%8B+quick+guide+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fdocker-quick-guide.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Docker%20%F0%9F%90%8B%20quick%20guide&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/docker-quick-guide.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Docker%20%F0%9F%90%8B%20quick%20guide&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/docker-quick-guide.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/docker-quick-guide.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/internet-search-tricks-tips-for-developers.md">Internet search tips & tricks for developers</a><details><summary> Read More 🔽</summary>

# Internet search tips & tricks for developers
<!-- 7 June 2020 -->
All of the below mentioned tips works in both DuckDuckGo & Google (i use both :wink:), it should work fine in other search engines too.

1. **`file:pdf golang`**

> Use it to search for books, presentations or specific file types

2. **`inurl:docs.djangoproject.com templates`**

> Use it to look for occurence of some phrases in the URL of the website mentioned.
`inurl` [docs.djangoproject.com](docs.djangoproject.com) look for `templates` phrase.

3. **`site:github.com synatx error`**

> Limit search results to a specific site, good for looking for bug fixes.

4. **`"how to add pagination in django"`**

> Double quotes can be used for exact matches of the phrase (doesn't work sometimes).

5. **`related:http://freecodecamp.org`**

> Related specifier, "related:<domain>" returns the root domain of similar websites

6. **`intitle:best vim plugins`** 

> Intitle specifier returns results that contains your searched word in the title.

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Internet+search+tips+%26+tricks+for+developers+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Finternet-search-tricks-tips-for-developers.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Internet%20search%20tips%20%26%20tricks%20for%20developers&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/internet-search-tricks-tips-for-developers.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Internet%20search%20tips%20%26%20tricks%20for%20developers&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/internet-search-tricks-tips-for-developers.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/internet-search-tricks-tips-for-developers.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Killing+Open+Ports+in+Linux+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fkill-open-ports-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Killing%20Open%20Ports%20in%20Linux&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/kill-open-ports-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Killing%20Open%20Ports%20in%20Linux&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/kill-open-ports-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/kill-open-ports-linux.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/my-vim-cheatsheet.md">My Vim Cheatsheet</a><details><summary> Read More 🔽</summary>

# My Vim Cheatsheet
<!-- 14 June, 2020 -->

<pre>                         
 _______ _______ _______ 
|\     /|\     /|\     /|
| +---+ | +---+ | +---+ |
| |   | | |   | | |   | |
| |v  | | |i  | | |m  | |
| +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|
                         
</pre>

I have started transitioning slowly to lightweight editors, because of my low system configuration.
And what can be better than `vim`. I will keep a log of things I learn in the process.

> Update: I started using vim "actively" from Nov 12, 2020 and it has now been 1 month complete in Vim & I don't think I am moving to another text editor in future.

For starters I use **neovim** (v0.4.4).

All my Plugins & Colorschemes are listed in my [**dotfiles**](https://github.com/Bhupesh-V/.Varshney#initvim-or-vimrc)

## Super Basic Stuff

> Some must know stuff filtered from the vast array of vim things.

### Editing

- **`i`** insert text before the cursor position
- **`a`** append text after the cursor position (my advice, always use this instead of `i`)
- **`A`** append text at end of line
- **`o`** open a new line after current line
- **`O`** open a new line before current line
- **`x`** delete character under cursor
- **`D`** delete until the end of line
- **`r`** replace the character under cursor
- **`R`** replace stuff until we want
- **`dd`** Delete current line.
- **`cc`** delete current line and switch to insert mode.
- **`C`** delete everything from the cursor position to the EOL.

## Basic Stuff

### Undo/Redo/Repeat

- <kbd>u</kbd> : Undo latest changes in vim.
- <kbd>Ctrl</kbd> + <kbd>r</kbd> : to redo
- <kbd>.</kbd> : repeat last change in vim.

### Cut/Copy/Paste

> I felt like a rookie when I used to search this, anyways here is how you do it:

1. Enable visual mode by pressing `v`.
2. Use arrow keys to select text.
3. Use <kbd>d</kbd> to Cut. OR
4. Use <kbd>y</kbd> to yank (copy) text (only inside vim)
   > `:"+y` : for yanking(copying) text to system's clipboard.
5. Use <kbd>p</kbd> to paste after the cursor position or <kbd>P</kbd> to paste before the cursor.
   > `:"+p` : to paste from system's clipboard

### Search & Replace

1. Move your cursor to the desired word
2. Use `*` to select all its occurrences.
3. Hit <kbd>Esc</kbd> and use **`:%s//<replace-word>/`** to replace all the selected words.
   > `:nohlsearch` : for clearing search highlighting.
   Also read (:h usr_12.txt), section 12.2 for a nice overview on search.

   When in search mode instead of hitting Enter use `Ctrl + g` and `Ctrl + t` to traverse matches while still being in search mode.

## Intermediate Stuff

1. **`:earlier N`** : Time travel in past N seconds.
2. **`:later N`** : Time travel in future N seconds.
3. **`:echo $MYVIMRC`** : to view location of your default `.vimrc` file.
4. Use `==` in Visual Mode to fix line indent.
5. When in command mode (:), use <kbd>Ctrl</kbd> + <kbd>f</kbd> to browse through your command history, live edit any command and hit enter to run it (the quick fix window).
6. Use **`:resize 60`** to resize windows horizontally or **`:vertical resize 60`** for vertical resizing. Also signed values can be used like +5, -2.
7. Use **`:right`**, **`:left`** or **`:center`** to align text. Assuming width of document is `textwidth` (default is 80). You can also specify arguments for e.g `:center 100` will move the start of line to 100th column.
8. To list all your active/inactive buffers, use **`:buffers`** in command mode. You can switch to a buffer by providing the buffer name, `:buffer <TAB>` to see all buffers.
9. Use `:verb map <key>` to check which key is mapped to what operation. Useful when debugging your mappings and differentiating them from that of a plugin.
   > Read help for checking key notations `:h key-notation`
10. Use vim's `wildignore` setting to exclude searching for files and directories according to your project. For e.g for python projects this could look like
    ```vim
    set wildignore+=*/.git/*,*/site-packages/*,*/lib/*,*/bin/*,*.pyc
    ```
    This should exclude searching through your virtual environments [Read manual `:h 'wildignore'`].
    Another handy trick is to exclude media files from appearing in search by excluding them as well.
    ```vim
    set wildignore+=*.jpg,*.bmp,*.gif,*.png,*.jpeg,*.avi,*.mp4,*.mkv,*.pdf,*.odt
    ```
11. `:syntax` will output all highlight groups for syntax highlighting of the current open file. It can come handy when you are writing your own colorscheme.
12. Scrolling 2 or more windows together. When in multiple windows (or splits), you can use `scrollbind`.
    Pick one window then `:set scb`, pick another window `:set scb` for disabling use `:set noscb`
13. To search for pattern in vim help text use `:helpgrep` or `:helpg`
14. If you have spell-checking (`:set spell`) enabled use `zg` to exclude certain words from being reported as misspelled. This adds the words to your own list of words called a _spellfile_. On neovim this fill is created automatically, although you can do it manually.
    ```bash
    mkdir -p ~/.vim/spell/
    ```
    then in `vimrc`
    ```vim
    set spellfile=~/.vim/spell/en.utf-8.add
    ```

### Code Folding

It helps you view only a selected range of text (Read `:h usr_28.txt`) for a quick overview.

Quick settings to put in vimrc

```vim
set foldmethod=indent
set foldcolumn=2
```

**za**: Toggle code folding.
**zR**: Open all folds.
**zM**: Close all folds.
**zo**: Open current fold.
**zc**: Close current fold.


### Navigation

- **w** jump through beginning of words in a line
- **e** jump to end of words in a line
- **b** to move backward
- **H** jump to top of text under screen (not to be confused with top of file).
- **M** jump to middle
- **L** jump to bottom
- **gg** go to top of file
- **GG** go to end of file
- **0** go to beginning of line
- **$** go to end of current line
- **^** go to first character in a line
- **g_** go to last character of the line
- **zb** put current line at bottom of screen
- **zt** put current line at top of screen
- **Ctrl+f** scroll down 1 page
- **Ctrl+b** scroll up 1 page

**Character Wise**

- f : find next
- F : find backward
- t : find next char & place cursor before
- T : find next char & place cursor before backward
- ; : go to the next occurrence of f/t
- , : go to previous occurrence of f/t


### Completions

Use <kbd>Ctrl</kbd> + <kbd>x</kbd> +

1. <kbd>f</kbd>	= File name completion
2. <kbd>l</kbd>	= Whole line completion (context aware, handy if you are copy pasting a previously typed line)
3. <kbd>i</kbd>	= Keywords in current & included file ("include" means when you import or #include)
4. <kbd>s</kbd>	= Spelling suggestions
5. <kbd>k</kbd>	= Keywords from dictionary. For this to work add `set dictionary+=/usr/share/dict/words` to your vimrc

> use `:help ins-completion` to see more such completions


### Registers

Take registers as "special vim storage locations". There are exactly 21 registers which store different kind of stuff, from these 4 registers are read-only.
In command mode use `:di` or `:reg` to display contents of all these registers. Do `h registers` to read the docs

## File Browsing

Vim has a default file browser called netrw, below are some handy tips that will help:

1. **R** : rename a file/directory.
2. **qf** : Show file info.
3. **x** : open file in associated program, use it open media files like images.
4. **Ctrl + l** : refresh netrw, Opens a new buffer. Use `:e .` instead.
5. **d** : Make a new directory.
6. **gh** : toggle display of hidden files.
7. **D** : Delete a file/directory (Doesn't work on non-empty directories).


---
I will only add stuff here when I start using it or use it for the first time.



**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=My+Vim+Cheatsheet+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fmy-vim-cheatsheet.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=My%20Vim%20Cheatsheet&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/my-vim-cheatsheet.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=My%20Vim%20Cheatsheet&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/my-vim-cheatsheet.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/my-vim-cheatsheet.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Record+your+Desktop+using+%60ffmpeg%60+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Frecord-your-desktop-using-ffmpeg-on-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Record%20your%20Desktop%20using%20%60ffmpeg%60&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/record-your-desktop-using-ffmpeg-on-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Record%20your%20Desktop%20using%20%60ffmpeg%60&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/record-your-desktop-using-ffmpeg-on-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/record-your-desktop-using-ffmpeg-on-linux.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Releases+on+GitHub+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fmaking-releases-github-gittag.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Releases%20on%20GitHub&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/making-releases-github-gittag.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Releases%20on%20GitHub&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/making-releases-github-gittag.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/making-releases-github-gittag.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/seo-tools.md">SEO Tools</a><details><summary> Read More 🔽</summary>

# SEO Tools
<!--15 Oct 2019 -->
Here is a list of some tools to test your website for SEO and Social Media.

- [Facebook's Sharing Debugger](https://developers.facebook.com/tools/debug/sharing/).
- [Twitter Card Validator](https://cards-dev.twitter.com/validator).
- [Google's Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool/u/0/).
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
- [web.dev](https://web.dev/)


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=SEO+Tools+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fseo-tools.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=SEO%20Tools&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/seo-tools.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=SEO%20Tools&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/seo-tools.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/seo-tools.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/searching-your-way-through-vim.md">Searching your way through vim</a><details><summary> Read More 🔽</summary>

# Searching your way through vim
<!-- Dec 9, 2020 -->

1. Matching a word "exactly"

`/.*\<hello world\>\&.*\<goodbye world\>/`

2. Searching between 2 words (inclusive)

`\&` allows to match two regular expression parts at the same position. To have both strings match in the same line, you need to allow for an arbitrary number of characters before the matches.
Example : `/.*red\&.*blue/`
Say you want to find how many f-strings are used in your python program the search query for that would be `f"\&.*"`

3. Search between 2 words on different lines.
   `try\_.\{-}except`
   This will highlight everything between try/except block inclusive.

Read `:help pattern.txt` for everything related to searching.


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Searching+your+way+through+vim+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fsearching-your-way-through-vim.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Searching%20your%20way%20through%20vim&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/searching-your-way-through-vim.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Searching%20your%20way%20through%20vim&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/searching-your-way-through-vim.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/searching-your-way-through-vim.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Semantic+Versioning+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fsemantic-versioning.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Semantic%20Versioning&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/semantic-versioning.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Semantic%20Versioning&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/semantic-versioning.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/semantic-versioning.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=What%27s+a+Procfile+%F0%9F%91%80+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fcreating-procfile-in-heroku.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=What%27s%20a%20Procfile%20%F0%9F%91%80&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/creating-procfile-in-heroku.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=What%27s%20a%20Procfile%20%F0%9F%91%80&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/creating-procfile-in-heroku.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/creating-procfile-in-heroku.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Writing+Cleaner+Commits+-+Template+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fwrite-clean-commits-template.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Writing%20Cleaner%20Commits%20-%20Template&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/write-clean-commits-template.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Writing%20Cleaner%20Commits%20-%20Template&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/write-clean-commits-template.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/write-clean-commits-template.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Miscellaneous/writing-cover-letter-tips.md">Writing Cover letter - Tips</a><details><summary> Read More 🔽</summary>

# Writing Cover letter - Tips
<!-- Dec 8, 2020 -->

I am not a hiring expert but I think these tips can help someone stand ahead of the crowd.
This might also help when you are cold-emailing a recruiter.

1. Keep the letter to 2 paragraphs. The 1st para highlighting **WHY** do you want to work there & 2nd para highlighting **HOW** hiring you is going to benefit them.
2. Do research about the company. Go through their social, blogs etc. Yes this is the time to be a stalker on internet
3. Always add a personal touch while explaining why do you want to work with them. This is the time to be as "thoughtful" as you can. 
4. Don't use any copy-paste templates, not worth it. If a company is asking for a cover letter means that they know a _Resume_ has limitations, they want to hear the WHY & HOW of hiring you is going to help them.
5. Explain something exceptional/cool you did.


> This is a progressive post, I will add/delete as I learn. Suggestions welcome


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Writing+Cover+letter+-+Tips+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FMiscellaneous%2Fwriting-cover-letter-tips.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Writing%20Cover%20letter%20-%20Tips&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/writing-cover-letter-tips.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Writing%20Cover%20letter%20-%20Tips&url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/writing-cover-letter-tips.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Miscellaneous/writing-cover-letter-tips.md)
</details></li>
</ul>




### Python

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/check-indentation-errors-in-python.md">Check indentation errors in python 🐍</a><details><summary> Read More 🔽</summary>

# Check indentation errors in python 🐍
<!-- 18 Oct 2020 -->
Use `tabnanny` in python standard library for this.

```bash
python -m tabnanny hack-nasa.py
```


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Check+indentation+errors+in+python+%F0%9F%90%8D+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fcheck-indentation-errors-in-python.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Check%20indentation%20errors%20in%20python%20%F0%9F%90%8D&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/check-indentation-errors-in-python.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Check%20indentation%20errors%20in%20python%20%F0%9F%90%8D&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/check-indentation-errors-in-python.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/check-indentation-errors-in-python.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Python/datetim-eobject-to-string-and-vice-versa.md">Converting 📅⏲ datetime object to string & vice-versa</a><details><summary> Read More 🔽</summary>

# Converting 📅⏲ datetime object to string & vice-versa
<!-- 7 Nov, 2020 -->

Sometimes only the standard lib `datetime` is necessary to do all date/time related tasks. 

> I am logging this here because I always forget how to do this 😶 (I want to end this once and for all)

## `datetime` object to string

```python
>>> from datetime import datetime
>>> d = datetime.now()
>>> d
datetime.datetime(2020, 11, 7, 20, 15, 58, 389341)
>>> d.strftime("%d %b, %Y")
'07 Nov, 2020'
```

## From string to `datetime` object

```python
>>> from datetime import datetime
>>> date_string = "2020-06-20T08:22:54Z"
>>> datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
datetime.datetime(2020, 6, 20, 8, 22, 54)
```

Both `strptime` & `strftime` can ofc be chained.

```python
>>> from datetime import datetime
>>> date_string = "2020-06-20T08:22:54Z"
>>> datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ').strftime("%d %b, %Y")
```

This can be handy when you are getting date/time fields from external resource (like an API) and only want to display a part of it (like days, month etc).

[**Format codes for `strptime` and `strftime`**](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

<table><thead><tr><th>Directive</th><th>Meaning</th><th>Example</th></tr></thead><tbody><tr><td>%a</td><td>Weekday as locale’s abbreviated name.</td><td>Sun, Mon, …, Sat (en_US);<br>So, Mo, …, Sa (de_DE)</td></tr><tr><td>%A</td><td>Weekday as locale’s full name.</td><td>Sunday, Monday, …, Saturday (en_US);<br>Sonntag, Montag, …, Samstag (de_DE)</td></tr><tr><td>%w</td><td>Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.</td><td>0, 1, …, 6</td></tr><tr><td>%d</td><td>Day of the month as a zero-padded decimal number.</td><td>01, 02, …, 31</td></tr><tr><td>%b</td><td>Month as locale’s abbreviated name.</td><td>Jan, Feb, …, Dec (en_US);<br>Jan, Feb, …, Dez (de_DE)</td></tr><tr><td>%B</td><td>Month as locale’s full name.</td><td>January, February, …, December (en_US);<br>Januar, Februar, …, Dezember (de_DE)</td></tr><tr><td>%m</td><td>Month as a zero-padded decimal number.</td><td>01, 02, …, 12</td></tr><tr><td>%y</td><td>Year without century as a zero-padded decimal number.</td><td>00, 01, …, 99</td></tr><tr><td>%Y</td><td>Year with century as a decimal number.</td><td>0001, 0002, …, 2013, 2014, …, 9998, 9999</td></tr><tr><td>%H</td><td>Hour (24-hour clock) as a zero-padded decimal number.</td><td>00, 01, …, 23</td></tr><tr><td>%I</td><td>Hour (12-hour clock) as a zero-padded decimal number.</td><td>01, 02, …, 12</td></tr><tr><td>%p</td><td>Locale’s equivalent of either AM or PM.</td><td>AM, PM (en_US);<br>am, pm (de_DE)</td></tr><tr><td>%M</td><td>Minute as a zero-padded decimal number.</td><td>00, 01, …, 59</td></tr><tr><td>%S</td><td>Second as a zero-padded decimal number.</td><td>00, 01, …, 59</td></tr><tr><td>%f</td><td>Microsecond as a decimal number, zero-padded on the left.</td><td>000000, 000001, …, 999999</td></tr><tr><td>%z</td><td>UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).</td><td>(empty), +0000, -0400, +1030, +063415, -030712.345216</td></tr><tr><td>%Z</td><td>Time zone name (empty string if the object is naive).</td><td>(empty), UTC, GMT</td></tr><tr><td>%j</td><td>Day of the year as a zero-padded decimal number.</td><td>001, 002, …, 366</td></tr><tr><td>%U</td><td>Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.</td><td>00, 01, …, 53</td></tr><tr><td>%W</td><td>Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.</td><td>00, 01, …, 53</td></tr><tr><td>%c</td><td>Locale’s appropriate date and time representation.</td><td>Tue Aug 16 21:30:00 1988 (en_US);<br>Di 16 Aug 21:30:00 1988 (de_DE)</td></tr><tr><td>%x</td><td>Locale’s appropriate date representation.</td><td>08/16/88 (None);<br>08/16/1988 (en_US);<br>16.08.1988 (de_DE)</td></tr><tr><td>%X</td><td>Locale’s appropriate time representation.</td><td>21:30:00 (en_US);<br>21:30:00 (de_DE)</td></tr><tr><td>%%</td><td>A literal '%' character.</td><td>%</td></tr></tbody></table>

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Converting+%F0%9F%93%85%E2%8F%B2+datetime+object+to+string+%26+vice-versa+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fdatetim-eobject-to-string-and-vice-versa.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Converting%20%F0%9F%93%85%E2%8F%B2%20datetime%20object%20to%20string%20%26%20vice-versa&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/datetim-eobject-to-string-and-vice-versa.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Converting%20%F0%9F%93%85%E2%8F%B2%20datetime%20object%20to%20string%20%26%20vice-versa&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/datetim-eobject-to-string-and-vice-versa.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/datetim-eobject-to-string-and-vice-versa.md)
</details></li>
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Cryptographically+strong+random+string+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fcryptographically-strong-random-string.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Cryptographically%20strong%20random%20string&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/cryptographically-strong-random-string.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Cryptographically%20strong%20random%20string&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/cryptographically-strong-random-string.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/cryptographically-strong-random-string.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Difference+b%2Fw+Class+%26+Function+Based+Views+in+Django+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fdifference-class-and-function-based-views-djnago.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Difference%20b/w%20Class%20%26%20Function%20Based%20Views%20in%20Django&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/difference-class-and-function-based-views-djnago.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Difference%20b/w%20Class%20%26%20Function%20Based%20Views%20in%20Django&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/difference-class-and-function-based-views-djnago.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/difference-class-and-function-based-views-djnago.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Fastest+Python+First%3A+Tips+and+Tricks+%F0%9F%8F%83+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Ffaster-python-tips-and-tricks.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Fastest%20Python%20First%3A%20Tips%20and%20Tricks%20%F0%9F%8F%83&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/faster-python-tips-and-tricks.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Fastest%20Python%20First%3A%20Tips%20and%20Tricks%20%F0%9F%8F%83&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/faster-python-tips-and-tricks.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/faster-python-tips-and-tricks.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Functional+Programming+in+Python+%F0%9F%90%8D+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Ffunctional-programming-in-python.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Functional%20Programming%20in%20Python%20%F0%9F%90%8D&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/functional-programming-in-python.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Functional%20Programming%20in%20Python%20%F0%9F%90%8D&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/functional-programming-in-python.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/functional-programming-in-python.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=PEP8+-+the+fashion+%F0%9F%92%83+police+of+Python+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fpep8.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=PEP8%20-%20the%20fashion%20%F0%9F%92%83%20police%20of%20Python&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/pep8.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=PEP8%20-%20the%20fashion%20%F0%9F%92%83%20police%20of%20Python&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/pep8.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/pep8.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Publishing+a+Package+on+PyPI+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fpublishing-a-package-on-pypi.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Publishing%20a%20Package%20on%20PyPI&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/publishing-a-package-on-pypi.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Publishing%20a%20Package%20on%20PyPI&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/publishing-a-package-on-pypi.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/publishing-a-package-on-pypi.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Specify+dev+dependencies+in+setup.py+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fspecify-dev-dependencies-python-package-setup.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Specify%20dev%20dependencies%20in%20setup.py&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/specify-dev-dependencies-python-package-setup.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Specify%20dev%20dependencies%20in%20setup.py&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/specify-dev-dependencies-python-package-setup.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/specify-dev-dependencies-python-package-setup.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Writing+Unit+Tests+in+Python+%E2%9C%85+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FPython%2Fwriting-tests-in-python-using-unittest.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Writing%20Unit%20Tests%20in%20Python%20%E2%9C%85&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/writing-tests-in-python-using-unittest.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Writing%20Unit%20Tests%20in%20Python%20%E2%9C%85&url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/writing-tests-in-python-using-unittest.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Python/writing-tests-in-python-using-unittest.md)
</details></li>
</ul>




### Shell

<ul>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/alternative-to-ls-linux.md">Alternative to 'ls' commnand</a><details><summary> Read More 🔽</summary>

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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Alternative+to+%27ls%27+commnand+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Falternative-to-ls-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Alternative%20to%20%27ls%27%20commnand&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/alternative-to-ls-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Alternative%20to%20%27ls%27%20commnand&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/alternative-to-ls-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/alternative-to-ls-linux.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Colorize+Output+in+Terminal+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fcolorize-output-in-terminal-bash.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Colorize%20Output%20in%20Terminal&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/colorize-output-in-terminal-bash.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Colorize%20Output%20in%20Terminal&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/colorize-output-in-terminal-bash.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/colorize-output-in-terminal-bash.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/copy-one-file-to-multiple-files.md">Copy one file to multiple files in Bash</a><details><summary> Read More 🔽</summary>

# Copy one file to multiple files in Bash
<!--24 Dec 2019 -->
```bash
for f in file{1..10}.py; do cp main.py $f; done
```
> this will create new files file_1.py, file_2.py etc and copy contents of _main.py_ file to all of them.

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Copy+one+file+to+multiple+files+in+Bash+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fcopy-one-file-to-multiple-files.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Copy%20one%20file%20to%20multiple%20files%20in%20Bash&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/copy-one-file-to-multiple-files.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Copy%20one%20file%20to%20multiple%20files%20in%20Bash&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/copy-one-file-to-multiple-files.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/copy-one-file-to-multiple-files.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/extract-file-id-from-drive-shareable-link.md">Extract file id from drive shareable link</a><details><summary> Read More 🔽</summary>

# Extract file id from drive shareable link

I host my blog images on Google Drive sometimes, the normal shareable link is not
the actual image source.
Instead this is :

`https://drive.google.com/uc?export=view&id=<INSERT-ID>`

`INSERT_ID` is the file id (in the shareable link)which is higlighted below

[https://drive.google.com/file/d/**1ifRiquoNw3awVTX6geyNoDp8FW6tafOE**/view?usp=sharing]()

here is a bash script to convert the link.

```bash
#!/usr/bin/env bash

str="$1"
# remove everything after the last /
remove_last=${str%/*}
# get everything after the last /
get_last=${remove_last##*/}
echo "https://drive.google.com/uc?export=view&id=$get_last"
```

[Also a Python version](https://gist.github.com/Bhupesh-V/7ad79f1cf6e007df1be02aeba22ec586)

You can now use it in `<img>` src

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Extract+file+id+from+drive+shareable+link+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fextract-file-id-from-drive-shareable-link.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Extract%20file%20id%20from%20drive%20shareable%20link&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/extract-file-id-from-drive-shareable-link.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Extract%20file%20id%20from%20drive%20shareable%20link&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/extract-file-id-from-drive-shareable-link.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/extract-file-id-from-drive-shareable-link.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/find-bootup-time-in-linux.md">Find boot-up time in linux 🐧</a><details><summary> Read More 🔽</summary>

# Find boot-up time in linux 🐧
<!-- 18 Oct 2020 -->
We can achieve this using the `systemd` service. Just run this

```bash
systemd-analyze
```

Demo:

```bash
Startup finished in 36.655s (kernel) + 58.030s (userspace) = 1min 34.685s
graphical.target reached after 57.709s in userspace
```

> The `graphical.target` specifies how long it took to reach to the _log-in_ screen.

## Other tricks

1. You can also plot service initializations in a SVG graph.
```bash
systemd-analyze plot > demo.svg
```

2. Check which service takes most of the time.
```bash
systemd-analyze blame
```

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Find+boot-up+time+in+linux+%F0%9F%90%A7+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ffind-bootup-time-in-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Find%20boot-up%20time%20in%20linux%20%F0%9F%90%A7&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-bootup-time-in-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Find%20boot-up%20time%20in%20linux%20%F0%9F%90%A7&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-bootup-time-in-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-bootup-time-in-linux.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/find-default-git-branch-name.md">Find default git branch name</a><details><summary> Read More 🔽</summary>

# Find default git branch name
<!-- 25 July 2020 -->
```bash
git remote show origin | awk '/HEAD/ {print $3}'
```


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Find+default+git+branch+name+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ffind-default-git-branch-name.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Find%20default%20git%20branch%20name&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-default-git-branch-name.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Find%20default%20git%20branch%20name&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-default-git-branch-name.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-default-git-branch-name.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Find+files+changed+7+days+ago+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ffind-files-changed-7-days-ago.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Find%20files%20changed%207%20days%20ago&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-files-changed-7-days-ago.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Find%20files%20changed%207%20days%20ago&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-files-changed-7-days-ago.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-files-changed-7-days-ago.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/find-fonts-in-linux.md">Find fonts available in Linux</a><details><summary> Read More 🔽</summary>

# Find fonts available in Linux

```bash
fc-list
```

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Find+fonts+available+in+Linux+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ffind-fonts-in-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Find%20fonts%20available%20in%20Linux&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-fonts-in-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Find%20fonts%20available%20in%20Linux&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-fonts-in-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-fonts-in-linux.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Finding+all+Python+Virtual+Environments+in+your+system+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ffind-all-python-virtual-environments-in-your-system.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Finding%20all%20Python%20Virtual%20Environments%20in%20your%20system&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-all-python-virtual-environments-in-your-system.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Finding%20all%20Python%20Virtual%20Environments%20in%20your%20system&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-all-python-virtual-environments-in-your-system.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/find-all-python-virtual-environments-in-your-system.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/generate-random-numbers-in-bash.md">Generate random numbers in bash</a><details><summary> Read More 🔽</summary>

# Generate random numbers in bash
<!-- July 29 2020 -->
Easiest way is to use the `$RANDOM` variable.

```bash
>> echo "$RANDOM"
12261
```

Each time this parameter is referenced, a random integer between **0** and **32767** is generated.

A better way which I like is to use the GNU coreutil, `shuf`

One Random number between 69 & 420
```bash
shuf -i69-420 -n1
```

Five Random numbers between 69 & 420
```bash
shuf -i69-420 -n5
```

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Generate+random+numbers+in+bash+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fgenerate-random-numbers-in-bash.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Generate%20random%20numbers%20in%20bash&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/generate-random-numbers-in-bash.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Generate%20random%20numbers%20in%20bash&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/generate-random-numbers-in-bash.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/generate-random-numbers-in-bash.md)
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

I [wrote a small shell script](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/sys.sh) to get _(almost)_ realtime update of your system.

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Get+System+info+using+Shell+Commands+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fget-system-info.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Get%20System%20info%20using%20Shell%20Commands&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-system-info.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Get%20System%20info%20using%20Shell%20Commands&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-system-info.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-system-info.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Get+Total+System+Memory+using+%60vmstat%60+command+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Ftotal-memory-using-vmstat.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Get%20Total%20System%20Memory%20using%20%60vmstat%60%20command&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/total-memory-using-vmstat.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Get%20Total%20System%20Memory%20using%20%60vmstat%60%20command&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/total-memory-using-vmstat.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/total-memory-using-vmstat.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/get-last-commit-date-of-file.md">Get last commit date of file</a><details><summary> Read More 🔽</summary>

# Get last commit date of file
<!-- 15 nov 2020 -->
this can be done using the `git log` command

```bash
git log --follow -p -- filename
```

this by default renders the diffed version history of the file over time. We can use
`awk` to look for pattern _Date_ in this.

```bash
git log --follow -p -- README.md | awk '/Date/ { print $4,$3,$6 }'
```

this will grab the date of each commit which modified this file!

```bash
14 Nov 2020
11 Nov 2020
11 Nov 2020
7 Nov 2020
...
```

Here is simple script that will list last commit date of each file inside a git repo.

```bash
#!/usr/bin/env bash

# Utility to list last commit date of each file in a git repo

[[ ! -d ".git" ]] && echo -e "Not a git repo" && exit 1

for file in $(du --exclude='.git' -a . | awk '{ print $2 }'); do
	if [[ -f "${file:2}" ]]; then
		last_modify_date=$(git log --follow -p -- "${file:2}" | awk '/Date/ { print $4,$3,$6 }' | head -1)
		if [[ "$last_modify_date" ]]; then
			printf "%s : %s\n" "$last_modify_date" "${file:2}"
		fi
	fi
done

```



**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Get+last+commit+date+of+file+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fget-last-commit-date-of-file.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Get%20last%20commit%20date%20of%20file&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-last-commit-date-of-file.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Get%20last%20commit%20date%20of%20file&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-last-commit-date-of-file.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/get-last-commit-date-of-file.md)
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


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Line+Discipline+in+Unix%2FLinux+Machines+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fline-discipline-in-unix-linux.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Line%20Discipline%20in%20Unix/Linux%20Machines&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-discipline-in-unix-linux.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Line%20Discipline%20in%20Unix/Linux%20Machines&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-discipline-in-unix-linux.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-discipline-in-unix-linux.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/line-editors-tips-tricks.md">Line Editing in Linux, Tips and Tricks</a><details><summary> Read More 🔽</summary>

# Line Editing in Linux, Tips and Tricks

I will log various ways through which tools like `sed`, `cut` and `tr` can be used.

## `sed` 😥

- Print specific lines from a file using line numbers
  ```bash
  # print lines 12 to 22
  sed -n '12,22p' file.txt
  ```

- Omit first line of output.
  ```bash
  sed -n '1!p'
  ```

## `tr` ➡️

- Translate (or convert) all () to [] in a textfile.
  ```bash
  tr '()' '[]'
  ```

- Translate all occurences of multiple spaces with a single space.
  ```bash
  tr -s ' '
  ```

## `cut` ✂️

- Print every 4th word (or field) from a space separated STDIN.
  ```bash
  cut -d' ' -f4
  ```
  I don't know about you but this is pretty cool.


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Line+Editing+in+Linux%2C+Tips+and+Tricks+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fline-editors-tips-tricks.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Line%20Editing%20in%20Linux%2C%20Tips%20and%20Tricks&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-editors-tips-tricks.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Line%20Editing%20in%20Linux%2C%20Tips%20and%20Tricks&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-editors-tips-tricks.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/line-editors-tips-tricks.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/monitor-network-data-usage.md">Monitor network (data) usage</a><details><summary> Read More 🔽</summary>

# Monitor network (data) usage

The amount of data sent(uploaded) & received (downloaded) can be found out
using the following bash script.

- Only works per session, i.e stats are gathered once you power up your PC (or login).
- Good to have if you have limited data avaiability & want to montior your data usage.

```bash

netu() {
    # [net]work [u]sage: check network usage stats

    net_device=$(route | awk '/default/ {print $8}')
    TRANSMITTED=$(ifconfig "$net_device" | awk '/TX packets/ {print $6$7}')
    RECEIVED=$(ifconfig "$net_device" | awk '/RX packets/ {print $6$7}')

    pc_uptime=$(uptime -p | awk '{for (i=2; i<NF; i++) printf $i " "; if (NF >= 1) print $NF; }')
    printf "%s\n\n" "Network Usage since $pc_uptime"
    printf "%s\n" "$(tput bold)🔼 TRANSMITTED $(tput sgr0): $TRANSMITTED"
    printf "%s\n" "$(tput bold)🔽 RECEIVED    $(tput sgr0): $RECEIVED"
}

```

### Demo
![netu](https://user-images.githubusercontent.com/34342551/89729900-9d0b6100-da57-11ea-8497-233b64e42dc6.png)


[Grab it from here](https://github.com/Bhupesh-V/.Varshney/blob/316cde84f3a666cf3f503a2de34e8289074ffbce/.bash_functions#L69)

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Monitor+network+%28data%29+usage+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fmonitor-network-data-usage.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Monitor%20network%20%28data%29%20usage&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/monitor-network-data-usage.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Monitor%20network%20%28data%29%20usage&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/monitor-network-data-usage.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/monitor-network-data-usage.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/print-lines-between-two-words.md">Print lines between 2 words</a><details><summary> Read More 🔽</summary>

# Print lines between 2 words
<!-- 24 Aug 2020 -->

You may arrive in a situation where you may want to "extract" out text between two words.
For example to view the latest changelog (where `x.x.x` is the latest version) in a [CHANGELOG.md](https://github.com/Bhupesh-V/dotman/blob/master/CHANGELOG.md) file.

### Using `sed`

```bash
sed -n -e '/x.x.x/,/0.1.0/ p' CHANGELOG.md | sed -e '1d;$d'
```

`sed -e '1d;$d'` removes the first & last line.

### Using `awk`

```bash
awk '/x.x.x/,/0.1.0/' CHANGELOG.md | awk 'NR>2 {print last} {last=$0}'
```

`awk 'NR>2 {print last} {last=$0}'` removes the first & last line.

> NOTE: `NR` means which Line number is being processed

#### Resources

- [How to show lines after each grep match until other specific match?](https://unix.stackexchange.com/questions/21076/how-to-show-lines-after-each-grep-match-until-other-specific-match)
- [What is the easiest way to remove 1st and last line from file with awk?](https://stackoverflow.com/questions/15856733/what-is-the-easiest-way-to-remove-1st-and-last-line-from-file-with-awk)

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Print+lines+between+2+words+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fprint-lines-between-two-words.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Print%20lines%20between%202%20words&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/print-lines-between-two-words.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Print%20lines%20between%202%20words&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/print-lines-between-two-words.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/print-lines-between-two-words.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/random-emoji-one-liner.md">Random emoji 😲 in one line</a><details><summary> Read More 🔽</summary>

# Random emoji 😲 in one line
<!-- 30 July 2020 -->

```bash
printf "%b\n" "\U1F$(shuf -i600-700 -n1)"
```

> PS: I am still working on a better way, this will only generate emojis in UNICODE range `1F601` to `1F700` while ignoring codepoints like `1F60A` 😊. Let me know if you have a beter way (create an issue)


**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Random+emoji+%F0%9F%98%B2+in+one+line+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Frandom-emoji-one-liner.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Random%20emoji%20%F0%9F%98%B2%20in%20one%20line&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/random-emoji-one-liner.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Random%20emoji%20%F0%9F%98%B2%20in%20one%20line&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/random-emoji-one-liner.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/random-emoji-one-liner.md)
</details></li>
<li><a target="_blank" href="https://github.com/Bhupesh-V/til/blob/master/Shell/shell-redirections-quick-guide.md">Shell Redirections ↔ Quick Guide</a><details><summary> Read More 🔽</summary>

# Shell Redirections ↔ Quick Guide

File descriptors:

- **`stdin`**  : 0
- **`stdout`** : 1
- **`stderr`** : 2


## Redirecting `stderr`

1. Use **`2>`**. Compatible with both `bash` and `sh`

## Redirecting both `stderr` & `stdout`

1. With `bash`, use **`&>`**
2. With `sh`, use **`> where-to-redirect 2>&1`**

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Shell+Redirections+%E2%86%94+Quick+Guide+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FShell%2Fshell-redirections-quick-guide.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Shell%20Redirections%20%E2%86%94%20Quick%20Guide&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/shell-redirections-quick-guide.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Shell%20Redirections%20%E2%86%94%20Quick%20Guide&url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/shell-redirections-quick-guide.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/Shell/shell-redirections-quick-guide.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Auto-complete+in+plain+HTML+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FWebDev%2Fhtml-datalist-auto-complete.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Auto-complete%20in%20plain%20HTML&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/html-datalist-auto-complete.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Auto-complete%20in%20plain%20HTML&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/html-datalist-auto-complete.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/html-datalist-auto-complete.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=I+learned+about+Open+Graph+protocol+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FWebDev%2FOpenGraph.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=I%20learned%20about%20Open%20Graph%20protocol&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/OpenGraph.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=I%20learned%20about%20Open%20Graph%20protocol&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/OpenGraph.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/OpenGraph.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=Live+Editing+HTML+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FWebDev%2Flive-edit-html.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=Live%20Editing%20HTML&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/live-edit-html.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=Live%20Editing%20HTML&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/live-edit-html.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/live-edit-html.md)
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

**Share on** [![Twitter share](https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V)](https://twitter.com/intent/tweet?url=%60async%60+%26+%60defer%60+Attributes+by+%40bhupeshimself+https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2Fblob%2Fmaster%2FWebDev%2Fasync-defer-html-javascript.md)
[![Reddit share](https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url)](https://www.reddit.com/submit?title=%60async%60%20%26%20%60defer%60%20Attributes&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/async-defer-html-javascript.md)
[![Telegram share](https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com)](https://telegram.me/share/url?text=%60async%60%20%26%20%60defer%60%20Attributes&url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/async-defer-html-javascript.md)
[![LinkedIn Share](https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/Bhupesh-V/til/blob/master/WebDev/async-defer-html-javascript.md)
</details></li>
</ul>

## Usage

See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## Author [![bhupesh-twitter-image](https://kutt.it/bhupeshimself)](https://twitter.com/bhupeshimself)

👤 **[Bhupesh Varshney](https://bhupesh-v.github.io)** 

## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>
<a href="https://ko-fi.com/bhupesh">
  <img title="ko-fi/bhupesh" alt="Support on ko-fi" src="https://user-images.githubusercontent.com/34342551/88784787-12507980-d1ae-11ea-82fe-f55753340168.png" width="185">
</a>

## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [MIT](https://github.com/Bhupesh-V/til/blob/master/LICENSE) licensed.

## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
