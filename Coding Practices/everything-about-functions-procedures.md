# Routines: Functions & Procedures
<!-- 27 Jan, 2021 -->

                                        _________ Routines ________
                                        |                          |
                                   Functions                   Procedures
                               (Returns a value)        (Doesn't return a value)



## Best practices

- A routine should not w/r global variables instead it should communicate with other routines.
- A routine should have a single, clearly defined purpose (1 Task = 1 Routine)
- **Hide Pointer Operation**: 
  - Isolate pointer operations in routines by this you can be certain that the code is correct & if in future you find a better data type then pointers you can change the program without traumatizing your code.
- Use a _function_ if the primary purpose of the routine is to return the value indicated by function "name" otherwise use a _procedure_.
- Don't hesitate to create small functions even if the operation seems one or two liner
- Make sure a _function_ always returns a valid value (mentally exercise each possible control flow path).
- Don't return references or pointers to local data since they will be out of scope once the function completes instead save the information as a class/struct member data.


## Cohesion

- Make sure cohesion is strong inside a function, below are some types of cohesion you need to worry about
  - **Functional Cohesion**: It is the strongest and best kind of cohesion (a routine performs one & only one operation). E.g. `GetCustomerName()`, `EraseFile()`.
  - **Sequential Cohesion**: I exists when a routine contains operation that must be performed in a specific order, that share data from step to step & that don't make up a complete function when done together.
  - **Temporal Cohesion**: It occurs when operations are combined into a routine because they are all done at the same time. E.g `Startup()`, `Shutdown()`.<br>
   Functions like these tend to be a hodgepodge of code to fix this think of temporal routines as _organisers_ of other events.
   _Startup()_ for e.g would read a config file, setup a memory manager etc. Make the temporal routine to perform specific activities rather than performing operations directly itself.
  - **Logical Cohesion**: It occurs when several operations are stuffed into the same routine & one of the operations is selected by a control _flag_ that's passed in.
  Instead of having using a flag to decide on operation its cleaner to have _n_ routines each of which does 1 distinct operation. If the operations use the same code or share data the code should be moved into a lower level routine & all the routines should be packaged into a class/module.
  Its all right to write a logically cohesive routine if its code consist solely of a series of if or case statements calls to other routines (only dispatching commands), its generally called a "_event handler_".

## Naming a `routine()`

- Avoid meaningless, vague verbs for e.g `HandleCalculation()`, `OutputUser()`.
  The verb is vague because the operation performed by the routine are vague. The routine suffers from weakness of purpose & the weak name is a symptom.
- Make names of routines as long as necessary and possible (9-15 chars)
- To name a _function_, use a description of return value.
- To name a _procedure_, use a strong verb + object. E.g `CheckOrderInfo()`, `PrintDocument()`


## Parameters

- Put parameters in "INPUT-MODIFY-OUTPUT" order i.e, list the parameters that are input first, input-and-output second & output only third.
- Put status or error variables last (think Go errors)
- Don't use routine parameters as working variables. It's dangerous to use the parameters passed in a routine as working variables use local variables instead (think formal/actual parameters)


> Most of the stuff documented here is inspired and/or taken from the legendary books: Clean Code & Code Complete. This can be understood as a summary of some chapters from these books.
