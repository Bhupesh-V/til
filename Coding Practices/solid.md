# SOLID: Design Principles
<!-- 05 Feb, 2021 -->

1. **S**ingle Responsibility Principle
   - An object should do exactly one thing, and should be the only object in the codebase that does that one thing.
   - A class should have one, and only reason to change

2. **O**pen-closed principle
   - A class should be open to extension, but closed to change.
   - You should be able to extend classes behaviour, without modifying it.

3. **L**iskov substitution principle
   - Derived classes must be substitutable for their base classes.
   - An extension of the Open Close Principle and it means that we must make sure that new derived classes are extending the base classes without changing their behavior.

4. **I**nterface segregation principle
   - An interface should have as few methods as is feasible to provide the functionality of the role defined by the interface.
   - Make fine grained interfaces that are client specific.

5. **D**ependency Inversion principle
   - Depend on abstractions, not on concretions (concrete details)
   - High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces)
   - Abstractions should not depend on details. Details should depend on abstractions.


## Resources

- [Dependency Inversion Principle](https://www.oodesign.com/dependency-inversion-principle.html)
- [Liskov's Substitution Principle](https://www.oodesign.com/liskov-s-substitution-principle.html)

