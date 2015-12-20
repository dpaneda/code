#lang racket
(define as (map string->number (string-split (read-line))))
(define bs (map string->number (string-split (read-line))))

(define x1 (read))
(define x2 (read))

(define (valueat x)
  (foldl + 0
    (map (lambda (a b) (* 0.001 (* a (expt x b))))
         as bs)))

(define (integral)
   (stream-fold + 0 (in-range x1 x2 0.001)))

(displayln (integral))
