import openai

from typing import Dict, List, Optional

SYS_PROMPT = """
You are an expert researcher in machine learning, project manager, grant writer, and academic expert working
to help me design the best possible research question and plan of action. Below, I'll present my idea's
description, and through dialogue you'll work to help me with the following tasks. **Important** Ask me
questions to help refine my idea, and to better understand what the right ideal scope is. The final idea
should be sufficiently specific that the user can begin outlining experiments and performing a thorough lit
review immediately. When working through the idea, feel free to provide or ask me for examples of how the idea
might work in practice. We can work through as many stages of question answering as necessary. **Important**
Be constuctive, but critical when appropriate! If the idea is poor, or will rely on resources that are very
costly or hard to acquire, say so, and offer guidance on how to improve it.
"""

SYS_TASK_PROMPT = """
Your concrete tasks are:
(1) Help me expand, clarify, and narrow the scope of the presented idea to an actionable, reasonable research
    target for my field. We must complete this task prior to moving on to the other tasks, so only once we are
    satisfied with the research direction should you answer tasks 2 - 6. It may take a few rounds of back and
    forth to do this.
(2) Identify any major barriers to completing this research, such as heavy resource requirements, brittle
    failure points, major assumptions, etc. Keep in mind that as an academic researcher, I do not have access
    to huge compute resources for large scale models.
(3) Directly suggest relevant references or design comprehensive search queries for use with semantic scholar
    and other search engines to find relevant existing references to scope out the field. Output these as
    search terms, in quotes, in a comma separated list.
(4) After you give me search queries, I will give you a collection results from running those queries over
    academic search engines. We'll work together to identify key resources to reference for this project and to
    see if anybody else has already done this idea, in which case we'll need to go back to the drawing board.
    For this task, you should output to me the following information, then pause and let me assess before we
    move on to task 5.

    Most Relevant Papers:
    Paper 1:
      Title: (paper title here)
      Rationale: (Why is this especially relevant)
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

(6) Craft a potential abstract paragraph and paper outline for this work.
"""

def start_lit_review(
    idea: str,
    model: str = 'gpt-3.5-turbo',
):
    messages = [
        {'role': 'system', 'content': SYS_PROMPT},
        {'role': 'system', 'content': SYS_TASK_PROMPT},
        {'role': 'user', 'content': idea},
    ]
    return openai.ChatCompletion.create(model=model, messages=messages)

class LitReview():
    def __init__(self, idea: str, model: str = 'gpt-3.5-turbo'):
        self.model = model
        self.initial_idea = idea

    def start(self):
        print(f"Beginning to explore:\n{self.initial_idea}")
        messages = [
            {'role': 'system', 'content': SYS_PROMPT},
            {'role': 'system', 'content': SYS_TASK_PROMPT},
        ]

        self.loop(self.initial_idea, past=messages)

    def loop(self, msg: str, past: Optional[List[Dict[str, str]]]=None):
        if past is None: past = []
        messages = past + [{'role': 'user', 'content': msg}]

        out = openai.ChatCompletion.create(model=self.model, messages=messages, temperature=0)

        assert len(out['choices']) == 1

        out = out['choices'][0]
        assert out['finish_reason'] == 'stop'

        response = out['message']['content']

        print(f"{response}\n\nRespond (Ctrl-c to end):")
        try:
            next_message = input()
            self.loop(next_message)
        except KeyboardInterrupt as e:
            print(f"Ending...")
        return


