(defparameter *partitions* 250 "Number of partitions on each axis")
(defvar *npoints* (read))
(defvar *points* (make-array *npoints*))
(defvar *collisions* (make-hash-table :test #'equal))
(defvar *col* 0)

(defstruct point 
  (x 0 :type (integer 0 99999))
  (y 0 :type (integer 0 99999))
  (radius 0 :type (integer 0 99999))
  :type vector)

(defun square (x) (* x x ))

(defun collide (a b)
  (let ((dx (abs (- (point-x a) (point-x b))))
        (dy (abs (- (point-y a) (point-y b))))
        (radius-distance (+ (point-radius a) (point-radius b))))
    (cond
      ((> dx radius-distance) nil)
      ((> dy radius-distance) nil)
      (T (< (sqrt (+ (square dx) (square dy))) radius-distance)))))

(dotimes (i *npoints*)
  (setf (aref *points* i) (make-point :x (read) :y (read) :radius (read))))

(defun first-x (p) (- (point-x p) (point-radius p)))
(defun first-y (p) (- (point-y p) (point-radius p)))
(defun last-x (p) (+ (point-x p) (point-radius p)))
(defun last-y (p) (+ (point-y p) (point-radius p)))

(loop for p across *points*
      minimize (point-x p) into xmin
      maximize (point-x p) into xmax 
      minimize (point-y p) into ymin
      maximize (point-y p) into ymax
      finally 
        (progn
          (defvar *xmin* xmin)
          (defvar *xmax* xmax)
          (defvar *ymin* ymin)
          (defvar *ymax* ymax)))

;(defvar *xmin* 0)
;(defvar *ymin* 0)
;(defvar *xmax* 100000)
;(defvar *ymax* 100000)

(fresh-line)
(format t "xmin: ~d, xmax: ~d, ymin: ~d, ymax: ~d" *xmin* *xmax* *ymin* *ymax*)
(fresh-line)


(defvar *space* (make-array (list *partitions* *partitions*) :initial-element nil))

(defvar *xcutsize* (/ (- *xmax* *xmin*) *partitions*))
(defvar *ycutsize* (/ (- *ymax* *ymin*) *partitions*))

(defvar *xcuts* (loop for i from *xmin* by *xcutsize* to *xmax* collect i))
(defvar *ycuts* (loop for i from *ymin* by *ycutsize* to *ymax* collect i))

(defun cut-position (n)
  (max 0 (min (1- *partitions*) (floor (/ n *xcutsize*)))))

; Load the array
(dotimes (p *npoints*)
  (let* ((point (aref *points* p))
         (a (- (cut-position (last-y point)) (cut-position (first-y point))))
         (b (- (cut-position (last-x point)) (cut-position (first-x point)))))
     ;(when (> a 0) (print a))
     ;(when (> b 0) (print b))
     (loop for i from (cut-position (first-x point)) 
          to (cut-position (last-x point)) do
      (loop for j from (cut-position (first-y point)) 
           to (cut-position (last-y point)) do
       (push p (aref *space* i j))))))


;(sb-ext:gc :full t)
;(room)

; Do the real work \o/
(fresh-line)
(print "Array loaded")
(fresh-line)

(dotimes (i *partitions*)
  (dotimes (j *partitions*)
    (do* ((l (aref *space* i j) (cdr l))
         (a (first l) (first l)))
      ((null l))
      (dolist (b (cdr l))
        (when (collide (aref *points* a) (aref *points* b))
          (incf *col*))))))
          ;(format t "a: ~A ~A~%" a (aref *points* a))
          ;(format t "b: ~A ~A~%" b (aref *points* b))
          ;(setf (gethash (cons a b) *collisions*) T))))))


(fresh-line)
(prin1 *col*)
(fresh-line)
(prin1 (hash-table-count *collisions*))
(fresh-line)

;; Bruteforce approach
;(defvar *collisions2* (make-hash-table :test #'equal))
;
;(dotimes (i *npoints*)
;  (loop for j from (1+ i) to (1- *npoints*) do
;    (when (collide (nth i *points*) (nth j *points*))
;      (setf (gethash (append (nth i *points*) (nth j *points*)) *collisions2*) T))))
;
;(fresh-line)
;(prin1 (hash-table-count *collisions2*))
;(fresh-line)

;(dotimes (i *partitions*)
;  (dotimes (j *partitions*)
;    (fresh-line)
;    (format t "[~d][~d]: ~A" (nth i *xcuts*) (nth j *ycuts*) (aref *space* i j))))
