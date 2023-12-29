# Retrieval-Augmented Generation (RAG)

Currently LLMs have these 2 problems:
1. They lack valid source while generating text.
2. They are often out-of date.

The RAG framework is a new approach to solve these problems. In this appraoch a LLM first finds relevant passages from a large corpus (content store like the Internet) and then generates text based on user prompt. This way it solves both the problems mentioned above.
