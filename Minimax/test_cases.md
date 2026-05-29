## Sample Test Cases

### Test Case 1: X Can Win Immediately


### Test Case 2: Forced Draw

**Board**
```text
X O X
X O O
O X _
```

**Turn**
```text
X
```

**Expected Output**
```text
0
```

---

### Test Case 3: Empty Board

**Board**
```text
_ _ _
_ _ _
_ _ _
```

**Turn**
```text
X
```

**Expected Output**
```text
0
```

---

### Test Case 4: X Already Won

**Board**
```text
X X X
O O _
_ _ _
```

**Turn**
```text
O
```

**Expected Output**
```text
1
```

---

### Test Case 5: O Already Won

**Board**
```text
X X O
X O _
O _ _
```

**Turn**
```text
X
```

**Expected Output**
```text
-1
```
