### Step 1: View the file

```bash
cd inhere
find inhere/ -type f -size 1033c ! -executable
cat <location-the-previous-command-prints>
```

### Step 2: Copy the password

### Step 3: Exit the view mode

```bash
exit
```

### Step 4: Ssh again but to bandit6

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

Then paste the password
