# Topic: Password Spraying

### Member: Dave Nguyen, John Win

### Example tools: hydra

## Project Description

Create a password-spraying tool, containing a set of key functionalities based on Hydra, along with a vulnerable machine. 

## Learning Goals

- We want to learn how attackers systematically try commonly used passwords across many accounts to avoid lockout mechanisms
- We want to explore how to use Hydra to perform password spraying on multiple services (SSH, HTTP, SMB)
- We want to learn how to optimize the attack efficiency, such as parallelization, and multi-threading (Stretch Goal 1)
- We want to learn how hackers can bypass multi-factor authentication (MFA) (Stretch Goal 2)


## Development Goals

- Once a naive machine (with no lockout mechanism) has been cracked, build a machine with lockout mechanisms
- Evade lockout and detection mechanisms while also be able to crack the machine
- Use multithreading for sending multiple requests to the vulnerable machine from multiple attacker machines 


## Testing and Benchmarking

- We will have unit tests to check if each function within the spraying tool is working
- We also will have functional tests to test the entire spraying process
- For performance, we also will have a test that measures the speed of the cracking process. The goal is to have the vulnerable machine represent a real-life login server with a set speed of server response time. There will be three different test suites. For each test suite, we will collect data and benchmark how differently the server responds and how efficient the spraying process is depending on how short or long the delay is for the password input. 
  1. Tests using simple and naive passwords 
  2. Tests using moderate passwords with alphanumeric characters
  3. Tests using strong passwords with phrases and mixed characters 


## Schedule of Development

- Week 3-4: Implementation of basic functionalities to test open services/ log-in pages on a machine
- Week 5-6: Implementation of multithreading
- *Week 7-8: Implementation of the unit, functional tests, and time measurements
- Week 9-10: Stretch goal + Presentation
