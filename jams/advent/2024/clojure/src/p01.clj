(require '[clojure.string :as str])

(defn parse-ints [line]
  (->> (str/split line #" +")
       (map #(Integer/parseInt %))))

(defn slurp-ints []
  (map parse-ints
       (str/split-lines (slurp *in*))))

(let
 [input (slurp-ints)
  l (sort (map first input))
  g (sort (map second input))
  distance (fn [a b] (abs (- a b)))
  freqs (frequencies g)
  similarity-score (fn [n] (* n (get freqs n 0)))]
  (prn (apply + (map distance l g)))
  (prn (apply + (map similarity-score l))))
