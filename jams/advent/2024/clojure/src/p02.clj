(require '[clojure.string :as str])

(defn parse-ints [line]
 (->> (str/split line #" +")
      (map #(Integer/parseInt %))))

(defn slurp-ints []
  (map parse-ints
      (str/split-lines (slurp *in*))))

(defn increasing [l]
  (every? 
   #(and (pos? %1) (< %1 4))
   (map - l (rest l))))

(defn safe [l]
  (or
   (increasing l)
   (increasing (reverse l))))

(defn drop-nth [n coll]
  (concat
   (take n coll)
   (drop (inc n) coll)))

(defn safe-with-drop [l]
  (some identity
         (for [i (range (count l))]
           (safe (drop-nth i l)))))

(defn solve [input]
  (prn (count (filter true? (map safe input))))
  (prn (count (filter true? (map safe-with-drop input)))))

(pr (solve (slurp-ints)))

(comment 
  ; Used to develop with the inline REPL

  (def sample
    [[7 6 4 2 1]
     [1 2 7 8 9]
     [9 7 6 2 1]
     [1 3 2 4 5]
     [8 6 4 4 1]
     [1 3 6 7 9]])

  (solve sample)
)

