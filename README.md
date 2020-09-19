# Examples of usage

```python
(thread
 ('MAKE THIS TEXT LOWER CASE',
  (lambda x: x.lower()),
  (print)))

(print
 (thread
  (100,
   (lambda x: x / 2.25))))

(thread
 (100,
  ('/', 2, 6, 8),
  ('+', 100.55),
  (print)))
```
