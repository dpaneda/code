(defun square (n)
  (* n n))

(defun choose (n k)
  (labels ((prod-enum (s e)
             (do ((i s (1+ i)) (r 1 (* i r))) ((> i e) r)))
           (fact (n) (prod-enum 1 n)))
    (/ (prod-enum (- (1+ n) k) n) (fact k))))

(defun binom (n k &optional (acc 1))
  (cond ((or (< n k) (< k 0)) NIL)
        ((or (= k 0) (= n k)) acc)
        (T (binom (- n 1) (- k 1) (* acc (/ n k))))))

(defun coef (n) (binom n 5))

(defun forfor (n)
  (let ((ret 0)
        (vals (make-hash-table)))
  (loop for a from 1 to n do
    (loop for b from 1 to n do
      (loop for c from 1 to n do
        (loop for d from 1 to n do
          (loop for e from 1 to n do
            (loop for f from 1 to n do
              (loop for g from 1 to n do
                (when (= n (+ a b c d e f g))
                  (if (gethash a vals)
                    (incf (gethash a vals))
                    (setf (gethash a vals) 1))
                  (incf ret (+ (square a) 
                           (square b) 
                           (square c) 
                           (square d)
                           (square e)
                           (square f)
                           (square g)))
                  (setq ret (mod ret 3211123))))))))))
  (loop for key being the hash-keys of vals do 
        (format t "~d: ~d~%" key (gethash key vals)))
  ret))

(defun forfor-fast (n)
  (let ((c 1)
        (sum 0))
    (loop for i from (- n 2) downto 5 do
      (setq sum (mod (+ sum (* (coef i) (square c))) 3211123))
      (incf c))
    (mod (* sum 7) 3211123)))

;(require :sb-sprof)
;(declaim (optimize speed))
;(sb-sprof:with-profiling (:max-samples 10000
;                               :mode :alloc
;                               :report :flat)

(loop for n = (read)
  until (eq n :eof) do 
    ;(print (forfor n))
    (format t "~d~%" (forfor-fast n)))

