# Reuse arguments from last command
**_Posted on 22 Mar, 2022_**


### Get all of the arguments:

```
<command> !*
```

### Get only the last argument: 

```
<command> !$
```

### Get `n`th arguments

If you want a single argument from a list of arguments from the previous command, you can use <command> !!:<argNumber>

Example:

```
ls foo/ bar/ baz/
ls !:2 # Gives the results of ls bar/
ls foo/ bar/ baz/
ls !:1 # Gives the results of ls foo/
```

**Index of shortcuts**:

```
!^      first argument
!$      last argument
!*      all arguments
!:2     second argument

!:2-3   second to third arguments
!:2-$   second to last arguments
!:2*    second to last arguments
!:2-    second to next to last arguments

!:0     the command
!!      repeat the previous line
```

## Keyboard shortcuts

\<command\> <kbd>Esc</kbd><kbd>.</kbd>:  To get last argument of previous command

