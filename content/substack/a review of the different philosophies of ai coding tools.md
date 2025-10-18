Title: A Review of The Different Philosophies of AI Coding Tools
Date: 2025-08-10 20:30
Category: Blog
Tags: substack
Slug: a review of the different philosophies of ai coding tools
Source: Substack
Original-URL: https://www.greatcto.me/p/a-review-of-the-different-philosophies
Summary: !gray stone stack on gray rockhttps://images.unsplash.com/photo-1585589292739-37a1df63b0c9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlY...

[![gray stone stack on gray rock](https://images.unsplash.com/photo-1585589292739-37a1df63b0c9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyNHx8cGhpbG9zb3BoZXIlMjdzJTIwc3RvbmV8ZW58MHx8fHwxNzU0Mzg0MTYyfDA&ixlib=rb-4.1.0&q=80&w=1080 "gray stone stack on gray rock")](https://images.unsplash.com/photo-1585589292739-37a1df63b0c9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyNHx8cGhpbG9zb3BoZXIlMjdzJTIwc3RvbmV8ZW58MHx8fHwxNzU0Mzg0MTYyfDA&ixlib=rb-4.1.0&q=80&w=1080)

Photo by [Aubrey Odom](true) on [Unsplash](https://unsplash.com)

*Hi everyone,*

*Thank you for reading Great CTOs Focus on Outcomes. I publish weekly and have an archive of over 150 posts, each packed with valuable insights on various topics relevant to CTOs and the issues they face, distilled from my career experience.*

*I strive to make each post a helpful resource on the topic it focuses on so that when a CTO has a need, they can reference a self-contained and referenceable nugget of insight. To this end, I regularly revisit and refine posts, ensuring you always receive the best and most up-to-date information with the most clarity.*

```
If you’d like to support the growth of this resource, consider upgrading to paid and take advantage of the other ways I can help you.
```

[Subscribe now](https://www.greatcto.me/subscribe?)

```
This post is an active draft. I am sharing it early so I can improve it as a resource with your feedback. I will continue to refine the descriptions, terminology and the table of tools so it can be the best possible reference for understanding the different philosophies of these tools and choosing which may best fit your needs.
```

There’s an explosion of tools in the sphere of AI-assisted software development. It’s frankly overwhelming.

As I've shared in previous posts, if you want any hope at all of learning these tools, I suggest you don’t try to keep up with the news announcements. It’s too easy to fall into the trap of trying to start with a tool and then look for a problem to solve with it, and before you do, see the next bit of news and start something new and so on… Something better always seems to come along.

What I will attempt in this post is to give you a framework of some choices when selecting tools for types of problems and where you are on your learning journey.

# The Different Philosophies of AI-assisted Software Development Tools

There are several different dimensions by which the various AI-assistance tools differentiate themselves. There may be more, but some of the most material differences I’ve identified are as follows:

* Who is providing the tool
* Form Factors
* Model Selection
* Agents / Modes
* Sub-Agent support
* Task decomposition and orchestration
* Opinionated Practices & System Prompts

## Who is providing the tool

Who provides the tool and how can significantly impact the capabilities available and the nature of integrations available.

There is a wide array of ways in which the creation and improvement of these tools are being supported:

* As open source (a collective effort from individuals and companies - note, many of these are quickly co-opted by a dominant organisation that is monetising the tool in some way)
* By a company focused only on that tool (Cursor, Kilo).
* By a more general software development tool company (SourceGraph, Cognition)
* and other cases, it's backed by a “FAANG“ Company (Amazon, Google, etc.) or a Foundation model provider (OpenAI, Anthropic, etc.).

## Form Factors

* Integrated Development Environments (IDEs) - Forks and Extensions
* Command Line Interfaces (CLIs)
* Ambient (Event-driven)
* Other

### Integrated Development Environments (IDEs) - Forks and Extensions

The most obvious starting point for developers is to begin with either extensions to their IDE, whatever they are using, whether it be VSCode, Jetbrains, NeoVim, Zed, Emacs or something else.

Some of the most popular options are forks of popular IDEs - Cursor and Windsurf both being forks of VS Code (an obvious candidate as a very popular Open Source Software option from Microsoft), which has the benefit of parity with most modern IDE capabilities that are expected, as well as support for compatible extensibility options such as plugins and extensions that those ecosystems support.

### Command Line Interfaces (CLIs)

More recently, there has been an explosion of CLI options following the lead of examples such as Claude Code. These tools anticipate the post-IDE era, where the way that people interface with AI-coding models is sufficiently different from how they have been interfacing with code previously.

### Ambient (Event-driven)

The popularity of Devin suggests there is another mode of interaction with coding models, and that we could describe as a ‘virtual teammate’ or, as we have in this post, as Ambient.

### Other

I will use a catch-all category to describe some other options I have observed, which are present but less common.

* Use of Desktop Assistants such as Claude Desktop with tools such as Model Context Protocol Servers (MCPs), which have access to local filesystem or remote repositories for delivering code. I wouldn’t recommend it, but I also can’t say I haven’t done it. As I wrote previously, [there’s something powerful about being able to interface across many systems in one interface layer](https://www.greatcto.me/p/reclaiming-focus-why-saas-fatigue?r=6qaf&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false), so yes, I have, on occasion, edited files through Claude Desktop.
* Programmatically. Yes, you can call your model directly through code you write and instruct it to make changes to code, so at times, I am sure this happens.
* Through AI workbenches, studios and other tools designed for working with models, for fine-tuning, for evaluations, etc.

## Model Selection

Whether the tool is built around the idea of supporting a Model Switcher or not can be a significant difference maker in terms of the effectiveness of the tool.

Model Switching can be great for cost management, flexibility, taking advantage of new models or remaining productive when there are shifts in reliability.

Tools focused on a few specific models for particular responsibilities can fine-tune system prompts and patterns specifically for the capabilities of those models and often correlate with improved developer satisfaction with the tools, even when models rate worse on benchmarks (e.g. Claude Code, Amp)

## Agents / Models

Another philosophical difference that’s worth noting is the choice of some tools providing different modes, while others deliberately choose not to.

At one end of the spectrum is the excellent Cline - a VS Code extension which features just two modes - ‘Plan’ and ‘Act’. These modes, as well as features such as its excellent MCP support, make Cline a fantastic tool to start learning and practising AI-coding with.

To be explicitly planning because you are in the ‘plan’ mode can give you some confidence that the tool is building up good context on what you are trying to achieve. You can explicitly switch to have it generate code once you are confident in the plan that you have developed, with the assistance of the model. The model you use for each mode in Cline can be different.

Roo Code, which happens to be a fork of Cline (as its open source software - OSS), expands the number of modes to be more like different types of activities you might undertake, such as an architect, asking a question, debugging, etc. Roo is very configurable and allows for specific models and settings to be defined per mode.  
  
Some tools may not have implemented any modes. That could be because they are simpler tools, or in some cases, it’s a deliberate choice. A case in point is Amp. Amp has chosen to provide agent functionality, which the model can choose to use or the user can encourage the model to use with their prompt. It creates some additional learning for the user, but in practice it’s a powerful paradigm.

## Sub-agents & Tool-calling

Amp, Claude Code and other tools also support the concept of sub-agents. This is likely calling another model with fresh context. One of the most significant issues with tools output matching your intent is the issue of Context Rot, where the context window is filled, and the performance of the model worsens.

The model the user is interacting with, being able to pass a smaller amount of context to another model with its context, allows for less context being consumed by the master model, and the sub-agent model uses only a small amount of its context to complete the task it’s been set. These can run in parallel, so that particular tasks that could be implemented independently may be delegated to several sub-agents to do, and they pass back the result once they are done.

I refer to tool-calling because one way you can achieve something similar is to have a tool call to another model. The main model passes a prompt to a tool, which provides it to a separate model.

## Task Decomposition & Orchestration

I haven’t included Task decomposition & orchestration on the table, as most of the tools include an approach to this now. What I mean by the phrase ‘Task Decomposition & Orchestration’ is the capability of the tools to break a plan into smaller tasks and work through those tasks systematically. This allows content to be much more focused on specific tasks, reducing the likelihood of triggering Context Rot.

Some of the tools apply this approach during a specific planning mode (e.g. Cline). Others have the model under the direction of the system prompts and what is interpreted from the user prompts to determine when it’s planned adequately and when to start executing on that plan (e.g. Amp).

## Opinionated Practices & System Prompts

Another differentiator in these tools is the degree to which the creators have strong opinions on the way the tools and models should be applied in development and how these translate into the system prompts (i.e. prompts that the tools have defined to give the models direction on how to behave).  
  
The models are very capable of producing code even without being wrapped in a tool, so a tool at its simplest could exist without a system prompt contributed by the tool developer. It would just operate with the user prompt provided. This marks one end of the spectrum, with the tools listed at various points along the spectrum.

It’s hard to assess this dimension without extracting all the system prompts, so I haven’t featured it on the table at this stage. Nonetheless, it's a dimension the tools could be evaluated on, and one you will get a feel for when using various tools and comparing the experience.

---

[!](https://substackcdn.com/image/fetch/$s_!hTXp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f061880-2ebd-4b14-be7b-4c276058ead3_1707x282.jpeg)

[Weekly Livestream on AI's Impact on Work](https://www.youtube.com/@hyprlive)

---

```
This post is an active draft. I am sharing it early so I can improve it as a resource with your feedback. I will continue to refine the descriptions, terminology and the table of tools so it can be the best possible reference for understanding the different philosophies of these tools and choosing which may best fit your needs.
```

[Share](https://www.greatcto.me/p/a-review-of-the-different-philosophies?utm_source=substack&utm_medium=email&utm_content=share&action=share)

*What were the factors that influenced your tool choices? Which of these factors will influence your decisions? What did I get wrong in my table or the descriptions of the different facets? Sound off in the comments.*

[Leave a comment](https://www.greatcto.me/p/a-review-of-the-different-philosophies/comments)

```
If you enjoyed this publication, please help others find us and benefit from the insights.
```

[Share Great CTOs Focus on Outcomes](https://wioota.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

*Originally published on [Substack](https://www.greatcto.me/p/a-review-of-the-different-philosophies)*