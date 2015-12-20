#lang racket
(define (multiples g)
    (define (sum n) (/ (* n (+ n 1)) 2))
    (let* ([n (- (read) 1)] [a (quotient n 3)] [b (quotient n 5)])
      (+ (* 3 (sum a)) (* 5 (sum b)))))

(for-each displayln (map multiples (range (read))))
