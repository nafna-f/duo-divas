# DuoDivas Planning Page

_Due to the nature of this project, we have decided having a planning page / file will help keep transparency and organize our thoughts. Previously, this was a google docs, but having to upload a pdf file over and over seems very counterintuitive._

## General Process:

- Use a sorting sequence to randomize the data.

### Questions:

- ~~What are we getting from this data specifically?~~

 	Heading details were provided by Mr. Dillon initially and are now provided in the three csv files provided.

- ~~Is it randomized?~~

 	It is. But our whole goal is to be ethical about this, so we should randomize the data on our own just in case (also for statistics).

- ~~Specifically, what do you want?~~

 	Mr. Dillon wishes for, at it's core, a program that can fill out AP seats and assign students to AP courses. However, on a more complex level, he wants us to ethically consider and analyze how we sort these. This will be given to the AP Department for consideration, so useful features and accessibility will be critical. We will have to look at graphical data and statistics and point/out notice any trends in data and (if applicable) change our code / add new modes as necessary. This whole thing is essentially a social experiment, akin to the plane seating lab in Ethi:CS.

- ~~Is this program for seats of ONE AP Course, or multiple? When I run it, what is this "input", so to speak?~~

 	Multiple. But starting with one may be a good idea. The input can be whatever we want it to be, such as sorting options, filters, etc.

- ~~What graphical interface?~~

 	A terminal interface is Mr. Dillon's preferred approach.

- ~~Do we count waitlists? Do we make waitlists?~~

 	Waitlists should be counted, but it is reccommended to give them a lesser priority than those who are applicable and have it at a lower ranked choice. **Waitlisted** students are simply students who are eligible to enter the course but do not meet the grade requirement.

- ~~What about duplicate ranking?~~

 	Duplicate ranks should just be ignored. It's our choice how we want to handle this in certain algorithms (for example, ensuring every student has a seat).

- ~~APENG? We don't know what APENG courses are being ranked.~~

 	APENG has specific course codes. We will have to align them.

- ~~Do we take into account if they've taken the AP course before?~~

 	Talos takes cares of this. Talos will not allow a student to choose an AP course they are not eligible (exception: waitlist) for or have taken before.

- Explain "ap_preferences.csv" to me. Specifically, why does a student have multi-line entries if all their rankings are to be on one line? Also, does the things in parenthesis "(must rank AP Physical Sci in other section)" matter to us?

- ~~What does "ZZNOAP{NAME}" mean? What about "ZQAP{NAME}"?~~

- ~~We did some research, and the Talos site has "Active Courses" and "Courses". What is the difference, and do we care about either?~~

- ~~There's a lot of codes that aren't courses, such as ZZNOAP{NAME} and ZQAP{NAME}. This is not highlighted in ap_courses.csv. Is there an easier way we can access this without having to read 1.1k entries on Talos?~~

- These questions are not significant to us, for now. When they are, we will provide the appropriate answers.

## Ideas / Plans:

### Our Sorting Algorithms / Features

- **Best Come First:** Simply rank ALL seats by best choice/grades (accounting eligibility).
- **Automate A Percent:** Best Come First, except only for **x%** of seats in each AP Course, where x is an input given by the user.
- **Everyone Deserves A Chance:** Be able to ensure **every** student is assigned at least **1** AP course.
- **Everyone Deserves Their Choice:** Best Come First, except seats are ranked **only** by choice.
- **No Choice:** Best Come First, except seats are ranked **only** by grades (the course they are assigned to must adhere to their choices but may **not** be their first choice even if they're REALLY eligible for it.

Some of these choices are more for testing purposes rather than actual use. How these turn out will dictate what we will do in the future. This section is subject to change, check back frequently!

### Plans

(Plans that are highlighted **in bold** are plans that are approved by Mr. Dillon. Not all plans are required to be approved to follow through (for example, branching, since it is more of an internal development)

- ~~Branching: We will branch off to do our work and push the latest **working version** of our project onto main. This way, we will always have a working version to refer back to and not need to be as cautious when working in experimental environments.~~
- ~~SQLITE3: Instead of using Classes, we have switched to Sqlite3, a MUCH better alternative for our data organization. We have finally been able to create content because of this!~~
- ~~SETUP: Dua is currently handling reading data from the files provided, whilst Naf is working on the sqlite tables themselves (setup, testing, etc.). We are using seperate branches for this, as always.~~
- THE BREAKDOWN: This is the main part of the project. We're breaking it down into multiple portions, as follows. We will start with BEST COME FIRST. 
{ Make a helper function STUDENT_PREFS that will return a nicer, concise list of the APs the students actually prefer and not all that BLOAT.}
{ Organize Lists by overall highest average. Use CHECK_ELIGIBILITY to see if they are eligible. }

## Concerns:

- Debugging: Since this project is mainly algorithmic, we will have to put a **lot** of effort into debugging. The unfortunate truth.
- The First Working Version: Getting our main algorithm to work is not just it. We need to make it work and be **extensive**, because a lot of our features and work will revolve around our main algorithm. We really have to double down on making sure this works, or else the rest of the project "fumbles", to use the parlance of our times.  
