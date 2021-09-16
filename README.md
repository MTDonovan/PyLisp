# Examples of usage

```python
(thread
 ('MAKE THIS TEXT LOWER CASE',
  (lambda x: x.lower()),
  (print)))

# prints 'make this lower text'

(print
 (thread
  (100,
   (lambda x: x / 2.25),
   (round, 2))))

# prints 44.44

(thread
 (100,
  ('/', 2, 6, 8),
  ('+', 100.55),
  (print)))

# prints 101.59166666666667
```
