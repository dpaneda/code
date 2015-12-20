(defun read-integer-list (n)
  (let ((l nil))
    (loop for i from 1 to n do
	  	(push (read) l))
    l))

(defun read-sorted-integer-list (n)
  (sort (read-integer-list n) '>))

(defun recur-solve-case (mcost ncost)
  (defun recur (mcost ncost mcuts ncuts total)
    (let
      ((mc (or (car mcost) -1)) 
       (nc (or (car ncost) -1)))
      (cond
        ((not (or mcost ncost)) total)
        ((> mc nc)
          (recur (cdr mcost) ncost (1+ mcuts) ncuts (+ total (* ncuts mc))))
        (T
          (recur mcost (cdr ncost) mcuts (1+ ncuts) (+ total (* mcuts nc)))))))
  (recur mcost ncost 1 1 0))

(loop for i from 1 to (read) do
  (let ((M (read))
        (N (read)))
	  (prin1 
      (mod 
        (recur-solve-case
          (read-sorted-integer-list (1- M))
          (read-sorted-integer-list (1- N)))
        1000000007))
    (fresh-line)))
