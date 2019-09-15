; 1.2


(/ (+ 5 4 (- 2 (- 3  (+ 6 (/ 4 5)))))
   (* 3 (- 6 2 ) (- 2 7)))

(defn square [x]
  (* x x))

; 1.3
(defn sumsq [& l]
  (apply + (map square (sort (rest l)))))

; 1.4 The first element of the slist evaluates to + or - depending on the sign of b
(defn a-plus-abs-b [a b]
  ((if (> b 0) + -)
   a
   b))


; 1.5 Infinite recursion on applicative, 0 on normal
