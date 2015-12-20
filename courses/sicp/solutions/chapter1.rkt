#lang racket

; 1.3
(define (sum-square-largest x y z)
  (cond ((and (< x y) (< x z))
         (+ (* y y) (* z z)))
        ((and (< y x) (< y z))
         (+ (* x x) (* z z)))
        (else
         (+ (* x x) (* y y)))))

(define (sqrt-iter guess x) 
  (if (good-enough? guess x)
      guess 
      (sqrt-iter (improve guess x) x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (improve-ratio guess x) 0.001))

(define (improve-ratio guess x)
  (/ (abs (- guess (improve guess x)))
     guess))

(define sqrt
  (lambda (x)
    (sqrt-iter 1.0 x)))

; 1.11

(define (f n)
  (if (< n 3)
      n
      (+ 
       (f (- n 1)) 
       (* 2 (f (- n 2)))
       (* 3 (f (- n 3))))))

(define (f2 n)
     (define (iter a b c count) 
     (if (= count 0) 
       a 
       (iter b c (+ c (* 2 b) (* 3 a)) (- count 1)))) 
   (iter 0 1 2 n))

; 1.12

(define (pascal row n)
  (if (or (= n 1) (= n row))
      1
      (+ (pascal (- row 1) (- n 1)) (pascal (- row 1) n))))

; Change count
(define (count-change amount) 
   (cc amount 5))

(define (cc amount kinds-of-coins) 
   (cond ((= amount 0) 1) 
         ((or (< amount 0) (= kinds-of-coins 0)) 0) 
         (else (+ (cc amount 
                      (- kinds-of-coins 1)) 
                  (cc (- amount 
                         (first-denomination kinds-of-coins)) 
                      kinds-of-coins))))) 
 
(define (first-denomination kinds-of-coins) 
   (cond ((= kinds-of-coins 1) 50) 
         ((= kinds-of-coins 2) 25) 
         ((= kinds-of-coins 3) 10) 
         ((= kinds-of-coins 4) 5) 
         ((= kinds-of-coins 5) 1)))

; 1.16

(define (fast-expt b n) 
  (cond ((= n 0) 1)
        ((even? n) 
         (square (fast-expt b (/ n 2)))) 
        (else 
         (* b (fast-expt b (- n 1))))))

(define (fast-expt-iter b n)
  (define (iter b n a)
    (cond 
      ((= n 0) a)
      ((even? n)
        (iter (square b) (/ n 2) a))
      (else 
        (iter b (- n 1) (* a b)))))
  (iter b n 1))

(define (square n)
  (* n n))

(define (even? n)
  (= (remainder n 2) 0))

; 1.17

(define (por a b)
  (cond 
    ((= b 0) 0)
    ((even? b)
     (por (double a) (halve b)))
    (else
     (+ a (por a (- b 1))))))

(define (double a)
  (+ a a))

(define (halve a)
  (/ a 2))

; 1.18
(define (por2 a b)
  (define (iter a b carry) 
    (cond 
      ((= b 0) carry)
      ((even? b)
       (iter (double a) (halve b) carry))
      (else
       (iter a (- b 1) (+ carry a)))))
  (iter a b 0))

; 1.21

(define (smallest-divisor n) (find-divisor n 2))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))

(define (divides? a b) (= (remainder b a) 0))

; 1.22
(define (prime? n) 
   (= n (smallest-divisor n))) 
  
(define (timed-prime-test n) 
   (start-prime-test n (current-process-milliseconds))) 
  
(define (start-prime-test n start-time) 
   (and (prime? n) 
       (report-prime n (- (current-process-milliseconds) start-time)))) 
  
(define (report-prime n elapsed-time) 
   (newline) 
   (display n) 
   (display " *** ") 
   (display elapsed-time)
   true)

(define (search-for-primes a n)
  (cond 
    ((= n 0))
    (else
     (search-for-primes 
      (+ a 1) 
      (if (timed-prime-test a) (- n 1) n)))))

; 1.23
(define (smallest-divisor-fast n) (find-divisor-fast n 2))

(define (next-even n)
  (if (= n 2) 2 (+ n 2)))

(define (find-divisor-fast n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (next-even test-divisor)))))

(define (prime-fast? n) 
   (= n (smallest-divisor-fast n)))

; 1.29
(define (cube x) (* x x x))

(define (sum term a next b) 
  (if (> a b) 
      0 
      (+ (term a)
         (sum term (next a) next b))))

(define (integral f a b dx) 
  (define (add-dx x) (+ x dx)) 
  (* 
   (sum f (+ a (/ dx 2.0)) add-dx b)
   dx))

(define (inc n)
  (+ n 1))

(define (simpson f a b n)
  (define h (/ (- b a) n))
  (define (yk k)
    (f (+ a (* k h))))
  (define (term k)
    (* (cond ((or (= k 0) (= k n)) 1) 
             ((odd? k) 4) 
             (else 2)) 
       (yk k)))
  (* (/ h 3) (sum term 0 inc n)))

; 1.30
(define (sumi term a next b)
  (define (iter a result)
    (if (> a b) 
        result
        (iter (next a) (+ result (term a)))))
  (iter a 0))

(define (simpsoni f a b n)
  (define h (/ (- b a) n))
  (define (yk k)
    (f (+ a (* k h))))
  (define (term k)
    (* (cond ((or (= k 0) (= k n)) 1) 
             ((odd? k) 4) 
             (else 2)) 
       (yk k)))
  (* (/ h 3) (sumi term 0 inc n)))

; 1.31
(define (prod term a next b) 
  (if (> a b) 
      1 
      (* (term a)
         (prod term (next a) next b))))

(define (fact n)
  (prod 
   (lambda (x) x)
   1
   inc
   n))

(define (pi-est n)
  (define (term n)
    (if (even? n)
        (/ (+ n 2) (+ n 1))
        (/ (+ n 1) (+ n 2))))
  (* (prod term 1 inc n)
     4.0))

; 1.32
(define (gaccumulate combiner null-value term a next b)
  (if (> a b) 
      null-value 
      (combiner (term a)
         (gaccumulate combiner null-value term (next a) next b))))

(define (suma term a next b)
  (gaccumulate + 0 term a next b))

; 1.33
(define (filtered-accumulate filter? combiner null-value term a next b)
  (if (> a b) 
      null-value 
      (combiner 
       (if (filter? a) (term a) null-value)
       (filtered-accumulate filter? combiner null-value term (next a) next b))))

(define (sum-square-primes a b)
  (filtered-accumulate prime? + 0 square a inc b))

; 1.35
(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) 0.0001))
  (define (try guess)
    (let ((next (f guess)))
      (display next)
      (newline)
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define (golden)
  (fixed-point (lambda (x) (+ 1 (/ 1 x))) 1.0))

; 1.36
(define (xx)
  (fixed-point (lambda (x) (/ (log 1000) (log x))) 10))

(define (xxav)
  (fixed-point 
   (lambda (x)
     (average
      x
      (/ (log 1000) (log x)))) 
   10))

; 1.37
(define (cont-frac n d k)
  (define (loop i)
    (if (> i k) 
      .0
      (/ (n i)
         (+ 
          (d i) 
          (loop (inc i))))))
  (loop 1))

; 1.38
(define (euler-cont k)
  (define (d i)
    (let ((n (inc i)))
      (if (= (remainder n 3) 0)
          (* 2 (/ n 3))
          1)))
  (+ 
   (cont-frac (lambda (x) 1) d 10)
   2))

; 1.39
(define (tan-cf x k)
  (define (n i) (if (= i 1) x (- (square x))))
  (define (d i) (- (* 2 i) 1))
  (cont-frac n d k))

; 1.40
(define (cubic a b c) 
   (lambda (x) 
     (+ (cube x) 
        (* a (square x)) 
        (* b x) 
        c)))

; 1.41
(define (doublef f)
  (lambda (n)
    (f (f n))))

; 1.42
(define (compose f g)
  (lambda (n)
    (f (g n))))

; 1.43
(define (repeated f n)
  (if (= n 0) 
      (lambda (x) x)
      (compose f (repeated f (- n 1)))))

; 1.44
(define (smooth f)
  (define dn 0.0001)
  (lambda (n)
    (/ 
     (+ 
      (f (- n dn)) (f n) (f (+ n dn)))
     3)))

(provide (all-defined-out))
