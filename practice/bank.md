# SCD practice bank

NPTEL = assignment question (2026); EXTRA = self-written.

## Week 1 · Software process & models

**NPTEL-W1-Q1** (MCQ) Which of the following is NOT a typical phase in the software development process?

- A. User Interface (UI) design
- B. Requirements gathering
- C. Testing
- D. Maintenance

**Answer:** A. Phases: requirements, design, development, testing, maintenance.

**NPTEL-W1-Q2** (MCQ) Clients in software development can be ____________

- A. Internal users of a company
- B. External users of a company
- C. Other software systems
- D. All of the above

**Answer:** D. Clients: external users, internal to the company, or another software (e.g. Razorpay).

**NPTEL-W1-Q3** (MCQ) What is the main purpose of the design phase in software development?

- A. To write well-documented code
- B. To create a big-picture view of the system
- C. To develop a user interface
- D. To fix bugs in the code

**Answer:** B. Design gives the big-picture view and structure of the system.

**NPTEL-W1-Q4** (MCQ) How do developers typically collaborate on code in the development phase?

- A. Working independently all the time
- B. Using version control systems like Git
- C. Writing all the code in one sitting
- D. None of the above

**Answer:** B. Distributed development uses tools like GitHub/Git.

**NPTEL-W1-Q5** (MCQ) What is a major drawback of the waterfall model of software development?

- A. It is time-consuming
- B. It requires expensive resources
- C. It is difficult to adapt to changing requirements
- D. It is not suitable for large projects

**Answer:** C. Late changes cost time and money; clients may not know what they need.

**NPTEL-W1-Q6** (MCQ) A biology research lab is developing a new computer model to simulate the growth rate of a specific bacteria strain under different environmental conditions. Who is the primary user of the model?

- A. An external user
- B. Internal to the company
- C. Another software
- D. None of the above

**Answer:** B. The lab itself uses the model: an internal client.

**NPTEL-W1-Q7** (MCQ) A marketing team at a travel booking website develops a mobile app internally and conducts initial usability testing with a small group of colleagues from different departments who were not involved in development. This is an example of ___________

- A. Alpha testing
- B. Beta testing
- C. Gamma testing
- D. Delta testing

**Answer:** A. Alpha = internal employees, lab/staging. Beta = actual users in real life.

**NPTEL-W1-Q8** (MSQ) Which of the following statements are true?

- A. Description of what your functions can do without describing the implementation in detail is known as an interface
- B. The code implemented by the interface cannot change once it has been designed
- C. The code implemented by the interface can change once it has been designed

**Answer:** A, C. Implementation may change as long as the interface stays the same.

**NPTEL-W1-Q9** (MCQ) A bank wants to introduce a blockchain feature. Map the task to the phase of the software development process.

Providing the implemented blockchain feature to a few select users and checking for any errors.

- A. Requirement Specification
- B. Software Design
- C. Software Development
- D. Testing
- E. Maintenance

**Answer:** D. Release to select users to find errors = testing.

**NPTEL-W1-Q10** (MCQ) A bank wants to introduce a blockchain feature. Map the task to the phase of the software development process.

Outlining the different modules of the new feature and how it will interact with existing features of the banking system.

- A. Requirement Specification
- B. Software Design
- C. Software Development
- D. Testing
- E. Maintenance

**Answer:** B. Modules and interactions = big-picture design.

**NPTEL-W1-Q11** (MCQ) A bank wants to introduce a blockchain feature. Map the task to the phase of the software development process.

Gathering information about how blockchain works and getting regulatory information from RBI.

- A. Requirement Specification
- B. Software Design
- C. Software Development
- D. Testing
- E. Maintenance

**Answer:** A. Gathering goals/constraints = requirements.

**NPTEL-W1-Q12** (MCQ) A bank wants to introduce a blockchain feature. Map the task to the phase of the software development process.

Getting feedback about the feature from users and outlining updates for the next release.

- A. Requirement Specification
- B. Software Design
- C. Software Development
- D. Testing
- E. Maintenance

**Answer:** E. Monitoring usage and planning updates = maintenance.

**EXTRA-W1-Q1** (MCQ) A payment gateway acts as a middleman between ________.

- A. the client and the tester
- B. two banks
- C. the user and the developer
- D. the bank and the merchant's website/app

**Answer:** D. It validates encrypted card details with the bank and transfers money to the merchant.

**EXTRA-W1-Q2** (MCQ) Software that is divided into separately addressable components that are integrated to satisfy requirements is said to be made of ________.

- A. sprints
- B. modules
- C. interfaces
- D. prototypes

**Answer:** B. Lecture 2 summary.

**EXTRA-W1-Q3** (MCQ) What is usually the FIRST step in the software development process?

- A. Testing
- B. Learning a programming language
- C. Writing code
- D. Gathering requirements

**Answer:** D. Understand the problem and set explicit goals first.

**EXTRA-W1-Q4** (MCQ) A payment gateway such as Razorpay serving an e-commerce site is an example of a client that is ________.

- A. an external user
- B. another software
- C. a tester
- D. internal to the company

**Answer:** B. It interfaces with another software system.

**EXTRA-W1-Q5** (MCQ) An employee resource portal built by an internal products team for HR is an example of a client that is ________.

- A. another software
- B. internal to the company
- C. none
- D. an external user

**Answer:** B. The users are inside the company.

**EXTRA-W1-Q6** (MCQ) Why is a design needed before coding?

- A. To reduce the number of clients
- B. Because coding cannot start without UML
- C. To avoid testing
- D. Different developers may implement functionality differently, and new features need a big-picture view

**Answer:** D. Integration problems and no overview when adding features.

**EXTRA-W1-Q7** (MCQ) Beta testing is conducted by ________.

- A. only the designers
- B. actual users in a real-life setting
- C. internal employees in a lab
- D. only the developers

**Answer:** B. Alpha = internal; beta = real users.

**EXTRA-W1-Q8** (MCQ) Which is NOT a purpose of the maintenance phase?

- A. Change code for upgrades and updates
- B. Monitor how users use the software
- C. Add features
- D. Gather the initial requirements from scratch

**Answer:** D. Maintenance: monitor, update, add features.

**EXTRA-W1-Q9** (MCQ) In the waterfall example (2+3+4+3 months), after how long does the client first see the software?

- A. 3 months
- B. 7 months
- C. 12 months
- D. 2 months

**Answer:** C. 2+3+4+3 = 12 months; then the client says 'I don't like it'.

**EXTRA-W1-Q10** (MSQ) Which are drawbacks of the waterfall model?

- A. Changes later increase cost and time
- B. Clients may not know what they need
- C. Designers may not know which design is most feasible/usable
- D. It cannot be used with version control

**Answer:** A, B, C. The three drawbacks in Lecture 6.

**EXTRA-W1-Q11** (MCQ) The model whose steps bend upward after implementation to form a V shape is the ________.

- A. V-model
- B. Iterative model
- C. Agile model
- D. Waterfall model

**Answer:** A. Verification and validation on the right arm.

**EXTRA-W1-Q12** (MSQ) Which are agile frameworks/practices mentioned in the course?

- A. Scrum
- B. Test-driven development
- C. Sprints
- D. Kanban

**Answer:** A, D, C, B. Frameworks: Scrum, Kanban. Practices: sprints, TDD.

**EXTRA-W1-Q13** (MCQ) Which is a key difference between building a house and building software?

- A. Software is made of abstract logical components and keeps changing
- B. Houses are never designed first
- C. Software has no requirements
- D. Software cannot be tested

**Answer:** A. Abstract, adaptable and evolving vs tangible and static.

**EXTRA-W1-Q14** (MCQ) Inventory management is the act of measuring the ________ of products available.

- A. colour and size only
- B. seller names
- C. delivery speed only
- D. amount, location, pricing and mix

**Answer:** D. Definition from Lecture 2.

**EXTRA-W1-Q15** (MCQ) Amazon's home page differs between users because it is customised using ________.

- A. the developer's choice
- B. your phone model
- C. your bank
- D. the items you viewed and your shopping history

**Answer:** D. Personalisation uses view and purchase history.

**EXTRA-W1-Q16** (MCQ) Amazon Pay is best described as a ________.

- A. mobile wallet
- B. payment gateway only
- C. testing tool
- D. inventory system

**Answer:** A. A way to carry cash digitally; features like add money and auto reload.

**EXTRA-W1-Q17** (MCQ) The implementation behind interface A (inputs W, X, Y → output Z) is rewritten but the inputs and outputs stay the same. What happens to the interface?

- A. It turns into a class
- B. It stays the same
- C. It must be redesigned
- D. It becomes invalid

**Answer:** B. Code behind an interface may change as long as the interface remains.

**EXTRA-W1-Q18** (MCQ) Software bugs cost the US economy about how much in 2016, according to the lecture?

- A. $59.5 billion
- B. $100 billion
- C. $1.1 trillion
- D. $10 million

**Answer:** C. 2002: about $59.5 billion; 2016: $1.1 trillion.

**EXTRA-W1-Q19** (MCQ) Alpha testing is done in ________.

- A. a lab or staging environment
- B. the requirements phase
- C. real-life user settings
- D. the maintenance phase

**Answer:** A. Alpha = internal staff in a lab/staging; beta = real life.

**EXTRA-W1-Q20** (MCQ) A team builds key features, deploys, shows the client, takes feedback and refines in the next cycle. This is the ________ model.

- A. iterative
- B. V
- C. waterfall
- D. sequential

**Answer:** A. Repeated cycles with client feedback; agile is a popular iterative model.

**EXTRA-W1-Q21** (MCQ) A team delivers small increments and quick prototypes of key features using sprints. This is ________ methodology.

- A. Waterfall
- B. Agile
- C. Big-bang
- D. V-model

**Answer:** B. Agile frameworks: Scrum, Kanban.

**EXTRA-W1-Q22** (MCQ) In the V-model, after implementation the steps ________.

- A. end with maintenance only
- B. repeat the requirements phase
- C. bend upward: verify and validate modules, then the whole system
- D. are skipped

**Answer:** C. The right arm tests each level against the corresponding design level.

**EXTRA-W1-Q23** (MCQ) Which of these is static, unlike software?

- A. A constructed building
- B. A music player app
- C. An agile team
- D. A website

**Answer:** A. Buildings are tangible and static; software keeps changing (Winamp → Saavn).

## Week 2 · FBS & Think and Link

**NPTEL-W2-Q1** (MCQ) What is the consequence of NOT integrating Function, Behavior, and Structure during the design phase?

- A. It creates an incoherent and potentially redundant design with multiple solutions.
- B. It increases development time.
- C. It makes the software more complex.
- D. It is difficult to communicate the design to stakeholders.

**Answer:** A. E.g. only mood detection as a function: many possible solutions, not decidable.

**NPTEL-W2-Q2** (MSQ) What are the advantages of integrating Function, Behavior, and Structure during conceptual design?

- A. It creates a unified view of the design solution.
- B. It helps ensure the solution meets all the requirements.
- C. It facilitates clear communication within the development team.
- D. It reduces the risk of getting stuck during the design process.

**Answer:** A, B, C, D. All four benefits were listed in Lecture 11.

**NPTEL-W2-Q3** (MCQ) How many possible FBS graphs can exist for a single software design problem?

- A. There is always a single, correct FBS graph.
- B. There can be multiple possible FBS graphs depending on the design approach.

**Answer:** B. BSF, FSB and other combinations are all possible.

**NPTEL-W2-Q4** (MCQ) In __________, you can explore the graph and then edit the graph by adding the features available in Think&Link.

- A. Planning Phase
- B. Introduction Phase
- C. Induction Phase
- D. Brainstorm Phase

**Answer:** C. Introduction: explore only. Induction: explore and edit, then evaluate. Ideation: build from scratch.

**NPTEL-W2-Q5** (MCQ) The formal realisation evaluation criteria in a FBS graph ensures that _________

- A. FBS graph can be used for formal documentation
- B. FBS graph is formally correct
- C. FBS graph can be used in formal conversations
- D. FBS graph converts to the corresponding UML diagrams

**Answer:** D. Formal realisation = the graph can be translated to UML.

**NPTEL-W2-Q6** (MCQ) The most important reason to link function, structure and behaviour is to _________

- A. Describe in depth a part of a solution
- B. Create a correct solution
- C. Develop an integrated solution
- D. Create different solutions for a given problem

**Answer:** C. Linking gives an integrated view of the design.

**NPTEL-W2-Q7** (MSQ) Consider: "The emotion camera captures the user emotion, then provides it to the playlist generator which then creates a playlist based on the mood". This statement describes ____________

- A. interactions in the design solution
- B. implementation of the mood based music playing feature
- C. description of a use case

**Answer:** A, B. It is a behaviour (interaction of structures). The portal gave partial credit for either one; the accepted key lists both.

**NPTEL-W2-Q8** (MCQ) The __________ evaluation criteria is indicative of the interconnected function, structure and behaviour nodes in the FBS graph.

- A. Consistency
- B. Complexity
- C. Connectivity
- D. Competency

**Answer:** C. Connectivity = how F, S, B nodes are interlinked.

**NPTEL-W2-Q9** (MCQ) The _________ evaluation criteria is indicative of the number of nodes in each of the categories of function, behaviour and structure.

- A. Complexity
- B. Level adjacency
- C. Validity
- D. Correctness

**Answer:** A. Complexity = number of nodes per category.

**NPTEL-W2-Q10** (MCQ) The stage which precedes the development stage in the traditional SDLC is?

- A. Requirement stage
- B. Design stage
- C. Maintenance stage
- D. Testing stage

**Answer:** B. Requirements → Design → Development → Testing → Maintenance.

**EXTRA-W2-Q1** (MCQ) In FBS, the 'why' of the design corresponds to ________.

- A. Interface
- B. Behaviour
- C. Structure
- D. Function

**Answer:** D. Why = function; what = structure; how = behaviour.

**EXTRA-W2-Q2** (MCQ) An 'emotion recognition camera' in the mood-based music player is a ________.

- A. Requirement
- B. Function
- C. Structure
- D. Behaviour

**Answer:** C. Physical component.

**EXTRA-W2-Q3** (MCQ) 'Playlist creation' in the mood-based music player is a ________.

- A. Function
- B. Structure
- C. Behaviour
- D. Class

**Answer:** A. A feature of the solution.

**EXTRA-W2-Q4** (MCQ) 'User places face near the camera' is best classified as a ________ node.

- A. Structure
- B. Test
- C. Function
- D. Behaviour

**Answer:** D. An interaction that leads to achieving a function.

**EXTRA-W2-Q5** (MCQ) In the FBS graph, the nodes and links represent ________.

- A. Only classes and objects
- B. Only the user interface
- C. Test cases
- D. F/B/S elements and the connections among them

**Answer:** D. Nodes = F, B, S; links connect them.

**EXTRA-W2-Q6** (MCQ) Think & Link phases in order (as shown in the lecture) are ________.

- A. Ideation, Induction, Introduction
- B. Induction, Introduction, Ideation
- C. Introduction, Induction, Ideation
- D. Planning, Coding, Testing

**Answer:** C. Explore, then edit and evaluate, then create your own.

**EXTRA-W2-Q7** (MCQ) In which Think & Link phase do you write your own design problem and build an FBS graph from scratch?

- A. Induction
- B. Maintenance
- C. Introduction
- D. Ideation

**Answer:** D. Done for two problems.

**EXTRA-W2-Q8** (MCQ) Which FBS evaluation criterion is about the number of nodes in each of F, B, S?

- A. Formal realisation
- B. Consistency
- C. Connectivity
- D. Complexity

**Answer:** D. Complexity = node counts.

**EXTRA-W2-Q9** (MCQ) 'Facial recognition', 'voice-based mood detection' and 'user-history-based mood detection' are different ________ for the function 'mood detection'.

- A. behaviours
- B. phases
- C. requirements
- D. structures

**Answer:** D. Many structures can realise one function; integration with behaviour helps decide.

**EXTRA-W2-Q10** (MCQ) Experienced designers continuously think about the ________ of the design.

- A. cost, time and people
- B. why, what and how
- C. code, test and release
- D. who, when and where

**Answer:** B. Why = function, what = structure, how = behaviour.

**EXTRA-W2-Q11** (MCQ) One way to integrate F, B and S is to ________.

- A. start from a known solution and evaluate whether it applies
- B. wait for beta testing
- C. write the code first
- D. skip the structures

**Answer:** A. E.g. existing mood-detecting cameras as candidate structures.

**EXTRA-W2-Q12** (MCQ) 'User authentication' in the mood-based music player is a ________.

- A. behaviour
- B. structure
- C. function
- D. use case diagram

**Answer:** C. A feature of the solution.

**EXTRA-W2-Q13** (MCQ) 'Voice sentiment analysis algorithm' is a ________.

- A. requirement
- B. behaviour
- C. function
- D. structure

**Answer:** D. A logical component.

**EXTRA-W2-Q14** (MCQ) 'System fetches songs based on the mood' is a ________.

- A. behaviour
- B. structure
- C. function
- D. class

**Answer:** A. An action by structures that achieves a function.

**EXTRA-W2-Q15** (MCQ) In an FBS graph you must always start from a function node.

- A. True
- B. False

**Answer:** B. You can start from any node: F, B or S.

**EXTRA-W2-Q16** (MCQ) In Think & Link you answer planning questions and create a graph from scratch in the ________ phase.

- A. Induction
- B. Maintenance
- C. Ideation
- D. Introduction

**Answer:** C. Third phase; done for two problems.

**EXTRA-W2-Q17** (MCQ) Which is NOT a rating category in the Think & Link evaluation wheel?

- A. Needs Improvement
- B. Excellent
- C. Missing
- D. Meets Expectation

**Answer:** B. Ratings: Meets Expectation, Needs Improvement, Inadequate, Missing.

**EXTRA-W2-Q18** (MCQ) A software conceptual design is a design description that can be represented ________.

- A. only as a test plan
- B. graphically, numerically or textually
- C. only as UML
- D. only as code

**Answer:** B. Lecture 13 summary.

## Week 3 · UML, VeriSIM, quality

**NPTEL-W3-Q1** (MCQ) What are the two main types of views used in UML diagrams to represent a software design?

- A. Sequential view and logical view
- B. Structural view and dynamic behavioral view
- C. Abstract view and concrete view
- D. Functional view and non-functional view

**Answer:** B. Class diagram = structural; sequence/state/activity = dynamic.

**NPTEL-W3-Q2** (MCQ) What is design tracing in the context of VeriSIM?

- A. Analyzing the comments and code annotations left by developers.
- B. Constructing a state diagram that models a specific scenario in the software design.
- C. Manually reviewing the class diagram for errors and inconsistencies.
- D. Stepping through the code line by line to identify bugs.

**Answer:** B. Transitions come from sequence-diagram messages; state variables from the class diagram.

**NPTEL-W3-Q3** (MCQ) What is the main difference between functional requirements and non-functional requirements according to the lecture?

- A. Functional requirements define what the system should do, while non-functional requirements define how the system should look.
- B. Functional requirements are easier to define, while non-functional requirements are more subjective.
- C. Functional requirements focus on the system's features, while non-functional requirements focus on its behavior.
- D. Functional requirements are provided by the developers, while non-functional requirements come from the users.

**Answer:** C. Functional = what the system does; non-functional = how it behaves.

**NPTEL-W3-Q4** (MCQ) Rido is a ride sharing app, where users can share rides with others to reach their destination.

Consider the requirement: "When users pay for their rides (UPI, Net banking, mobile wallets etc.), payment failures can occur. Rido should be able to seamlessly handle such failures." This is a quality attribute related to __________

- A. Correctness
- B. Reliability
- C. Robustness
- D. None of the above

**Answer:** C. Robustness = recovering from errors/unexpected situations.

**NPTEL-W3-Q5** (MCQ) Rido is a ride sharing app, where users can share rides with others to reach their destination.

During beta testing, Rido crashed often when many users tried to book rides. Rido is unable to satisfy the requirement of ___________

- A. Correctness
- B. Reliability
- C. Robustness
- D. None of the above

**Answer:** B. Reliability = behaving the same way over time; crashing often breaks it.

**NPTEL-W3-Q6** (MCQ) ATM withdrawal system (class diagram with ATM and Account classes, and a sequence diagram for withdrawal).

The class diagram only contains data members in the class and it has nothing to do with the behavior of the class.

- A. True
- B. False

**Answer:** B. Classes have three compartments: name, attributes, operations (methods).

**NPTEL-W3-Q7** (MCQ) ATM withdrawal system (class diagram with ATM and Account classes, and a sequence diagram for withdrawal).

"balance" in the "Account" class in the class diagram is _____________

- A. A class
- B. An object
- C. A data member of the "Account" class
- D. A member function of the "Account" class

**Answer:** C. Attributes sit in the middle compartment.

**NPTEL-W3-Q8** (MCQ) ATM withdrawal system (class diagram with ATM and Account classes, and a sequence diagram for withdrawal).

"setOption()" in the ATM class in the class diagram is _____________

- A. A class
- B. An object
- C. A data member of the "ATM" class
- D. A member function of the "ATM" class

**Answer:** D. Operations sit in the bottom compartment.

**NPTEL-W3-Q9** (MCQ) ATM withdrawal system (class diagram with ATM and Account classes, and a sequence diagram for withdrawal).

What are the possible values that the "deposit()" function of the "Account" class returns?

- A. True or False
- B. 1 or 0
- C. Deposited amount
- D. Depositor name

**Answer:** A. Return type is bool in the class diagram.

**NPTEL-W3-Q10** (MCQ) ATM withdrawal system (class diagram with ATM and Account classes, and a sequence diagram for withdrawal).

If checkPin() function from the ATM class returns false then what message will it show to the user?

- A. Low account balance
- B. Correct PIN
- C. Incorrect PIN
- D. Re-enter PIN

**Answer:** C. Read off the else-branch of the sequence diagram.

**EXTRA-W3-Q1** (MCQ) A class in a UML class diagram has three compartments: name, ________, and operations.

- A. attributes
- B. lifelines
- C. states
- D. messages

**Answer:** A. Top = name, middle = attributes, bottom = operations.

**EXTRA-W3-Q2** (MCQ) In a sequence diagram, the horizontal arrows represent ________.

- A. classes
- B. requirements
- C. messages exchanged in order
- D. attributes

**Answer:** C. Vertical dashed lines are lifelines.

**EXTRA-W3-Q3** (MCQ) Which view models the possible life histories of an object of a class?

- A. Interaction view
- B. Activity view
- C. State machine view
- D. Structural view

**Answer:** C. Dynamic view; activity = flow of control; interaction = message sequence.

**EXTRA-W3-Q4** (MSQ) Which are kinds of knowledge needed for design comprehension?

- A. Problem domain knowledge
- B. Knowledge of dynamic behaviours in the design
- C. Knowledge of main goals in the diagrams
- D. Design diagram knowledge

**Answer:** A, D, C, B. The four from Lecture 17.

**EXTRA-W3-Q5** (MCQ) VeriSIM stands for ________.

- A. Visual Software Integrated Modelling
- B. Verifying designs by Simulating scenarios
- C. Verifying Sequence Interaction Models
- D. Validating Software In Modules

**Answer:** B. It builds integrated understanding of class and sequence diagrams.

**EXTRA-W3-Q6** (MCQ) In design tracing, the transitions of the state diagram correspond to ________.

- A. messages in the sequence diagram
- B. attributes in the class diagram
- C. use cases
- D. FBS functions

**Answer:** A. States hold variables from the class diagram.

**EXTRA-W3-Q7** (MCQ) The extent to which a program behaves according to its specification is ________.

- A. Portability
- B. Correctness
- C. Reliability
- D. Robustness

**Answer:** B. A functional requirement.

**EXTRA-W3-Q8** (MCQ) A wallet app rejects negative amounts and copes with very high traffic. This shows ________.

- A. Modularity
- B. Reliability
- C. Robustness
- D. Correctness

**Answer:** C. Handling unexpected input and conditions.

**EXTRA-W3-Q9** (MSQ) Which are non-functional requirements?

- A. Reliability
- B. Robustness
- C. Security
- D. Performance

**Answer:** A, B, D, C. Correctness is the functional one.

**EXTRA-W3-Q10** (MCQ) Modelling is ________.

- A. deploying software
- B. creating an external, explicit representation of the system to be built
- C. writing test cases
- D. gathering requirements

**Answer:** B. FBS graph and UML are both models.

**EXTRA-W3-Q11** (MCQ) A class diagram is a ________ diagram.

- A. timing
- B. static structure
- C. deployment-only
- D. dynamic behaviour

**Answer:** B. Classes, attributes, operations and relationships.

**EXTRA-W3-Q12** (MCQ) The UML view that shows the flow of control among computational activities is the ________ view.

- A. interaction
- B. state machine
- C. activity
- D. structural

**Answer:** C. State machine = object life history; interaction = messages.

**EXTRA-W3-Q13** (MCQ) Lifelines appear in a ________ diagram.

- A. sequence
- B. use case only
- C. FBS
- D. class

**Answer:** A. Objects on top with vertical lifelines; arrows are messages.

**EXTRA-W3-Q14** (MCQ) The main building block of object-oriented modelling is the ________ diagram.

- A. class
- B. timing
- C. sequence
- D. activity

**Answer:** A. From Lecture 16.

**EXTRA-W3-Q15** (MCQ) The system used as the context in VeriSIM is an ________.

- A. ATM
- B. online shop
- C. automated door-locking system
- D. music player

**Answer:** C. Register, lock and unlock with a passcode.

**EXTRA-W3-Q16** (MCQ) In the door-locking system, the user chooses lock and enters an incorrect passcode. The door ________.

- A. unlocks
- B. remains unlocked
- C. explodes
- D. locks

**Answer:** B. Incorrect passcode: no state change.

**EXTRA-W3-Q17** (MCQ) In design tracing, the variables in the states are taken from the ________ diagram.

- A. deployment
- B. FBS
- C. use case
- D. class

**Answer:** D. Transitions come from the sequence diagram.

**EXTRA-W3-Q18** (MCQ) Reliability is the extent to which a program ________.

- A. is portable
- B. meets its specification
- C. recovers from unexpected input
- D. behaves the same way over time in the same operating environment

**Answer:** D. Do not confuse with correctness and robustness.

**EXTRA-W3-Q19** (MCQ) Quality attributes are often implicit and not shown in the UML diagrams.

- A. True
- B. False

**Answer:** A. So note them and the decisions based on them explicitly (Lecture 20).

## Week 4 · Mapping & abstraction

**NPTEL-W4-Q1** (MCQ) What do the structures in the FBS framework represent?

- A. The functionalities and features of the software.
- B. The physical and logical components that make up the software.
- C. The interactions between different functionalities.
- D. The user interface elements of the software.

**Answer:** B. F = features, S = components, B = interactions.

**NPTEL-W4-Q2** (MCQ) What is the key difference between the FBS and UML modelling representations?

- A. FBS focuses on user interface design, while UML focuses on system functionalities.
- B. FBS is used for code generation, while UML is for design communication.
- C. FBS provides a high-level overview, while UML diagrams offer more detailed views.
- D. FBS is created before requirements definition, while UML comes after.

**Answer:** C. Different levels of abstraction.

**NPTEL-W4-Q3** (MSQ) Purpose of the modeling is _________

- A. To provide a vehicle for communication and idea generation
- B. To do analysis and comprehension
- C. To get hold of stakeholders and gather requirements
- D. To come up with a blueprint for implementation

**Answer:** A, B, D. FBS: communication; UML: analysis; detailed UML: blueprint.

**NPTEL-W4-Q4** (MCQ) If a team of software designers want to first communicate the key ideas of the software before detailing out the solution, the appropriate model to be used is __________

- A. FBS
- B. Simple UML models
- C. Detailed UML models

**Answer:** A. FBS = high-level overview for communication.

**NPTEL-W4-Q5** (MCQ) A software design team wants a model which a development team can directly transform to code. Which is most appropriate?

- A. FBS
- B. Simple UML models
- C. Detailed UML models

**Answer:** C. Detailed UML maps closely to code; tools can generate code.

**NPTEL-W4-Q6** (MCQ) __________ is used to divide a software system into multiple independent modules, which are capable of carrying out the desired functionalities.

- A. Abstraction
- B. Modularization
- C. Decomposition

**Answer:** B. Modularization = independent co-working modules.

**NPTEL-W4-Q7** (MCQ) __________ is a way of hiding details in the design at each stage of the design process.

- A. Abstraction
- B. Modularization
- C. Decomposition

**Answer:** A. Abstraction hides details; level of detail = level of abstraction.

**NPTEL-W4-Q8** (MCQ) While creating a software conceptual design, you are breaking down the implementation components. Which software engineering process are you following?

- A. Design analysis
- B. Testing
- C. Decomposition
- D. Implementation

**Answer:** C. Breaking down components = decomposition.

**EXTRA-W4-Q1** (MCQ) Function ↔ Behaviour mapping in FBS initiates which process?

- A. Evaluation and refinement
- B. Requirement definition
- C. Design analysis
- D. Reusability

**Answer:** B. From the mapping table in Lecture 23.

**EXTRA-W4-Q2** (MCQ) Structure ↔ Behaviour mapping initiates ________.

- A. Requirement definition
- B. Maintenance only
- C. Reusability
- D. Design analysis, testing, implementation and requirements change

**Answer:** D. Mapping table.

**EXTRA-W4-Q3** (MCQ) Function ↔ Structure mapping corresponds to ________.

- A. Testing
- B. Reusability and change in needs
- C. Evaluation and decomposition
- D. Requirement definition

**Answer:** B. Mapping table.

**EXTRA-W4-Q4** (MCQ) Behaviour ↔ Behaviour and Structure ↔ Structure mappings correspond to ________.

- A. Reusability
- B. Evaluation, decomposition and refinement
- C. Requirement definition
- D. Deployment

**Answer:** B. Mapping table.

**EXTRA-W4-Q5** (MCQ) Order the abstraction levels from high to low:

- A. FBS → UML → detailed UML → code
- B. Detailed UML → UML → FBS → code
- C. UML → FBS → code → detailed UML
- D. Code → UML → FBS

**Answer:** A. Detail is added as we go down.

**EXTRA-W4-Q6** (MCQ) In moving from FBS to UML, functions are expanded into ________.

- A. state diagrams
- B. use cases
- C. sequence diagrams
- D. class diagrams

**Answer:** B. Structures → class diagrams; behaviours → sequence diagrams.

**EXTRA-W4-Q7** (MCQ) In moving from FBS to UML, structures are detailed into ________.

- A. class diagrams
- B. test cases
- C. sequence diagrams
- D. use cases

**Answer:** A. Behaviours → sequence diagrams.

**EXTRA-W4-Q8** (MCQ) In moving from FBS to UML, behaviours are described by ________.

- A. components
- B. sequence diagrams
- C. use cases
- D. class diagrams

**Answer:** B. As in the mood-detection example.

**EXTRA-W4-Q9** (MCQ) Experts, according to the course summary, spend a lot of time in the ________.

- A. testing phase only
- B. initial phases: understanding the problem and modelling
- C. coding phase
- D. maintenance phase only

**Answer:** B. Lecture 25.

**EXTRA-W4-Q10** (MCQ) The model that is a vehicle for communication and idea generation is the ________.

- A. FBS graph
- B. detailed UML model
- C. test report
- D. source code

**Answer:** A. UML models are for analysis; detailed UML for blueprint.

**EXTRA-W4-Q11** (MCQ) UML models are used for ________.

- A. bug fixing only
- B. gathering requirements
- C. deployment
- D. analysis and comprehension

**Answer:** D. As in VeriSIM.

**EXTRA-W4-Q12** (MCQ) Tools can automatically generate code from ________.

- A. FBS graphs
- B. requirement lists
- C. detailed UML diagrams
- D. test reports

**Answer:** C. Detailed UML corresponds closely to implementation.

**EXTRA-W4-Q13** (MCQ) In detailed UML, every class in the model maps to ________ in the implementation code.

- A. one or more classes
- B. a database only
- C. exactly zero classes
- D. one test

**Answer:** A. Close correspondence with code.

**EXTRA-W4-Q14** (MCQ) UML diagrams are an example of ________ level abstraction.

- A. medium
- B. very low
- C. high
- D. no

**Answer:** A. FBS = high; detailed UML = low (near code).

**EXTRA-W4-Q15** (MCQ) The FBS representation is an example of ________ level abstraction.

- A. code
- B. low
- C. medium
- D. high

**Answer:** D. It gives an overview of the solution.

**EXTRA-W4-Q16** (MCQ) Modules produced by modularization are the ________ of the software.

- A. basic building blocks
- B. requirements
- C. clients
- D. test cases

**Answer:** A. Independent, co-working modules.

**EXTRA-W4-Q17** (MCQ) Software development is described as a ________.

- A. systematic process of problem-solving
- B. hardware process
- C. one-time coding task
- D. random activity

**Answer:** A. Lecture 22.

**EXTRA-W4-Q18** (MCQ) Software design is more complex than design in architecture because software is ________.

- A. static
- B. abstract and intangible
- C. cheap
- D. physical

**Answer:** B. Though design processes across domains are similar.

**EXTRA-W4-Q19** (MCQ) The mapping table of FBS elements to software processes is based on the ________.

- A. Kanban
- B. Alpha testing
- C. Waterfall model only
- D. Rational Unified Process

**Answer:** D. Header of the slide table in Lecture 23.
