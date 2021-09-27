# Research
## Overview
**Under Construction** Please check back later!

## General Resources
### [Various Resources by Matt Might](https://matt.might.net/articles/)
This is a link to [Matt Might's](https://matt.might.net) blog. See the section on "Graduate School" for
specific articles relevant to this topic. A few to look at in particular:
  * https://matt.might.net/articles/phd-school-in-pictures/
  * https://matt.might.net/articles/peer-review-rebuttals/
  * https://matt.might.net/articles/books-papers-materials-for-graduate-students/
  * https://matt.might.net/articles/advice-for-phd-thesis-proposals/

### [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html)
This essay, by [John Schulman](http://joschu.net/index.html), provides an end-to-end guide to pursuing ML
research. Note the two excellent citations to other essays, also linked here. I have yet to read it in full.

### [You and Your Research](http://www.cs.virginia.edu/~robins/YouAndYourResearch.html)
This is a (transcribed) talk by [Richard Hamming](https://en.wikipedia.org/wiki/Richard_Hamming). I have yet
to read it in full.

### [Principles of Effective Research](https://michaelnielsen.org/blog/principles-of-effective-research/)
This blog post, by [Michael Nielsen](https://michaelnielsen.org/blog/michael-a-nielsen/) describes several
principles of effective research. In comparison to some of the other resources here, these are more
self-oriented, and are thus highly relevant to the [intrapersonal](../intrapersonal) skills section of this
guide as well. I have yet to read this in full.

### [Lessons from My First Two Years of AI Research](https://web.mit.edu/tslvr/www/lessons_two_years.html)
This blog post by [Tom Silver] touches on lots of components of starting ML/AI research projects, and is
relevant here and in other sections of this module. I have yet to read it in full.

### [How to start a Deep Learning Project](https://twitter.com/MattNiessner/status/1441027241870118913)
A useful twitter thread with some good pointers.

## Table of Contents
  1. [Finding / Designing New Projects](#finding-designing-new-projects)
  2. [Starting Projects](#starting-projects)
  3. [Finishing Projects](#finishing-projects)

## Finding / Designing New Projects
### Guiding Questions
  1. How do you come up with a new project?
  2. How to gauge the viability / likelihood of success of a new project?

### Overall Commentary & Key Take-aways
#### How do you come up with a new project?
There are a number of distinct, valuable perspectives to keep in mind when thinking about designing new
projects. Some will resonate differently with different people.
##### Paper Arithmetic
A really powerful strategy that is likely the one that (especially early PhD students) most people should most
often employ is one I call "Paper Arithmetic". In this perspective, you look at _recent_, _well-regarded_
papers in your particular subfield, and try to find 3 things:
  1. Technical holes left in these lines of research
  2. Clever ways to combine ideas, techniques, features of different papers together.
  3. Motivating problems, datasets, scenarios that are understudied but clearly important.

If you can find a set of 3 of these things that synergize well, that's a paper. Why is this calld "Paper
Arithmetic"? Because rather than starting form an idea, you start with existing papers, and the background set
of knowledge/context, and try to find different combinations that yield promising research ideas.

###### Examples
My first paper during my PhD was entitled [Semi-Supervised Biomedical Translation with Cycle Wasserstein
Regression GANs](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/16938/15951). This paper, while
it undeniably has many flaws, is a great example of Paper Arithmetic. Why? The core technical method is a
direct combination of two other papers: the [Cycle GAN] paper for unsupervised image-image translation
and the [Wassertsein GAN] paper for stabilizing generative learning. The technical hole left in these lines of
research is ways that cycle GANs can be producitvely deployed in real-world learning contents on data
modalities that are not images (for which successful use of GANs was much less prevalent), and the motivating
problem was paired vs. unpaired data disparities in treatment effect estimation in healthcare contexts.

##### Immersion & Ethnography
Especially in application contexts, what separates high-impact from low-impact papers is a deep understanding
of the _real_ problems you're trying to solve and the _real_ constraints on the needed solutions. Immersing
yourself in the application area of interest until you appreciate those problems from an instinctive, habitual
level is, in my opinion, the best way to gain this understanding. If you can't gain this yourself (e.g., in a
multi-discplinary context), find collaborators who can, and trust their judgement (though not blindly, and not
without limit).

If you can provide a solution that (1) solves a real problem, (2) fits into the users' real workflow, and (3)
doesn't introduce new, other problems or require new ways of doing things, then this is a great starting point
to having real impact.

###### Key Resource Paper
An important subset of this area is when you produce a paper that provides a key resource for your community.
For example, at the time of writing this, my most cited paper is also my least technically
interesting--namely, [Clinical BERT](https://arxiv.org/abs/1904.03323) a paper that provides a pre-trained
clinical BERT model for use in clinical NLP tasks. This paper was well-timed but provided a resource that met
a clear need in the community, and thus has been used many times in many downstream works. As this is a
resource for the community you're already in, you will (or should) naturally already have this understanding
of the problems people face.

##### Gestalt
I highlight this not because it is typically a good strategy, but because it is an unfortunately common
strategy and because it is a trap. This strategy of coming up with a new project is when you suddenly, out of
the blue, have a great idea, and on further thinking about it, you convince yourself further and further that
this beautiful castle in the sky with minimal grounding. Often, when you try to execute on ideas generated in
this fashion, you'll find three things
  1. You didn't fully understand the space in which you're researching.
  2. You didn't appreciate the existing related literature, which already does what you're hoping to do.
  3. You didn't have a real motivating problem in mind that is sufficiently pressing, actionable, and
     operationalized to make a functional research project.

I can give so many examples of papers I've pursued in this vein, but the sad reality is that as of the time of
this writing, very few of them are published. 

However, this is not to say that great projects can't come out of this sort of project ideation. How can you
turn an initially gestalt-motivated idea into something more likely to succeed?
  1. Talk to experts in the areas of interest and explain your idea. If they're also excited (and not just
     encouraging, but actually sufficiently excited so as to want to get involved), you may be onto something
     worth pursuing! This is a critical first step because the reality is that unless you have years of
     experience in an area, you shouldn't trust your own intuition about the viability of the project, but you
     (likely) can trust the intuition of an expert. If you can bring them on as an actual collaborator, not
     only does that show they think it could succeed, but you'll have their expertise throughout the rest of
     the project.
  2. Write a formal project proposal, focusing specifically on how the project fits into the related
     literature. Try to (you'll often have to narrow your scope) find a way to fit your project into one of
     the other frameworks presented.
  3. Identify an operationalized target for your project and a series of go/no-go experiments (meaning
     experiments for which if you can't get your idea to work, you'll set the project aside [at least
     temporarily] and move onto other ideas). While success is better than failure, failing fast is also much
     better than failing slow.

### Specific Resources
*Under Construction*

### Interview Highlights
*Under Construction*

## Starting Projects
### Guiding Questions
  1. How do you scope a new project?
  2. How do you determine the preliminary milestones and timeline of a new project?
  3. How do you do a literature review for a new project?
       1. How do you find relevant papers?
       2. How do you read papers you do find? _Also see general paper reading question._

### Overall Commentary & Key Take-aways
*Under Construction*

### Specific Resources
#### [How to do good research, get in published in SIGKDD, and get it cited!](https://www.cs.ucr.edu/~eamonn/Keogh_SIGKDD09_tutorial.pdf)
This guide is largely focused on hos to structure projects for publication and impact, and is very related to
communication questions as well. It is thus also featured in the [communication](skill_modules/communication)
section of this guide, but it is very relevant here too!

#### [Stanford InfoLab Tips for Writing Technical Papers](https://cs.stanford.edu/people/widom/paper-writing.html)
This guide is a great starting point for writing technical papers. I particularly value their discussion on
the introduction, which states that an effective introduction must focus on answering five key questions:
  1. What is the problem?
  2. Why is it interesting and important?
  3. Why is it hard? (E.g., why do naive approaches fail?)
  4. Why hasn't it been solved before? (Or, what's wrong with previous proposed solutions? How does mine differ?)
  5. What are the key components of my approach and results? Also include any specific limitations.

I highlight this resource here (as well as in the [communications](communication) section) because you need to
do research such that you can eventual frame it into a compelling paper/project. Therefore, thinking about how
you would frame your project, even as you're just beginning the work, can help you structure the project
overall.

### Interview Highlights
*Under Construction*

## Finishing Projects
### Guiding Questions
  1. How much of time is spent at various stages and in various tasks of a project? E.g., how much time is
     spent doing ideation vs. literature review, experiment design, coding, writing, etc.?
  2. What is your general philosophy for working on an established project? E.g.,...
       1. To what extent do you have a running draft that is a "living" reflection of your project?
       2. Are you laser focused on the next minimum viable experiment, or are you more responsive to
          observations you make along the way?
       3. How do you trade-off time locally between experimentation, writing, figure design, etc.?
  3. When do you (drastically) pivot a project to something new?
  3. When do you give up on a project? When do you keep pushing?

### Overall Commentary & Key Take-aways
*Under Construction*

### Specific Resources

### Interview Highlights
*Under Construction*
