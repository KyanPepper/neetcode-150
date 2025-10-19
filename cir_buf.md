# 622. Design Circular Buffer (Ring Buffer) — Non-Destructive Read

**Difficulty:** Medium  
**Topics:** Array, Design, Queue, Data Structure  

---

## Problem Statement

Design a **circular buffer** (ring buffer) with a fixed capacity `k`.  
The buffer uses two pointers:

- **read**: points to the oldest element (next to be *observed*).  
- **write**: points to the next position where a new element will be written.  

When the `write` pointer reaches the end of the buffer, it wraps back to the front.  
The `read` pointer is fixed at the oldest element and does **not move** (non-destructive reads).  

Implement the following operations:

- **`write(int value)`**  
  Write `value` at the `write` pointer and advance it circularly.  
  Return `true` if successful; return `false` if the buffer is **full** (no overwriting allowed).  

- **`read()`**  
  Return (but **do not remove**) the element at the `read` pointer.  
  Return `-1` if the buffer is empty.  


## Constraints

- `1 <= k <= 1000`  
- Values are integers in `[-10^4, 10^4]`  
- All operations must run in **O(1)** time.  

---

## Example

**Input**
```plaintext
["CircularBuffer","write","write","write","isFull","read","write","peekRear","read","isEmpty"]
[[3],[10],[20],[30],[],[],[40],[],[],[]]
