#lang racket

(define (read-integer-list)
  (map string->number (string-split (read-line))))

(define (list-range lst start end)
    (take (drop lst start) (- (add1 end) start)))

(define (read-query A)
  (let ([Q (read)]
        [l (read)]
        [r (read)])
    (if (eq? Q 'Q)
      (begin (displayln (apply lcm (list-range A l r))) A)
      (append
        (take A l)
        (list  (* r (list-ref A l)))
        (drop A (add1 l))))))

(define (resolve-n-queries l n)
  (when (positive? n)
    (resolve-n-queries (read-query l) (sub1 n))))

(define N (string->number (read-line)))
(define A (read-integer-list))
(define K (string->number (read-line)))

(resolve-n-queries A K)
