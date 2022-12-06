#lang racket

(define (value badge)
  (let ([c (char->integer badge)])
    (if (char-lower-case? badge)
      (- c 96)
      (- c 38))))

(define (badge l)
  (car
    (apply set-intersect 
           (map string->list l))))

(displayln (apply + 
    (for/list ([e (in-slice 3 (in-lines))])
              (value (badge e)))))
