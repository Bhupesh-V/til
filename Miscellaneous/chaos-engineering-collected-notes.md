# Chaos Engineering 🐒️
<!-- 07 Mar, 2021 -->

Act of studying a system so as to build confidence in its capability to withstand harsh conditions. This is done by literally breaking (experimenting with) the system.

> Although chaos engineering really seems to only help some large-scale distributed operations in the world, its principles can be applied to even smaller systems to achieve strong systems

The said "[experiments](https://www.gremlin.com/community/tutorials/your-first-chaos-experiment/)" follow certain steps:

1. Define the steady state of the system that specifies normal or expected behaviour (e.g latency, throughput)
2. Segregate environments for experimenting
   - _Normal Group_ (Main production app)
   - _Experimental Group_ 
3. Introduce variables that reflect real world events (server crash, hard-drive malfunction, sending large payload data, limited network connection).

The harder is to break the steady state, the more confidence we have in the behaviour of our system

## Advanced principles:

1. **Run Experiments in prod 💣️**:<br>
   Systems behave differently depending on environment & since a _experimental group_ may not exactly have the same usage metrics, it becomes necessary to experiment in production. 
2. **Automate experiments to run continuously**:<br>
   Running experiments manually can be time-consuming & costly.
3. **Minimize Blast Radius**:<br>
   Experimenting in production has the potential to cause unnecessary customer pain. 


## Tools

- Netflix's [chaosmonkey](https://github.com/Netflix/chaosmonkey) is a resiliency tool that helps applications tolerate random instance failures.
- [pumba](https://github.com/alexei-led/pumba) is a chaos testing, network emulation and stress testing tool for containers.

## Resources & Credits

- [Chaos Architecture](https://www.infoq.com/presentations/chaos-architecture-mindset/)
- [Principles of chaos engineering](https://principlesofchaos.org/)
- [Chaos Engineering - Gremlin](https://www.gremlin.com/chaos-engineering/)
