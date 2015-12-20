(defun factor (n)
  (when (> n 1)
    (loop with max-d = (isqrt n)
	  for d = 2 then (if (evenp d) (+ d 1) (+ d 2)) do
	  (cond ((> d max-d) (return (list n))) ; n is prime
		((zerop (rem n d)) (return (cons d (factor (truncate n d)))))))))


(defun common-factors (l1 l2)
	(defun recur (l1 l2 res)
    (and 
      (or (null l1) (null l2)) 
      (return-from recur res))
		(let ((a (car l1))
					(b (car l2))
					(r1 (cdr l1))
					(r2 (cdr l2)))
      (cond       
        ((= a b)
         (recur r1 r2 (cons a res)))
        ((< a b)
         (recur r1 l2 res))
        (T (recur l1 r2 res)))))
  (recur l1 l2 nil))


(defun read-factorized-integer-list (n)
    (let ((l nil))
      (loop for i from 1 to n do
            (setf l (append l (factor (read)))))
      (sort l '<)))


(defvar Alist (read-factorized-integer-list (read)))
(defvar Blist (read-factorized-integer-list (read)))

;(print Alist)
;(print Blist)

;(prin1 (common-factors Alist Blist))

(prin1 
  (mod 
    (apply '* (common-factors Alist Blist)) 
    1000000007))
