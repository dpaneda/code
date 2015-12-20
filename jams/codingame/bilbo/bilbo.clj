(ns Player
  (:gen-class))

(require 'clojure.string)

(def initial-state 
  {:pos 0
   :runes (into [] (repeat 30 \[))
   :code '()})

(defn abs [n] (max n (- n)))

(defn rune-distance
  [from to]
  (min
    (mod (- from to) 30)
    (mod (- to from) 30)))

(defn letter-distance
  [from to]
  (min
    (mod (- (int from) (int to)) 27)
    (mod (- (int to) (int from)) 27)))

(defn rune-travel
  [from to]
  (let
    [right (mod (- from to) 30)
     left (mod (- to from) 30)]
    (if (< left right)
      (repeat left \>)
      (repeat right \<))))

(defn rune-change
  [from to]
  (let
    [up (mod (- (int to) (int from)) 27)
     down (mod (- (int from) (int to)) 27)]
    (if (< up down)
      (repeat up \+)
      (repeat down \-))))

(defn rune-cost
  "Total instruccion cost of transform a rune into another"
  [runes pos what rune-pos]
  (+
   (rune-distance pos rune-pos)
   (letter-distance what (nth runes rune-pos))))

(defn best-rune
  "Find the optimum rune to change"
  [pos runes what]
  (let [cost (partial rune-cost runes pos what)]
    (apply min-key (concat [cost] (range 0 30)))))

(defn print-rune
  [{:keys [pos runes code]} what]
  (let 
    [target-rune (best-rune pos runes what)]
    {
     :pos target-rune
     :runes (assoc runes target-rune what)
     :code (concat code 
                   (rune-travel pos target-rune)
                   (rune-change (nth runes target-rune) what)
                   '(\.))
    }))

(defn print-runes
  [state [letter & letters]]
  (if 
    (nil? letter) state
    (print-runes
     (print-rune state letter)
      letters)))

(defn -main []
  (println (apply str (:code (print-runes initial-state 
                                          (clojure.string/replace (read-line) \space \[))))))
