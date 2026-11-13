---
title: How to Write a Better AI Prompt: Lessons From a Peanut Butter and Jelly Sandwich
slug: how-to-write-a-better-ai-prompt
description: John M Pogue uses the peanut butter and jelly sandwich exercise, the old saying garbage in, garbage out, and his own missed request to show how to write a better AI prompt and how to check what the AI did.
author: John M Pogue
date: 2026-11-13
category: AI and Automation
reading_time: 5 min
keywords: AI prompt, how to write a better AI prompt, prompt engineering, prompting strategies, garbage in garbage out, prompt chaining, peanut butter and jelly exercise, checking AI output
---

# How to Write a Better AI Prompt: Lessons From a Peanut Butter and Jelly Sandwich

**The short answer:** An AI prompt is the instruction you type into an artificial intelligence (AI) tool. To write a better AI prompt, spell out each step you want, give one task per request, and then ask the tool to tell you what it did and what it left out. A vague prompt still gets an answer that sounds sure of itself, so the checking step matters as much as the asking.

## Why does a vague AI prompt get a poor answer?

A vague prompt gets a poor answer because the tool only has your words to go on. It cannot see the picture in your head.

Teachers have used a simple exercise for decades to prove this. They ask a class to write instructions for making a peanut butter and jelly sandwich. Then the teacher follows those instructions exactly as written. "Put the peanut butter on the bread" ends with the whole jar sitting on top of the loaf. Nobody said to open the jar, pick up a knife, or take out a slice.

The exercise was built to teach children how computers work. A 1999 classroom version from National Engineers Week, adapted from an Intel education kit, states the goal plainly: a computer follows a precise set of instructions and cannot fill in what you meant.

I thought of that sandwich in November 2026 while taking Google Cloud's Generative AI Leader training through Google Launchpad for Veterans, presented by VetNet, Google's veterans network, and taught by Patrick Haggerty of ROI Training. The class had reached the part on prompting, and the sandwich explained it better than any slide could. You know what you want. The tool only knows what you typed.

## What does "garbage in, garbage out" mean for AI?

"Garbage in, garbage out" means a computer's results can only be as good as what you feed it. The saying is older than most people think. Its earliest known appearance in print is a 1957 newspaper article about United States Army mathematicians working with early computers. George Fuechsel, an IBM programmer and instructor, is usually credited with spreading it in the early 1960s.

The saying still holds for AI, with one change that catches people off guard. An early computer given bad input gave back an error or plain nonsense, so you knew something was wrong. An AI tool given a vague prompt fills the gaps with a reasonable guess and hands back a polished answer.

I call that "vague in, confident out." The answer reads well, so you trust it, and the gap stays hidden until it costs you something.

## How do you break a big request into steps?

You break a big request into steps by naming each action in the order you want it done, the way a parent talks a child through a chore.

An old stand-up routine from the early 1980s shows it well. A mom wants her kids clean before bed, and she does not leave it at "go take a shower." Every night she walks them through it one move at a time: leave the table, head upstairs, undress, step in, and start the water. Any parent in the audience knew why.

People who work with AI have a name for this habit. They call it prompt chaining, which means splitting one big job into smaller requests and handing them over one at a time. Google lists it among the prompting techniques its Generative AI Leader exam covers.

The mom in the routine did not need the term. She had kids, and she knew that one big instruction leaves too much room for surprises. Personally, I was the King of Loopholes.

## How do you check what the AI did?

You check by asking the tool to tell you, in plain words, what it did and what it left out.

I learned this the hard way in November 2026. I was using Claude Duet, an AI assistant from Anthropic that was in preview at the time, to help me apply for accommodations. I gave it my request and it went to work. Before I moved on, I asked one clarifying question about what it had done.

The answer was eye opening. The main accommodation, the one that mattered most to me, had not been applied for.

Nothing on my screen had looked wrong. The form only allowed one accommodation per request, and I had asked for several at once. So I gave new directions: put in a separate request for each accommodation. That fixed it.

I think about how close I came to walking away. I would have believed the job was done, and I would have found out weeks later, when the thing I needed most never showed up. One question saved me from that.

## What does a better AI prompt look like?

A better AI prompt gives the tool what you would give a new coworker on day one. Anthropic suggests a simple test in its prompting guide: show your prompt to a colleague who knows little about the task and ask them to follow it. If they would be confused, the AI will be too.

Before you send a prompt, check it against this list:

1. **Say the goal.** Write one sentence on what you want and why you want it. Anthropic's guide says the reason helps the tool aim its answer.
2. **Give the background.** Say who the result is for, what you already have, and any limits.
3. **List the steps in order.** Name each action, the way the mom in the routine did.
4. **Give one task per request.** If the job has four parts, send four requests.
5. **Show an example.** If you have a sample of the result you want, include it. Anthropic's guide recommends three to five examples.
6. **Ask for a playback.** End with: "Tell me what you did and what you left out."

Steps one through five are the sandwich and the shower. Step six is the one most people skip, and it is the one that caught my missing request.

## Say what you mean, then ask what it heard

None of these habits started with AI. A teacher with a jar of peanut butter, a mom at bedtime, and an Army mathematician in 1957 were all teaching the same lesson: the one giving the instructions is responsible for making them clear. I like to say you never start from zero, and prompting is one more proof. The people who came before us already worked out how to give clear instructions. We only have to carry it forward.

The new part is the second half. AI tools answer with so much polish that it is easy to stop checking. So I now treat every request as a two-way conversation. I say what I mean, one step at a time. Then I ask what it heard.

That one extra question has saved me many times. I expect it will continue.

## References

- [The Microprocessor: Peanut Butter & Jelly Activity](https://gems.education.purdue.edu/wp-content/uploads/2019/01/The_Microprocessor_Peanut_Butter__Jelly_Activity.pdf), National Engineers Week (1999), hosted by Purdue University
- [Garbage in, garbage out (GIGO)](https://www.techtarget.com/searchsoftwarequality/definition/garbage-in-garbage-out), TechTarget, on the 1957 first use and George Fuechsel
- [Garbage in, garbage out](https://www.worldwidewords.org/qa-gar1.html), World Wide Words, on the history of the saying
- [*Bill Cosby: Himself*](https://en.wikipedia.org/wiki/Bill_Cosby:_Himself) (1983), "Same Thing Happens Every Night," the stand-up routine described above
- [Generative AI Leader certification exam guide](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf), Google Cloud, on prompting techniques including prompt chaining
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Anthropic, on the colleague test, giving reasons, and examples
- [Google Launchpad for Veterans](https://cloud.google.com/blog/topics/training-certifications/register-for-the-gen-ai-training-and-certification-program-for-veterans/), Google Cloud, on the no-cost Generative AI Leader training for veterans
- [Patrick Haggerty](https://www.linkedin.com/in/patrickhaggerty/), Director of Google Cloud Learning at ROI Training
- [ROI Training](https://www.roitraining.com/)

## Further Reading

Some links in this article are affiliate links. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.

**Start here if you are new to AI prompts**

- [*AI Prompt Engineering Absolute Beginner's Guide*](https://link.amazon/B05ZEqhIc) by Michael Miller (Addison-Wesley Professional, 2025). A plain-language walk through the parts of a good prompt, written for everyday users.

**Watch**

- [*The AI Doc: Or How I Became an Apocaloptimist*](https://link.amazon/B082QuHoz) (2026), directed by Daniel Roher and Charlie Tyrell. A father-to-be interviews the people building AI about its promise and its risks. Available to rent or buy on Prime Video as of November 2026.

**Go deeper if you build with AI**

- [*Prompt Engineering for LLMs*](https://link.amazon/B02yydSkn) by John Berryman and Albert Ziegler (O'Reilly Media, 2024). Written for people building apps on large language models (LLMs), the technology behind AI chat tools.

**From my instructor, for Google Cloud professionals**

- [*Google Professional Cloud Architect Study Guide*](https://link.amazon/B02cS2zQl) by Patrick Haggerty (O'Reilly Media, 2026). A guide to Google Cloud design and to passing the Professional Cloud Architect exam.
