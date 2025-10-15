# ExamplePhysicsUsageV1
NOT CORRECT FLOWCHART SYNTAX
- Colour = Path - Eg. Option 1 (Red), Option 2 (Blue) then the red line corresponds to Option 1
- Diamond - Choices given to user
- Parallelogram - Input/Output
- Note - Additional information
- Rectangle - System information / Processing



#### Flowchart is loosely based on this Physics Example:
- Opens the Physics StudyAgent through a command such as "sb physics"
- User presented with 2 options:
    1. Study (if pre-existing study data exists)
        - User is then given the following 2 options:
        1. Continue with last session -> [Work done by moving charges in magnetic fields]
            - Loads the last session's context
            - Continues from last session
        2. Start new session
            - Discards last session's context
            - Gives the user the following options to start a new session:
                - "Solenoids"
                - "Equipotential lines"
                - "..."
            - User picks an option and a new session starts
    2. Prepare for exam (if no pre-existing exam data exists)
        - User is then given the following options:
            - Prepare for "PHY-TASK 2"
                - Conducts diagnostics quiz
            - Prepare for new exam
                - Collects the following initialising data from the user:
                    - {SYSTEM: Enter exam:}           {USER: "PHY-HSC"}
                    - {SYSTEM: Enter time & date:}    {USER: "Oct 13th at 10am"}
                    - {SYSTEM: Provide notification:} {USER: "./PHY-HSC-Assessment-task-notification.pdf"}
                - Collects existing progress data from user:
                    - {SYSTEM: Enter practice test directory:}  {USER: "./Practice_Tests/"}
                - Collects resources from user:
                    - {SYSTEM: Enter class resources:}          {USER: "./Resources/Class_Materials/"}
                    - {SYSTEM: Enter curriculum resources:}     {USER: "./Resources/Curriculum/"}
                    - {SYSTEM: Enter notes:}                    {USER: "./Study_Notes/"}
                - 


## Conclusions:
StudyBrain System can be broken into these components:

    1. **Start/Opening**
    2. **Exam Preparation**
    3. **Studying**

----
# Start / Opening
- The process of starting up the StudyBrain system
- Done through a command such as "sb physics"
- Starts the StudyBrain system and the SubjectAgent

----

# Exam Preparation
Broken down into the following components:

    1. Gathering the Exam Data
    2. Testing User - Diagnostics quiz
    3. Processing Results

## Gathering the Exam Data
The following information has to be collected from the user:

    - Initialising data
        - Exam name
        - Time and data
        - Assessment notification

    - Existing progress data
        - Practice tests

    - Resources
        - Class materials
        - Curriculum documentation
        - Study notes

After finding this data we need to:
    
    - Identify the areas, topics and concepts covered by the curriculum
    - Identify the areas, topics and concepts being tested by the assessment task

Then, for each area, topic or concept we need to determine the user's:
        
    * Conceptual understanding - How much they understand the area, topic or concept
    * Functional knowledge/ability - How likely/often they will get this a question from this area, topic or concept correct when asked.



## Testing the User
If we don't have enough data to evaluate the user's Conceptual Understanding and Functional Knowledge/Ability for an area, topic or concept, we need to manually test them using a diagnostics test.
A diagnostics test involves the following:

    1. Identify the areas, topics or concepts that need to be tested
    2. Pick one area, topic or concept to test the user on
    3. Determine the scope of the area, topic or concept
    4. Research (within the scope) the area, topic or concept using a combination of:
        - The course curriculum
        - Past papers
        - The internet
    5. Compile a list of sub-areas/topics/concepts to be tested.
    6. Convert the list into a series of questions.
    7. Repeat the following instructions until the list of questions is complete:
        1. Ask the user a question
        2. Get the user's answer + any comments
        3. Mark the user's answer and convert the comments to a confidence rating
        4. Display the result to the user
        5. Save the question and results

This process can be adapted to use practice papers and should prioritise practice papers over diagnostics quizzes.

## Processing Results
After gathering data and thorough testing of the user we should be ready to begin processing the results.  
The processing of results involves determining the user's Conceptual Understanding and Functional Knowledge/Ability for all areas, topics and concepts that we identified earlier. 

After we've finished processing the results we should be left with a file that looks something like this:

    Example Physics Exam Prep Data and Results
    ------------------------------------------
    
    EXAM NAME: PHYS-Task-2
    
    DATE: 13/10/26
    TIME: 10:00 AM

    RESULTS:
    ---------------------------------------------------------------------------------
    |    Module 1 - Motion                       - [Con=95%|Func=80%]               
    |    Module 2 - Kinematics                   - [Con=72%|Func=70%]               
    |    Module 3 - Waves and Thermodynamics     - [Con=94%|Func=96%]               
    |    Module 4 - Electricity and Magnetism    - [Con=30%|Func=20%]               
    ||        - Electricity                           - [Con=20%|Func=10%]          
    |||            - Electric Potential                    - [Con=10%|Func=5%]      
    ||||                - Incorrect Question: "What is Electric Potential?"         
    |||            - Power                                 - [Con=10%|Func=5%]      
    ||||                - Incorrect Question: "What is Electrical Power?"
    ||||                - Incorrect Question: "How do you calculate Electrical Power?"
    ||        - Magnetism                             - [Con=10%|Func=10%]          
    |||            - Solenoids                             - [Con=10%|Func=10%]     
    ||||                - Incorrect Question: "Why do Solenoids create a magnetic field?"
    ---------------------------------------------------------------------------------

The results follow this format:

    [Area, Topic, Concept]  - [{Conceptual Understanding} | {Functional Knowledge}]

Sub-areas/topics/concepts are indented below its parent area, topic or concept with the same format.

After reaching the last sub-area/topic/concept, the questions the user got incorrect are shown.
    

----

# Studying
After we've finished the Exam Preparation process we can move onto studying.
This is the process of teaching the user new information that targets their weak areas.
Using the Exam Prep Data and Results file we can form a list of areas/topics/concepts the user needs to work on. 
The studying process for one area/topic/concept goes as follows:

    1. Choose an area/topic/concept to study
    2. Identify the scope of the area/topic/concept
    3. Research (within the scope) and find keypoints of the area/topic/concept using a combination of:
        - Resources
            - Study notes
            - Class/Teacher resources
        - The internet
    4. Turn the keypoints into a paragraph of information
    5. Create a series of practice questions based on the information
    6. Mark the user's answers and update the Conceptual Understanding for that area/topic/concept

Before continuing onto the next area/topic/concept the user's Functional Knowledge/Ability has to be assessed, this is done by:

    1. Finding the incorrect question(s) for that area/topic/concept
    2. Creating similar exam style questions to the one that was incorrect
    3. Testing the user on each question and getting their confidence
    4. Mark answers and update the Functional Knowledge for that area/topic/concept

If the user's post study results are too low, the Study Agent has 2 choices:
    
    - Move onto the next area/topic/concept
    - Repeat this area/topic/concept

The best choice should be made based on the time left until the exam and the potential mark benefits.