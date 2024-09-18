### Step 1: View the file

```bash
cd inhere
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat <location-the-previous-command-prints>
```

### Step 2: Copy the password

### Step 3: Exit the view mode

```bash
exit
```

### Step 4: Ssh again but to bandit7

```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

Then paste the password
