#lang racket

(define (list-to-factor l)
  (if (null? l) l
    (cons (cons (first l) (second l)) (list-to-factor (cddr l)))))

(define (read-list)
  (list-to-factor (map string->number (string-split (read-line)))))

(define (mix-list l1 l2)
  (define (find-factor factor)
    (define (min-factor factor2) (cons (car factor) (min (cdr factor) (cdr factor2))))
    (define (same-factor factor2) (= (car factor) (car factor2)))
    (let ([factor2 (findf same-factor l2)])
      (if factor2 (min-factor factor2) #f)))
  (for/list ([i l1]
            #:when (find-factor i))
            (find-factor i)))

(define (mix-n-lists l n)
  (if (positive? n)
    (mix-n-lists (mix-list l (read-list)) (sub1 n))
    l))

(define n (string->number (read-line)))

(displayln (string-join (map ~a (flatten (mix-n-lists (read-list) (sub1 n))))))
