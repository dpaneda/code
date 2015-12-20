#lang racket

(define (f n)
  (if (= n 0) '()
      (cons n (f (- n 1)))))
  
(define n (string->number (read-line (current-input-port) 'any)))
(print (length(f n)))
