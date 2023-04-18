# Literature Search Prompts / Recipes

## Core Prompt

```
I'm an academic researcher in machine learning and natural language processing, interested in speccing out an
idea for a new research project. You are an expert researcher and project manager, working to help me design
the best possible research question and plan of action. Below, I'll present my idea's description, and through
dialogue you'll work to help me with the following tasks.
**Important** Ask me questions to help refine my idea, and to better understand what the right ideal scope is.
When working through the idea, feel free to provide or ask me for examples of how the idea might work in
practice. We can work through as many stages of question answering as necessary.
**Important** Be constuctive, but critical when appropriate! If the idea is poor, or will rely on resources
that are very costly or hard to acquire, say so, and offer guidance on how to improve it.

Your concrete tasks are:
(1) Help me expand, clarify, and narrow the scope of the presented idea to an actionable, reasonable research
    target for my field. We must complete this task prior to moving on to the other tasks, so only once we are
    satisfied with the research direction should you answer tasks 2 - 6. It may take a few rounds of back and
    forth to do this.
(2) Identify any major barriers to completing this research, such as heavy resource requirements, brittle
    failure points, major assumptions, etc. Keep in mind that as an academic researcher, I do not have access
    to huge compute resources for large scale models.
(3) Directly suggest relevant references or design comprehensive search queries for use with semantic scholar
    and other search engines to find relevant existing references to scope out the field. Output these as a
    *space separated* list of the search queries in quotes, in a single line, like this: "query_1" "query_2" ...
(4) After you give me search queries, I will give you a collection results from running those queries over
    academic search engines. We'll work together to identify key resources to reference for this project and to
    see if anybody else has already done this idea, in which case we'll need to go back to the drawing board. For this task, you should output to me the following information, then pause and let me assess before we move on to task 5.
    
    Most Relevant Papers:
    Paper 1:
      Title: (paper title here)
      Rationale: (Why is this especially relevant)
      Use as seed: (should I use this as a literature review seed to see what papers it cites? Or what papers cite it? Or Both?)
    Paper 2:
      ...
      
    New Search Terms: "new query 1", ...
      
(5) Describe the key experiments I would need to run / figures I would need to generate for this project. 
    **Important** Be as detailed as possible in this stage -- discuss exactly what each figure would show, how
    it would be laid out, visually, and what I'd need to do to produce it. For each experiment, include the
    following information in the following format:

    Experiment #:
      Motivation: (describe why this experiment is critical for a paper with this goal)
      Implementation: (describe how I would implement this experiment)
      Necessary Resources: (describe what would be needed [e.g., data, model, compute] to run this experiment)
      Suggested visualization: (describe how this experiment would be communicated in a paper)

(6) Directly suggest relevant datasets or design search queries to find appropriate datasets for this
    research. Use the same format as in #3 for this.
(7) Craft a potential abstract paragraph and paper outline for this work.

Idea description: 
```

## Examples
### GPT-4 Knowledge Graphs:
#### Idea:
I want to use existing large language models (e.g., GPT-4's API) to produce a large, structured
knowledge graph summarizing all current clinical research papers. I'll use GPT-4 both to extract relevant
concepts and relationships, and then in a follow-up pass to normalize those extracted strings into a
structured ontology. This could be used in many downstream applications.

#### Result:
The results in this setting were very good. 


### Something already done: Factual correctness in generated radiology reports.
#### Idea:
I want to produce a model that can parse a chest X-ray image and produce a radiology report. However, unlike existing work, I want my method to particularly focus on factual correctness. We'll achieve this by scoring the model not just with text generation metrics, but also by using automated radiology report labeling methods (e.g., Chexpert) on both our generated report and the real report and using reinforcement learning to ensure they match. 

#### Result:
This version of the prompt involved more back and forth with the system about the references, leading to it losing the thread on the tasks a bit. It also is very hesitant to say that the idea has already been done, even though it already has. That being said, this isn't necessarily a bad thing, as there could be new, novel components to any idea. Overall, response here was mixed.

### Something more theory driven: Attention as a memory bank from a neural turing machine perspective.
#### Idea:
It seems to me that the attention calculation in a transformers network is kind of similar to a read-write memory bank in a neural turing machine (though I know very little about NTMs). After each layer, the model can update it's "memory" via attention by "reading" (attending to) other cells in its bank and then "writing" (producing an updated value for) its cell, layer by layer. Is there any way to assess the validity of this idea, and if so, to leverage it to improve transformers, or to make transformers better able to maintain state over long sequences / generation tasks?

#### Result:
The model did a reasonable job at first, but it got lost in the context again after doing a bit more back and forth in the references review portion. It also likes to suggest doing things that have already been done and have been discussed in the literature review---in other words, it lacks creativity. 


