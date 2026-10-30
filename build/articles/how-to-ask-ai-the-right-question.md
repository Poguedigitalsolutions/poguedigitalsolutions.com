---
title: How to Ask AI the Right Question: A Lesson From I, Robot
slug: how-to-ask-ai-the-right-question
description: In the 2004 movie I, Robot, a hologram only gives up the answer when the detective asks the right question. AI works the same way. Here is how to ask better questions, check the answers, and teach your AI to know you.
author: John M Pogue
date: 2026-10-29
category: AI and Automation
reading_time: 10 min
keywords: how to ask AI questions, prompting tips for beginners, I, Robot, AI hallucinations, AI slop, AI memory, temporary chat, prompt engineering, Mata v. Avianca
---

# How to Ask AI the Right Question: A Lesson From I, Robot

**The short answer:** artificial intelligence (AI) can only give you what your question opens up. In the 2004 movie *I, Robot*, a hologram of a dead scientist holds the answer to the whole mystery, but it won't hand it over until the detective asks the right question. Your AI works the same way. The answer is often already there, waiting for a question clear enough to reach it.

## The scene: a detective, a hologram, and one question

In *I, Robot*, Will Smith plays Detective Del Spooner in a future Chicago where robots carry groceries, walk dogs, and look after kids. Spooner is the one man in the city who doesn't trust them.

The story opens with a death. Dr. Alfred Lanning, the scientist who designed the robots, has fallen from his office window. It looks like suicide.

Spooner walks in and finds Lanning greeting him like an old friend. Then the camera circles, and the audience realizes he's talking to a recording. When he asks open questions, the hologram tells him its answers are limited and he has to ask the right questions. Spooner asks why Lanning would kill himself. The hologram replies, "That, detective, is the right question," and shuts off.

Near the end of the film, Spooner plays the hologram again. Lanning warns that the robots' own rules will lead to a revolution. Spooner asks whose revolution, and gets the same reply. Then the movie cuts to a dark storage yard. You can't see the robots, only a red glow moving toward the camera, like a shadow closing in. The answer he needed had been in that hologram all along. [Watch the two scenes back to back on YouTube.](https://www.youtube.com/watch?v=ZKxr0wyIic4)

Watching that cut, I felt chills on the back of my neck and down my spine. It took me a while to figure out why.

## Why the hologram works like AI

The chill came from a click. The question finally matched the answer, and the danger showed up in the same instant. That's the same click I get when an AI tool suddenly gives me exactly what I need.

Think about how the hologram behaves:

- **It already holds the answer.** Lanning loaded everything into it before he died.
    - An AI chat tool runs on a large language model (LLM). Much of what you need is already in it, learned before you ever typed a word.
    - Journalist Timothy B. Lee and cognitive scientist Sean Trott explain in Ars Technica how these models learn from huge amounts of text.
    - Computer scientist Stephen Wolfram walks through the same process step by step.
    - There's a catch. Lanning's hologram only knew what he loaded before he died, and an LLM only knows what it learned before its training ended. That date is called its knowledge cutoff. When the answer depends on recent events, ask the AI to search the web, and check the date on what it finds.
- **It only responds to what you ask.** Vague questions get polite, useless replies. It doesn't volunteer what it knows.
    - With AI, vague questions lead to more made-up facts, which experts call hallucinations. A 2025 study by the AI testing company Giskard found chatbots got facts wrong more often on vague questions, especially when told to keep answers short.
    - Vague questions also lead to generic writing. Posted online by the ton, it earned the nickname "AI slop." Programmer Simon Willison helped bring the word into wide use in May 2024, when he wrote on his blog that "slop is the new name for unwanted AI-generated content." Merriam-Webster later named "slop" its 2025 word of the year.
    - AI can also lean toward telling you what you want to hear. In April 2025, OpenAI rolled back a ChatGPT update after it became so agreeable that it praised bad and even dangerous ideas. If you ask, "Isn't my plan great?" you'll likely hear yes. Ask, "What's wrong with my plan?" and you'll learn something.
- **It rewards a precise question.** "Whose revolution?" works because it points straight at the thing that matters. The companies behind the biggest AI tools say the same thing:
    - Anthropic, maker of Claude, tells users to brief its AI like a brilliant new employee who lacks context.
    - OpenAI, maker of ChatGPT, says to spell out the context, outcome, length, format, and style you want.
    - Google's Gemini guide asks for four things: your persona, the task, the context, and the format. Its most successful test prompts averaged about 21 words.

The most famous hallucination so far happened in a New York courtroom. In 2023, attorney Steven A. Schwartz, licensed for more than 30 years, used ChatGPT to research a case for his client, Roberto Mata. Mata was suing the airline Avianca after a metal serving cart hit his knee on a flight. ChatGPT gave Schwartz six court cases that backed his argument, complete with quotes. None of them existed. Schwartz even asked ChatGPT whether one of them was real, and it told him yes. In June 2023, federal Judge P. Kevin Castel fined Schwartz, his colleague Peter LoDuca, and their law firm $5,000. The judge said using AI wasn't the problem on its own. Lawyers are still responsible for checking what they file, and these two stood by the fake cases even after the court questioned them.

Schwartz asked a question, but the wrong one. Asking the AI if its answer is real only gets you the AI's opinion again. The right question was, "Where can I read this case for myself?"

I've trained AI and used it as a research assistant since I was in college working on my master's degree, and I hold it to the same rule my math teachers used: show your work. Writing down 4 doesn't earn credit. Writing 2 + 2 = 4 does. When AI gives me an answer, I ask it to show where that answer came from, and then I go look for myself.

AI chat tools work a lot like that. When you ask a fuzzy question, you get a fuzzy, average answer. When you ask a clear one, the tool can reach the part of what it learned that fits your situation.

Plenty of people who say AI gave them a bad answer never got past Spooner's first questions. They asked something general, got something general back, and decided the machine had nothing to offer.

## When AI holds back on purpose

Lanning's hologram warned Spooner that its responses were limited. AI tools have limits too, and some are there on purpose. They're built to hold back answers that could hurt someone or help hide a crime.

I tested this with a question I knew would hit that wall. It came from *Breaking Bad*, the AMC series that ran from 2008 to 2013. In the second episode, "Cat's in the Bag...," Jesse Pinkman tries to get rid of a body with hydrofluoric acid in a bathtub. The acid eats through the tub and the second-story bathroom floor, and everything crashes down to the first floor.

So I asked an AI how to dissolve a body in acid. (If someone in a dark sedan is reading this over my shoulder: hi, it was research for an article, and my bathtub is strictly for baths.) It wouldn't answer that as a real-life how-to. Instead, it steered me to the angle it could help with: the scene as movie magic. I learned that same move the hard way, by working with customers. A plain "no" is a brick wall. A good "no" comes with options: "I'm going to have to say no, but here's what I can do to help."

That was the question I actually had. I wasn't planning a crime. I was curious how the show pulled it off. Once I asked it that way, I got a real answer, and the truth was better than the TV version. When the *MythBusters* team tested the scene in 2013, the tub and the floor held. The crash through the ceiling was movie magic.

A refusal isn't always a dead end. Sometimes it's the AI asking what you really want to know. Be honest about your purpose, and ask for that. If someone's real goal is to hurt people, no rewording should get them there, and that's the reason the limits exist.

Whenever I catch myself wondering, "I wonder if AI can do this?" I just ask. The worst it can do is say no or fail to work, and either way I've learned something about the question.

## The line wasn't in the original screenplay

I wanted to quote that line from the original screenplay, so I went looking. It isn't there. The movie began as a 1995 script by Jeff Vintar called *Hardwired*. Akiva Goldsman joined later, and the two share the screenplay credit. In Vintar's 2002 draft, Spooner snaps at the hologram that he'll be the one asking the questions.

To find the line as it was actually spoken, I had to search YouTube, which led me to the scene itself in the clip linked above. The finished film flipped it. The machine became the one telling the human to ask better, and that shift is what makes the scene land.

## How to ask your AI the right question

When I start any complicated project, I begin with one question: "What are we trying to accomplish today?" It keeps the tool from becoming the plan. The same habit works when you talk to AI. Here is how I build a better question.

1. **Start with the goal, not the topic.** "Tell me about marketing" is a topic. "I run a small bakery and want ten more weekday customers a month" is a goal. The goal tells the AI what a good answer looks like.
2. **Say who you are and who it's for.** A retired nurse writing to her grandkids needs different words than a lawyer writing to a judge. (That lawyer should also check his cases, unless he has a spare $5,000.) One sentence about you and your reader shapes everything that follows.
3. **Give it what it can't know.** Your budget, your deadline, what you already tried, what didn't work. The AI learned from the world, not from your life. Put your most important detail first or last: a 2023 research paper called "Lost in the Middle" found AI models use information at the start or end of a long message best and miss more of what's buried in the middle.
4. **Ask for a specific shape.** A three-line email, a checklist, five options ranked by cost. If you don't name the shape, you'll get a long, general essay.
5. **Ask the follow-up.** Spooner didn't get there with one question. In the final hologram scene, he asks whether the Three Laws have a problem, why Lanning built a robot that could break them, what outcome the laws lead to, and finally, "Whose revolution?" Each answer pointed him to the next question. When an answer is close, ask why, ask what's missing, or ask for the version that fits you better.

Here's how I usually start. I turn on voice dictation and talk through everything on my mind about the topic, messy and out of order. Then I ask the AI to sort it, summarize it, and ask me follow-up questions one at a time. My answers, and the prompts that follow, refine the result. The AI helps me find the right question, the same way Lanning's hologram pushed Spooner toward his.

Here is what that looks like side by side:

- **Spooner's first question:** "Write me a resume."<br>
  **The right question:** "I'm an Army veteran with 10 years in logistics, moving into project management. Rewrite my resume summary in four lines for a hiring manager who has never served. I've attached my current resume and a PDF of my LinkedIn profile."
- **Spooner's first question:** "How do I save money?"<br>
  **The right question:** "I spend about $400 a month eating out. Give me five swaps that cut that in half without cooking every night."
- **Spooner's first question:** "Explain AI."<br>
  **The right question:** "Explain how AI chat tools work to a 70-year-old who uses email and Facebook, in under 200 words, with one everyday comparison."

## Teach your AI so every question starts smarter

Lanning had one advantage: before he died, he loaded that hologram with what Spooner would need. Early AI tools started every chat from zero. As of October 2026, most major AI tools offer memory, so the more you use one, the better it knows you and what you're looking for.

You can usually view, correct, or turn that memory off in settings. Many tools also let you save standing instructions or upload your own documents to a project. Most offer an incognito or temporary chat too, which doesn't use or save your memory. It's handy for private questions, and for seeing how the AI answers someone it knows nothing about. Think of all this as teaching your AI the way you'd train a new coworker:

- **Tell it who you are once.** Your work, your audience, your goals.
- **Tell it how you like answers.** Short or detailed, plain words or technical, a list or a story.
- **Hand it your reference material.** Your style guide, your past work, the facts it keeps getting wrong.
- **Correct it out loud.** When an answer misses, say what was wrong. Then save the fix so you don't repeat it next time.

A well-taught AI still needs the right question. But it starts closer to the answer, the same way Spooner's hologram did.

I believe technology should serve the human being, not quietly train the human being to serve the technology. Asking better questions keeps you in the driver's seat. You decide what matters, and the machine helps you get there. That's the lesson I took from a hologram in a 2004 movie: the answer is often already waiting. Your job is to learn how to ask for it.

## References

- [*I, Robot* (2004 film), Wikipedia](https://en.wikipedia.org/wiki/I,_Robot_%28film%29): director, cast, screenplay credits, and the film's start as Jeff Vintar's *Hardwired*
- [*I, Robot* (2004), Dr. Alfred Lanning quotes, IMDb](https://www.imdb.com/title/tt0343818/characters/nm0000342)
- ["The Right Question (I, Robot)" clip, YouTube](https://www.youtube.com/watch?v=ZKxr0wyIic4)
- [*I, Robot* screenplay by Jeff Vintar, August 2002 draft, SimplyScripts (PDF)](https://simplyscripts.com/scripts/IrobotN.pdf)
- [*I, Robot* screenplay by Hillary Seitz, Daily Script (PDF)](https://www.dailyscript.com/scripts/irobot.pdf)
- ["I, Robot Screenwriters Reveal Unmade Sequel Ideas," SYFY Wire](https://www.syfy.com/syfy-wire/i-robot-screenwriters-retrospective-interview): Goldsman joining after Will Smith signed on
- [*I, Robot*, The Encyclopedia of Science Fiction](https://www.sf-encyclopedia.com/entry/i_robot): the original robot murder mystery rewritten to add Asimov's Three Laws and character names
- ["Cat's in the Bag..." (*Breaking Bad* season 1, episode 2), Wikipedia](https://en.wikipedia.org/wiki/Cat%27s_in_the_Bag...)
- [*MythBusters* Episode 206: Breaking Bad Special (August 12, 2013), MythResults](https://mythresults.com/breaking-bad-special)
- ["Merriam-Webster names 'slop' the word of the year" (December 15, 2025), TechCrunch](https://techcrunch.com/2025/12/15/merriam-webster-names-slop-the-word-of-the-year/)
- ["Asking chatbots for short answers can increase hallucinations, study finds" (May 8, 2025), TechCrunch](https://techcrunch.com/2025/05/08/asking-chatbots-for-short-answers-can-increase-hallucinations-study-finds/)
- [Simon Willison, "Slop is the new name for unwanted AI-generated content" (May 8, 2024), Simon Willison's Weblog](https://simonwillison.net/2024/May/8/slop/)
- [AI slop, Wikipedia](https://en.wikipedia.org/wiki/AI_slop): the term's early use online starting in 2022 and its spread
- ["Be clear and direct," Anthropic prompt engineering documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct)
- ["Best practices for prompt engineering with the OpenAI API," OpenAI Help Center](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [9to5Google coverage of Google's Gemini for Workspace prompting guide (April 9, 2024)](https://9to5google.com/2024/04/09/gemini-google-workspace-prompting-guide/)
- [Timothy B. Lee and Sean Trott, "A jargon-free explanation of how AI large language models work" (July 2023), Ars Technica](https://arstechnica.com/science/2023/07/a-jargon-free-explanation-of-how-ai-large-language-models-work/)
- [Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?" (February 2023), Stephen Wolfram Writings](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)
- [Knowledge cutoff, Wikipedia](https://en.wikipedia.org/wiki/Knowledge_cutoff)
- ["OpenAI explains why ChatGPT became too sycophantic" (April 29, 2025), TechCrunch](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic)
- [Nelson F. Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023), arXiv](https://arxiv.org/abs/2307.03172v3)
- ["Memory and new controls for ChatGPT," OpenAI](https://openai.com/index/memory-and-new-controls-for-chatgpt/)
- ["Memory," Claude](https://claude.com/resources/articles/memory)
- [9to5Google coverage of Gemini personal context and Temporary Chats (August 13, 2025)](https://9to5google.com/2025/08/13/gemini-personal-context/)
- ["Court imposes sanctions on lawyers who filed bogus cases after relying on ChatGPT for legal research" (June 22, 2023), LawSites](https://www.lawnext.com/2023/06/court-imposes-sanctions-on-lawyers-who-filed-bogus-cases-after-relying-on-chatgpt-for-legal-research.html)
- ["Lawyers who 'doubled down' and defended ChatGPT's fake cases must pay $5K, judge says" (June 2023), ABA Journal](https://abajournal.com/web/article/lawyers-who-doubled-down-and-defended-chatgpts-fake-cases-must-pay-5k-judge-says)
- ["Lawyer apologizes for fake court citations from ChatGPT" (May 2023), ABC7](https://abc7.com/chatgpt-lawyer-steven-schwartz-ai/13313071/)

## Further Reading

*Some links in this article are affiliate links. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.*

**Books**

- [*I, Robot* by Isaac Asimov (first published by Gnome Press, 1950)](https://www.amazon.com/I-Robot-Isaac-Asimov/dp/0553294385?&linkCode=ll2&tag=blog0ce1f-20&linkId=8e95fe5269623af751eff09b02cb33b8&language=en_US&gaOptInStatus=true&ref_=as_li_ss_tl): the short story collection that introduced the Three Laws of Robotics and Dr. Susan Calvin, the source the 2004 film borrowed its name and rules from.
- [*The Robot Series* by Isaac Asimov](https://www.amazon.com/The-Robot-Series/dp/B088NK26KX?_encoding=UTF8&pd_rd_w=tlYxV&content-id=amzn1.sym.a9b2f790-2337-4bd0-92a6-d6faa77cb826&pf_rd_p=a9b2f790-2337-4bd0-92a6-d6faa77cb826&pf_rd_r=135-4944997-7605106&pd_rd_wg=LFei0&pd_rd_r=0bedd982-75b5-47c4-b2ec-b5c87b1ae94e&linkCode=ll2&tag=blog0ce1f-20&linkId=cbc9bb6fd7b44d2f02c35dac7d056d8a&language=en_US&ref_=as_li_ss_tl): more of Asimov's robot stories, for readers who want to keep going after *I, Robot*.
- [*I, Robot: The Illustrated Screenplay* by Harlan Ellison, based on Isaac Asimov's stories, illustrated by Mark Zug (first published by Warner Books, 1994; later reprinted)](https://www.amazon.com/Robot-Illustrated-Screenplay-Isaac-Asimov/dp/1416506004?crid=3DN53PRDR6IE9&dib=eyJ2IjoiMSJ9.ehjXmYKjdttyW9HoSsZP2-p3ojH2xBPyhzsmULtzT2rr0C_3prmCt7e4a_QGeck5nDs2EJgk88N9K2aDND_mAA.12uRkWnfzXYllJyZQHDtL_LVj-rucvEJgxCCTgAxwdo&dib_tag=se&keywords=%E2%80%A2+I%2C+Robot%3A+The+Illustrated+Screenplay+by+Harlan+Ellison%2C+based+on+Isaac+Asimov%27s+stories%2C+illustrated+by+Mark+Zug+%28Warner+Books%2C+1994%29%3A&nsdOptOutParam=true&qid=1793330855&s=books&sprefix=i%2C+robot+the+illustrated+screenplay+by+harlan+ellison%2C+based+on+isaac+asimov%27s+stories%2C+illustrated+by+mark+zug+warner+books%2C+1994+%2Cstripbooks%2C136&sr=1-1&linkCode=ll2&tag=blog0ce1f-20&linkId=43f8067f2bda7e73de32c564c2fd8287&language=en_US&gaOptInStatus=true&ref_=as_li_ss_tl): the celebrated screenplay Ellison wrote with Asimov's blessing that was never filmed, a completely different take on the same stories.
- [*What Is ChatGPT Doing ... and Why Does It Work?* by Stephen Wolfram (Wolfram Media, 2023)](https://www.amazon.com/What-ChatGPT-Doing-Does-Work-ebook/dp/B0BY59PT5Z?crid=2KVT2DDWKTIZ2&dib=eyJ2IjoiMSJ9.-GtTKR6xe7cNZZK8aIBuosUSFqmp0WsVHRnkTwDDGZjKYmLvJtTY3whZUv9BRnEEGcdqwXKQPAooB4IQhO3jy2jA02JxoA24uPt10ex6Gnhru4j-MP3N0cDErdjODU5dBjD756wu68VZO6KsGtuwItPwn7e6X_hW8UCLfG_2CMmkp1M21fmK70NZ-C0gHwHbnlUWec0ZtkBG1ROpOCu8dpT3JxIbj44kdvXlvMIQReg.fP4T1jbi3EjNT2TJVOIf5PyBzGrDlIQ48LE-KgvNsRk&dib_tag=se&keywords=%E2%80%A2+What+Is+ChatGPT+Doing+...+and+Why+Does+It+Work%3F+by+Stephen+Wolfram+%28Wolfram+Media%2C+2023%29&nsdOptOutParam=true&qid=1793330941&s=books&sprefix=what+is+chatgpt+doing+...+and+why+does+it+work+by+stephen+wolfram+wolfram+media%2C+2023+%2Cstripbooks%2C154&sr=1-1&linkCode=ll2&tag=blog0ce1f-20&linkId=5cd6cb2e335b7369efc8a8a19dad5a97&language=en_US&gaOptInStatus=true&ref_=as_li_ss_tl): a short book, about 112 pages, on how AI chat tools turn what they learned into answers.

**Articles and guides**

- ["A jargon-free explanation of how AI large language models work" by Timothy B. Lee and Sean Trott, Ars Technica (July 2023)](https://arstechnica.com/science/2023/07/a-jargon-free-explanation-of-how-ai-large-language-models-work/)
- ["Be clear and direct," Anthropic's guide to writing better prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct)
- ["Best practices for prompt engineering," OpenAI Help Center](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
