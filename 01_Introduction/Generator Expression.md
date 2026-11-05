# Generator Expressions & Built-in Iteration Guide
*A practical reference for Applied AI / Machine Learning interviews*

---

## 1. Generator Expression: Syntax Breakdown

A **generator expression** produces a lazy iterator that computes elements on demand rather than allocating memory upfront for an entire collection.

### Core Anatomy

```python
( <expression> for <var> in <iterable> )
```

| Component | Role | Example |
| :--- | :--- | :--- |
| `<expression>` | Value yielded on each step | `x ** 2` |
| `for <var> in` | Variable assignment per step | `for x in` |
| `<iterable>` | Source stream or collection | `range(1_000_000)` |

---

### Syntactic Variations

#### 1. Filtering with Trailing `if`
Filters items out. If the condition is `False`, the item is skipped.

```python
# Syntax: (expr for item in iterable if condition)
even_squares = (x**2 for x in nums if x % 2 == 0)
```

#### 2. Transforming with Inline `if-else` (Ternary)
Alters the value produced. Every element in the source is processed.

```python
# Syntax: (val_true if cond else val_false for item in iterable)
labels = (1 if score >= threshold else 0 for score in predictions)
```

#### 3. Nested Iterators (Flattening)
Executes from left to right, matching the nesting order of standard `for` loops.

```python
# Outer loop first, inner loop second
tokens = (token for doc in documents for token in doc.split())
```

#### 4. Parentheses Elision Rule
When a generator expression is the **sole positional argument** to a function, the outer parentheses can be omitted.

```python
# Valid & idiomatic:
total = sum(x**2 for x in range(10))

# Parentheses REQUIRED when multiple arguments exist:
best = max((x for x in scores if x > 0), default=0)
```

---

## 2. Deep Dive: `all()` and `any()`

Both functions consume iterables lazily and implement **short-circuit evaluation**, making them $O(1)$ auxiliary space and worst-case $O(N)$ runtime.

### `all(iterable)`

Returns `True` if **every** element in the iterable is truthy (or if the iterable is empty).

```python
# Evaluates lazily: stops at the first False
all(num % k == 0 for num in nums)
```

* **Short-circuit trigger:** Encountering a single falsy value halts execution immediately.
* **Edge case (Vacuous Truth):** `all([])` returns `True`.

### `any(iterable)`

Returns `True` if **at least one** element in the iterable is truthy.

```python
# Evaluates lazily: stops at the first True
has_nan = any(math.isnan(val) for val in tensor_values)
```

* **Short-circuit trigger:** Encountering a single truthy value halts execution immediately.
* **Edge case:** `any([])` returns `False`.

---

## 3. High-Frequency Interview Methods to Pair with Generators

### Reductions & Aggregations

| Method | Typical Use Case | Example |
| :--- | :--- | :--- |
| `sum(iterable, start=0)` | Fast cumulative arithmetic | `sum(len(seq) for seq in batches)` |
| `max(iterable, default=...)` | Finding optimal metrics | `max((score for score in vals), default=-1)` |
| `min(iterable, default=...)` | Finding minimum error/loss | `min(abs(target - x) for x in samples)` |
| `str.join(iterable)` | String serialization | `",".join(str(i) for i in ids)` |

---

### Stream Manipulation Tools (`itertools`)

For streaming inference, batch slicing, or sliding windows, know these standard library tools:

```python
import itertools
```

#### `itertools.islice(iterable, stop)` or `islice(iterable, start, stop, step)`
Inspects the first $K$ items of an infinite or large generator without reading everything into memory.

```python
# Stream first 100 samples from a generator
first_hundred = list(itertools.islice(large_stream_gen, 100))
```

#### `itertools.batched(iterable, n)` *(Python 3.12+)*
Batches any iterator into tuples of length $n$.

```python
# Mini-batching raw inputs
for batch in itertools.batched(stream, 32):
    process_batch(batch)
```

#### `itertools.chain(*iterables)` / `chain.from_iterable(iterable)`
Combines multiple streams seamlessly without creating temporary joined lists.

```python
merged_stream = itertools.chain(gen_a, gen_b)
```

---

## 4. Applied AI Interview Comparison Matrix

| Pattern | Memory | Short-Circuits? | When to Use |
| :--- | :--- | :--- | :--- |
| `all(x % k == 0 for x in nums)` | $O(1)$ | **Yes** | **Default choice.** Idiomatic, lazy, avoids list overhead. |
| `all([x % k == 0 for x in nums])` | $O(N)$ | **No** | **Anti-pattern.** Allocates full boolean list before calling `all()`. |
| `for x in nums: if ... return False` | $O(1)$ | **Yes** | Use when intermediate side-effects, complex logging, or index tracking are required. |

---

## 5. Defensive Edge Cases to Mention Out Loud

1. **Division by Zero:** Always check if divisors or denominators can be $0$ before modulo/division operations.
   ```python
   if k == 0:
       raise ValueError("Divisor k cannot be zero.")
   ```
2. **Empty Collections:** Explicitly state the mathematical contract:
   * $\text{all}(\emptyset) = \text{True}$
   * $\text{any}(\emptyset) = \text{False}$
3. **Generator Exhaustion:** Remember that generator expressions are **single-pass iterators**. Once consumed (e.g., by calling `sum()` or iterating over them), they cannot be iterated over again.