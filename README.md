# Agent-Factory

This project is a collection of hands-on examples that showcase advanced techniques for building, optimizing, and customizing agentic systems.

[![YouTube Tutorial](https://img.shields.io/badge/YouTube-Watch%20Tutorial-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@airoundtable)

### List of projects:
- [x] [semantic-caching](#semantic-caching)
- [x] [llm-dynamic-tool-call](#llm-dynamic-tool-call)

## Project description:
<!-- ================ -->
<!-- semantic-caching -->
<!-- ================ -->
<a id="semantic-caching"></a>
<h3><a style=" white-space:nowrap; " href="https://github.com/Farzad-R/Agent-Factory/tree/main/semantic_caching"><b>Semantic Caching:</b></a></h3>
<p>
This project shows how semantic caching can make LLM applications faster and cheaper by smartly reusing previous question–answer pairs.

You'll find practical tutorials that walk you through how semantic caching and reranking work, plus a dashboard that helps you experiment and find the best caching strategy for your own data.

The project also includes a RAG chatbot with semantic caching built in, so you can try it out yourself and clearly see the difference it makes.

**YouTube video:** [Link](https://youtu.be/9GxOsJ-kQtg?si=jVoVoQTZhT_6EUVp)

<!-- ======================= -->
<!-- llm-dynamic-tool-call -->
<!-- ======================= -->
<a id="llm-dynamic-tool-call"></a>
<h3><a style=" white-space:nowrap; " href="https://github.com/Farzad-R/Agent-Factory/tree/main/llm-dynamic-tool-call"><b>LLM Dynamic Tool Call:</b></a></h3>
<p>
This project tackles a common problem: how do you manage 70+ tools for an LLM agent without overwhelming the model or breaking your budget?

We tested 4 different approaches (naive, category-based routing, semantic retrieval, and hybrid) with real e-commerce scenarios. The results show that semantic retrieval beats passing all tools to the model—achieving better accuracy while using 82% fewer tokens.

The project includes a complete Jupyter notebook with 11 test cases, detailed metrics, comparison charts, and a production-ready ChromaDB implementation. You'll see exactly which approach works best and why.

**YouTube video:** [Link](https://youtu.be/TlMNI0hTtYU?si=weBvJ0-MffMaP_PU)