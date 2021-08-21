# Blue-Green Deployment Strategy
**_Posted on 21 Aug, 2021_**

> Useful in case you need to continuously roll out updates with almost no downtime

1. Basically stands for copying your production container (🟦) to a new one (🟩)
2. Applying your changes to the new green container
3. Push this container to prod alongside the blue one
4. Perform any automated tests / QA
5. Gradually redirect your users to the new deployment (load balancing)
6. Once the transition completes, the blue container can become a backup in case you need to rollback or it can be dumped
