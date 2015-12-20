#lang racket
(require 2htdp/batch-io)

(define (solve l)
  (define (iter l acc)
    (if (null? l) acc
        (iter (cdr l) (cons (car l) acc))))
  (iter l '()))

(for-each displayln (solve (read-lines 'stdin)))
