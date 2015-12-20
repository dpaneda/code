; Not the best possible code, one of the my first programs in clojure, sorry :P

(ns Player
  (:gen-class))

(use '[clojure.string :only [split join]])
(use '[clojure.set :only [difference intersection]])

(defn prop
  ([conns n i]
   (prop #{i} (into #{} (range n)) conns 0))
  ([notified remaining conns step]
   (defn prop-step []
     (let
       [new-remaining (difference remaining notified)
        new-border (into #{} (flatten (map (partial nth conns) notified)))]
       (list
         (intersection new-remaining new-border)
         new-remaining)))
   (if (empty? remaining)
     step
     (let
       [[new-notified new-remaining] (prop-step)]
       (if (empty? new-notified)
         (if (empty? new-remaining) step 0)
         (prop new-notified new-remaining conns (inc step)))))))

(defn read-conn
  [i conns]
  (let
    [old-value (nth conns i)
     new-conns (map dec (map read-string (split (read-line) #" ")))]
  (assoc conns i (concat old-value new-conns))))

(defn read-conns
  ([n]
   (read-conns n 0 (into [] (map list (range n)))))
  ([n i conns]
  (if (>= i n)
    conns
    (read-conns
      n
      (inc i)
      (read-conn i conns)))))

(defn read-solve-case
  []
  (let
    [n (read-string (read-line))
     conns (read-conns n)
     candidates (range n)
     results (map list candidates (map (partial prop conns n) candidates))
     sorted_results (sort-by second results)
     filtered_results (filter #(pos? (second %)) sorted_results)]
    (if (empty? filtered_results)
      0
      (let
        [minimum (second (apply min-key second filtered_results))
         valid_results (filter #(= minimum (second %)) filtered_results)
         def_list (map inc (map first valid_results))]
        (join " " (sort def_list))))))


(def ncases (read-string (read-line)))

(dotimes [_ ncases] 
  (println (read-solve-case)))
