(defun read-integer-list (n)
    (let ((l nil))
      (loop for i from 1 to n do
            (push (read) l))
        (reverse l)))

(defvar N (read))
(defvar M (read))

(defvar L (read-integer-list N))

(loop for i from 1 to M do
  (prin1
    (apply 'min (subseq L (read) (1+ (read)))))
  (princ #\newline))
