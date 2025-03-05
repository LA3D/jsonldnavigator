# Extracts form Antropic Prompt Engineering Guide
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

## Be clear, direct, and detailed
When interacting with Claude, think of it as a brilliant but very new employee (with amnesia) who needs explicit instructions. Like any new employee, Claude does not have context on your norms, styles, guidelines, or preferred ways of working. The more precisely you explain what you want, the better Claude’s response will be.

The golden rule of clear prompting
Show your prompt to a colleague, ideally someone who has minimal context on the task, and ask them to follow the instructions. If they’re confused, Claude will likely be too.
​
How to be clear, contextual, and specific
Give Claude contextual information: Just like you might be able to better perform on a task if you knew more context, Claude will perform better if it has more contextual information. Some examples of contextual information:
What the task results will be used for
What audience the output is meant for
What workflow the task is a part of, and where this task belongs in that workflow
The end goal of the task, or what a successful task completion looks like
Be specific about what you want Claude to do: For example, if you want Claude to output only code and nothing else, say so.
Provide instructions as sequential steps: Use numbered lists or bullet points to better ensure that Claude carries out the task the exact way you want it to.
​
## Use examples (multishot prompting) to guide Claude's behavior
Examples are your secret weapon shortcut for getting Claude to generate exactly what you need. By providing a few well-crafted examples in your prompt, you can dramatically improve the accuracy, consistency, and quality of Claude’s outputs. This technique, known as few-shot or multishot prompting, is particularly effective for tasks that require structured outputs or adherence to specific formats.

Power up your prompts: Include 3-5 diverse, relevant examples to show Claude exactly what you want. More examples = better performance, especially for complex tasks.
​
Why use examples?
Accuracy: Examples reduce misinterpretation of instructions.
Consistency: Examples enforce uniform structure and style.
Performance: Well-chosen examples boost Claude’s ability to handle complex tasks.
​
Crafting effective examples
For maximum effectiveness, make sure that your examples are:

Relevant: Your examples mirror your actual use case.
Diverse: Your examples cover edge cases and potential challenges, and vary enough that Claude doesn’t inadvertently pick up on unintended patterns.
Clear: Your examples are wrapped in <example> tags (if multiple, nested within <examples> tags) for structure.

Ask Claude to evaluate your examples for relevance, diversity, or clarity. Or have Claude generate more examples based on your initial set.

Our CS team is overwhelmed with unstructured feedback. Your task is to analyze feedback and categorize issues for our product and engineering teams. Use these categories: UI/UX, Performance, Feature Request, Integration, Pricing, and Other. Also rate the sentiment (Positive/Neutral/Negative) and priority (High/Medium/Low). Here is an example:

<example>
Input: The new dashboard is a mess! It takes forever to load, and I can’t find the export button. Fix this ASAP!
Category: UI/UX, Performance
Sentiment: Negative
Priority: High</example>

Now, analyze this feedback: {{FEEDBACK}}

## Let Claude think (chain of thought prompting) to increase performance
When faced with complex tasks like research, analysis, or problem-solving, giving Claude space to think can dramatically improve its performance. This technique, known as chain of thought (CoT) prompting, encourages Claude to break down problems step-by-step, leading to more accurate and nuanced outputs.

​
Before implementing CoT
​
Why let Claude think?
Accuracy: Stepping through problems reduces errors, especially in math, logic, analysis, or generally complex tasks.
Coherence: Structured thinking leads to more cohesive, well-organized responses.
Debugging: Seeing Claude’s thought process helps you pinpoint where prompts may be unclear.
​
Why not let Claude think?
Increased output length may impact latency.
Not all tasks require in-depth thinking. Use CoT judiciously to ensure the right balance of performance and latency.
Use CoT for tasks that a human would need to think through, like complex math, multi-step analysis, writing complex documents, or decisions with many factors.
​
How to prompt for thinking
The chain of thought techniques below are ordered from least to most complex. Less complex methods take up less space in the context window, but are also generally less powerful.

CoT tip: Always have Claude output its thinking. Without outputting its thought process, no thinking occurs!
Basic prompt: Include “Think step-by-step” in your prompt.
Lacks guidance on how to think (which is especially not ideal if a task is very specific to your app, use case, or organization)

Example:
User Role:	Draft personalized emails to donors asking for contributions to this year’s Care for Kids program.

Program information:
<program>{{PROGRAM_DETAILS}}
</program>

Donor information:
<donor>{{DONOR_DETAILS}}
</donor>

Think before you write the email in <thinking> tags. First, think through what messaging might appeal to this donor given their donation history and which campaigns they’ve supported in the past. Then, think through what aspects of the Care for Kids program would appeal to them, given their history. Finally, write the personalized donor email in <email> tags, using your analysis.
​

## Use XML tags to structure your prompts
When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

XML tip: Use tags like <instructions>, <example>, and <formatting> to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.
​
Why use XML tags?
Clarity: Clearly separate different parts of your prompt and ensure your prompt is well structured.
Accuracy: Reduce errors caused by Claude misinterpreting parts of your prompt.
Flexibility: Easily find, add, remove, or modify parts of your prompt without rewriting everything.
Parseability: Having Claude use XML tags in its output makes it easier to extract specific parts of its response by post-processing.
There are no canonical “best” XML tags that Claude has been trained with in particular, although we recommend that your tag names make sense with the information they surround.
​
Tagging best practices
Be consistent: Use the same tag names throughout your prompts, and refer to those tag names when talking about the content (e.g, Using the contract in <contract> tags...).
Nest tags: You should nest tags <outer><inner></inner></outer> for hierarchical content.
Power user tip: Combine XML tags with other techniques like multishot prompting (<examples>) or chain of thought (<thinking>, <answer>). This creates super-structured, high-performance prompts.

##  Giving Claude a role with a system prompt
When using Claude, you can dramatically improve its performance by using the system parameter to give it a role. This technique, known as role prompting, is the most powerful way to use system prompts with Claude.

The right role can turn Claude from a general assistant into your virtual domain expert!

System prompt tips: Use the system parameter to set Claude’s role. Put everything else, like task-specific instructions, in the user turn instead.
​
Why use role prompting?
Enhanced accuracy: In complex scenarios like legal analysis or financial modeling, role prompting can significantly boost Claude’s performance.
Tailored tone: Whether you need a CFO’s brevity or a copywriter’s flair, role prompting adjusts Claude’s communication style.
Improved focus: By setting the role context, Claude stays more within the bounds of your task’s specific requirements.
​
How to give Claude a role
Use the system parameter in the Messages API to set Claude’s role:

## Prefill Claude's response for greater output control
When using Claude, you have the unique ability to guide its responses by prefilling the Assistant message. This powerful technique allows you to direct Claude’s actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios.

In some cases where Claude is not performing as expected, a few prefilled sentences can vastly improve Claude’s performance. A little prefilling goes a long way!

​
How to prefill Claude’s response
To prefill, include the desired initial text in the Assistant message (Claude’s response will continue from where the Assistant message leaves off):
Power user tip: Prefilling { forces Claude to skip the preamble and directly output the JSON object. This is cleaner, more concise, and easier for programs to parse without additional processing.

## Chain complex prompts for stronger performance
When working with complex tasks, Claude can sometimes drop the ball if you try to handle everything in a single prompt. Chain of thought (CoT) prompting is great, but what if your task has multiple distinct steps that each require in-depth thought?

Enter prompt chaining: breaking down complex tasks into smaller, manageable subtasks.

​
Why chain prompts?
Accuracy: Each subtask gets Claude’s full attention, reducing errors.
Clarity: Simpler subtasks mean clearer instructions and outputs.
Traceability: Easily pinpoint and fix issues in your prompt chain.
​
When to chain prompts
Use prompt chaining for multi-step tasks like research synthesis, document analysis, or iterative content creation. When a task involves multiple transformations, citations, or instructions, chaining prevents Claude from dropping or mishandling steps.

Remember: Each link in the chain gets Claude’s full attention!

Debugging tip: If Claude misses a step or performs poorly, isolate that step in its own prompt. This lets you fine-tune problematic steps without redoing the entire task.

How to chain prompts
Identify subtasks: Break your task into distinct, sequential steps.
Structure with XML for clear handoffs: Use XML tags to pass outputs between prompts.
Have a single-task goal: Each subtask should have a single, clear objective.
Iterate: Refine subtasks based on Claude’s performance.
​
Example chained workflows:
Multi-step analysis: See the legal and business examples below.
Content creation pipelines: Research → Outline → Draft → Edit → Format.
Data processing: Extract → Transform → Analyze → Visualize.
Decision-making: Gather info → List options → Analyze each → Recommend.
Verification loops: Generate content → Review → Refine → Re-review.
Optimization tip: For tasks with independent subtasks (like analyzing multiple docs), create separate prompts and run them in parallel for speed.