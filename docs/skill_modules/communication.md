# Communicating Your Research
**Under Construction**

## Overview
This section details how to effectively communicate your research, in particular through papers, figures, and
presentations. Given that one major goal in writing papers is so that reviewers and peers will read them, rate
them highly, and cite them, in this section we'll also discuss how to review papers so the parallels are
clear.

## Table of Contents
  1. [How do you write papers?](#how-do-you-write-papers)
  2. [How do you make good figures?](#how-do-you-make-good-figures)
  3. [How do you review papers?](#how-do-you-review-papers)

## General Resources
  1. [Make it Clear](https://mitpress.mit.edu/books/make-it-clear)

## How do you write papers?
### Guiding Questions
  1. What should the overall structure be?
  2. How do you write the Introduction / Framing section(s)?
  3. How do you write the Experiments / Results section(s)?
  4. How do you make your papers reproducible? In what ways will reproducibly concretely help you?
  5. How do you respond to criticism about your paper? What do you do if you find a significant mistake in
     your paper after it has been published? After it has been significantly cited?
  6. How do you decide authorship ordering?

### Overall Commentary & Key Take-aways
#### Know _what_ you're trying to say.
As crazy as it sounds, in many cases when revising drafts (both those I've written and those written by
others), one of the most effective tools in my toolkit is to ask the author "What are we trying to say here?"
then taking whatever simple 1 - 3 sentence explanation comes out and writing that at the top of the relevant
paragraph, section, or draft.

This tool is so effective because it helps make your paper's message apparent (by stating it clearly) and
because it reflects the high priority of that information (by stating it first). The efficacy of this tool
leads naturally into the second principle, which is...

#### Know your framing.
Beyond just knowhing what you're trying to say, you need to know the entire framing of your paper. The framing
(typically laid out in full in the introduction of the paper) will guide the _entirety_ of the paper (and,
ideally, the research process itself). When thinking through the framing of the paper, I personally really
like a slight variation of the Stanford InfoLab tips mentioned below:
  1. What is the problem/question?
  2. Why is it interesting, important, and/or impactful?
     _Note here that "interesting" doesn't refer to the technical complexity of your solution, but rather why
     the investigation you're proposing is interesting in and of itself (if it is)_.
  3. Why is it hard? 
       a. Why do naive baselines fail?
          _In some cases, it may be self-evident why naive baselines fail. In such cases, while you should still
          know why they fail, you may not include that in your paper._
       b. Why hasn't it been solved before? / What's wrong with previous proposed solutions?
          Ideally, for this point, you can give a single clear problem that dictates why prior solutions fail,
          and use that to motivate your solution below.
  4. How do I solve the problem?
     a. Concretely, how do I address the problem identified in 3b? How do I differ from prior works?
  5. How will I convince you that my solution works? E.g., what are my results?
  6. What is the context in which my solution works? What are the limitations of my solutoin?

This framing both serves as an immediate outline for most introductions and serves to define the goals of most
of the sections in a traditional paper structure.

A good recipe when thinking about using this framing is that for each point, you want to state it clearly,
motivate it (ideally iwth citation, experimental results, arguments, or proofs), and connect it back to the
main message of your paper. For example, if you argue that a problem is important because it affects industry
applications, find a citation for it! If you argue that existing approaches fail because of an empirical
property, then cite it, or, if nobody has noted it previously, show it empirically! To motivate why one of
your experiments helps establish your claim, argue qualitatively why the particular result you observe for the
particular test you run offers that support!

#### Paper Structure
In general, you'll include the following sections, in something like the following order. I've included a
smattering of notes of each of these, but they should be expanded---feel free to [contribute]('../contact') if
you want to help expand on any of these points!
  0. *Abstract*
  1. *Introduction.*
     In the introduction, you describe the framing of the paper and preview everything else you'll say in the
     main body. See the section above for more details.
  2. *Related works.*
     Here you establish your credentials, and show that you aren't missing any major sections related to your
     work.
  3. *Methods.*
     a. *Preliminary Notation.*
     b. *Problem API.*
        In many papers, especially those for core ML conferneces (e.g., NeurIPS, ICML, ICLR, AAAI), it is a
        great strategy to describe the "API" for your problem at the outset of your methods. Here, by "API for
        your problem," I mean stating "Given a dataset X with properties Y, our model f takes in samples from
        x and does Z...". This can give readers a chance to understand, in a technically precise manner, what
        your experimental data will look like, how your model will operate over that data, and how it might be
        used in practice.
     c. *Algorithm / Our Method.*
  4. *Experiments.*
     a. *Dataset descriptions.*
     b. *Experimental Goals and Procedures*
        Pursuant to the goals stated in the prior section, if you want your experiments to help convince the
        reader your method works, then you should outline specifically why you run every experiment you do,
        and how those experiments help establish that fact. Coupling this to how you will actually run those
        experiments in practice is a common approach and can help ensure the reader understands how the
        methods of your experiments connect to your overarching framing.
  5. *Results.*
  6. *Discussion.*
     a. *Limitations & Context.*
     b. *Key Takeaways.*
  7. *Conclusion.*

### Interview Highlights
*Under Construction*

### Specific Resources
#### [Stanford InfoLab Tips for Writing Technical Papers](https://cs.stanford.edu/people/widom/paper-writing.html)
This guide is a great starting point for writing technical papers. I particularly value their discussion on
the introduction, which states that an effective introduction must focus on answering five key questions:
  1. What is the problem?
  2. Why is it interesting and important?
  3. Why is it hard? (E.g., why do naive approaches fail?)
  4. Why hasn't it been solved before? (Or, what's wrong with previous proposed solutions? How does mine differ?)
  5. What are the key components of my approach and results? Also include any specific limitations.

#### [How to do good research, get in published in SIGKDD, and get it cited!](https://www.cs.ucr.edu/~eamonn/Keogh_SIGKDD09_tutorial.pdf)
This guide is more comprehensive than just focusing on the writing part, and is featured also in the
[research](skill_modules/research) section of this guide, but it is very relevant here too! Note the synergy
between this and the Stanford InfoLab tips above.

#### Ten Tips for Writing CS Papers, Parts [1](http://www.nowozin.net/sebastian/blog/ten-tips-for-writing-cs-papers-part-1.html) and [2](http://www.nowozin.net/sebastian/blog/ten-tips-for-writing-cs-papers-part-2.html)
This is a series of 10 tips by [Dr. Sebastian Nowozin](http://www.nowozin.net/sebastian/) that are more
focused on the immediate technical craft of writing itself, but still very useful.

## How do you make good figures?
### Guiding Questions
  1. What kinds of figures are there?
  2. What design philosophies or technologies do you use?
  3. How do you make a good overview figure?
  4. How do you make a good results/data figure?

### Overall Commentary & Key Take-aways
*Under Construction*

### Specific Resources
*Under Construction*

#### [Effective Use of Figures in Research Papers](https://cs.stanford.edu/~marinka/slides/marinka-figures19.pdf)
This slide deck, by [Professor Marinka Zitnik](https://dbmi.hms.harvard.edu/people/marinka-zitnik), walks
through how to make impressive, well-designed figures for both conference and journal venues.

### Interview Highlights
*Under Construction*

## How do you review papers?
### Guiding Questions
  1. When should you start reviewing?
  2. For what venues should you review?
  3. How do you review papers?

### Overall Commentary & Key Take-aways
#### Goals in Reviewing
There are two, sometimes contradictory, goals in reviewing modern conference ML papers. First, you review to
help the _venue_ ensure it only accepts high-quality papers that will be impactful and (practically speaking)
well cited. Second, you review to help the _author_ best improve their work in this paper and in general. It
is important to keep in mind that you need to service these two goals at once in most reviewing contexts, even
when they may not fully align. For example, it may become clear early in reading a paper that the paper will
not be a good fit for a specific venue---stopping the review there may be suitable for helping the venue, but
doesn't serve the author well at all. Conversely, offering highly detailed feedback about effective writing
techniques, figure suggestions, framing tips, etc. may help the author significantly, but if you do this at
the expense of missing something critical (e.g., a poor statistical practice, mistake in a proof, or that the
paper is highly redundant with existing work) you may be failing in the venue's goal.

Of course, you also have your own goal, which is to satisfy both of these goals as effectively as possible in
as little time as possible.

#### Structuring Reviews
I like to structure my reviews in line with both common guidelines for reviewing (e.g., summary, key
strengths, key weaknesses, presentation issues, etc.), but also in line with the guidelines for writing
papers and the goals listed above. In particular, I do something like the following:

##### Summary
I often write my summary section using the framing outline given in the section above, identifying for each
point in the outline what my best guess is for how the authors would respond to that point.  Interestingly, in
my experience this is often both faster and more helpful than a free-form summary. It is helpful for the
authors as it (tacitly) encourages them to focus on those framing questions in a revision and helps expose any
areas where there intent wasn't clearly communicated, and it is helpful for the venue as it can help align
reviewers on a common understanding of the work.
##### "Key Strengths" & "Key Weaknesses"
  1. Key Strengths: These are the reasons I would argue the paper should be accepted. They are not the
     small things I liked about the paper (e.g., "Figure 1 is really clear!"), but are the major factors that
     define this work as a meaningful, impactful advancement over the current literature (e.g., "This work
     poses a novel solution to a meaningful problem, and demonstrates consistent improvement via that
     solution."). The *primary goal* of this section is to aid the venue in making the correct decision for
     the paper (though of course identifying the major strengths and weakensses will also help the author, and
     should be written carefully with that in mind).
  2. Key Weaknesses: These are the reasons I would argue the paper should be rejected. Like "Key Strengths",
     the focus is on major things (e.g., "I have serious concerns about the statistical validitiy of
     Experiment 2"), not minor things (e.g., "There are a number of typos in the work, though it is still
     understandable."). Again, the *primary goal* is to aid the venue. Note that I can (and often do) have
     both key strengths and key weaknesses, and it may be that there are more key strengths than key
     weaknesses on a paper I ultimately recommend rejecting, or vice-versa, depending on the magnitude of each
     concern.
##### "Minor Strengths" / "Minor Weaknesses"
Here, the focus is on the other minor strengths and weaknesses, that, while nontrivial, would not change my
decision either way alone (though many together certainly could). As these are not (in general) wht will
decide the recommendation either way, the primary goal here is to help the author, not the venue.
##### "Presentaiton" / "Minor Missing References"
In some cases, either due to review forms or details of the paper, I'll separately highlight any commentary on
presentation quality or missing references. Missing references, in particular, however, usually comes up
earlier, both in the key/minor weaknesses and in the summary.  Note: **To adequately check if references are
missing you must attempt to find missing references!** Usually, with a few quick google searches I can
determine if any major holes exist in the references for a given submission, and I am consistently surprised
at how few reviewers do this. I have also personally caught at least one case of plagarism / dual submission
violation in this way, that would have otherwise gone unnoticed, so it is an important, understated step!
##### "Overall Recommendation"
Here I just synthesize previously noted things into a single accept/reject recommendation. Some people state
that you should always give extreme recommendations, but I disagree with this -- skepticisim and
self-reflection are integral in any part of science, and accordingly I am always skeptical of my own opinions,
and tend to give less confident scores (e.g., minor accept/reject vs. extreme accept/reject).  However, that
is just my take, and other opinions may differ. If there is any ambiguity in the key strengths/weaknesses
sections as to which way the recommendation will go (e.g., if both lists are equally populuated), I'll try to
reconcile that here and clarify my thought process.
##### "Questions for the Author" / "Author Response Guidance"
In this section, I have up to two subsections, splitting my questions for the author / guidance on changes I'd
want to see based on whether or not satisfactory answers to them would likely change my score. The motivation
for breaking things up like this is two-fold:
  1. It helps me clarify what things are defining my decision, and helps me pre-register my response function
     to the author response, which makes me more honest and transparent as a reviewer. It also similarly
     signals to other reviewers how I might be likely to update my score.
  2. It helps authors know where they should spend their time in the rebuttal phase and how they would need to
     change their paper in the future to get a reviewer like me to give them a better score.

If/as [more](https://neuripsconf.medium.com/neurips-2021-changes-to-the-review-process-909e797580cf) reviewing
systems move to open reviewing platforms like [OpenReview](https://openreview.net/), I think this will be
increasingly important to help prevent authors from feeling like they're being "strung along" by reviewers and
to make reviewers think more about their scores in terms of "deltas" (what would need to change for my score
to change) and less in terms of qualitative, ill-defined impressions.

### Specific Resources
#### Reviewer Guidelines
The first place to start when thinking about how to be a better reviewer is by looking at the guidelines
posted by the venues asking for reviews! Here are a few:
  1. [NeurIPS 2021](https://neurips.cc/Conferences/2021/Reviewer-Guidelines)
  2. [ICML 2020](https://icml.cc/Conferences/2020/ReviewerGuidelines)
  3. [ICLR 2021](https://iclr.cc/Conferences/2021/ReviewerGuide)
  4. [AAAI 2020](https://aaai.org/Conferences/AAAI-20/wp-content/uploads/2019/09/AAAI-20-Reviewing-Guidelines.pdf)
  5. KDD--Actually, I can't find anything for KDD after 2011. If you find anything, [contact me](../contact).

### Interview Highlights
*Under Construction*

### Other Links
These are links that are interesting and relevant, but not as directly informative or essential as those in
other sections.
  1. https://blog.ml.cmu.edu/2020/12/01/icml2020exp/
