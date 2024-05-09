# Design by contract (DbC)

**_Posted on 09 May, 2024_**

- First introduced native support was in [Eiffel programming language](https://www.eiffel.com/values/design-by-contract/introduction/).
- Think of [DbC](https://en.wikipedia.org/wiki/Design_by_contract) as having `if` checks before and after you manipulate data inside live code. Yes they are basically look like _assertions_.
- Major components of DbC:
  - **Precondition**
    - Conditions that must be met before a function is executed.
    - Client obligations, supplier benefits.
  - **Postcondition**
    - Conditions that must be met after a function is executed.
    - Client benefits, supplier obligations.
  - **Invariants**
    - General rules that must be true for the entire duration of the function.
    - Conditions that must be met before and after a function is executed.

## Resources

- [How are `TDD` and `DbC` related?](https://stackoverflow.com/a/28680756/8209510)
  - TDD is external to business logic, DbC is internal.
- [Code Contracts in `.NET`](https://learn.microsoft.com/en-us/dotnet/framework/debug-trace-profile/code-contracts)
- [Design by Contract and Assertions](https://www.eiffel.org/doc/solutions/Design_by_Contract_and_Assertions)