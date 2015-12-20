(defun pow-2 (x) (* x x))

(defun distance (A B)
  (sqrt 
    (+
      (pow-2 (- (car B) (car A)))
      (pow-2 (- (cdr B) (cdr A))))))

(defun calculate-distances (bikers bikes matrix *N* *M*)
  (let ((res nil))
    (dotimes (a *N*)
      (dotimes (b *M*)
        (let ((dist (distance (aref bikers a) (aref bikes b))))
          (push (list a b dist) res)
          (setf (aref matrix a b) dist))))
    res))

(defun read-n-coordinates (n)
  (if (= n 0) nil
    (cons (cons (read) (read)) (read-n-coordinates (1- n)))))

(defparameter *N* (read))
(defparameter *M* (read))
(defparameter *K* (read))

(defvar bikers (make-array *N* :initial-contents (read-n-coordinates *N*)))
(defvar bikes (make-array *M* :initial-contents (read-n-coordinates *M*)))

(defvar distances-matrix (make-array (list *N* *M*)))
(defvar distances (sort (calculate-distances bikers bikes distances-matrix *N* *M*) #'> ::key #'caddr))

(defun row-count (matrix row)
  (loop for i below (cadr (array-dimensions matrix))
    counting (aref matrix row i)))

(defun column-count (matrix row)
  (loop for i below (car (array-dimensions matrix))
    counting (aref matrix i row)))

(defun try-remove (matrix x y bikers-left bikes-left)
  (let 
    ((xcount (row-count matrix x))
     (ycount (column-count matrix y))
     (xremove bikers-left)
     (yremove bikes-left))
    (if (and (> xcount 1) (> ycount 1))
      (setf (aref matrix x y) nil))
    (when (and (= xcount 1) (> bikers-left *K*))
      (setf (aref matrix x y) nil)
      (decf xremove))
    (when (and (= ycount 1) (> bikes-left *K*))
      (setf (aref matrix x y) nil)
      (decf yremove))
    (values-list (list xremove yremove))))

(defvar bikers-left *N*)
(defvar bikes-left *M*)

(dolist (d distances)
  (let ((biker (car d))
        (bike (cadr d)))
    (multiple-value-setq (bikers-left bikes-left) (try-remove distances-matrix biker bike bikers-left bikes-left))))

(print distances-matrix)

(prin1 (round (pow-2 
  (loop for i below (cadr (array-dimensions distances-matrix)) maximize
    (loop for j below (car (array-dimensions distances-matrix)) maximize 
      (or (aref distances-matrix j i) 0))))))
(fresh-line)
