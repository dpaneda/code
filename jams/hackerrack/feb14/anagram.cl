(defun read-ordered-string ()
  (sort 
    (coerce (read-line) 'list)
    'char<))

(defvar A (read-ordered-string))
(defvar B (read-ordered-string))

(defun check-diff (A B)
	(defun recur (A B n)
		(cond
		  ((or (not B) (not A))
        (+ (list-length B) (list-length A) n))
			((char< (car A) (car B))
				(recur (cdr A) B (1+ n)))
			((char> (car A) (car B))
			 	(recur A (cdr B) (1+ n)))
			(T
				(recur (cdr A) (cdr B) n))
		)
	)
	(recur A B 0)
)

(compile 'check-diff)
(prin1 (check-diff A B))
(fresh-line)
