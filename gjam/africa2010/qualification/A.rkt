#lang racket

(define (solve-problem)
  (for ([i (in-range (read))])
    (printf "Case #~a: ~a" (+ 1 i) (solve-case))))

(define (solve-case)
  (let ((credit (read))
        (nitems (begin (read-line) (read-line)))
        (items (map string->number (string-split (read-line)))))
    (search-buy credit items 0 1)))

(define (search-buy credit items i j)
  (cond 
    ((= credit (+ (list-ref items i) (list-ref items j)))
      (format "~a ~a\n" (+ 1 i) (+ 1 j)))
    ((< j (sub1 (length items)))
      (search-buy credit items i (add1 j)))
    (else
      (search-buy credit items (+ i 1) (+ i 2)))
    ))

(solve-problem)
