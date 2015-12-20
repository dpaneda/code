#lang racket
(require racket/pretty)
(require "chapter1.rkt")

; Racket kills my machine if I don't limit the memory use :-/
(custodian-limit-memory (current-custodian) (* 100 1024 1024))

; 2.1
(define (numer x) (car x)) 
  
(define (denom x) (cdr x)) 
  
(define (print-rat x) 
   (newline) 
   (display (numer x)) 
   (display "/") 
   (display (denom x)))

(define (make-rat n d)
  (let ((g ((if (< d 0) - +) (gcd n d))))
     (cons (/ n g) (/ d g))))

; 2.2
(define make-segment cons)
(define start-segment car)
(define end-segment cdr)

(define make-point cons)
(define x-point car)
(define y-point cdr)

(define (mid-point-segment s)
  (let ((a (start-segment s))
        (b (end-segment s)))
    (make-point (/ (+ (x-point a) (x-point b)) 2)
                (/ (+ (y-point a) (y-point b)) 2))))

(define (print-point p) 
  (newline) 
  (display "(") 
  (display (x-point p)) 
  (display ",") 
  (display (y-point p)) 
  (display ")")
)

(define (pmake-rectangle p) make-segment)

(define (rect-length r)
  (- (x-point (end-segment r))
     (x-point (start-segment r))))

(define (rect-height r)
  (- (y-point (end-segment r))
     (y-point (start-segment r))))

(define (rect-area r)
  (* (rect-length r) (rect-height r)))

(define (rect-perimeter r)
  (* 2 (+ (rect-length r) (rect-height r))))

; Any alternative implementation, should respect the contract
; of rect-length and rect-heigth and all should work fine

;(define a (make-point 1 1))
;(define b (make-point 11 11))
;(define s (make-segment a b))

; 2.6
(define zero (lambda (f) (lambda (x) x)))

(define (add-1 n)
  (lambda (f) (lambda (x) (f ((n f) x)))))

; 2.7
(define make-interval cons)
(define lower-bound car)
(define upper-bound cdr)

; 2.8
(define (sub-interval a b)
  (make-interval
   (- (lower-bound a) (upper-bound b))
   (- (upper-bound a) (lower-bound b))))

; helper
(define (read-interval)
  (make-interval (read) (read)))

; 2.9
; Being a<x> an interval: (a-x, a+x), it's easy to deduce that:
; a<x> + b<y> = (a+b)<x+y>
; a<x> - b<y> = (a-b)<x+y>
; However, we could not find a function for the same on the multiplication
; Take this example:
; 2<1> * 1<1> = (1, 3) * (0, 2) = (0, 6) = 3<3>

; 2.12
(define (make-center-percent c p)
  (let ((width (* c (/ p 100.0))))
    (make-interval (- c width) (+ c width))))

(define (center i)
  (/
   (- (upper-bound i) (lower-bound i))
   2))

(define (percent i)
  (* 100 
     (/
      (- (upper-bound i) (lower-bound i))
      (+ (upper-bound i) (lower-bound i)))))

; 2.13

(define (mul-interval x y) 
   (let ((p1 (* (lower-bound x) (lower-bound y))) 
         (p2 (* (lower-bound x) (upper-bound y))) 
         (p3 (* (upper-bound x) (lower-bound y))) 
         (p4 (* (upper-bound x) (upper-bound y)))) 
     (make-interval (min p1 p2 p3 p4) 
                    (max p1 p2 p3 p4))))

(define (div-interval x y) 
   (if (>= 0 (* (lower-bound y) (upper-bound y))) 
       (error "Division error (interval spans 0)" y) 
       (mul-interval x  
                     (make-interval (/ 1. (upper-bound y)) 
                                    (/ 1. (lower-bound y))))))

(define (add-interval a b)
  (make-interval
   (+ (lower-bound a) (lower-bound b))
   (+ (upper-bound a) (upper-bound b))))

(define (par1 r1 r2) 
  (div-interval (mul-interval r1 r2)
                (add-interval r1 r2)))

(define (par2 r1 r2) 
  (let ((one (make-interval 1 1)))
    (div-interval 
     one (add-interval (div-interval one r1)
                       (div-interval one r2)))))

(define (print-center i)
  (display (center i))
  (display "<")
  (display (percent i))
  (display ">")
  (newline)
  )

; 2.17
(define (last-pair l)
  (if (null? (cdr l))
      l
      (last-pair (cdr l))))

; 2.18
(define (reverse l) 
   (define (iter l result) 
     (if (null? l) 
         result 
         (iter (cdr l) (cons (car l) result)))) 
   (iter l '()))

; 2.20
(define (same-parity n . l)
  (define (iter l)
    (cond 
      ((null? l) l)
      ((equal? (even? n) (even? (car l)))
         (cons (car l) (iter (cdr l))))
      (else 
       (iter (cdr l)))))
  (cons n (iter l)))

; 2.23
(define (for-each f l)
  (cond ((null? l) #t)
        (else
         (f (car l))
         (for-each f (cdr l)))))

; 2.24
; '(1 (2 (3 4)))

; 2.25
; cadaddr
; caar
; cadadadadr (fuUUUUU)

; 1.26
; '(1 2 3 4 5 6)
; '((1 2 3) 4 5 6)
; '((1 2 3) (4 5 6))

; 2.27
(define (deep-reverse l)
  (define (iter l result) 
    (if (null? l) 
        result 
        (iter (cdr l) 
              (cons 
               (deep-reverse (car l)) 
               result)))) 
  (if (not (pair? l)) 
      l
      (iter l '())))

; 2.28
(define (fringe l)
  	(cond
		((null? l) l)	  	
		((pair? l)
			(append
				(fringe (car l))
				(fringe (cdr l))))
	  	(else
		  	(list l))))

; 2.29
(define make-mobile cons)
(define make-branch cons)
(define left-branch car)
(define right-branch cdr)

(define (total-weight mobile)
  (if (pair? mobile)
	(+ 
	  (total-weight (left-branch mobile)) 
	  (total-weight (right-branch mobile)))
	mobile))

(define (balanced? mobile)
  (= 
    (total-weight (left-branch mobile)) 
	(total-weight (right-branch mobile))))

(define mob 
  (make-mobile 
	(make-mobile 2 
	    (make-mobile 5 8)) 
	(make-mobile 4 3)))

; 2.30
(define (square-tree tree)
  (cond
	((null? tree) tree)
	((pair? tree)
	 (cons 
	   (square-tree (car tree))
	   (square-tree (cdr tree))))
	(else (* tree tree))))

(define (square-tree-map tree)
  (map
	(lambda (t)
	  (if (pair? t)
		(square-tree-map t)
		(* t t)))
	tree))

; 2.31
(define (tree-map f tree)
  (map
	(lambda (t)
	  (if (pair? t)
		(square-tree-map t)
		(f t)))
	tree))

(define (sq-tree-map tree)
  (tree-map (lambda (x) (* x x)) tree))

; 2.32
(define (subsets s)
  (if (null? s)
	'(())
	(let ((rest (subsets (cdr s))))
	  (append rest (map (lambda (x) (cons (car s) x)) rest)))))

; 2.33
(define nil '())

(define (accumulate op initial sequence) 
  (if (null? sequence) 
	initial 
	(op (car sequence)
		(accumulate op initial (cdr sequence))))) 

; Comment as we need real map on matrix ops
;(define (map p sequence)
;  (accumulate (lambda (x y) (cons (p x) y)) nil sequence))

(define (append seq1 seq2)
  (accumulate cons seq2 seq1))

(define (length sequence)
  (accumulate (lambda (x y) (+ y 1)) 0 sequence))

; 2.34
(define (horner-eval x coefficient-sequence)
  (accumulate (lambda (this-coeff higher-terms) (+ this-coeff (* x higher-terms)))
			  0
			  coefficient-sequence))

; 2.35
(define (count-leaves t)
  (accumulate + 0
	(map (lambda (node) (if (pair? node) (count-leaves node) 1))
	  t)))

; 2.36
(define (accumulate-n op init seqs)
  (if (null? (car seqs))
	nil
	(cons (accumulate op init (map car seqs))
		  (accumulate-n op init (map cdr seqs)))))

; 2.37
(define (dot-product v w)
  (accumulate + 0 (map * v w)))

(define (matrix-*-vector m v)
  (map (lambda (w) (dot-product w v)) m))

(define (transpose mat)
  (accumulate-n cons nil mat))

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
  	(map (lambda (row) (matrix-*-vector cols row)) m)))

;(dot-product (list 1 2 3) (list 4 5 6))
;(define matrix (list (list 1 2 3 4) (list 5 6 7 8) (list 9 10 11 12)))
;(define vector (list 1 2 1 2))
;(matrix-*-vector matrix vector)
;(transpose matrix)
;(matrix-*-matrix matrix (transpose matrix))

; 2.38
(define fold-right accumulate)

(define (fold-left op initial sequence)
  (define (iter result rest)
	(if (null? rest)
	  result
	  (iter (op result (car rest))
			(cdr rest))))
  (iter initial sequence))

;(fold-right / 1 (list 1 2 3))
;(fold-left / 1 (list 1 2 3))
;(fold-right list nil (list 1 2 3))
;(fold-left list nil (list 1 2 3))
; op should be associative

; 2.39
(define (r-reverse sequence)
  (fold-right (lambda (x y) (append y (list x))) nil sequence))

(define (l-reverse sequence)
  (fold-left (lambda (x y) (cons y x)) nil sequence))

;(r-reverse (list 1 2 3 4 5))
;(l-reverse (list 1 2 3 4 5))

; 2.40
(define (enumerate-interval from to)
  (if (> from to)
	nil
	(cons from (enumerate-interval (+ from 1) to))))

(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))

(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))

(define (make-pair-sum pair)
  (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

(define (unique-pairs n) 
  (flatmap (lambda (i)  
              (map (lambda (j) (list i j)) 
                   (enumerate-interval 1 (- i 1)))) 
            (enumerate-interval 1 n))) 
  
(define (prime-sum-pairs n) 
  (map make-pair-sum
        (filter prime-sum? (unique-pairs n)))) 

;(unique-pairs 4)
;(prime-sum-pairs 5)

; 2.41
(define (unique-triples n) 
  (flatmap (lambda (i)  
              (map (lambda (pair) (cons i pair)) (unique-pairs (- i 1))))
            (enumerate-interval 1 n)))

(define (find-triples n s)
  (filter (lambda (triple) (= (apply + triple) s)) (unique-triples n)))

; 2.42
(define (queens board-size)
  (define (queen-cols k)
	(if (= k 0)
	  (list empty-board)
	  (filter
		(lambda (positions) (safe? k positions))
		(flatmap
		  (lambda (rest-of-queens)
			(map (lambda (new-row)
				   (adjoin-position new-row
									k
									rest-of-queens))
				 (enumerate-interval 1 board-size)))
		  (queen-cols (- k 1))))))
  (queen-cols board-size))

(define empty-board nil)

(define (adjoin-position row col board)
  (cons (cons row col) board))

(define (safe? k board)
  (let ((queen (car board)))
	(cond
	  ((pair? (filter (lambda (pos) (= (car pos) (car queen))) (cdr board)))
	   #f)
	  ((pair? (filter 
				(lambda (pos) 
				  (= 
					(- (max (car pos) (car queen)) 
					   (min (car pos) (car queen)))
					(- (max (cdr pos) (cdr queen)) 
					   (min (cdr pos) (cdr queen)))))
				(cdr board)))
	   #f)
	  (else
		#t))))

;(pretty-print (length (queens 4)))
;(pretty-print (length (queens 8)))

; picture solutions on picture.rkt


