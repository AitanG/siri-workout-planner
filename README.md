# Siri workout planner

This repo contains the code for a mini app I made to plan my workouts. It uses Siri as the interface, computes the optimal next set of exercises based on my workout history, and sends me a push notification with my full workout plan.

I was inspired to build this when I learned that by doing the same set of exercises over and over again, I wasn't being very efficient with the time and energy I was spending in the gym. I used to like repeating the same dozen or so exercises because it would reduce the cognitive burden of deciding what to do next. This app removes that cognitive burden essentially by outsourcing it to a Python script hosted in Google Cloud Functions, which instantly ranks hundreds of exercises 6-12 times per workout in order to generate a plan that exactly fits my preferences.

With a little bit of upfront work, anyone can become a user of this app! Reach out if you want to try it out.

<img src="https://github.com/AitanG/siri-workout-planner/blob/master/example-output.png?raw=true" alt="Example output" width="300"/>


## High-level architecture

<img src="https://github.com/AitanG/siri-workout-planner/blob/master/architecture.png?raw=true" alt="High-level architecture" width="500"/>

1. Siri triggers an automation via the iOS Shortcuts app. The automation has arguments (user key, gym, number of power sets to generate) which are either implied by the Siri command or requested by Siri.
1. The shortcut opens the Pushover app, which waits for the notification. [Pushover](https://pushover.net/) is a mobile app with a simple API for sending push notifications with text.
1. The shortcut triggers If This Then That (IFTTT) webhook with arguments.
1. IFTTT essentially passes those arguments along with its Google Cloud Functions invocation, but securely handling authentication.
1. Google Cloud Functions runs a Python script, which retrieves complete workout history from Google Sheets, computes a workout plan, and then makes the necessary updates to workout history and sends a push notification with the human-readable workout plan to Pushover.
