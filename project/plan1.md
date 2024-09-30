# Topic: Password Cracking

### Member: Dave Nguyen, John Win

### Example tools: johnTheRipper and hashCat

## Project Description

Create a password-cracking tool with a basic set of key functionalities based on John the ripper and hashCat.

## Learning Goals

- We want to understand how the cryptography hash function works (MD5, SHA256)
- Understand how multithreading works and how this can be implemented in the context of password cracking
- Learn how dictionary and brute-force attacks work
- How can we keep trying new passwords while not alerting the system (Stretch)
- Set up a key-logging ability in the vulnerable machine that sends back logs to a “mothership” (Stretch)

## Development Goals

- List of features we want to have:
- Support multiple hash functions like MD5, SHA1, SHA256
- The tool will read from a word list (rockyou.txt)
- Ability to crack the password with or without the salt
- Have features to increase efficiency like multithreading
- Have features to keep retrying the password while not alerting the system

## Testing and Benchmarking

- For correctness, we will have unit tests for hashing algorithms
  We also will have functional tests to test the entire cracking process
- For performance, we also will have a test that measures the speed of the cracking process

* Performance test for simple and naive passwords
* Performance test for moderate passwords with alphanumeric characters
* Performance test for strong passwords with phrases and mixed characters

## Schedule of Development

- Week 1-2: Implementation of dictionary attacks (using a list of passwords)
- Week 3-4: Implementation of multithreading
- Week 4-5: Implementation of the unit, functional tests, and time measurements
- Week 6-7: Stretch goal + Presentation
