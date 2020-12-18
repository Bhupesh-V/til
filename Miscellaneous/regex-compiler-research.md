# Creating a Regex Compiler/Parser - Research
<!-- 18 Dec, 2020 -->
Making a regex parser/compiler is not simple as it sounds, here is the overview of the steps:

1. Convert the expression to Postfix notation.
   > While converting to postfix, you also need to handle Character Classes & Range Quantifiers. Tutorials on internet haven't done this. Read [this](https://patents.google.com/patent/US8898094B2/en) for an insight on how to do this.
2. Convert the postfix in above step to AST.
3. Convert the AST to a state machine, preferably a NFA (non-deterministic finite automata)


## Resources

- [Regular Expression Matching Can Be Simple And Fast](https://swtch.com/~rsc/regexp/regexp1.html) by Russ Cox
- [Converting Regular Expressions to Postfix Notation with the Shunting-Yard Algorithm
](https://medium.com/@gregorycernera/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm-63d22ea1cf88)
- [Postfix to NFA using Thompson algorithm](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)
- [Regex Compiler: Part 2](https://kean.blog/post/regex-compiler)
- [Regular Expressions Based on Nondeterministic Finite Automaton](https://dannysu.com/2015/10/31/regex-nfa/)
- [Using NFA to evaluate regular expressions](http://prnbs.github.io/projects/regular-expression-parser/)
- [How to implement regular expression NFA with character ranges?](https://stackoverflow.com/questions/20767047/how-to-implement-regular-expression-nfa-with-character-ranges)
- [Regex under the hood: Implementing a simple regex compiler in Go](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079)

