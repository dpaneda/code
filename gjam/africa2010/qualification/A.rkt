#lang racket
(define (solve-problem)
  (for ([i (in-range (read))])
    (printf "Case #~a: ~a" (+ 1 i) (solve-case))))

(define (solve-case)
  (let ((credit (read))
        (nitems (read))
        (items (map string->number (regexp-split #px" " (and (read-line) (read-line))))))
    (search-buy credit items)))

(define (search-buy credit items)
  (define sol 0)
  (for ([i (length items)])
    (for ([j (in-range (+ 1 i) (length items))])
      (and (= credit (+ (list-ref items i) (list-ref items j)))
         (set! sol (format "~a ~a\n" (+ 1 i) (+ 1 j))))))
  sol)

(solve-problem)
