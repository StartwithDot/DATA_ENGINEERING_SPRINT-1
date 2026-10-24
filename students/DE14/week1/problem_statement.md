# Week 1 - Set up your tools and understand the ask

**Data Sprint 1 · Week 1 of 15 · Theme: set up your tools, understand the client, and make your first page and diagram**

Read this whole file before you start anything. Then work through the task groups in order. Every task is small: do one task, save one file, make one commit, then start the next task.

## 1. What We Are Doing

This week you set up the tools you will use for all 15 weeks. You also learn what the client really needs: you write a short discovery brief, list open questions, draw the whole system on one page, and summarise the four data sources..

The task groups this week:

- **Group 0 - Set up your tools**: Tasks 1 to 4 (`G0.1`, `G0.2`, `G0.3`, `G0.4`)
- **Group 1 - Discovery Brief [MILESTONE]**: Tasks 5 to 7 (`B1.1`, `B1.2`, `A1.1`)
- **Group 2 - Source Summaries and the Client Ask**: Tasks 8 and 9 (`B2.1`, `B2.2`)

There are no Python coding tasks and no SQL table tasks this week on purpose. You only run two small check queries as part of setup. Weeks 2 and 3 teach Python from zero, and Week 2 also starts your first tables in Snowflake.

## 2. Why We Are Doing It

The client is a financial technology (fintech) company. It does due diligence on Indian companies. Due diligence means checking a company before a deal or investment. Its analysts check four things: is the company real and active (MCA, the company registry), was it ever in insolvency (IBBI), how does it compare with its state (MCA CDM state statistics), and what was the interest-rate background (RBI, the central bank).

Over 15 weeks we build one Snowflake data platform (bronze, silver, gold) that answers those questions, and it ends in a Metabase dashboard.

Before we build anything, we must agree on what we are building. Building the wrong thing well is the most expensive mistake in data work. That is why Week 1 has the **Discovery Brief milestone**. The cohort must agree on the discovery brief before starting later project work.

This week is also your first contact with the tools. It is normal to feel slow. Go one task at a time.

## 3. What to Learn First (Prerequisites)

**Before this week: what you must already have**

| You need | Where |
|---|---|
| The client story and the four data sources | `docs/01-project-brief.md` |
| Your Snowflake account details from the program lead (account URL, username, first password, role, warehouse, database) | The message from the program lead and `docs/02-tools-setup.md` |
| Git, GitHub account, VS Code, and a browser | `docs/02-tools-setup.md` and https://code.visualstudio.com |
| Fork, clone, commit, pull request commands | `docs/03-student-guide.md` |
| A word you do not know | `docs/08-glossary.md` |
| This week's reading and videos | `docs/09-resources.md` |
| A tool that will not work | `docs/10-troubleshooting.md` |
| What a tool is for and why we use it | `docs/11-tools-and-technology.md` |
| The team project repo practice | `CONTRIBUTING.md` |

**By the end of this week you can**

- Set up Git and GitHub, make a commit, and open a pull request
- Sign in to Snowflake with MFA, open a Workspace, and run a small check query
- Connect the Snowflake extension in VS Code and run a `.sql` file
- Create a practice team project folder with a README, `.gitignore`, and folder layout
- Describe the client's real problem in writing, in language the client would recognise
- Explain what each of the four data sources is for, without reading from the brief
- Draw the whole system on one page, so a non-technical person can see how it fits together
- Write five open questions for the client

**Core concepts to review first**

- **How your tasks are numbered.** Each week numbers its tasks in the order you should do them. Every task also keeps a stable ID like `G0.1` or `B1.1`. That ID goes in your commit message and in your pull request title, so anyone can find the task behind any commit.
- **The four places you work.** Each task tells you which one to use. The full list is in section 4.
- **What "your week folder" means.** It is `students/DEx/week1/` inside your cloned class repo. `DEx` is your own student number. If you are DE12, your folder is `students/DE12/week1/`. Every path in this file uses `DEx`; replace it with your number.
- **MFA (a second sign-in step).** Snowflake requires MFA for human users who sign in with a password. Set up an authenticator app at first login.
- **Workspace, not Worksheet.** The Snowflake SQL editor is in Snowsight > Projects > Workspaces. Use the word Workspace.
- **The one exception for data files, later in the course.** Downloaded data never goes in your week folder. It goes to `data/raw/...` at the repo root, and it is never committed.

**You do not clean any data this week.** That is deliberate. Cleaning starts in Week 7. This week is tool setup, understanding the client, and first writing and diagram tasks.

## 4. Where to Find Resources

**Where you work**

You work in four places. Each task tells you which one to use.

1. **VS Code** - your main place. You write and save your class work here, inside `students/DEx/week1/`. Task 4 uses a separate practice project folder. You also commit here.
2. **VS Code terminal** - you run Git commands here. Later you will run Python commands here.
3. **Snowflake (Snowsight, in the browser)** - you run SQL here. Snowflake is where the data lives. It is not where you save your work. Write and commit in VS Code. Do not push from Snowflake.
4. **The web** - you use the browser for Snowflake, GitHub, and the source websites.

**The one rule:** save individual class work in `students/DEx/week1/`. Task 4 uses a separate practice project folder. Run SQL in Snowflake. Run Git in the VS Code terminal.

Example: if you are DE12, a setup SQL file goes to `students/DE12/week1/setup/snowflake_check.sql`.

**Docs to keep open**

| Doc | Use it for |
|---|---|
| `docs/02-tools-setup.md` | Tool install and first setup for Tasks 1 to 3 (`G0.1` to `G0.3`): Git, GitHub, Snowflake login, VS Code extension |
| `docs/03-student-guide.md` | Git commands, commits, branches, and pull requests |
| `CONTRIBUTING.md` | Team project repo layout and delivery folder rules |
| `docs/01-project-brief.md` | Client story and the four sources |
| `docs/02-tools-setup.md` | Tool install details if something is missing |
| `docs/08-glossary.md` | Words you do not know |
| `docs/09-resources.md` | Reading and videos |
| `docs/10-troubleshooting.md` | A tool that will not work |
| `docs/11-tools-and-technology.md` | What a tool is for and why we use it |

**Your week in order**

| Day | Learn first (exact items) | Then do | Time |
|---|---|---|---|
| **1** | `docs/02-tools-setup.md` and `docs/03-student-guide.md`. Use https://git-scm.com/book/en/v2 if you need more Git detail. | Tasks 1 and 2 (`G0.1`, `G0.2`) | about 3 hours |
| **2** | `docs/02-tools-setup.md`, https://docs.snowflake.com/en/user-guide/vscode-ext, and `CONTRIBUTING.md`. | Tasks 3 and 4 (`G0.3`, `G0.4`) | about 2.5 hours |
| **3** | `docs/01-project-brief.md` sections 1 to 4, read twice. The MCA data dictionary that is published with the Company Master Data catalog on https://data.gov.in | Tasks 5 and 6 (`B1.1`, `B1.2`) | about 2 hours |
| **4** | Mermaid flowcharts page on https://mermaid.js.org | Task 7 (`A1.1`) | about 1 hour |
| **5** | Visit the four source websites yourself: https://data.gov.in, https://ibbi.gov.in, https://mcacdm.nic.in, https://data.rbi.org.in | Tasks 8 and 9 (`B2.1`, `B2.2`) | about 1.5 hours |

At the end of the week there is a cohort review: you walk through your discovery brief and we check the words together.

**Search keywords if you get stuck this week**

- "git first commit pull request"
- "Snowflake MFA first login Workspace"
- "VS Code Snowflake extension"
- "Mermaid flowchart syntax"
- "MCA Company Master Data data.gov.in"
- "discovery brief"

## 5. Step-by-Step Guide

How to work: one task, one file, one commit. Finish a task, save the file, commit it, then start the next task. The full Git steps are in `docs/03-student-guide.md`. Never squash-merge. This week, start with the setup group. Do not skip `G0.1` and `G0.2`: later tasks need your repo and Snowflake login.

**Git in 5 commands** (example for Task 1; full explanation in `docs/03-student-guide.md`)

```
git status
git checkout -b g0-1-setup-check
git add students/DEx/week1/setup/hello.md
git commit -m "G0.1 first commit and setup check"
git push -u origin g0-1-setup-check
```

After the push, open the pull request on GitHub. The pull request steps are in `docs/03-student-guide.md` and `docs/02-tools-setup.md`. Stay on `g0-1-setup-check` while you keep updating this pull request. Do not run `git checkout main`. The rule for all 15 weeks: **one task, one file, one commit.** Never squash-merge.

### Group 0 - Set up your tools

#### Task 1 - First commit and pull request (ID `G0.1`)

##### 1. What We Are Doing
You make your first commit and your first pull request (PR). A PR asks the class repo to take your work. You work in VS Code and the VS Code terminal. If you have not forked and cloned the class repo yet, do that first. The steps are in `docs/02-tools-setup.md` and `docs/03-student-guide.md`. To fork and clone: on GitHub, fork the class repo. In VS Code, clone your fork to a folder on your computer, then open that folder in VS Code.

##### 2. Why We Are Doing It
Every task in this course ends in a commit and a PR. Doing it once now makes every later task easier. The class repo tracks your progress.

##### 3. What to Learn First
- Git words: repository, branch, commit, push, pull request.
- Commands: `git status`, `git checkout -b`, `git add`, `git commit -m`, `git push`.

##### 4. Where to Find Resources
- `docs/02-tools-setup.md` and `docs/03-student-guide.md`.
- https://git-scm.com/book/en/v2 and https://docs.github.com.
- Search keywords: "git first commit pull request", "git checkout -b", "GitHub open pull request".

##### 5. Step-by-Step Guide
1. Open VS Code with your cloned class repo. If you have not forked and cloned it yet, fork the class repo on GitHub. In VS Code, clone your fork to a folder on your computer. Open that folder in VS Code.
2. Open the VS Code terminal. Go to the repo root.
3. Run `git status`. Read the output.
4. In VS Code, create the folder `students/DEx/week1/setup` if it is missing. Create a file named `hello.md`.
5. In `hello.md`, write one short line: your name and "setup check".
6. Run these commands in the VS Code terminal:

   ```
   git status
   git checkout -b g0-1-setup-check
   git add students/DEx/week1/setup/hello.md
   git commit -m "G0.1 first commit and setup check"
   git push -u origin g0-1-setup-check
   ```

   Stay on `g0-1-setup-check` while you keep updating this pull request. Do not run `git checkout main`.
7. Open GitHub. Open a pull request from your branch to the class repo main branch. Follow the pull request steps in `docs/03-student-guide.md` and `docs/02-tools-setup.md`.
8. Check the pull request shows one file changed.
9. Open the pull requests list for the class repo. Open one teammate's pull request. Read the changed files. Leave one specific review comment that names a line and says what to change or what is good. The review steps are in `docs/03-student-guide.md`. If no teammate pull request is open yet, wait until one is open and do this step then.

**How to think about it:** A commit is a saved checkpoint. A pull request is a request to add your checkpoint to the class repo.

If you get stuck:
- Read the Git error text. It often names the file or branch.
- Search "git first commit pull request" or open `docs/02-tools-setup.md` and `docs/03-student-guide.md` again.
- Ask in Discord and paste the full error text.

##### 6. What to Commit
- [ ] `students/DEx/week1/setup/hello.md` (replace `DEx` with your number)
- [ ] Done when: the file exists in your branch
- [ ] Done when: the commit message is `G0.1 first commit and setup check`
- [ ] Done when: the pull request is open
- [ ] Done when: you left one specific review comment on a teammate's pull request

Commit message: `G0.1 first commit and setup check`

#### Task 2 - Snowflake first login and first query (ID `G0.2`)

##### 1. What We Are Doing
You sign in to Snowflake for the first time, set up MFA, open a Workspace, and run a small check query. You save the query and the four returned values in SQL comments in one `.sql` file. You work in the browser (Snowsight) and in VS Code.

##### 2. Why We Are Doing It
You need a working Snowflake login before Week 2, when you create your first tables. The check query proves your role and warehouse work.

##### 3. What to Learn First
- How to sign in to Snowsight with the account URL, username, and first password from the program lead.
- What MFA is: a second sign-in step with an authenticator app.
- What a role and a warehouse are in Snowflake.
- How to run a query in a Workspace.

##### 4. Where to Find Resources
- `docs/02-tools-setup.md`.
- https://docs.snowflake.com. Search for "Planning for the deprecation of single-factor password sign-ins" and "Snowsight Workspaces".
- Search keywords: "Snowflake MFA first login", "Snowsight Workspaces", "Snowflake CURRENT_USER CURRENT_ROLE".

##### 5. Step-by-Step Guide
1. Open a browser. Go to the Snowflake account URL from the program lead.
2. Sign in with your username and first password. Change the password when Snowflake asks.
3. Set up MFA with an authenticator app. Do not skip this step.
4. Open Projects > Workspaces.
5. At the top of the Workspace, set your role and warehouse to the ones the program lead gave you (usually `STUDENT_ROLE` and `STUDENT_WH`).
6. Create a SQL file in the Workspace. Paste this query and run it:

   ```sql
   SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE();
   ```

7. In VS Code, create `students/DEx/week1/setup/snowflake_check.sql`. Save the same query in this file.
8. Below the query in the same file, add four SQL comments with the four returned values: user, role, warehouse, database. Do **not** write your password.
9. Commit the file.

**How to think about it:** MFA protects your account. Your password never goes into a file.

If you get stuck:
- Check that you set up MFA. Read the Snowflake sign-in message again.
- Check the role and warehouse boxes at the top of the Workspace.
- Search "Snowflake MFA first login" or ask in Discord with the full error text. Do not paste your password.

##### 6. What to Commit
- [ ] `students/DEx/week1/setup/snowflake_check.sql` (replace `DEx` with your number)
- [ ] Done when: the query runs in a Workspace
- [ ] Done when: the SQL file has the four returned values as SQL comments
- [ ] Done when: no password is written anywhere
- [ ] Done when: the pull request is updated

Commit message: `G0.2 Snowflake login and first query`

#### Task 3 - Connect VS Code to Snowflake and run a .sql file (ID `G0.3`)

##### 1. What We Are Doing
You install the official Snowflake extension in VS Code, sign in, and run a `.sql` file from VS Code. You save one observation as a SQL comment. You work in VS Code.

##### 2. Why We Are Doing It
VS Code is where your files live. The Snowflake extension lets you run a saved `.sql` file without copying it to the browser by hand.

##### 3. What to Learn First
- How to open the Extensions panel in VS Code.
- How to open the Command Palette.
- How to sign in to the Snowflake extension.

##### 4. Where to Find Resources
- `docs/02-tools-setup.md` and https://docs.snowflake.com/en/user-guide/vscode-ext.
- https://code.visualstudio.com.
- Search keywords: "Snowflake VS Code extension", "Snowflake Execute All Statements", "VS Code Command Palette".

##### 5. Step-by-Step Guide
1. Open VS Code. Open the Extensions panel.
2. Search for Snowflake. Install the official extension published by Snowflake. Pick the one with the Snowflake badge.
3. Open the Command Palette. Sign in with your account identifier, username, and password, or SSO or key-pair. Complete MFA if asked.
4. Create `students/DEx/week1/setup/vscode_snowflake_check.sql`.
5. Type this query and save the file:

   ```sql
   SELECT CURRENT_VERSION();
   ```

6. Run the file with the Command Palette command `Snowflake: Execute All Statements`.
7. Look at the result. In the same `.sql` file, write one SQL comment line about what you saw.
8. Commit the `.sql` file.

**How to think about it:** The extension runs SQL from VS Code. The file still lives in your repo, so it can be committed.

If you get stuck:
- Check the extension publisher is Snowflake. Remove other Snowflake extensions if you installed the wrong one.
- Check your account identifier and username. Exact menu names may change, so follow https://docs.snowflake.com/en/user-guide/vscode-ext.
- Ask in Discord with the full error text.

##### 6. What to Commit
- [ ] `students/DEx/week1/setup/vscode_snowflake_check.sql` (replace `DEx` with your number)
- [ ] Done when: `SELECT CURRENT_VERSION();` runs from VS Code
- [ ] Done when: the SQL file has one comment line about what you saw
- [ ] Done when: the pull request is updated

Commit message: `G0.3 connect VS Code to Snowflake`

#### Task 4 - Create your project folder on your computer (ID `G0.4`)

##### 1. What We Are Doing
You create a practice team project folder on your computer. It has a `README.md`, a `.gitignore`, and the team folder layout. You work in VS Code, the VS Code terminal, and the browser for GitHub.

##### 2. Why We Are Doing It
Each team keeps its own project folder or Git repo on a laptop. The team leader later mirrors the latest reviewed files into the class repo `delivery/` and `platform/` folders. This task is a safe practice run.

##### 3. What to Learn First
- The difference between the class repo and a team project repo.
- How to create folders and files in VS Code.
- `git init`, `git add`, `git commit`, and how to push to GitHub.

##### 4. Where to Find Resources
- `CONTRIBUTING.md` for the team project repo layout and delivery folder rules.
- https://docs.github.com and https://git-scm.com/book/en/v2.
- Search keywords: "git init first commit", "GitHub create empty repository", "README gitignore project layout".

##### 5. Step-by-Step Guide
1. Read `CONTRIBUTING.md` for the team project repo layout and delivery folder rules.
2. In VS Code, create a new folder on your computer outside the class repo. Name it `team-project-practice`. Open this folder in VS Code.
3. Create this layout:

   ```
   team-project-practice/
     README.md
     .gitignore
     python/
     sql/
     dbt/
     airflow/
     docs/
   ```

4. In `README.md`, write one short line: the project name and its purpose.
5. In `.gitignore`, write these lines:

   ```
   .venv/
   .env
   data/
   ```

6. Open the VS Code terminal in `team-project-practice`. Run:

   ```
   git init
   git add .
   git commit -m "G0.4 create team project folder"
   ```

7. If you want remote publication, create an empty repository on GitHub and push your folder. Copy the repository link if you do this. This step is optional.
8. In your class repo, create `students/DEx/week1/setup/project_repo_notes.md`. Write the local project folder path and folder tree. Add the GitHub repository link if you created one.
9. Commit the notes file in your class repo.

**How to think about it:** The team repo is where real project files live. Your practice repo is a safe place to learn the layout. Do not put data or passwords in it.

If you get stuck:
- Check you opened `team-project-practice`, not the class repo. Run `git status` to see where you are.
- Read `CONTRIBUTING.md` again.
- Ask in Discord with the full error text.

##### 6. What to Commit
- [ ] Your practice team repo on your computer has `README.md`, `.gitignore`, `python/`, `sql/`, `dbt/`, `airflow/`, `docs/`
- [ ] `students/DEx/week1/setup/project_repo_notes.md` (replace `DEx` with your number)
- [ ] Done when: the notes file has the local project folder path and folder tree
- [ ] Done when: the notes file has the GitHub repository link if you created one
- [ ] Done when: no data file and no password are in the team repo
- [ ] Done when: the pull request is updated

Commit message: `G0.4 create team project folder`

### Group 1 - Discovery Brief **[MILESTONE]**

#### Task 5 - Write the discovery brief (ID `B1.1`)

##### 1. What We Are Doing
You write a one-page discovery brief in your own words. It says what we are building, who uses it, and what "done" looks like. You work in VS Code.

##### 2. Why We Are Doing It
The client pays us to answer questions about Indian companies. If you cannot say in plain words what the client needs, every later task can be built correctly and still be useless.

##### 3. What to Learn First
- `docs/01-project-brief.md` section 1, read twice (about 30 minutes).
- Nothing else. Your own words, not a copy.

##### 4. Where to Find Resources
- `docs/01-project-brief.md` section 1, read twice (about 30 minutes).
- Search keywords: "discovery brief", "project brief", "client requirements", "due diligence Indian companies".

##### 5. Step-by-Step Guide
1. Create `students/DEx/week1/discovery/` if it is missing. Create `students/DEx/week1/discovery/discovery_brief.md` inside it.
2. Type these headings and fill each one with 2 to 5 lines: `## What we are building`, `## Who uses it`, `## Questions it must answer`, `## What is still unclear`, `## What "done" looks like`.
3. Keep it to about one page. Write as if the client will read it.

**How to think about it:** this is a short business page, not an essay. Short sentences beat long ones.

If you get stuck:
- Read section 1 of the brief again, slowly, one heading at a time.
- Look up any word you do not know in `docs/08-glossary.md`.
- Ask in Discord and paste the sentence you are stuck on.

##### 6. What to Commit
- [ ] `students/DEx/week1/discovery/discovery_brief.md` (replace `DEx` with your number)
- [ ] Done when: the file has all five headings filled
- [ ] Done when: a person outside the course can follow it
- [ ] Done when: the pull request is open

Commit message: `B1.1 write discovery brief`

#### Task 6 - List the open questions (ID `B1.2`)

##### 1. What We Are Doing
You add exactly five questions to the same discovery brief. These are questions you would ask the client in a meeting. You work in VS Code, in the same file as Task 5.

##### 2. Why We Are Doing It
The brief cannot decide everything. The questions you ask now decide how far back the history goes and what "risk" means to the client.

##### 3. What to Learn First
Nothing new. You use what you learned in Task 5.

##### 4. Where to Find Resources
- `docs/01-project-brief.md` (the section you already read).
- `docs/03-student-guide.md`, for the pull request update.
- Search keywords: "open questions client discovery", "requirement questions data project", "stakeholder interview questions".

##### 5. Step-by-Step Guide
1. Open `students/DEx/week1/discovery/discovery_brief.md`.
2. Add a heading `## Open Questions`.
3. Write exactly five questions you would ask the client in a thirty minute meeting. Make each one a question the brief alone cannot answer.
4. Do not answer them yourself. Just list them.

**How to think about it:** a good question cannot be answered by reading the brief. If the brief already answers it, it is not an open question.

If you get stuck:
- Re-read your own `## What is still unclear` section and turn those notes into questions.
- Check the question list in `docs/01-project-brief.md` and see which one is still not decided.
- Ask in Discord and paste one of your questions for review.

##### 6. What to Commit
- [ ] `students/DEx/week1/discovery/discovery_brief.md` (same file as Task 5, now with the new heading)
- [ ] Done when: there are five real questions
- [ ] Done when: the same pull request from Task 5 is updated (do not open a second pull request)

Commit message: `B1.2 add open questions to discovery brief`

#### Task 7 - Draw the whole system on one page (ID `A1.1`)

##### 1. What We Are Doing
You draw the whole system as one Mermaid diagram. It shows the four data sources on the left, the pipeline in the middle, and the users on the right. You write the file in VS Code and preview it in VS Code or on GitHub.

##### 2. Why We Are Doing It
One page shows the client and your teammates how the four sources become one dashboard. You will redraw it with more detail in Weeks 6, 9, 11 and 15.

##### 3. What to Learn First
- What a flowchart is: boxes joined by arrows.
- The Mermaid flowchart syntax (about 20 minutes, only the flowchart part).

##### 4. Where to Find Resources
- The Mermaid flowchart page on https://mermaid.js.org (about 20 minutes, only the flowchart part).
- Markdown preview in VS Code: https://code.visualstudio.com, search for "Markdown preview".
- Search keywords: "mermaid flowchart LR syntax", "mermaid arrow label", "VS Code markdown preview mermaid", "GitHub render mermaid".

##### 5. Step-by-Step Guide
1. Create `students/DEx/week1/design/` if it is missing.
2. Create `students/DEx/week1/design/context_diagram.md` inside it.
3. Paste this starter block and edit it. It is only a skeleton. Fill each label from `docs/01-project-brief.md`.

   ````markdown
   ```mermaid
   flowchart LR
       A[Label 1] --> P[Label 4]
       B[Label 2] --> P
       C[Label 3] --> P
       %% Add the fourth source yourself.
       P --> D[Label 5]
       D --> U[Label 6]
   ```
   ````

4. Add the missing fourth source and label every source with its format. Add the people on the right.
5. To preview, open the Markdown preview in VS Code (see https://code.visualstudio.com and search for "Markdown preview"). GitHub also renders Mermaid once you push the file.

**How to think about it:** this diagram is the project map. If a box needs its own smaller boxes inside it, you have added too much detail.

If you get stuck:
- Compare your diagram with `docs/01-project-brief.md`. The fourth source is the one not yet listed.
- Search "mermaid flowchart LR syntax" and copy one working line, then change the text.
- Read the error text Git or GitHub shows. It usually names the bad line.

##### 6. What to Commit
- [ ] `students/DEx/week1/design/context_diagram.md` (replace `DEx` with your number)
- [ ] Done when: the diagram has four sources on the left
- [ ] Done when: the pipeline is in the middle and the users are on the right
- [ ] Done when: it fits on one page
- [ ] Done when: it is added to the discovery brief pull request

Commit message: `A1.1 draw one page system diagram`

> **Why this is a milestone:** building the wrong thing well is the most expensive mistake in data work. The cohort must agree on the discovery brief before starting later project work.
>
> **On Task 7:** if a box needs its own smaller boxes inside it, you have added too much detail. This diagram is the project map.

### Group 2 - Source Summaries and the Client Ask

#### Task 8 - Summarise the four sources (ID `B2.1`)

##### 1. What We Are Doing
You visit the four data source websites, then write a short summary of each one. You look in the browser first, then write in VS Code.

##### 2. Why We Are Doing It
The analyst must know which source answers which question. MCA says the company is real, IBBI says it was ever in insolvency, MCA CDM compares it with its state, RBI gives the interest-rate background.

##### 3. What to Learn First
Nothing new. Spend about 40 minutes clicking the four sites: https://data.gov.in, https://ibbi.gov.in, https://mcacdm.nic.in, https://data.rbi.org.in.

##### 4. Where to Find Resources
- The four sites: https://data.gov.in, https://ibbi.gov.in, https://mcacdm.nic.in, https://data.rbi.org.in (about 40 minutes).
- `docs/01-project-brief.md` for the source names only. Do not copy the text.
- Search keywords: "MCA Company Master Data", "IBBI CIRP list", "MCA CDM state statistics", "RBI DBIE policy rate".

##### 5. Step-by-Step Guide
1. In VS Code, create `students/DEx/week1/discovery/source_summary.md`.
2. Write a heading per source, then exactly three sentences: what it is, which client question it answers, how it arrives (file type and how often).
3. Do not copy from `docs/01-project-brief.md`. Your own words.
4. For RBI, add one note: the RBI data portal DBIE is now at https://data.rbi.org.in, and the policy rate series only lists the days when the rate changed, so a missing month does not mean missing data. Our downloaded RBI data ends in 2024. That is OK. RBI is background only.

**How to think about it:** three sentences per source. One sentence for what it is, one for the client question, one for how it arrives.

If you get stuck:
- Open the site and look at the page title and the file list before you write.
- Search "IBBI CIRP list" or "MCA CDM statistics" to see the page you need.
- Ask in Discord and paste your three sentences for one source.

##### 6. What to Commit
- [ ] `students/DEx/week1/discovery/source_summary.md` (replace `DEx` with your number)
- [ ] Done when: all four sources are covered, each with three sentences
- [ ] Done when: the RBI note is included
- [ ] Done when: a pull request is open

Commit message: `B2.1 summarise the four data sources`

#### Task 9 - Write the onboarding paragraph (ID `B2.2`)

##### 1. What We Are Doing
You write one paragraph, 6 to 10 sentences, that a new teammate could read on their first day. You work in VS Code.

##### 2. Why We Are Doing It
A new teammate may join the project later. One paragraph should be enough for them to know what the project is and why it exists.

##### 3. What to Learn First
Nothing new. You use what you learned in Task 8.

##### 4. Where to Find Resources
- Your own `students/DEx/week1/discovery/source_summary.md` from Task 8.
- Search keywords: "project onboarding summary", "how to write a project overview paragraph".

##### 5. Step-by-Step Guide
1. Create `students/DEx/week1/discovery/teammate_onboarding.md`.
2. Write one paragraph of 6 to 10 sentences: who the client is, what we build, which sources we use, what the finished thing answers.
3. Read it once as if you were the new teammate. Cut anything they do not need.

**How to think about it:** a new teammate knows nothing about our project. Write only what they need on day one.

If you get stuck:
- Start from your Task 8 summaries and join them into sentences.
- Read it aloud. If a sentence is hard to say, make it shorter.
- Ask in Discord and paste the paragraph.

##### 6. What to Commit
- [ ] `students/DEx/week1/discovery/teammate_onboarding.md` (replace `DEx` with your number)
- [ ] Done when: it is one paragraph
- [ ] Done when: it stands alone (no links needed to understand it)
- [ ] Done when: the pull request is open

Commit message: `B2.2 write the teammate onboarding paragraph`

## 6. What to Commit

End of week checklist:

- [ ] Tasks 1 to 4 - setup: `hello.md`, Snowflake check query, VS Code extension check, and project repo notes
- [ ] Tasks 5 and 6 - discovery brief with open questions, in a pull request
- [ ] Task 7 - the one-page system map in `students/DEx/week1/design/context_diagram.md`
- [ ] Tasks 8 and 9 - source summaries and the onboarding paragraph
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No data file, no credential, and no `.venv` anywhere in your commits

All class-repo files go inside `students/DEx/week1/` (replace `DEx` with your number). The practice team repo in Task 4 is separate, on your computer.

**If you are short on time, cut in this order:** Task 9 (`B2.2`) first, then Task 4 (`G0.4`). Never cut Tasks 1, 2, 3, 5, 6 and 7. The discovery brief is a milestone, and the written reasoning cannot be added back later.

When your week is done, make sure your pull request is open and updated as you go (`docs/03-student-guide.md` has the steps).

Next: `week2/problem_statement.md`.
