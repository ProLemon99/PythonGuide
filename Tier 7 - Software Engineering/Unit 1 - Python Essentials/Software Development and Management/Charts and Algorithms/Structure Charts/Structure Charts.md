# **Structure Charts**

Structure charts illustrate the hierarchical organisation and execution sequence of subroutines within a system, including data exchanges to clarify their interrelations. These charts facilitate a top-down design approach, detailing how subroutines are called, including conditions and repetitions for these calls.

Essential for software development, structure charts serve as blueprints for coding, helping allocate tasks among developers and aiding in maintenance and upgrades by identifying potential error or upgrade sites.

Various names and drawing techniques exist for these diagrams, but they share a focus on depicting a system's hierarchical design, execution sequence, and decision-making processes.

Symbols used include rectangles for subroutines, lines for subroutine calls, diamonds for decisions, circular arrows for repetitions, and circles for data parameters, with filled circles representing control parameters that influence execution order.

Structure charts are read top-to-bottom for hierarchy and left-to-right for execution order, with subroutines appearing multiple times if called by different higher-level tasks.

## **Symbols**
![Symbols](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Structure%20Charts/Images/symbols.png)

## **Example 1**
**Example of a Library Management System**
![Example 1](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Structure%20Charts/Images/example1.png)

Further detail for each of the lower-level subroutines can be shown in a separate structure chart, using the same name as the subroutine used in the main structure chart. This method of providing successively more detail as required is known as refinement.

## **Example 2 (with code)**
The following is a very simple example to show you how this might look with a very basic Python program. It has no control variables (such as a login to check credentials), but has parameters, a decision structure and repetition.

To make it easy, the 'subroutines' of a Python program are simply functions within `main()`.

**Simple Example with Python Code**
![Example 2](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Structure%20Charts/Images/example2.avif)