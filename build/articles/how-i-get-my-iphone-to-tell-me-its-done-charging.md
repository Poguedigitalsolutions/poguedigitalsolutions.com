---
title: How I Get My iPhone to Tell Me It's Done Charging
slug: how-i-get-my-iphone-to-tell-me-its-done-charging
description: iOS has no built-in full-charge alert, but the Shortcuts app can build one in a minute. Here's the setup, and why 80% is a better target than 100% for your battery.
author: John M Pogue
date: 2026-10-20
category: AI and Automation
reading_time: 3 min
keywords: iPhone full charge alert, iPhone battery notification, Shortcuts battery level automation, iPhone charge limit, optimized battery charging, iPhone battery health
---

# How I Get My iPhone to Tell Me It's Done Charging

**The short answer:** iOS has no built-in "fully charged" alert, but you can build one in about a minute with a Shortcuts automation that fires at a battery level you choose. Set it to 80% instead of 100%, because sitting at a full charge is what wears a lithium-ion battery down. On an iPhone 15 or newer, the Charge Limit setting does the job without any alert at all.

## A small question with a useful answer

This afternoon I plugged in my iPhone and wondered why it can't just tell me when it's full. I wanted to unplug it at 100% and stop cooking the battery on the charger for hours.

I approach every problem with curiosity, so the deep dive begins. iOS has no built-in "fully charged" alert. You can build one yourself in about a minute with the Shortcuts app, which is already on your phone. Along the way I learned that 100% isn't the number I should have been chasing.

## How to set up a full-charge alert

Here's the whole setup. No apps to buy, nothing to download.

1. Open the **Shortcuts** app and tap **Automation** at the bottom of the screen.
2. Tap **+** (or **New Automation**) and choose **Battery Level**.
3. Drag the slider to **100%**, pick **Equals 100%**, and select **Run Immediately** so it doesn't ask you every time.
4. Tap **Next**, then **New Blank Automation**.
5. Add the action **Show Notification** and type your message, something like "Fully charged. Unplug me."
6. Want to hear it from across the room? Add **Speak Text** as a second action.
7. Tap **Done**.

Next time your phone hits 100%, it taps you on the shoulder.

## What I learned: 100% is the wrong target

I grew up thinking you had to "condition" a battery by running it full and empty. That was true for older battery types. Your iPhone uses lithium-ion, and what wears it down is sitting at a high charge for long stretches, especially when it's warm.

Unplugging at 100% beats leaving it on the charger all night. Stopping around 80% is better still. So if you build the alert, set it to 80% instead of 100%. Same steps, different number.

If you have an iPhone 15 or newer, you may not need the alert at all. Go to **Settings > Battery > Charging** and set a charge limit between 80% and 100%. The phone stops charging near your limit and holds it there while plugged in. It will occasionally top off to 100% on its own, which helps it keep the battery reading accurate. That's normal.

On an older iPhone, turn on **Optimized Battery Charging** in the same menu. It learns your routine and holds at 80% until shortly before you usually unplug.

## The bigger lesson

I started with a tool question: how do I get an alert? The better question was the one I ask before every project. What are we trying to accomplish today? I wanted a longer-lasting battery. The alert was one way to get there, and the charge limit turned out to be a simpler one.

That's how I work with clients at Pogue Digital Solutions, LLC. Strategy comes before software. Once you know the goal, the right tool is usually already sitting on your phone or in your business, waiting for you to use it. Knowing where to look is where my skills come into play for your business.

If you try this, tell me in the comments which route you picked. And if you have a small process in your business you wish would just tap you on the shoulder, that's exactly the kind of problem I like to solve.

## References and further reading

- [About Charge Limit and Optimized Battery Charging on iPhone](https://support.apple.com/108055), Apple Support. Apple's own explanation of both settings, which iPhones support them, and why the phone sometimes charges past your limit.
- [Setting triggers in Shortcuts on iPhone or iPad](https://support.apple.com/guide/shortcuts/apde31e9638b/ios), Apple Shortcuts User Guide. The official walkthrough for automations like the Battery Level trigger used in this article.
- [BU-808: How to Prolong Lithium-based Batteries](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries), Battery University. The research behind the advice: sitting at a full charge stresses a lithium-ion battery more than normal use does, and a lower charge target extends its life.
- [Your iPhone Quietly Got a New Feature to Extend Its Battery Life](https://www.gearpatrol.com/tech/iphone-charge-limit-feature), Gear Patrol. A plain-English look at the Charge Limit setting and how the phone learns your habits.
