(defn order-S [S W acc]
  (if (empty? S) 
    acc
    (let [c (first S)
          acc (if (neg? (compare c (first acc))) (str acc c) (str c acc))]
      (recur (rest S) W acc))))

(defn read-solve-case []
  (let [S (read-line)
        W (first S)]
    (order-S (rest S) W (str W))))

(def ncases (read-string (read-line)))

(dotimes [i ncases] 
  (printf "Case #%d: %s\n" (inc i) (read-solve-case)))
