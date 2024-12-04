(require '[clojure.string :as str])

; Reads everything as a single line, because there is persistent
; state between different lines
(defn read-file []
  (str/replace (slurp *in*) "\n" ""))

(defn parse-muls [line]
  (->>
   line
   (re-seq #"mul\((\d+),(\d+)\)")
   (map (fn [[_ a b]] (* (Integer/parseInt a) (Integer/parseInt b))))))

(defn solve [input]
  (apply + (parse-muls input)))

(defn solve2 [input]
  (solve 
   (str/replace input #"don't\(\)(?:(?!do\(\)).)*" "")))

(def input (read-file))

(prn (solve input))
(prn (solve2 input))

(comment
  ; Used to develop with the inline REPL

  (def sample
    ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"])

  (def sample2
    ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])

  (solve sample)
  (solve2 sample2)
)
