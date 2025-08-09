Title: The Rapid Evolution of How We Interface with Models (And The Elephant Paths We Tread)
Date: 2025-07-08 20:30
Category: Blog
Tags: substack
Slug: the rapid evolution of how we interface with models (and the elephant paths we tread)
Source: Substack
Original-URL: https://www.greatcto.me/p/the-rapid-evolution-of-how-we-interface
Summary: !person about to touch waterhttps://images.unsplash.com/photo-1543341296-e988da5fe067?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaH...

[![person about to touch water](https://images.unsplash.com/photo-1543341296-e988da5fe067?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzM3x8dG91Y2glMjByZWZsZWN0aW9ufGVufDB8fHx8MTc1MTk3MjI1OHww&ixlib=rb-4.1.0&q=80&w=1080 "person about to touch water")](https://images.unsplash.com/photo-1543341296-e988da5fe067?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzM3x8dG91Y2glMjByZWZsZWN0aW9ufGVufDB8fHx8MTc1MTk3MjI1OHww&ixlib=rb-4.1.0&q=80&w=1080)

Photo by [Nazym Jumadilova](true) on [Unsplash](https://unsplash.com)

*Hi everyone,*

*Thank you for reading Great CTOs Focus on Outcomes. I publish weekly and have an archive of over 150 posts, each packed with valuable insights on various topics relevant to CTOs and the issues they face, distilled from my career experience.*

*I strive to make each post a helpful resource on the topic it focuses on so that when a CTO has a need, they can reference an atomic nugget of insight. To this end, I regularly revisit and refine posts, ensuring you always receive the best and most up-to-date information with the most clarity.*

```
If you’d like to support the growth of this resource, consider upgrading to paid and take advantage of the other ways I can help you.
```

[Subscribe now](https://www.greatcto.me/subscribe?)

# Observing My AI-Model Client Usage Patterns

In running my business, I have a lot to do to ensure it is viable. In addition to the direct value contributions, such as coaching and consulting, there are also marketing and sales activities, accounting, and other services.   
  
Unsurprisingly, given the nature of my business, much of the value my business provides relies on my knowledge, experience, and content. I utilise AI models to assist with various activities, but at the same time, I must be mindful of using tools that enhance rather than diminish the value I bring. I also don’t want models to replace my thinking, as this would provide my clients with less value and also atrophy my own thinking and learning capabilities in the process.   
  
I’ve adopted a range of practices for using models where I am either using the models to remove toil, such as repurposing something I’ve already created or leaning on the models to help improve my thinking by critiquing my work or providing different lenses over my work which I can use to expand my thinking and improve the robustness of the work.  
  
I started using LLMs more frequently when Bing integrated OpenAI’s models, along with some search capabilities. I had, of course, used LLMs before this, but it hadn’t become habitual until this point. So, I guess it was from the early days that I recognised the power that the combination of an LLM and tools presented - in this case, an LLM with access to more up-to-date information via search.  
  
I graduated to ChatGPT as the clients for this became more user-friendly, and also aggregators such as Poe, which had both text and image models in one place. Over time, I found more and more opportunities to help do the other tasks of running my business so I could focus on value delivery (and maximising the hours of work I am paid for).

## Writing Aesthetic and Later, MCP support: Enter Stage Right, Claude Desktop.

I used to use Claude Desktop a lot - it was front and centre during the period when I increased my use of models the most. However, change moves quickly in this environment of technological evolution, and my usage changed just as fast.  
  
I eventually shifted more of my use towards Claude as colleagues started to recommend it, particularly for its writing capabilities. Claude's models had an aesthetic to the prose they generated that I preferred over alternatives such as ChatGPT. I might have even been influenced by Claude's website and desktop visual aesthetics as well - non-threatening and homely earthen pottery tones that I am sure were well-researched as being calming to users coming to terms with what, in the early days, seemed akin to magic.   
  
Once MCP Server capabilities were added to the Windows Desktop client, my use of Claude over ChatGPT increased manyfold. There have been swings back and forth since. For instance, the significant improvement of ChatGPT’s image models has made it possible to create serviceable images with readable text for use in social media posts, birthday party invitations, or many other practical applications.

I also started introducing models into my orchestration tools, such as Rabbit Remix, Zapier and n8n. But most ideas start with something that can be experimented with, such as the Claude or ChatGPT web interfaces or their respective Windows desktop clients.

## As My Use of AI-coding IDEs Increased: Exit Stage Left, Claude Desktop.

After I started using AI-assisted software development tools, I found that I could accomplish many of the tasks I used to perform in Claude Desktop using those tools instead.

As I wrote in a recent post, [I found that with the MCP-wrapped APIs of many of the services I use regularly, I was able to interface with many of my day-to-day SaaS tools](https://www.greatcto.me/p/reclaiming-focus-why-saas-fatigue?r=6qaf&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) through this interface rather than directly through their web interfaces. This may prove disruptive to SaaS products over the long term.

One of the key reasons for the switch was that I found it quite brittle to configure the MCP Servers in Claude Desktop. You could get it done with a bit of patience, but it always took a bit longer due to syntax issues, copy-paste errors, human error, and so on.

The experience with VSCode-based editors, such as Cline, an AI-assisted software development extension for VS Code, revealed that many of these have a very resilient approach to installing MCP servers, as they utilise AI models to assist with the installation.

---

***CTO Life Line is a monthly Livestream conversation dedicated to helping CTOs move from barely surviving to thriving.***  
  
Co-hosts Daniel Walters and Noah Cantor stream episodes on LinkedIn and YouTube. Each episode delves deeply into a topic important to CTOs and has entertained a range of informative guests from around the world.

[Check out CTO Life Line](https://youtube.com/@ctolifeline-fh6br?si=UFBEq2Bd-whQYcAg)

---

Suppose it encounters an error in the syntax or identifies another issue, such as a permissions problem. In that case, it will attempt to resolve the issue and continue making changes and testing them until it has a proven working setup. That almost always results in a working MCP Server. The hit rate is thus much higher, and the time spent setting up a new MCP Server is much lower.

Additionally, you have access to all the other tools available in modern IDEs. So, if the model had made file changes, you could examine diffs, run linters and other verification tools, and utilise all the various other available tools.

For many of these tasks, an IDE may not be the ideal interface - it’s got a lot of chrome you don’t need; however, it does provide some hints about the capabilities a modern interface for interacting with models should feature.

# Desire Paths - From Bane of the Urban Planners to Useful Tool

In urban planning, there is the concept of desire paths, also known as elephant paths, which is presumably derived from the fact that elephants are considered some of the heaviest trampers of grass (despite humans having them well-covered in blades of grass).  
  
This concept has been well-publicised in design and later product circles, so I won’t spend too long rehashing what has been shared many times. You can read more about them here: <https://en.wikipedia.org/wiki/Desire_path>

[![undefined](https://substackcdn.com/image/fetch/$s_!cimS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc91eda6c-bfed-406c-89d8-b4f9a8969792_2560x1440.jpeg "undefined")](https://substackcdn.com/image/fetch/$s_!cimS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc91eda6c-bfed-406c-89d8-b4f9a8969792_2560x1440.jpeg)

Example from Wikipedia's Desire Paths page.

In the example above, it’s pretty apparent that the advantage people experience for this path over the concrete paths is one of a more direct route and one that’s a bit softer underfoot, to boot.

It reminds me of my earlier career, when I worked at Hitwise, an online consumer behaviour data analytics company. We could see user internet behaviour through anonymised taps on internet traffic. One trend we noticed was that many Google users used the search engine to navigate the internet, bypassing the URL bar in their browser. Initial responses to this observation were critical of these users, suggesting they were ignorant, as they didn’t even know how to use their browser.

But it occurred to some of us that these users weren’t stupid; they were pragmatic. The Google search box was positioned in the middle of the page and was large, not outside the main eyeline and competing with a smaller target, such as the browser bar. If you made a typo, Google would usually correct it and get you where you intended to go, anyway, thus being more resilient. Sound familiar?  
  
What is interesting is that it’s a typical response to fight these emergent behaviours rather than to embrace what they represent in terms of information. I recently saw this brilliant example courtesy of [Joaquín Peña Fernández](https://joapen.com/blog/)

[!](https://substackcdn.com/image/fetch/$s_!ODto!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cac2bac-25a6-4706-b9a7-85476f29c2a4_800x466.jpeg)

It looks like there’s been a progressive battle between the local council and the ‘elephants’. One wonders if there are even more bollards there today.

# So What Has This Got To Do With AI-models?

It’s interesting that, while the Claude Desktop client has progressed in terms of capability quite rapidly overall, it has been a few months without much significant improvement in how MCP configurations are managed. Additional debugging tools were added, but the configuration itself remains reliant on the manual editing of YAML files. You uttered the wrong incantation in the secret language of YAML formatting and invocations of npx and uv… but we will help you work out what you did wrong with developer-level tooling. It’s a world away from the core of the interface, which is chat.

This has left the usage of tools, via the explosion of MCP Servers which provide your AI assistant with access to thousands of tools and almost certainly many of the tools you use daily, primarily in the domain of more technically confident users and many less technically confident or time-poor individuals likely became discouraged by early attempts that resulted in error messages rather than successful tool configuration.

# What Does the Future Hold?

What does this mean for the future of interfaces such as Claude Desktop? Oddly, some of the most potent and accessible capabilities of LLMs are currently more usable in a development IDE than in the consumer-facing tool. Maybe the Desktop tool evolves. Perhaps it has reached the end of its life and needs to be replaced. Possibly, it remains a handy platform that allows for experimentation on how we best interface with the models.

## The Role of Foundational AI Providers such as Anthropic and OpenAI

Let me elaborate on that a bit further. I believe, with some evidence and application of strategic analysis, that the business model of the foundational AI providers is predicated on creating platforms for all of us to test and discover an adequate number of use cases to justify their astronomical investment levels and growth.

While I am convinced that AI-assisted development has changed software development forever, I am less sure about how all the other applications of generative AI models play out. There’s certainly utility - I am using them in a variety of ways in my business, as I mentioned, and I'm sure many others are. However, that doesn’t mean that the aggregate of these use cases and their revenue balances the massive scale of investment being deployed towards these companies by investors.  
  
To extend this further, I am also reasonably sure that these companies do not necessarily believe the user interfaces in these AI models today are what we will be using, as use cases are discovered and commoditised. The prices they charge to support these services stabilise as a result. It’s also not written in stone that the path to how we consume models in the future is dependent on these companies. Sure, the scale of investment stacks the deck in their favour, but maybe our elephant paths take us somewhere else.  
  
To my mind, I’d be pretty comfortable if the models became more open and more local and less of their management was consolidated into the hands of a few. Perhaps some capabilities will be impractical to manage this way, but many of today’s applications could be, with lower power draw and centralisation of data and IP. It remains to be seen what happens to tomorrow’s capabilities and use cases.

## What could this Mean For Software Interfaces?

What is most interesting to me is what happens to the user experience of software. That’s the question that drew me into software over three decades ago. We interact with software in numerous aspects of our lives. Some things have become easier - we can engage services that enrich our lives much more easily. Some things have become worse - for instance, we seem to have reached a peak in the time spent authenticating into things, despite the rise of biometrics and other tools that should have made things simpler and faster. We use so many more software tools today, and some terrible choices in IT security theatre have meant that, in aggregate, it’s still worse.

Part of the user experience challenges that software has presented for decades is its static nature, where a paradigm is chosen for a given software package because, at least, it is learnable. Unfortunately, with many more discrete software packages in use on average by individuals, the cognitive load involved in adapting to understand how each piece of software needs to be interacted with to achieve the user’s goals has increased.

The mix of deterministic and organic properties in a stochastic model presents interesting possibilities for how people may interact with software in the future, potentially leading to more humane and adaptable systems that can accommodate the user's ergonomics rather than the other way around.

It’s equal parts intriguing and terrifying.

[Share](https://www.greatcto.me/p/the-rapid-evolution-of-how-we-interface?utm_source=substack&utm_medium=email&utm_content=share&action=share)

*How are you currently interfacing with AI models, and how do you think this interaction may evolve in the future? Share your experiences and perspectives in the comments.*

[Leave a comment](https://www.greatcto.me/p/the-rapid-evolution-of-how-we-interface/comments)

```
If you enjoyed this publication, please help others find us and benefit from the insights.
```

[Share Great CTOs Focus on Outcomes](https://wioota.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

*Originally published on [Substack](https://www.greatcto.me/p/the-rapid-evolution-of-how-we-interface)*