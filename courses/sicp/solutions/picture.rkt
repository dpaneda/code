#lang racket
(require racket/pretty)
(require (planet "sicp.ss" ("soegaard" "sicp.plt" 2 1)))

; Racket kills my machine if I don't limit the memory use :-/
(custodian-limit-memory (current-custodian) (* 100 1024 1024))

; 2.44
(define (right-split painter n)
  (if (= n 0)
	painter
	(let ((smaller (right-split painter (- n 1))))
	  (beside painter (below smaller smaller)))))

(define (corner-split painter n)
  (if (= n 0)
	painter
	(let ((up (up-split painter (- n 1)))
		  (right (right-split painter (- n 1))))
	  (let ((top-left (beside up up))
			(bottom-right (below right right))
			(corner (corner-split painter (- n 1))))
		(beside (below painter top-left)
				(below bottom-right corner))))))

(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
	(let ((half (beside (flip-horiz quarter) quarter)))
	  (below (flip-vert half) half))))

(define (up-split painter n)
  (if (= n 0)
	painter
	(let ((smaller (up-split painter (- n 1))))
	  (below painter (beside smaller smaller)))))

; 2.45
(define (split out_split in_split)
  (define (split_proc painter n)
    (if (= n 0)
  	  painter
	  (let ((smaller (split_proc painter (- n 1))))
	    (out_split painter (in_split smaller smaller)))))
  split_proc)

;2.46
; We need to use racket library representation
;(define make-vect cons)
(define xcor-vect vector-xcor)
(define ycor-vect vector-ycor)

(define (add-vect v1 v2)
  (make-vect (+ (xcor-vect v1) (xcor-vect v2)) 
			 (+ (ycor-vect v1) (ycor-vect v2))))

(define (sub-vect v1 v2)
  (make-vect (- (xcor-vect v1) (xcor-vect v2)) 
			 (- (ycor-vect v1) (ycor-vect v2))))

(define (scale-vect v1 n)
  (make-vect (* n (xcor-vect v1)) (* n (ycor-vect v1))))

;2.47
;(define (make-frame origin edge1 edge2)
; (list origin edge1 edge2))

(define get-origin frame-origin)
(define get-edge1 frame-edge1)
(define get-edge2 frame-edge2)

(define (get-edge3 frame)
  (add-vect (get-edge1 frame) (get-edge2 frame)))

; 2.48
;(define make-segment cons)
(define start-segment segment-start)
(define end-segment segment-end)

;2.49
(define (outline frame)
  (segments->painter 
   (list
    (make-segment (get-origin frame) (get-edge1 frame))
    (make-segment (get-origin frame) (get-edge2 frame))
    (make-segment (get-edge2 frame) (get-edge3 frame))
    (make-segment (get-edge1 frame) (get-edge3 frame)))))

(define (x-frame frame)
  (segments->painter
   (list
    (make-segment (get-origin frame) (get-edge3 frame))
    (make-segment (get-edge1 frame) (get-edge2 frame)))))

(define (middle-vect v1 v2)
  (make-vect (/ (+ (xcor-vect v1) (xcor-vect v2)) 2)
			 (/ (+ (ycor-vect v1) (ycor-vect v2)) 2)))

(define (diamond frame)
  (let ((a (middle-vect (get-origin frame) (get-edge1 frame)))
		(b (middle-vect (get-edge1 frame) (get-edge3 frame)))
		(c (middle-vect (get-edge2 frame) (get-edge3 frame)))
		(d (middle-vect (get-origin frame) (get-edge2 frame))))
	(segments->painter
         (list
          (make-segment a b) (make-segment b c) (make-segment c d) (make-segment d a)))))

; Frame to test the painters
(define myframe (make-frame (make-vect 0 0) 
                            (make-vect 0 0.99) 
                            (make-vect 0.99 0)))

; 2.50
(define (flip-horizontal painter)
  ((transform-painter (make-vect 1 0)
                      (make-vect 0 0)
                      (make-vect 1 1))
   painter))

(define (rot180 painter)
  ((transform-painter (make-vect 1 1)
                      (make-vect 0 1)
                      (make-vect 1 0))
   painter))

(define (rot270 painter)
  ((transform-painter (make-vect 1 0)
                      (make-vect 1 1)
                      (make-vect 0 0))
   painter))

; 2.51